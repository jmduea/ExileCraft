# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ##############################################################################

import contextlib
import os
from typing import List

from sqlalchemy import create_engine, select, MetaData
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker, scoped_session, Session, Mapped

from modules.data.models.base_model import Base
from modules.data.models.item_models import ItemClass, ItemProperty, ItemVisualIdentity, Item, ItemRequirement, \
    ItemReleaseState
from modules.data.models.mod_models import Mod, ModGroup, ModType, GenerationType
from modules.data.models.shared_models import Domain
from modules.data.models.stat_models import Stat, StatValue
from modules.data.models.tag_models import Tag
from modules.data.parser.base_items_parser import ItemParser
from modules.data.parser.item_class_parser import ItemClassParser
from modules.data.parser.mods_parser import ModParser
from modules.data.parser.stats_parser import StatParser
from modules.data.parser.tags_parser import TagsParser
from modules.shared.config.constants import item_class_whitelist, domain_whitelist


class DatabaseManager:
    """The DatabaseManager class is responsible for managing the database connection and transactions.
    
    Attributes:
        engine (Engine): The SQLAlchemy Engine instance.
        session_factory (SessionFactory): The SQLAlchemy SessionFactory instance.
        session (Session): The SQLAlchemy Session instance.
        mods_manager (ModManager): The ModManager instance.
        stats_manager (StatManager): The StatManager instance.
        items_manager (ItemManager): The ItemManager instance.
        tags_manager (TagManager): The TagManager instance.
        translations_manager (TranslationManager): The TranslationManager instance.
    """
    
    def __init__(self):
        """The constructor for the DatabaseManager class."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'exilecraft.db')
        db_url = f"sqlite:///{db_path}"
        self.engine = create_engine(db_url, echo=True)
        self.session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
        self.session = scoped_session(self.session_factory)
        self.mods_manager = ModManager()
        self.stats_manager = StatManager()
        self.items_manager = ItemManager()
        self.tags_manager = TagManager()
        self.translations_manager = TranslationManager()
    
    def create_tables(self):
        """
        Create all tables in the database as defined in the Base model class.
        """
        Base.metadata.create_all(self.engine)
    
    def drop_tables(self):
        """
        Drop all tables in the database as defined in the Base model class.
        
        Returns:
            None
        """
        m = MetaData()
        m.reflect(self.engine)
        m.drop_all(self.engine)
    
    def get_session(self):
        """
        Get a new session with the database.

        Returns:
            Session: An instance of a SQLAlchemy Session.
        """
        return self.session
    
    def add_record(self, record):
        """
        Add a new record to the database.

        Args:
            record (Base): The record to add.
        """
        with self.transaction() as session:
            session.add(record)
    
    def get_record(self, model, record_id):
        """
        Get a record from the database.

        Args:
            model (Base): The model class the record belongs to.
            record_id: The id of the record.

        Returns:
            record: The requested record.
        """
        with self.transaction() as session:
            record = session.query(model).filter_by(id=record_id).first()
            return record
    
    def update_record(self, model, record_id, **kwargs):
        """
        Update a record in the database.

        Args:
            model (Base): The model class the record belongs to.
            record_id: The id of the record.
            **kwargs: Arbitrary keyword arguments.
        """
        with self.transaction() as session:
            select(model).get(record_id).update(kwargs)
            session.flush()
    
    def delete_record(self, model, record_id):
        """
        Delete a record from the database.

        Args:
            model (Base): The model class the record belongs to.
            record_id: The id of the record.
        """
        with self.transaction() as session:
            record = select(model).get(record_id)
            session.delete(record)
            session.flush()
    
    @contextlib.contextmanager
    def transaction(self):
        """
        Provide a transactional scope around a series of operations. If an error occurs during the transaction,
        the session is rolled back. If no error occurs, the session is committed.
        
        Returns:
            Session: An instance of a SQLAlchemy Session.
        """
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            print(f'An error occurred: {e}')
            raise
        finally:
            self.close_session()
    
    def close_session(self):
        """
        Close the current session with the database.
        """
        self.session.remove()


class TagManager:
    """
    Class for managing tag data.

    Attributes:
        tags_parser (TagsParser): An instance of the TagsParser class.

    Methods:
        insert_tags(): Insert all tags into the database.
        get_tag_id(): Get the id of a tag.
    """
    
    def __init__(self):
        self.tags_parser = TagsParser()
    
    def create_tag_objects(self, session):
        """
        Insert all tags into the database.

        Returns:
            None
        """
        tags_list = self.tags_parser.create_tags_list()
        tag_obj_list = []
        for tag in tags_list:
            try:
                tag_obj = session.scalars(select(Tag).filter_by(tag=tag)).one()
                tag_obj_list.append(tag_obj)
            except NoResultFound:
                tag_obj = Tag(tag=tag)
                tag_obj_list.append(tag_obj)
        return tag_obj_list
    
    def get_tag_id(self, session, tag):
        """
        Get the id of a tag.

        Args:
            session (): SQLAlchemy session.
            tag (): The tag to get the id for.

        Returns:
            int: The id of the tag.
        """
        tag_id = session.scalars(select(Tag.id).filter_by(tag=tag)).first()
        return tag_id


class StatManager:
    """
    Class for managing stat data.

    Attributes:
        stats_parser (StatParser): An instance of the StatParser class.

    Methods:
        insert_stats(): Insert all stats into the database.
        get_stat_id(): Get the id of a stat.
    """
    
    def __init__(self):
        self.stats_parser = StatParser()
    
    def create_stat_objects(self, session):
        """
        Insert all stats into the database.
        Returns:
            None
        """
        stat_list = self.stats_parser.get_all_stats()
        stat_obj_list = []
        for stat in stat_list:
            try:
                stat_obj = session.query(Stat).filter_by(name=stat.get('name')).one()
                stat_obj_list.append(stat_obj)
            except NoResultFound:
                stat_obj = Stat(name=stat.get('name'),
                                is_aliased=stat.get('is_aliased', False),
                                is_local=stat.get('is_local', False))
                stat_obj_list.append(stat_obj)
        return stat_obj_list
    
    def get_stat_id(self, session, stat):
        """
        Get the id of a stat from the database.
        Args:
            stat (): The stat to get the id for.
        Returns:
            stat_id (): The id of the stat.
        """
        stat_id = session.scalars(select(Stat.id).filter_by(name=stat)).first()
        return stat_id


class TranslationManager:
    pass


class FossilManager:
    pass


class EssenceManager:
    pass


class ItemManager:
    """
    Class for managing item data.

    Attributes:
        item_parser (ItemParser): ItemParser object.

    """
    
    def __init__(self):
        """Constructor for the ItemManager class that initializes the ItemParser object."""
        self.item_parser = ItemParser()
        self.item_class_parser = ItemClassParser()
    
    def create_item_class_objects(self, session):
        """
        Insert item classes into the database. This is a generic method that can be used for all item types.

        Returns:
            item_class_obj_list (list): A list of item class objects.
        """
        item_class_list = self.item_class_parser.create_item_class_list()
        item_class_obj_list = []
        for _dict in item_class_list:
            item_class_name = _dict["name"]
            try:
                item_class_obj = session.scalars(select(ItemClass).filter_by(name=item_class_name)).one()
                item_class_obj_list.append(item_class_obj)
            except NoResultFound:
                item_class_obj = ItemClass(**_dict)
                item_class_obj_list.append(item_class_obj)
        return item_class_obj_list
    
    def create_visual_identity_objects(self, session):
        visual_identity_list = self.item_parser.get_item_data_by_key("visual_identity")
        visual_identity_obj_list = []
        for _dict in visual_identity_list:
            try:
                visual_identity_obj = session.query(ItemVisualIdentity).filter_by(name=_dict[
                    'visual_identity'].get('id', None)).one()
                if visual_identity_obj not in visual_identity_obj_list:
                    visual_identity_obj_list.append(visual_identity_obj)
            except NoResultFound:
                visual_identity_obj = ItemVisualIdentity(name=_dict["visual_identity"].get("id", None),
                                                         dds_file=_dict["visual_identity"].get("dds_file", None))
                if visual_identity_obj not in visual_identity_obj_list:
                    visual_identity_obj_list.append(visual_identity_obj)
        return visual_identity_obj_list
    
    def insert_base_items(self, session):
        """
        Insert base items into the database. This is a generic method that can be used for all item types.

        Args:
            session (): SQLAlchemy session object.

        Returns:
            None
        """
        data = self.data
        for item, item_data in data.items():
            # Get the domain_id
            domain = item_data.get('domain')
            domain_id = db_manager.mods_manager.get_domain_id(domain)

            item_class = item_data.get('item_class')
            # Get the item_class_id
            item_class_id = db_manager.items_manager.get_item_class_id(session, item_class)

            tag_list = item_data.get("tags")
            item_class_subtype = self.item_parser.get_item_class_subtype(item_class, tag_list)
            # Get the item_class_subtype_id using the item_class_id and subtype name from item_class_subtype
            item_class_subtype_id = db_manager.items_manager.get_item_class_subtype_id(session, item_class_id,
                                                                                 item_class_subtype)

            visual_identity = item_data.get("visual_identity").get("id")
            # Get the visual_identity_id
            visual_identity_id = db_manager.items_manager.get_visual_identity_id(session, visual_identity)

            name = item_data.get("name")
            drop_level = item_data.get("drop_level")

            item_obj = session.scalars(select(Item).filter_by(meta_data_id=item)).first()
            if item_obj:
                continue
            else:
                item_dict = {
                    "visual_identity_id": visual_identity_id,
                    "name": name,
                    "meta_data_id": item,
                    "item_class_id": item_class_id,
                    "item_class_subtype_id": item_class_subtype_id,
                    "domain_id": domain_id,
                    "drop_level": drop_level,
                    "rarity": 'Normal',
                    "is_corrupted": False
                }
                item = Item(**item_dict)
                session.add(item)
                session.flush()
                item_id = item.id

                db_manager.items_manager.insert_item_tags(session, tag_list, item_id)
                implicit_list = item_data.get("implicits")
                self.insert_item_implicits(session, implicit_list, item_id)
                item_properties_dict = item_data.get("properties")
                item_requirements_dict = item_data.get("requirements")
                self.insert_item_properties(session, item_id, item_class_id, item_class_subtype,
                                            item_class_subtype_id, item_properties_dict,
                                            item_requirements_dict, drop_level)
        session.commit()
    
    def get_visual_identity_id(self, session, visual_identity):
        """
        Get visual identity id from the database.

        Args:
            session (): SQLAlchemy session object.
            visual_identity (): Visual identity.

        Returns:
            Visual identity id.
        """
        visual_identity_id = session.scalars(select(ItemVisualIdentity.id).filter_by(
            visual_identity=visual_identity)).first()
        return visual_identity_id
    
    def get_base_items(self, session, item_class_id):
        """
        Get base items from the database.
        Args:
            session (): SQLAlchemy session object.
            item_class_id (): Item class id.
        Returns:
            List of base item objects.
        """
        return select(Item).filter(Item.item_class_id == item_class_id).all()
    
    def get_base_items_from_subtype_display_name(self, session, subtype_display_name):
        """
        Get base items from the database.

        Args:
            session (): SQLAlchemy session object.
            subtype_display_name (): Display name of the item class subtype.

        Returns:
            List of base item objects.
        """
        subtype_id = session.scalars(select(ItemClassSubtype.id).filter_by(
            display_name=subtype_display_name)).first()

        if subtype_id is not None:
            base_item_objs = session.scalars(select(Item).filter_by(item_class_subtype_id=subtype_id)).all()
            return base_item_objs
    
    def insert_item_tags(self, session, tag_list, item_id):
        """
        Insert item tags into the database.
        Args:
            session (): SQLAlchemy session object.
            tag_list (): List of tags.
            item_id (): Item id.

        Returns:
            None
        """
        for tag in tag_list:
            tag_id = tag_manager.get_tag_id(session, tag)
            insert_stmt = insert(ItemTag).values(tag_id=tag_id, item_id=item_id)
            session.execute(insert_stmt)
        session.commit()
    
    def insert_item_implicits(self, session, implicit_list, item_id):
        """
        Insert item implicits into the database.
        Args:
            session (): SQLAlchemy session object.
            implicit_list (): List of implicits.
            item_id (): Item id.

        Returns:
            None
        """
        for implicit in implicit_list:
            mod_id = mod_manager.get_mod_id(implicit)
            insert_stmt = insert(ItemImplicitMod).values(mod_id=mod_id, item_id=item_id)
            session.execute(insert_stmt)
        session.commit()
    
    def insert_item_properties(self, session, item_id, item_class_id, item_class_subtype, item_class_subtype_id,
                               item_properties_dict, item_requirements_dict, drop_level):
        """
        Insert item properties into the database. This is a generic method that can be used for all item types.

        Args:
            session (): SQLAlchemy session object.
            item_id (): Item id.
            item_class_id (): Item class id.
            item_class_subtype (): Item class subtype.
            item_class_subtype_id (): Item class subtype id.
            item_properties_dict ():
            item_requirements_dict ():
            drop_level (): Drop level.

        Returns:
            None
        """
        subclasses = {
            'dex_armour': EvasionBase,
            'int_armour': EnergyShieldBase,
            'str_armour': ArmourBase,
            'str_dex_armour': ArmourEvasionBase,
            'str_int_armour': ArmourEnergyShieldBase,
            'str_dex_int_armour': ArmourEvasionEnergyShieldBase,
            'dex_int_armour': EvasionEnergyShieldBase,
            'ward_armour': WardBase,
            'one_hand_weapon': OneHandWeapon,
            'two_hand_weapon': TwoHandWeapon,
            'flask': Flask,
        }

        # Use the subclasses dictionary to get the subclass, or default to ItemProperties if not found
        subclass = subclasses.get(item_class_subtype, ItemProperty)

        properties = subclass()
        properties.id = item_id
        properties.item_class_id = item_class_id
        properties.item_class_subtype_id = item_class_subtype_id
        properties.level_req = drop_level

        # Add data from item_properties_dict to properties if attribute exists in subclass
        if item_properties_dict is not None:
            for key, value in item_properties_dict.items():
                if hasattr(properties, key):
                    setattr(properties, key, value)

        if item_requirements_dict is not None:  # Add data from item_requirements_dict to properties if attribute
            # exists in subclass
            for key, value in item_requirements_dict.items():
                if hasattr(properties, key):
                    setattr(properties, key, value)

        session.add(properties)
        session.commit()
    
    def get_item_class_subtypes_and_display_names(self, session, item_class_name):
        """
        Get the subtypes and display names for a given item class.

        If the item class is not found, an empty list is returned. If the item class is found, but no subtypes are
        found, an empty list is returned. If the item class is found and subtypes are found, a list of tuples is
        returned. The first element of the tuple is the subtype name and the second element is the subtype display name.

        Args:
            session (): SQLAlchemy session.
            item_class_name (): The name of the item class.

        Returns:
            list: A list of tuples containing the subtype name and subtype display name.
        """
        subtype_display_names = []
        if item_class_name == 'Offhands':
            subtype_display_names = ['Quivers']
            return subtype_display_names
        elif item_class_name == 'One Hand Weapons':
            subtype_display_names = ['Claws', 'Daggers', 'One Hand Axes', 'One Hand Maces', 'One Hand Swords',
                                     'Rune Daggers', 'Sceptres', 'Thrusting One Hand Swords', 'Wands']
            return subtype_display_names
        elif item_class_name == 'Two Hand Weapons':
            subtype_display_names = ['Bows', 'Staves', 'Two Hand Axes', 'Two Hand Maces', 'Two Hand Swords',
                                     'Warstaves']
            return subtype_display_names
        elif item_class_name == 'Jewels':
            subtype_display_names = ['Abyss Jewels', 'Jewels']
            return subtype_display_names
        elif item_class_name == 'Jewellery':
            subtype_display_names = ['Amulets', 'Belts', 'Rings']
            return subtype_display_names
        elif item_class_name == 'Flasks':
            subtype_display_names = ['Life Flasks', 'Mana Flasks', 'Hybrid Flasks', 'Utility Flasks',
                                     'Critical Utility Flasks']
            return subtype_display_names
        else:
            item_class_obj = session.scalars(select(ItemClass).filter_by(
                display_name=item_class_name)).first()
            if item_class_obj is not None:
                item_class_subtypes = item_class_obj.item_class_subtypes
                
                for subtype in item_class_subtypes:
                    display_name = subtype.display_name
                    subtype_display_names.append(display_name)
            return subtype_display_names
    
    def get_item_class_id(self, session, item_class):
        """
        Get the id of an item class.

        Args:
            session (): SQLAlchemy session.
            item_class (): The name of the item class.

        Returns:
            int: The id of the item class.
        """
        item_class_id = session.scalars(select(ItemClass.id).filter_by(
            name=item_class)).first()
        return item_class_id
    
    def get_item_class_subtype_id(self, session, item_class_id, item_class_subtype):
        """
        Get the id of an item class subtype.

        Args:
            session (): SQLAlchemy session.
            item_class_id (): The id of the item class.
            item_class_subtype (): The name of the item class subtype.

        Returns:
            int: The id of the item class subtype.
        """
        item_class_subtype_id = session.scalars(select(ItemClassSubtype.id).filter(
            ItemClassSubtype.item_class_id == item_class_id,
            ItemClassSubtype.name == item_class_subtype)).first()
        return item_class_subtype_id
    
    def create_item_objects(self, session):
        item_data_list = self.item_parser.create_item_data_list()
        item_obj_list = []
        for item_data in item_data_list:
            try:
                item_obj = session.query(Item).filter_by(name=item_data.get('name')).one()
                item_obj_list.append(item_obj)
            except NoResultFound:
                item_obj = Item(name=item_data.get('name'))
    
    def create_item_requirement_object(self, session, item_obj, requirements):
        item_requirements_object_list = []
        for key, value in requirements.items():
            try:
                item_requirements_obj = session.query(ItemRequirement).filter_by(requirement_type=key).one()
                item_requirements_object_list.append(item_requirements_obj)
            except NoResultFound:
                item_requirements_object = ItemRequirement(requirement_type=key, _value=value, item=item_obj)
                item_requirements_object_list.append(item_requirements_object)
        return item_requirements_object_list
    
    def create_item_release_state_objects(self, session):
        item_release_state_objects_list = []
        release_state_list = self.item_parser.get_item_data_by_key('release_state')
        for release_state in release_state_list:
            try:
                item_release_state_object = session.query(ItemReleaseState).filter_by(name=release_state[
                    'release_state']).one()
                if item_release_state_object not in item_release_state_objects_list:
                    item_release_state_objects_list.append(item_release_state_object)
            except NoResultFound:
                item_release_state_object = ItemReleaseState(name=release_state['release_state'])
                if item_release_state_object not in item_release_state_objects_list:
                    item_release_state_objects_list.append(item_release_state_object)
        return item_release_state_objects_list


class ModManager:
    """
    Class for managing mods in the database and inserting new mods into the database.

    Attributes
    ----------
    mods_parser : ModParser
        ModParser object for parsing mods.json.
    data : dict
        Dictionary containing all mods from mods.json.
    mod_id_cache : dict
        Dictionary containing mod_id's for each mod.

    Methods
    -------
        insert_mods(self) -> None : Inserts all mods from mods.json into the database.
        insert_mod_types(self) -> None : Inserts all mod types from mods.json into the database.
        insert_mod_stat_values(self, session, mod_id, mod_stat_values) -> None : Inserts all mod stat values for the
        given mod_id into the database.
        insert_mod_groups(self) -> None : Inserts all mod groups from mods.json into the database.
        insert_mod_generation_types(self) -> None : Inserts all mod generation types from mods.json into the database.
        insert_mod_domains(self) -> None : Inserts all mod domains from mods.json into the database.
        get_mod_type_id(self, session, mod_type) -> int : Gets the mod_type_id for the given mod_type string from the
            database using the given session object and mod_type string. If the mod_type does not exist in the database,
            returns None.
    """
    
    def __init__(self):
        self.mods_parser = ModParser()
        self.mod_id_cache = {}  # Cache for mod_id lookups
    
    def get_mod_id(self, session, mod_name):
        """
        Gets the mod_id for the given mod name from the database using the given session object and mod_name
        string. If the mod does not exist in the database, returns None.

        Args:
            self ():
            mod_name (): Name of the mod to get the mod_id for from the mod_id_cache or database.

        Returns:
            mod_id (int): The mod_id for the given mod.
        """
        try:
            mod_id = self.mod_id_cache[mod_name]  # Check cache first
        except KeyError:  # If not in cache, query database and add to cache
            mod = session.query(Mod).filter_by(mod_name=mod_name).one_or_none()
        except NoResultFound:
            mod_id = None
        return mod_id
    
    def insert_mod_generation_types(self, session):
        """
        Inserts all mod generation types from mods.json into the database

        Args:
            self ():

        Returns:
            None
        """
        for generation_type in self.mods_parser.get_all_mod_data_for_key('generation_type'):
            try:
                session.query(GenerationType).filter_by(generation_type=generation_type.get(
                    'generation_type')).one()
            except NoResultFound:
                session.add(GenerationType(generation_type=generation_type.get('generation_type')))
        session.commit()
    
    # def insert_mod_stat_values(self, mod_id, stats_list):
    #     """
    #     Insert the stat values for a mod into the database. This is used for mods that have multiple stats such as
    #     +# to maximum Life and +# to maximum Mana" or "Adds # to # Cold Damage to Attacks with Daggers".
    #
    #     Args:
    #         mod_id (): The mod_id for the given mod
    #         stats_list (): List of dictionaries containing the stat values for the mod in the form of
    #             {'stat': 'stat_name', 'stat_min_value': 0, 'stat_max_value': 0}
    #
    #     Returns:
    #         None
    #     """
    #     all_mods = {mod.mod_name: mod for mod in self.session.scalars(select(Mod)).all()}
    #     all_stats = {stat.stat_name: stat for stat in self.session.scalars(select(Stat)).all()}
    #     mod_stat_list = []
    #     for stat_dict in stats_list:
    #         stat = all_stats[stat_dict.get('stat')]
    #         mod = all_mods[stat_dict.get('mod_name')]
    #         stat_min_value = stat_dict.get('stat_min_value')
    #         stat_max_value = stat_dict.get('stat_max_value')
    #         mod_stat_dict = {
    #             'mod_id': mod_id,
    #             'stat_id': stat.id,
    #             'stat_min_value': stat_min_value,
    #             'stat_max_value': stat_max_value
    #         }
    #         if mod_stat_dict not in mod_stat_list:
    #             mod_stat_list.append(mod_stat_dict)
    #     self.session.execute(insert(ModStatValue), mod_stat_list)
    
    def get_generation_type_id(self, generation_type):
        """
        Gets the generation_type_id for the given generation_type from the database using the given session object and
        generation_type string. If the generation_type does not exist in the database, returns None.

        Args:
            generation_type (): Name of the generation_type to get the generation_type_id for from the database

        Returns:
            generation_type_id (int): The generation_type_id for the given generation_type
        """
        try:
            generation_type_id = session.query(GenerationType.id).filter_by(
                generation_type=generation_type).scalar()
        except NoResultFound:
            generation_type_id = None
        return generation_type_id
    
    def get_generation_type_obj(self, session, generation_type):
        """
        Gets the generation_type object for the given generation_type from the database using the given session object
        and generation_type string. If the generation_type does not exist in the database, returns None.

        Args:
            generation_type (): Name of the generation_type to get the generation_type object for from the database

        Returns:
            generation_type_obj (ModGenerationType): The generation_type object for the given generation_type
        """
        try:
            generation_type_obj = session.query(GenerationType).filter_by(
                generation_type=generation_type).one_or_none()
        except NoResultFound:
            generation_type_obj = GenerationType(generation_type=generation_type)
            session.add(generation_type_obj)
        return generation_type_obj
    
    def create_domain_objects(self, session):
        domain_list = self.mods_parser.get_all_mod_data_for_key('domain')
        domain_obj_list = []
        for domain in domain_list:
            try:
                # Query the domain in the database
                domain = session.query(Domain).filter_by(name=domain.get('domain')).one()
                domain_obj_list.append(domain)
            except NoResultFound:
                # If not found, add it to the session
                domain = Domain(name=domain.get('domain'))
                domain_obj_list.append(domain)
        return domain_obj_list
    
    def get_domain_id(self, domain):
        """
        Gets the domain_id for the given domain from the database using the given session object and domain string. If
        the domain does not exist in the database, returns None.

        Args:
            domain (): Name of the domain to get the domain_id for from the database

        Returns:
            domain_id (int): The domain_id for the given domain
        """
        try:
            domain_id = self.session.query(Domain.id).filter_by(domain=domain).scalar()
        except NoResultFound:
            domain_id = None
        return domain_id
    
    def get_domain_obj(self, domain: str, domain_objects_list: list):
        """Gets the domain object for the given domain from a list of Domain objects.
        
        Args:
            domain (str): Name of the domain to get the domain object for from the database.
            domain_objects_list (list): List of Domain objects to search through.
        Returns:
            domain_obj (Domain): The domain object for the given domain. If the domain is not found, returns None.
        """
        for domain_obj in domain_objects_list:
            if domain_obj.name == domain:
                return domain_obj
        return None
    
    def insert_mod_types(self, session):
        """
        Inserts all mod types from mods.min./json into the database.

        Args:
            self ():

        Returns:
            None
        """
        mod_types_list = self.mods_parser.get_all_mod_data_for_key('type')
        session.execute(insert(ModType), mod_types_list)
        session.commit()
    
    def get_mod_attribute_id(self, attribute, value):
        """
        Gets the mod attribute id for the given attribute and value from the database using the given session object
        and attribute string. If the attribute does not exist in the database, returns None.

        Args:
            attribute (): Name of the attribute to get the attribute id for from the database
            value (): Value of the attribute to get the attribute id for from the database

        Returns:
            attribute_id (): The attribute id for the given attribute

        """
        try:
            attribute_id = self.session.query(attribute.id).filter_by(attribute=value).scalar()
        except NoResultFound:
            attribute_id = None
        return attribute_id
    
    def get_mod_attribute_obj(self, model_class, column_name, value):
        """
        Gets the mod attribute object for the given attribute and value from the database using the given session object
        and attribute string. If the attribute does not exist in the database, creates a new attribute object and
        returns it.

        Args:
            model_class (cls): SQLAlchemy model class to query.
            column_name (str): Name of the column to filter by.
            value (): Value to filter by.

        Returns:
            attribute_obj (): The attribute object for the given attribute
        """
        try:
            attribute_obj = session.query(model_class).filter(getattr(model_class, column_name) == value).one()
        except NoResultFound:
            attribute_obj = model_class(**{column_name: value})
            session.add(attribute_obj)
            session.flush()
        return attribute_obj
    
    def insert_mod_groups(self, session):
        """
        Inserts all mod groups from mods.json into the database.

        Args:
            self ():

        Returns:
            None
        """
        mod_groups_list = self.mods_parser.get_all_mod_groups()
        session.execute(insert(ModGroup), mod_groups_list)
        session.commit()
    
    def get_mod_group_id(self, group):
        """
        Gets the mod_group_id for the given group from the database using the given session object and group string. If
        the group does not exist in the database, returns None.

        Args:
            session (): sqlalchemy session object
            group (): Name of the group to get the mod_group_id for from the database

        Returns:
            mod_group_id (int): The mod_group_id for the given group
        """
        try:
            mod_group_id = self.session.query(ModGroup.id).filter_by(group=group).scalar()
        except NoResultFound:
            mod_group_id = None
        return mod_group_id
    
    def get_mod_group_obj(self, group):
        """
        Gets the mod group object for the given group from the database using the given session object and group string.
        If the group does not exist in the database, creates a new group object and returns it.

        Args:
            group (): Name of the group to get the mod group object for from the database

        Returns:
            mod_group_obj (): The mod group object for the given group
        """
        try:
            mod_group_obj = self.session.query(ModGroup).filter_by(group=group).one_or_none()
        except NoResultFound:
            mod_group_obj = ModGroup(group=group)
            self.session.add(mod_group_obj)
        return mod_group_obj
    
    def insert_mods(self, session):
        """
        Inserts all mods from mods.json into the database. If the mod already exists in the database, it is skipped.

        When querying the database tables for the ids of the mod's domain, generation_type, mod_type, and mod_group,
        the query is done using the sqlalchemy session object and the name of the domain, generation_type, mod_type,
        and mod_group. If the domain, generation_type, mod_type, or mod_group does not exist in the database, it is
        inserted into the database. If the domain, generation_type, mod_type, or mod_group does exist in the database,
        the id is retrieved from the database.

        Args:
            self ():

        Returns:
            None
        """
        all_domains = {domain.name: domain for domain in session.scalars(select(Domain)).all()}
        
        all_generation_types = {generation_type.generation_type: generation_type for
                                generation_type in session.scalars(select(GenerationType)).all()}
        all_mod_types = {mod_type.type: mod_type for mod_type in session.scalars(select(ModType)).all()}
        all_mod_groups = {mod_group.group: mod_group for mod_group in session.scalars(select(ModGroup)).all()}
        all_tags = {tag.tag: tag for tag in session.scalars(select(Tag)).all()}
        all_stats = {stat.name: stat for stat in session.scalars(select(Stat)).all()}
        mod_dicts = self.mods_parser.get_all_mod_dicts()
        mod_obj_list = []
        for mod, mod_data in mod_dicts.items():
            mod_domain = all_domains[mod_data.get('domain')]
            mod_generation_type = all_generation_types[mod_data.get('generation_type')]
            mod_group = all_mod_groups[mod_data.get('group')]
            mod_type = all_mod_types[mod_data.get('type')]
            mod_obj = Mod(
                mod_name=mod,
                level_req=mod_data.get('level_req'),
                name=mod_data.get('name'),
                essence_only=mod_data.get('is_essence_only'),
                domain_id=mod_domain.id,
                domain=mod_domain,
                generation_type_id=mod_generation_type.id,
                generation_type=mod_generation_type,
                mod_group_id=mod_group.id,
                mod_group=mod_group,
                mod_type_id=mod_type.id,
                mod_type=mod_type,
                adds_tags=[all_tags[tag] for tag in mod_data.get('added_tags_list')],
                implicit_tags=[all_tags[tag] for tag in mod_data.get('implicit_tags_list')]
            )
            session.add(mod_obj)
            for stat in mod_data.get('stats_list'):
                stat_min_value = stat['values']['min']
                stat_max_value = stat['values']['max']
                stat_value_obj = StatValue(stat=all_stats[stat['stat']], mod=mod_obj,
                                           stat_min_value=stat_min_value,
                                           stat_max_value=stat_max_value)
                session.add(stat_value_obj)
                mod_obj.stat_values.append(stat_value_obj)
            mod_obj_list.append(mod_obj)
        session.add_all(mod_obj_list)
        
        session.commit()
    
    # def create_mod_objects(self, session, domain_obj_list, tag_obj_list, stat_obj_list):
    #
    #     mod_dict_list = self.mods_parser.get_all_mod_dicts()
    #     mod_obj_list = []
    #     for mod, mod_data in mod_dict_list.items():
    #         try:
    #             mod_obj = session.query(Mod).filter_by(name=mod).one()
    #             if mod_obj not in mod_obj_list:
    #                 mod_obj_list.append(mod_obj)
    #         except NoResultFound:
    #             mod_obj = Mod(name=mod)
    #             domain_obj = self.get_domain_obj(mod_data.get('domain'), domain_obj_list)
    #             mod_obj.domain = domain_obj
    #             session.add(mod_obj)
    #             session.flush()
    #             for tag in mod_data.get('spawn_weights_list'):
    #                 tag_obj = self.get_tag_obj(tag.get('tag'), tag_obj_list)
    #                 session.execute(insert(mod_tag_weights_association).values(mod_id=mod_obj.id, tag_id=tag_obj.id,
    #                                                                            weight=tag.get('weight')))
    #
    #                 mod_obj.tags.append(tag_obj)
    #             if mod_data.get('adds_tags_list') is not None:
    #                 for tag in mod_data.get('added_tags_list'):
    #                     tag_obj = self.get_tag_obj(tag, tag_obj_list)
    #                     mod_obj.adds_tags.append(tag_obj)
    #             if mod_data.get('implicit_tags_list') is not None:
    #                 for tag in mod_data.get('implicit_tags_list'):
    #                     tag_obj = self.get_tag_obj(tag, tag_obj_list)
    #                     mod_obj.implicit_tags.append(tag_obj)
    #             for stat in mod_data.get('stats_list'):
    #                 stat_obj = self.get_stat_obj(stat.get('stat'), stat_obj_list)
    #                 session.execute(insert(mod_stats_association).values(mod_id=mod_obj.id, stat_id=stat_obj.id,
    #                                                                      stat_min_value=stat.get('values').get('min'),
    #                                                                      stat_max_value=stat.get('values').get('max')))
    #                 mod_obj.stats.append(stat_obj)
    #             mod_obj.mod_type = self.get_mod_attribute_obj(ModType, 'type', mod_data.get('type'))
    #             mod_obj.mod_group = self.get_mod_attribute_obj(ModGroup, 'group', mod_data.get('group'))
    #             mod_obj.generation_type = self.get_mod_attribute_obj(GenerationType, 'generation_type',
    #                                                                  mod_data.get('generation_type'))
    #
    #             mod_obj_list.append(mod_obj)
    #     return mod_obj_list
    
    def get_tag_obj(self, tag, tag_obj_list):
        for tag_obj in tag_obj_list:
            if tag_obj.tag == tag:
                return tag_obj
        return None
    
    def get_stat_obj(self, stat, stat_obj_list):
        for stat_obj in stat_obj_list:
            if stat_obj.name == stat:
                return stat_obj
        return None
    
    def create_mod_type_objects(self, session):
        pass
    
    def create_mod_group_objects(self, session):
        pass
    
    def create_mod_generation_type_objects(self, session):
        pass


if __name__ == "__main__":
    db_manager = DatabaseManager()
    with db_manager.transaction() as session:
        db_manager.drop_tables()
        db_manager.create_tables()
        db_manager.mods_manager.insert_mod_generation_types(session)
        db_manager.mods_manager.insert_mod_groups(session)
        db_manager.mods_manager.insert_mod_types(session)
        tags_obj_list = db_manager.tags_manager.create_tag_objects(session)
        session.add_all(tags_obj_list)
        domain_obj_list = db_manager.mods_manager.create_domain_objects(session)
        session.add_all(domain_obj_list)
        stat_obj_list = db_manager.stats_manager.create_stat_objects(session)
        session.add_all(stat_obj_list)
    session.commit()
    with db_manager.transaction() as session:
        db_manager.mods_manager.insert_mods(session)
    session.commit()
