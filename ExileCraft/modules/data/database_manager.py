# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"),
#  to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE
#  SOFTWARE.
# ##############################################################################

import contextlib
import os
import re

from sqlalchemy import and_
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import scoped_session, Session, sessionmaker

from modules.data.models.base_model import Base
from modules.data.models.item_models import Item
from modules.data.models.item_models import ItemClass
from modules.data.models.item_models import ItemClassSubtype
from modules.data.models.item_models import ItemReleaseState
from modules.data.models.item_models import ItemVisualIdentity
from modules.data.models.mod_models import GenerationType
from modules.data.models.mod_models import Mod
from modules.data.models.mod_models import ModGroup
from modules.data.models.mod_models import ModSpawnWeight
from modules.data.models.mod_models import ModType
from modules.data.models.shared_models import Domain
from modules.data.models.stat_models import Stat
from modules.data.models.tag_models import Tag
from modules.data.models.translation_models import Translation
from modules.data.parser.base_items_parser import ItemParser
from modules.data.parser.item_class_parser import ItemClassParser
from modules.data.parser.mods_parser import ModParser
from modules.data.parser.stat_translations_parser import StatTranslationParser
from modules.data.parser.stats_parser import StatParser
from modules.data.parser.tags_parser import TagsParser

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "exilecraft.db")
db_url = f"sqlite:///{db_path}"


class DatabaseManager:
    """The DatabaseManager class is responsible for managing the database
    connection and transactions.

    Attributes: engine (Engine): The SQLAlchemy Engine instance.
    session_factory (SessionFactory): The SQLAlchemy SessionFactory
    instance. session (Session): The SQLAlchemy Session instance.
    """

    def __init__(self, db_url=db_url, **kwargs):
        """The constructor for the DatabaseManager class."""
        self.engine = create_engine(db_url, echo=True)
        self.session_factory = sessionmaker(
            bind=self.engine, expire_on_commit=False, autoflush=False, autocommit=False
        )
        self.session = scoped_session(self.session_factory)

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
        Provide a transactional scope around a series of operations. If an
        error occurs during the transaction,
        the session is rolled back. If no error occurs, the session is
        committed.

        Returns:
            Session: An instance of a SQLAlchemy Session.
        """
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
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
        session.add_all(tag_obj_list)
        return tag_obj_list

    @staticmethod
    def get_tag_object(tag_name):
        session = db_manager.get_session()
        try:
            return session.query(Tag).filter_by(tag=tag_name).one()
        except NoResultFound:
            return None


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
                stat_obj = session.query(Stat).filter_by(name=stat.get("name")).one()
                stat_obj_list.append(stat_obj)
            except NoResultFound:
                stat_obj = Stat(
                    name=stat.get("name"),
                    is_aliased=stat.get("is_aliased", False),
                    is_local=stat.get("is_local", False),
                )
                stat_obj_list.append(stat_obj)
        session.add_all(stat_obj_list)
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
    def __init__(self):
        self.translation_parser = StatTranslationParser()
        self.translation_obj_list = []

    def create_translation_objects(self, session):
        mods = session.scalars(select(Mod)).all()
        data = self.translation_parser.parse_json()

        for mod in mods:
            self.create_translation_for_mod(mod, data)
        session.add_all(self.translation_obj_list)

    def create_translation_for_mod(self, mod, data):
        stat_values = mod.stat_values

        min_values = [stat.stat_min_value for stat in stat_values]
        max_values = [stat.stat_max_value for stat in stat_values]

        translation_data = [
            self.get_translation_data(stat, data) for stat in stat_values
        ]
        translation_data = [
            t for t in translation_data if t is not None
        ]  # Filter out None values

        if translation_data:  # If there is at least one translation_data
            self.create_translation(
                mod, stat_values[0], min_values, max_values, translation_data[0]
            )

    def get_translation_data(self, stat, data):
        stat_obj = stat.stat
        stat_name = stat_obj.name
        for item in data:
            if stat_name in item["ids"]:
                return item["English"]
        return None

    def create_translation(self, mod, stat, min_values, max_values, translation_data):
        translations = set()  # Use a set to automatically eliminate duplicates
        for translation in translation_data:
            conditions = translation["condition"]

            # Initialize flags for matching conditions
            min_condition_matched = False
            max_condition_matched = False

            for i, condition in enumerate(conditions):
                # Skip this iteration if the index is out of range for min_values or max_values
                if i >= len(min_values) or i >= len(max_values):
                    continue

                min_condition = condition.get("min", float("-inf"))
                max_condition = condition.get("max", float("inf"))

                # Check if condition matches for both min and max values
                if (
                    min_condition <= min_values[i] <= max_condition
                    and min_condition <= max_values[i] <= max_condition
                ):
                    min_condition_matched = True
                    max_condition_matched = True

                # Check if condition matches for at least one value
                elif (
                    min_condition <= min_values[i] <= max_condition
                    or min_condition <= max_values[i] <= max_condition
                ):
                    min_condition_matched = True

            # If no condition matches for both values, continue to the next translation
            if not min_condition_matched and not max_condition_matched:
                continue

            hidden = "hidden" in translation
            formatted_string = self.get_formatted_string(
                translation, min_values, max_values
            )
            translations.add(formatted_string)  # Add to the set of translations

        if translations:
            # Join all unique translations into a single string
            formatted_string = " ".join(translations)
            self.create_and_append_translation(mod, hidden, formatted_string)

    def get_formatted_string(self, translation, min_values, max_values):
        translation_string = translation["string"]
        formats = translation["format"]
        formatted_values = [
            self.get_formatted_values(format, min_value, max_value)
            for format, min_value, max_value in zip(formats, min_values, max_values)
        ]

        # Create a dictionary of replacements
        replacements = {
            str(i): f"({fv[0]} to {fv[1]})" for i, fv in enumerate(formatted_values)
        }

        # Replace placeholders with corresponding formatted values, or with empty string if not
        # available
        formatted_string = re.sub(
            "{(\d*)}", lambda m: replacements.get(m.group(1), ""), translation_string
        )

        return formatted_string

    def get_formatted_values(self, format, min_value, max_value):
        if format == "#":
            formatted_min_value = str(min_value)
            formatted_max_value = str(max_value)
        elif format == "+#":
            formatted_min_value = (
                "+" + str(min_value) if min_value >= 0 else str(min_value)
            )
            formatted_max_value = (
                "+" + str(max_value) if max_value >= 0 else str(max_value)
            )
        elif format == "ignore":
            formatted_min_value = ""
            formatted_max_value = ""
        return formatted_min_value, formatted_max_value

    def create_and_append_translation(self, mod, hidden, formatted_string):
        translation_obj = Translation(hidden=hidden, string=formatted_string, mod=mod)
        self.translation_obj_list.append(translation_obj)


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
        """Constructor for the ItemManager class that initializes the
        ItemParser object."""
        self.item_parser = ItemParser()
        self.item_class_parser = ItemClassParser()

    def create_item_class_objects(self, session):
        """
        Insert item classes into the database. This is a generic method that
        can be used for all item types.

        Returns:
            item_class_obj_list (list): A list of item class objects.
        """
        item_class_list = self.item_class_parser.create_item_class_list()
        item_class_obj_list = []
        for _dict in item_class_list:
            item_class_name = _dict["name"]
            try:
                item_class_obj = session.scalars(
                    select(ItemClass).filter_by(name=item_class_name)
                ).one()
                item_class_obj_list.append(item_class_obj)
            except NoResultFound:
                item_class_obj = ItemClass(**_dict)
                item_class_obj_list.append(item_class_obj)
        session.add_all(item_class_obj_list)
        return item_class_obj_list

    def create_visual_identity_objects(self, session):
        visual_identity_list = self.item_parser.get_item_data_by_key("visual_identity")
        visual_identity_obj_list = []
        for _dict in visual_identity_list:
            try:
                visual_identity_obj = (
                    session.query(ItemVisualIdentity)
                    .filter_by(name=_dict["visual_identity"].get("id", None))
                    .one()
                )
                if visual_identity_obj not in visual_identity_obj_list:
                    visual_identity_obj_list.append(visual_identity_obj)
            except NoResultFound:
                visual_identity_obj = ItemVisualIdentity(
                    name=_dict["visual_identity"].get("id", None),
                    dds_file=_dict["visual_identity"].get("dds_file", None),
                )
                if visual_identity_obj not in visual_identity_obj_list:
                    visual_identity_obj_list.append(visual_identity_obj)
        session.add_all(visual_identity_obj_list)
        return visual_identity_obj_list

    # def insert_base_items(self, session):
    #     """
    #     Insert base items into the database. This is a generic method that
    #     can be used for all item types.
    #
    #     Args:
    #         session (): SQLAlchemy session object.
    #
    #     Returns:
    #         None
    #     """
    #     data = self.data
    #     for item, item_data in data.items():
    #         # Get the domain_id
    #         domain = item_data.get('domain')
    #         domain_id = db_manager.mods_manager.get_domain_id(domain)
    #
    #         item_class = item_data.get('item_class')
    #         # Get the item_class_id
    #         item_class_id = db_manager.items_manager.get_item_class_id(session, item_class)
    #
    #         tag_list = item_data.get("tags")
    #         item_class_subtype = self.item_parser.get_item_class_subtype(item_class, tag_list)
    #         # Get the item_class_subtype_id using the item_class_id and
    #         # subtype name from item_class_subtype
    #         item_class_subtype_id = db_manager.items_manager.get_item_class_subtype_id(session,
    #                                                                                    item_class_id,
    #                                                                                    item_class_subtype)
    #
    #         visual_identity = item_data.get("visual_identity").get("id")
    #         # Get the visual_identity_id
    #         visual_identity_id = db_manager.items_manager.get_visual_identity_id(session,
    #                                                                              visual_identity)
    #
    #         name = item_data.get("name")
    #         drop_level = item_data.get("drop_level")
    #
    #         item_obj = session.scalars(select(Item).filter_by(meta_data_id=item)).first()
    #         if item_obj:
    #             continue
    #         else:
    #             item_dict = {"visual_identity_id": visual_identity_id, "name": name,
    #                          "meta_data_id": item, "item_class_id": item_class_id,
    #                          "item_class_subtype_id": item_class_subtype_id, "domain_id":
    #                          domain_id,
    #                          "drop_level": drop_level, "rarity": 'Normal', "is_corrupted": False}
    #             item = Item(**item_dict)
    #             session.add(item)
    #             session.flush()
    #             item_id = item.id
    #
    #             db_manager.items_manager.insert_item_tags(session, tag_list, item_id)
    #             implicit_list = item_data.get("implicits")
    #             self.insert_item_implicits(session, implicit_list, item_id)
    #             item_properties_dict = item_data.get("properties")
    #             item_requirements_dict = item_data.get("requirements")
    #             self.insert_item_properties(session, item_id, item_class_id, item_class_subtype,
    #                                         item_class_subtype_id, item_properties_dict,
    #                                         item_requirements_dict, drop_level)
    #     session.commit()

    @staticmethod
    def get_visual_identity_id(session, visual_identity):
        """
        Get visual identity id from the database.

        Args:
            session (): SQLAlchemy session object.
            visual_identity (): Visual identity.

        Returns:
            Visual identity id.
        """
        visual_identity_id = session.scalars(
            select(ItemVisualIdentity.id).filter_by(visual_identity=visual_identity)
        ).first()
        return visual_identity_id

    @staticmethod
    def get_base_items(session, item_class_id):
        """
        Get base items from the database.
        Args:
            session (): SQLAlchemy session object.
            item_class_id (): Item class id.
        Returns:
            List of base item objects.
        """
        return select(Item).filter(Item.item_class_id == item_class_id).all()

    @staticmethod
    def get_base_items_from_subtype_display_name(session, subtype_display_name):
        """
        Get base items from the database.

        Args:
            session (): SQLAlchemy session object.
            subtype_display_name (): Display name of the item class subtype.

        Returns:
            List of base item objects.
        """
        subtype_id = session.scalars(
            select(ItemClassSubtype.id).filter_by(display_name=subtype_display_name)
        ).first()

        if subtype_id is not None:
            base_item_objs = session.scalars(
                select(Item)
                .filter_by(item_class_subtype_id=subtype_id)
                .order_by(Item.drop_level)
            ).all()
            return base_item_objs

    @staticmethod
    def get_item_class_subtypes_and_display_names(session, item_class_name):
        """
        Get the subtypes and display names for a given item class.

        If the item class is not found, an empty list is returned. If the
        item class is found, but no subtypes are
        found, an empty list is returned. If the item class is found and
        subtypes are found, a list of tuples is
        returned. The first element of the tuple is the subtype name and the
        second element is the subtype display name.

        Args:
            session (): SQLAlchemy session.
            item_class_name (): The name of the item class.

        Returns:
            list: A list of tuples containing the subtype name and subtype
            display name.
        """
        subtype_display_names = []
        if item_class_name == "Offhands":
            subtype_display_names = ["Quivers"]
            return subtype_display_names
        elif item_class_name == "One Hand Weapons":
            subtype_display_names = [
                "Claws",
                "Daggers",
                "One Hand Axes",
                "One Hand Maces",
                "One Hand Swords",
                "Rune Daggers",
                "Sceptres",
                "Thrusting One Hand Swords",
                "Wands",
            ]
            return subtype_display_names
        elif item_class_name == "Two Hand Weapons":
            subtype_display_names = [
                "Bows",
                "Staves",
                "Two Hand Axes",
                "Two Hand Maces",
                "Two Hand Swords",
                "Warstaves",
            ]
            return subtype_display_names
        elif item_class_name == "Jewels":
            subtype_display_names = ["Abyss Jewels", "Jewels"]
            return subtype_display_names
        elif item_class_name == "Jewellery":
            subtype_display_names = ["Amulets", "Belts", "Rings"]
            return subtype_display_names
        elif item_class_name == "Flasks":
            subtype_display_names = [
                "Life Flasks",
                "Mana Flasks",
                "Hybrid Flasks",
                "Utility Flasks",
                "Critical Utility Flasks",
            ]
            return subtype_display_names
        else:
            item_class_obj = session.scalars(
                select(ItemClass).filter_by(display_name=item_class_name)
            ).first()
            if item_class_obj is not None:
                item_class_subtypes = item_class_obj.item_class_subtype

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
        item_class_id = session.scalars(
            select(ItemClass.id).filter_by(name=item_class)
        ).first()
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
        item_class_subtype_id = session.scalars(
            select(ItemClassSubtype.id).filter(
                ItemClassSubtype.item_class_id == item_class_id,
                ItemClassSubtype.name == item_class_subtype,
            )
        ).first()
        return item_class_subtype_id

    def create_item_objects(self, session):
        item_data_list = self.item_parser.create_item_data_list()
        item_classes = {
            item_class.name: item_class
            for item_class in session.scalars(select(ItemClass)).all()
        }
        domains = {
            domain.name: domain for domain in session.scalars(select(Domain)).all()
        }
        release_states = {
            release_state.name: release_state
            for release_state in session.scalars(select(ItemReleaseState)).all()
        }
        visual_identities = {
            visual_identity.name: visual_identity
            for visual_identity in session.scalars(select(ItemVisualIdentity)).all()
        }
        tags = {tag.tag: tag for tag in session.scalars(select(Tag)).all()}
        mods = {mod.mod_name: mod for mod in session.scalars(select(Mod)).all()}
        item_obj_list = []
        for item_data in item_data_list:
            try:
                item_obj = (
                    session.query(Item).filter_by(name=item_data.get("name")).one()
                )
                item_obj_list.append(item_obj)
            except NoResultFound:
                item_class_subtype_name = item_data.get("item_class_subtype")
                item_obj = Item(
                    name=item_data.get("name"),
                    drop_level=item_data.get("drop_level"),
                )
                item_obj.release_state = release_states.get(
                    item_data.get("release_state")
                )
                item_obj.item_class = item_classes.get(item_data.get("item_class"))
                if item_class_subtype_name is not None:
                    item_obj.item_class_subtype = (
                        session.query(ItemClassSubtype)
                        .filter_by(
                            name=item_class_subtype_name,
                            item_class_id=item_obj.item_class.id,
                        )
                        .one_or_none()
                    )
                item_obj.domain = domains.get(item_data.get("item_domain"))
                item_obj.visual_identity = visual_identities.get(
                    item_data.get("visual_identity")
                )
                for implicit in item_data.get("implicit_list", []):
                    item_obj.implicits.append(mods.get(implicit))
                for tag in item_data.get("tag_list", []):
                    item_obj.tags.append(tags.get(tag))
                if item_data.get("item_requirements_dict") is not None:
                    item_obj.requirements = self.create_item_requirement_object(
                        session,
                        item_obj,
                        item_data.get("item_requirements_dict").get("requirements"),
                    )
                if item_data.get("item_properties_dict") is not None:
                    item_obj.properties = self.create_item_property_object(
                        session, item_obj, item_data.get("item_properties_dict")
                    )

            item_obj_list.append(item_obj)
        session.add_all(item_obj_list)
        return item_obj_list

    def create_item_release_state_objects(self, session):
        item_release_state_objects_list = []
        release_state_list = self.item_parser.get_item_data_by_key("release_state")
        for release_state in release_state_list:
            try:
                item_release_state_object = (
                    session.query(ItemReleaseState)
                    .filter_by(name=release_state["release_state"])
                    .one()
                )
                if item_release_state_object not in item_release_state_objects_list:
                    item_release_state_objects_list.append(item_release_state_object)
            except NoResultFound:
                item_release_state_object = ItemReleaseState(
                    name=release_state["release_state"]
                )
                if item_release_state_object not in item_release_state_objects_list:
                    item_release_state_objects_list.append(item_release_state_object)
        session.add_all(item_release_state_objects_list)
        return item_release_state_objects_list


class ModManager:
    """
    Class for managing mods in the database and inserting new mods into the
    database.

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
        insert_mods(self) -> None : Inserts all mods from mods.json into the
        database.
        insert_mod_types(self) -> None : Inserts all mod types from
        mods.json into the database.
        insert_mod_stat_values(self, session, mod_id, mod_stat_values) ->
        None : Inserts all mod stat values for the
        given mod_id into the database.
        insert_mod_groups(self) -> None : Inserts all mod groups from
        mods.json into the database.
        insert_mod_generation_types(self) -> None : Inserts all mod
        generation types from mods.json into the database.
        insert_mod_domains(self) -> None : Inserts all mod domains from
        mods.json into the database.
        get_mod_type_id(self, session, mod_type) -> int : Gets the
        mod_type_id for the given mod_type string from the
            database using the given session object and mod_type string. If
            the mod_type does not exist in the database,
            returns None.
    """

    def __init__(self):
        self.mods_parser = ModParser()
        self.mod_id_cache = {}  # Cache for mod_id lookups

    def create_mod_generation_type_objects(self, session):
        """
        Inserts all mod generation types from mods.json into the database

        Args:
            self ():

        Returns:
            None
        """
        generation_type_objects_list = []
        for generation_type in self.mods_parser.get_all_mod_data_for_key(
            "generation_type"
        ):
            try:
                mod_generation_type_obj = (
                    session.query(GenerationType)
                    .filter_by(generation_type=generation_type.get("generation_type"))
                    .one()
                )
                generation_type_objects_list.append(mod_generation_type_obj)
            except NoResultFound:
                mod_generation_type_obj = GenerationType(
                    generation_type=generation_type.get("generation_type")
                )
                generation_type_objects_list.append(mod_generation_type_obj)
        session.add_all(generation_type_objects_list)
        return generation_type_objects_list

    def create_domain_objects(self, session):
        domain_list = self.mods_parser.get_all_mod_data_for_key("domain")
        domain_obj_list = []
        for domain in domain_list:
            try:
                # Query the domain in the database
                domain = (
                    session.query(Domain).filter_by(name=domain.get("domain")).one()
                )
                domain_obj_list.append(domain)
            except NoResultFound:
                # If not found, add it to the session
                domain = Domain(name=domain.get("domain"))
                domain_obj_list.append(domain)
        session.add_all(domain_obj_list)
        return domain_obj_list

    def create_mod_type_objects(self, session):
        """
        Inserts all mod types from mods.min./json into the database.

        Args:
            self ():

        Returns:
            None
        """
        mod_types_list = self.mods_parser.get_all_mod_data_for_key("type")
        mod_type_objs_list = []
        for mod_type in mod_types_list:
            try:
                mod_type_obj = (
                    session.query(ModType).filter_by(type=mod_type.get("type")).one()
                )
                mod_type_objs_list.append(mod_type_obj)
            except NoResultFound:
                mod_type_obj = ModType(type=mod_type.get("type"))
                mod_type_objs_list.append(mod_type_obj)
        session.add_all(mod_type_objs_list)
        return mod_type_objs_list

    @staticmethod
    def get_mod_attribute_id(session, attribute, value):
        """
        Gets the mod attribute id for the given attribute and value from the
        database using the given session object
        and attribute string. If the attribute does not exist in the
        database, returns None.

        Args:
            attribute (): Name of the attribute to get the attribute id for
            from the database
            value (): Value of the attribute to get the attribute id for
            from the database

        Returns:
            attribute_id (): The attribute id for the given attribute

        """
        try:
            attribute_id = (
                session.query(attribute.id).filter_by(attribute=value).scalar()
            )
        except NoResultFound:
            attribute_id = None
        return attribute_id

    @staticmethod
    def get_mod_attribute_obj(session, model_class, column_name, value):
        """
        Gets the mod attribute object for the given attribute and value from
        the database using the given session object
        and attribute string. If the attribute does not exist in the
        database, creates a new attribute object and
        returns it.

        Args:
            model_class (cls): SQLAlchemy model class to query.
            column_name (str): Name of the column to filter by.
            value (): Value to filter by.

        Returns:
            attribute_obj (): The attribute object for the given attribute
        """
        try:
            attribute_obj = (
                session.query(model_class)
                .filter(getattr(model_class, column_name) == value)
                .one()
            )
        except NoResultFound:
            attribute_obj = model_class(**{column_name: value})
            session.add(attribute_obj)
            session.flush()
        return attribute_obj

    def create_mod_group_objects(self, session):
        """
        Inserts all mod groups from mods.json into the database.

        Args:
            self ():

        Returns:
            None
        """
        mod_groups_list = self.mods_parser.get_all_mod_groups()
        mod_group_obj_list = []
        for mod_group in mod_groups_list:
            try:
                # Query the group in the database
                mod_group = (
                    session.query(ModGroup)
                    .filter_by(group=mod_group.get("groups"))
                    .one()
                )
                mod_group_obj_list.append(mod_group)
            except NoResultFound:
                # If not found, add it to the session
                mod_group = ModGroup(group=mod_group.get("groups"))
                if mod_group not in mod_group_obj_list:
                    mod_group_obj_list.append(mod_group)
        session.add_all(mod_group_obj_list)
        return mod_group_obj_list

    @staticmethod
    def get_tag_obj(tag, tag_obj_list):
        for tag_obj in tag_obj_list:
            if tag_obj.tag == tag:
                return tag_obj
        return None

    @staticmethod
    def get_stat_obj(stat, stat_obj_list):
        for stat_obj in stat_obj_list:
            if stat_obj.name == stat:
                return stat_obj
        return None

    @staticmethod
    def get_filtered_mods(
        session: Session, item_obj: Item, generation_type: str
    ) -> Mod:
        """
        Get a list of mods that can spawn on the specified item for the specified generation type.

        Args:
            session (Session): SQLAlchemy Session object
            item_obj (Item): Item object to get the mods for
            generation_type (str): Generation type of the mods to filter on

        Returns:
            Mod: A list of Mod objects
        """
        item_tags = item_obj.tags
        tag_ids = [tag.id for tag in session.query(Tag).filter(Tag.tag.in_(item_tags))]

        spawn_weights_query = (
            session.query(ModSpawnWeight)
            .join(Tag)
            .filter(
                Tag.id.in_(tag_ids),
                ModSpawnWeight.weight > 0,
                ModSpawnWeight.tag == Tag.tag,
            )
            .subquery()
        )

        return (
            session.query(Mod)
            .join(Mod.generation_type, spawn_weights_query)
            .filter(
                and_(
                    Mod.domain_id == item_obj.domain_id,
                    Mod.generation_type.has(generation_type=generation_type),
                )
            )
            .all()
        )

    @staticmethod
    def get_translation_for_mod(session: Session, mod: Mod) -> Translation:
        """
        Get the translation for the specified mod.

        Note: This is not the same as mod.translated_string.

        Args:
            session (Session): SQLAlchemy session
            mod (Mod): Mod object to get the translation for

        Returns:
            Translation (object): Translation object that matches the specified mod
        """
        stat_ids = [stat["stat"] for stat in mod.stats]
        return session.scalar(select(Translation).filter(Translation.ids == stat_ids))


if __name__ == "__main__":
    db_manager = DatabaseManager()
    mod_manager = ModManager()
    item_manager = ItemManager()
    tag_manager = TagManager()
    stat_manager = StatManager()
    translation_manager = TranslationManager()
    with db_manager.transaction() as session:
        # item_obj = session.query(Item).filter(Item.name == "Coral Ring").one()
        #
        # filtered_mods = mod_manager.get_filtered_mods(
        #     session, item_obj, generation_type="prefix"
        # )

        # db_manager.drop_tables()
        db_manager.create_tables()
        # stat_list = stat_manager.create_stat_objects(session)
        # translation_data_list =
        # translation_manager.translation_parser.create_translation_objects()
        # translation_instances = [Translation(data=d) for d in translation_data_list]
        # session.add_all(translation_instances)
        # session.commit()
        # tag_list = tag_manager.create_tag_objects(session)
        # tag_name_to_obj = {tag.tag: tag for tag in tag_list}
        # item_class_list = item_manager.create_item_class_objects(session)
        # session.commit()
        # item_class_subtype_list = session.scalars(select(ItemClassSubtype)).all()
        #
        # item_class_name_to_obj = {item_class.name: item_class for item_class in item_class_list}
        # domain_list = mod_manager.create_domain_objects(session)
        # session.commit()
        # domain_name_to_obj = {domain.name: domain for domain in domain_list}
        # visual_identity_list = item_manager.create_visual_identity_objects(session)
        # session.commit()
        # visual_identity_name_to_obj = {visual_identity.name: visual_identity for
        # visual_identity in
        #                                visual_identity_list}
        # release_state_list = item_manager.create_item_release_state_objects(session)
        # session.commit()
        # release_state_name_to_obj = {release_state.name: release_state for release_state in
        #                              release_state_list}
        # item_data_list = item_manager.item_parser.create_item_data_list()
        # item_instances = [Item(data=d, item_class=item_class_name_to_obj[d.pop('item_class')],
        #                        domain=domain_name_to_obj[d.pop('item_domain')],
        #                        visual_identity=visual_identity_name_to_obj[
        #                            d.pop('visual_identity')],
        #                        release_state=release_state_name_to_obj[d.pop('release_state')])
        #                        for
        #                   d in item_data_list]
        # session.add_all(item_instances)
        # session.commit()
        # for item in item_instances:
        #     item_class_subtype_name = item.data.pop('item_class_subtype')
        #     item_class_id = item.item_class.id
        #     item_class_subtype = session.query(ItemClassSubtype).filter_by(
        #             name=item_class_subtype_name, item_class_id=item_class_id).first()
        #     item.item_class_subtype = item_class_subtype
        #
        # mod_data = mod_manager.mods_parser.get_all_mods()
        # generation_type_list = mod_manager.create_mod_generation_type_objects(session)
        # session.commit()
        # generation_type_name_to_obj = {generation_type.generation_type: generation_type for
        #                                generation_type in generation_type_list}
        # mod_group_list = mod_manager.create_mod_group_objects(session)
        # session.commit()
        # mod_group_name_to_obj = {mod_group.group: mod_group for mod_group in mod_group_list}
        # mod_type_list = mod_manager.create_mod_type_objects(session)
        # session.commit()
        # mod_type_name_to_obj = {mod_type.type: mod_type for mod_type in mod_type_list}
        # mod_instances = [Mod(domain=domain_name_to_obj[d.pop('domain')],
        #                      generation_type=generation_type_name_to_obj[d.pop(
        #                      'generation_type')],
        #                      group=mod_group_name_to_obj[d.pop('group')],
        #                      mod_type=mod_type_name_to_obj[d.pop('mod_type')], data=d) for d in
        #                  mod_data]
        # session.add_all(mod_instances)
        # session.commit()
        # mod_instances = session.query(Mod).all()
        # mod_name_to_obj = {mod.name: mod for mod in mod_instances}
        # for mod in mod_instances:
        #     stat_ids = [stat.get('stat') for stat in mod.stats]
        #     stat_translation = session.scalar(select(Translation).filter_by(ids=stat_ids))
        #     if stat_translation is None:
        #         complete_string = ''
        #         for stat in stat_ids:
        #             if complete_string != '':
        #                 break
        #             stat_translation = session.scalar(select(Translation).filter(
        #                     Translation.ids.contains(stat)))
        #             if stat_translation is None:
        #                 continue
        #             for stat_entry in mod.stats:
        #                 stat_values = {}
        #                 stat_name = stat_entry['stat']
        #                 min_value = stat_entry['values']['min']
        #                 max_value = stat_entry['values']['max']
        #                 stat_values[stat_name] = {'min': min_value, 'max': max_value}
        #                 translated_string = stat_translation.get_translation(stat_values=stat_values)
        #                 if translated_string:
        #                     complete_string += translated_string
        #                 else:
        #                     continue
        #         mod.translation_string = complete_string
        #         session.add(mod)
        #         session.commit()
        #     else:
        #         stat_values = {}
        #         for stat_entry in mod.stats:
        #             stat_name = stat_entry['stat']
        #             min_value = stat_entry['values']['min']
        #             max_value = stat_entry['values']['max']
        #             stat_values[stat_name] = {'min': min_value, 'max': max_value}
        #         translated_string = stat_translation.get_translation(stat_values=stat_values)
        #         mod.translation_string = translated_string
        #         session.add(mod)
        #     session.commit()
        # tag_instances = session.query(Tag).all()
        # tag_name_to_obj = {tag.tag: tag for tag in tag_instances}
        # for mod in mod_instances:
        #     mod_name = mod.name
        #     for spawn_weight in mod._spawn_weights:
        #         tag_name = spawn_weight.get('tag')
        #         weight = spawn_weight.get('weight')
        #         mod.spawn_weights.append(
        #             ModSpawnWeight(tag=tag_name_to_obj[tag_name], weight=weight,
        #                            mod=mod_name_to_obj[mod_name]))
        #     session.add(mod)
        # session.commit()
        # item_obj = session.query(Item).filter_by(name='Coral Ring').one()
        # mod_manager.generate_prefix_mod_list(session, item_obj)
