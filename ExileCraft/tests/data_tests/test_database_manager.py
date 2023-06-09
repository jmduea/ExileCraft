
# Generated by CodiumAI

import pytest

from modules.data.database_manager import DatabaseManager
from modules.data.models.global_models import Domain, GenerationType
from modules.data.models.item_models import ItemClass, ItemClassSubtype, Item, ItemProperties
from modules.data.models.mod_models import Mod, ModType
from modules.data.models.stat_models import Stat
from modules.data.models.tag_models import Tag

"""
Code Analysis

Main functionalities:
The DatabaseManager class provides methods for managing a database using SQLAlchemy. It can create and drop tables, add, update, and delete records, and perform transactions. It also includes methods for inserting and updating various models, such as Item, Mod, and Tag, and for getting data from the database, such as base items and item classes.

Methods:
- create_tables(): creates tables in the database based on the models defined in the code
- drop_tables(): drops tables in the database based on the models defined in the code
- get_session(): returns a scoped session for interacting with the database
- add_record(record): adds a record to the database
- get_record(model, record_id): retrieves a record from the database based on its ID
- update_record(model, record_id, **kwargs): updates a record in the database with new values
- delete_record(model, record_id): deletes a record from the database
- transaction(): context manager for performing a transaction on the database
- insert_item_tags(session, tag_list, item_id): inserts tags associated with an item into the database
- insert_item_implicits(session, implicit_list, item_id): inserts implicits associated with an item into the database
- add_or_update_base_item_type(base_item_dict, session): adds or updates a base item type in the database
- add_item_classes(item_class_dict, session): adds item classes to the database
- insert_item_properties(session, item_id, item_class_id, item_class_subtype, item_class_subtype_id, item_properties_dict, item_requirements_dict): inserts item properties and requirements into the database
- add_or_update_tag(tag_dict, session): adds or updates a tag in the database
- add_or_update_mod(mod_dict, session): adds or updates a mod in the database
- add_or_update_mod_type(type_dict, session): adds or updates a mod type in the database
- insert_domains(domain_whitelist, session): inserts domains into the database
- get_domain(session, item_domain): retrieves a domain from the database based on its name
- insert_generation_types(generation_type_whitelist, session): inserts generation types into the database
- add_or_update_stat(stat_dict, session): adds or updates a stat in the database
- get_visual_identity_id(session, visual_identity): retrieves a visual identity from the database based on its name
- get_item_class(session, item_class): retrieves an item class from the database based on its name
- get_item_class_subtype(session, item_class_id, item_class_subtype): retrieves an item class subtype from the database based on its name and item class ID
- get_tag(session, tag): retrieves a tag from the database based on its name
- get_mod(session, implicit): retrieves a mod from the database based on its name
- get_item_class_subtypes_and_display_names(session, item_class_name): retrieves item class subtypes and their display names from the database based on an item class name
- get_base_items_from_subtype_display_name(session, subtype_display_name): retrieves base items from the database based on a subtype display name
- get_base_items(session, item_class_id): retrieves base items from the database based on an item class ID

Fields:
- engine: SQLAlchemy engine for connecting to the database
- session_factory: session factory for creating sessions
- Session: scoped session for interacting with the database
"""


class TestDatabaseManager:
    @pytest.fixture
    def db_manager(self):
        # Setup code: create a new DatabaseManager instance
        db_manager = DatabaseManager(db_url='sqlite:///:memory:')
        
        yield db_manager
        
        # Teardown code: close the database session
        db_manager.close_session()
        
    #  Tests that tables are created successfully
    def test_create_tables(self, db_manager):
        db_manager.create_tables()
        session = db_manager.get_session()
        assert session.query(Domain).count() == 0
        assert session.query(GenerationType).count() == 0
        assert session.query(ItemClass).count() == 0
        assert session.query(ItemClassSubtype).count() == 0
        assert session.query(Item).count() == 0
        assert session.query(ItemProperties).count() == 0
        assert session.query(Mod).count() == 0
        assert session.query(ModType).count() == 0
        assert session.query(Stat).count() == 0
        assert session.query(Tag).count() == 0
        db_manager.close_session()