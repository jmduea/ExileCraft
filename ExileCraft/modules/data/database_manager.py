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

from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from modules.config.constants import domain_whitelist, generation_type_whitelist
from modules.data.models.association_models import item_tags_association, item_implicits_association
from modules.data.models.base_model import Base
from modules.data.models.global_models import Domain, GenerationType
from modules.data.models.item_models import Item, ItemClass, VisualIdentity, ItemClassSubtype, ItemProperties, \
    EvasionBase, EnergyShieldBase, ArmourBase, ArmourEvasionBase, ArmourEnergyShieldBase, ArmourEvasionEnergyShieldBase, \
    EvasionEnergyShieldBase, WardBase, OneHandWeapon, TwoHandWeapon, Flask
from modules.data.models.mod_models import Mod, ModType
from modules.data.models.stat_models import Stat
from modules.data.models.tag_models import Tag
from modules.data.parser import item_class_parser, stats_parser, tags_parser, mods_parser, base_items_parser, \
    stat_translations_parser

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'exilecraft.db')
db_url = f"sqlite:///{db_path}"


class DatabaseManager:
    """
    The DatabaseManager class provides an interface for interacting with a database.
    It provides basic CRUD operations, session management and a mechanism for working
    with transactions.
    """
    
    def __init__(self, db_url):
        """
        Initialize a new DatabaseManager instance.

        Args:
            db_url (str): The URL for the database.
        """
        self.engine = create_engine(db_url, echo=False)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)
    
    def create_tables(self):
        """
        Create all tables in the database as defined in the Base model class.
        """
        Base.metadata.create_all(self.engine)
    
    def drop_tables(self):
        """
        Drop all tables from the database.
        """
        Base.metadata.reflect(self.engine)
        Base.metadata.drop_all(self.engine)
    
    def get_session(self):
        """
        Get a new session with the database.

        Returns:
            Session: An instance of a SQLAlchemy Session.
        """
        return self.Session()
    
    def add_record(self, record):
        """
        Add a new record to the database.

        Args:
            record (Base): The record to add.
        """
        with self.transaction() as session:
            session.add(record)
            session.flush()
    
    def get_record(self, model, record_id):
        """
        Get a record from the database.

        Args:
            model (Base): The model class the record belongs to.
            record_id: The id of the record.

        Returns:
            record: The requested record.
        """
        session = self.get_session()
        record = session.query(model).filter(model.id == record_id).one_or_none()
        return record
    
    def update_record(self, model, record_id, **kwargs):
        """
        Update a record in the database.

        Args:
            model (Base): The model class the record belongs to.
            record_id: The id of the record.
            **kwargs: Arbitrary keyword arguments.
        """
        session = self.get_session()
        session.query(model).filter_by(id=record_id).update(kwargs)
        session.commit()
    
    def delete_record(self, model, record_id):
        """
        Delete a record from the database.

        Args:
            model (Base): The model class the record belongs to.
            record_id: The id of the record.
        """
        session = self.get_session()
        record = session.query(model).get(record_id)
        session.delete(record)
        session.flush()
    
    @contextlib.contextmanager
    def transaction(self):
        """
        Start a new transaction with the database. This method is intended to be used
        with the 'with' keyword in Python.

        Yields:
            Session: An instance of a SQLAlchemy Session.

        Raises:
            Exception: If there was an error during the transaction.
        """
        session = self.get_session()
        try:
            yield session
            session.flush()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def close_session(self):
        """
        Close the current session with the database.
        """
        self.Session.remove()
    
    ####################################################################################################################
    # ASSOCIATION MODEL INSERT METHODS
    ####################################################################################################################
    @staticmethod
    def insert_item_tags(session, tag_list, item_id):
        for tag in tag_list:
            tag_id = db_manager.get_tag(session, tag)
            insert_stmt = insert(item_tags_association).values(tag_id=tag_id, item_id=item_id)
            session.execute(insert_stmt)
            session.commit()
    
    @staticmethod
    def insert_item_implicits(session, implicit_list, item_id):
        for implicit in implicit_list:
            mod_id = db_manager.get_mod(session, implicit)
            insert_stmt = insert(item_implicits_association).values(mod_id=mod_id, item_id=item_id)
            session.execute(insert_stmt)
            session.commit()
    
    ##########################################################################################
    # BASE ITEM TYPE METHODS
    ##########################################################################################
    
    @staticmethod
    def add_or_update_base_item_type(base_item_dict, session):
        """
        Try to find a base item type in the database using its meta_data_id, if found, update it with new values
        provided in the base_item_dict, if not found, create a new record in the database.

        Args:
            base_item_dict (dict): A dictionary containing key-value pairs that represent the attributes
             of a BaseItem.
            session (Session): SQLAlchemy Session for database operations.

        Returns:
            BaseItemTypes: The added or updated BaseItemType object.
        """
        try:
            # try to find the record in the database
            base_item = session.query(Item).filter(Item.meta_data_id
                                                   == base_item_dict["meta_data_id"]).one()
            # if found, update its attributes
            for attr, new_value in base_item_dict.items():
                setattr(base_item, attr, new_value)
        except NoResultFound:
            # if not found, create a new record
            base_item = Item(**base_item_dict)
            session.add(base_item)
        return base_item
    
    @staticmethod
    def add_item_classes(item_class_dict, session):
        """
        Try to find an item class in the database using its display_name,
        if not found, create a new record in the database.

        Args:
            item_class_dict (dict): A dictionary containing key-value pairs that represent the attributes
             of an ItemClass.
            session (Session): SQLAlchemy Session for database operations.

        """
        
        try:
            item_class = session.query(ItemClass).filter(ItemClass.name
                                                         == item_class_dict["name"]).one()
        except NoResultFound:
            item_class = ItemClass(**item_class_dict)
            session.add(item_class)
    
    @staticmethod
    def insert_item_properties(session, item_id, item_class_id, item_class_subtype, item_class_subtype_id,
                               item_properties_dict, item_requirements_dict):
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
        subclass = subclasses.get(item_class_subtype, ItemProperties)
        
        properties = subclass()
        properties.id = item_id
        properties.item_class_id = item_class_id
        properties.item_class_subtype_id = item_class_subtype_id
        
        # Add data from item_properties_dict to properties if attribute exists in subclass
        if item_properties_dict is not None:
            for key, value in item_properties_dict.items():
                if hasattr(properties, key):
                    setattr(properties, key, value)
        
        # Add data from item_requirements_dict to properties if attribute exists in subclass
        for key, value in item_requirements_dict.items():
            if hasattr(properties, key):
                setattr(properties, key, value)
        
        session.add(properties)
        session.commit()
    
    #######################################################################################
    # TAGS METHODS
    #######################################################################################
    @staticmethod
    def add_or_update_tag(tag_dict, session):
        """
        Try to find a tag in the database using its tag_id, if found, update it with new values
        provided in the tag_dict, if not found, create a new record in the database.

        Args:
            tag_dict (dict): A dictionary containing key-value pairs that represent the attributes of a Tag.
            session (Session): SQLAlchemy Session for database operations.

        Returns:
            Tags: The added or updated Tag object.
        """
        try:
            # try to find the record in the database
            tag = session.query(Tag).filter(Tag.tag == tag_dict["tag"]).one()
            # if found, update its attributes
            for attr, new_value in tag_dict.items():
                setattr(tag, attr, new_value)
        except NoResultFound:
            # if not found, create a new record
            tag = Tag(**tag_dict)
            session.add(tag)
        return tag
    
    #######################################################################################
    # MOD METHODS
    #######################################################################################
    
    @staticmethod
    def add_or_update_mod(mod_dict, session):
        """
        Try to find a mod in the database using its mod_id, if found, update it with new values
        provided in the mod_dict, if not found, create a new record in the database.

        Args:
            mod_dict (dict): A dictionary containing key-value pairs that represent the attributes of a Mod.
            session (Session): SQLAlchemy Session for database operations.

        Returns:
            Mods: The added or updated Mod object.
        """
        try:
            # try to find the record in the database
            mod = session.query(Mod).filter(Mod.mod == mod_dict["mod"]).one()
            # if found, update its attributes
            for attr, new_value in mod_dict.items():
                setattr(mod, attr, new_value)
        except NoResultFound:
            # if not found, create a new record
            mod = Mod(**mod_dict)
            session.add(mod)
        return mod
    
    @staticmethod
    def add_or_update_mod_type(type_dict, session):
        """
        Try to find a mod type in the database using its mod_type, if found, update it with new values
        provided in the type_dict, if not found, create a new record in the database.

        Args:
            type_dict (dict): A dictionary containing key-value pairs that represent the attributes of a ModType.
            session (Session): SQLAlchemy Session for database operations.

        Returns:
            ModTypes: The added or updated ModType object.
        """
        try:
            # try to find the record in the database
            mod_type = session.query(ModType).filter(ModType.mod_type == type_dict["mod_type"]).one()
            # if found, update its attributes
            for attr, new_value in type_dict.items():
                setattr(mod_type, attr, new_value)
        except NoResultFound:
            # if not found, create a new record
            mod_type = ModType(**type_dict)
            session.add(mod_type)
        return mod_type
    
    @staticmethod
    def insert_domains(domain_whitelist, session):
        """
        Insert domains into the database using the provided list. If an error occurs during the process,
        it rolls back the session and prints the error.
        
        Args:
            domain_whitelist (list): A list of domains.
            session (Session): SQLAlchemy Session for database operations.
        """
        try:
            for domain in domain_whitelist:
                domain_record = Domain(domain=domain)
                session.add(domain_record)
            
            # Commit changes
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()
    
    @staticmethod
    def get_domain(session, item_domain):
        """
        Get the domain id from the database using the item domain name. If an error occurs during the process,
        it rolls back the session and prints the error.
        
        Args:
            item_domain (str): domain name for an item of interest
            session (Session): SQLAlchemy Session for database operations.

        Returns:
            domain_id
        """
        try:
            domain = session.query(Domain).filter_by(domain=item_domain).first()
            domain_id = domain.id
            return domain_id
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
    
    @staticmethod
    def insert_generation_types(generation_type_whitelist, session):
        """
        Insert generation types into the database using the provided list. If an error occurs during the
        process, it rolls back the session and prints the error.

        Args:
            generation_type_whitelist (list): A list of generation types.
            session (Session): SQLAlchemy Session for database operations.
        """
        try:
            for gen_type in generation_type_whitelist:
                gen_type_record = GenerationType(generation_type=gen_type)
                session.add(gen_type_record)
            
            # Commit changes
            session.commit()
            print("Domains and Generation Types inserted successfully.")
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()
    
    #######################################################################################
    # STAT METHODS
    #######################################################################################
    
    @staticmethod
    def add_or_update_stat(stat_dict, session):
        """
        Try to find a stat in the database using its stat_id, if found, update it with new values
        provided in the stat_dict, if not found, create a new record in the database.

        Args:
            stat_dict (dict): A dictionary containing key-value pairs that represent the attributes of a Stat.
            session (Session): SQLAlchemy Session for database operations.

        Returns:
            Stats: The added or updated Stat object.
        """
        try:
            # try to find the record in the database
            stat = session.query(Stat).filter(Stat.stat == stat_dict["stat"]).one()
            # if found, update its attributes
            for attr, new_value in stat_dict.items():
                setattr(stat, attr, new_value)
        except NoResultFound:
            # if not found, create a new record
            stat = Stat(**stat_dict)
            session.add(stat)
        return stat
    
    #################################################################################################################
    # QUERY METHODS
    #################################################################################################################
    @staticmethod
    def get_visual_identity_id(session, visual_identity):
        """
        Checks for a record for the visual_identity, if none is found creates a record and commits it to the
        database. After obtaining the visual_identity record, gets the id for that record and returns it.
        Args:
            session (Session): SQLAlchemy Session for database operations.
            visual_identity (str): The name of the item's visual identity as a string.
        Returns:
            visual_identity_id (int): id of the current item's visual_identity
        """
        try:
            visual_identity = session.query(VisualIdentity).filter_by(visual_identity=visual_identity).first()
        except NoResultFound:
            visual_identity = VisualIdentity(visual_identity=visual_identity)
            session.add(visual_identity)
            session.commit()
        finally:
            visual_identity_id = visual_identity.id
        return visual_identity_id
    
    @staticmethod
    def get_item_class(session, item_class):
        """
        Get the item_class record from the database using item_class string.
        Args:
            session (Session): SQLAlchemy Session for database operations.
            item_class (str): The item class name as a string.
        Returns:
            item_class_id: id of the current item_class being parsed
        """
        item_class = session.query(ItemClass).filter_by(name=item_class).first()
        item_class_id = item_class.id
        return item_class_id
    
    @staticmethod
    def get_item_class_subtype(session, item_class_id, item_class_subtype) -> int:
        """
        Get the item_class_subtype record from the database using the item_class_id and item_class_subtype string.
        
        Args:
            session (Session): SQLAlchemy Session for database operations.
            item_class_id (int): The id of the row for the corresponding item_class.
            item_class_subtype (str): The name of the item_class_subtype found from the armour_subtypes dictionary.

        Returns:
            item_class_subtype_id (int): The id of the row for the corresponding item_class_subtype.
        """
        item_class_subtype_row = session.query(ItemClassSubtype).filter(
            ItemClassSubtype.item_class_id == item_class_id, ItemClassSubtype.name == item_class_subtype).first()
        if item_class_subtype_row is not None:
            item_class_subtype_id = item_class_subtype_row.id
            return item_class_subtype_id
    
    @staticmethod
    def get_tag(session, tag):
        """
        Get the item_class record from the database using item_class string.
        Args:
            session (Session): SQLAlchemy Session for database operations.
            tag (str): The tag name as a string.
        Returns:
            tag_id: The id of the row for the corresponding tag.
        """
        tag_row = session.query(Tag).filter_by(tag=tag).first()
        tag_id = tag_row.id
        return tag_id
    
    @staticmethod
    def get_mod(session, implicit):
        mod_row = session.query(Mod).filter_by(mod=implicit).first()
        mod_id = mod_row.id
        return mod_id
    
    @staticmethod
    def get_item_class_subtypes_and_display_names(session, item_class_name):
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
            item_class = session.query(ItemClass).filter_by(display_name=item_class_name).first()
            if item_class is not None:
                item_class_subtypes = item_class.subtypes
                
                for subtype in item_class_subtypes:
                    display_name = subtype.display_name
                    subtype_display_names.append(display_name)
            return subtype_display_names
    
    @staticmethod
    def get_base_items_from_subtype_display_name(session, subtype_display_name):
        subtype_record = session.query(ItemClassSubtype).filter_by(
            display_name=subtype_display_name).first()
        
        if subtype_record is not None:
            base_items = session.query(Item).filter_by(item_class_subtype_id=subtype_record.id).all()
            return base_items
    
    @staticmethod
    def get_base_items(session, item_class_id):
        """
        Fetch all base items from the database that belong to the provided item class id.

        Args:
            session (Session): SQLAlchemy Session for database operations.
            item_class_id (int): The id of the item class whose base items are to be fetched.

        Returns:
            list: List of base items for the given item class id.
        """
        return session.query(Item).filter(Item.item_class_id == item_class_id).all()


if __name__ == "__main__":
    db_manager = DatabaseManager(db_url)
    session = db_manager.get_session()
    db_manager.drop_tables()
    db_manager.create_tables()
    db_manager.insert_domains(domain_whitelist, session)
    db_manager.insert_generation_types(generation_type_whitelist, session)
    tags_parser.insert_tags_into_db(db_manager)
    item_class_parser.insert_item_classes_into_db(db_manager)
    stats_parser.insert_stats_into_db(db_manager)
    stat_translations_parser.insert_stat_translations_into_db(db_manager)
    mods_parser.insert_mods_into_db(db_manager)
    base_items_parser.insert_visual_identities_into_db(db_manager)
    base_items_parser.get_item_info(db_manager)
    # fossils_parser.insert_fossils_into_db(db_manager)
    
    # for item in session.query(Item).filter(Item.has_tag('dex_int_armour')):
    #     print(item.name)
