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
import os
from pathlib import Path
from typing import List, Any, Optional, Union

from jinja2 import Template
from sqlalchemy import String, ForeignKey, Integer, Float
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.association_models import item_tags_association, item_implicits_association
from modules.data.models.base_model import Base, intpk, str50, InfluencedItemMixin
from modules.shared.config.constants import ITEM_PROPERTIES, ITEM_REQUIREMENTS

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


class Item(Base):
    """
    Item model
    
    Attributes:
        id: Primary Key
        release_state: Release state of the item
        name: Name of the item
        meta_data: Metadata of the item
        domain: Domain of the item
        item_class: Class of the item
        visual_identity: Visual identity of the item
        tags: Tags of the item
        implicits: Implicits of the item
        requirements: Requirements of the item
        properties: Properties of the item
    """
    __tablename__ = 'items'
    
    # Table Columns
    release_state: Mapped["ItemReleaseState"] = relationship("ItemReleaseState", back_populates='items',
                                                             uselist=False, lazy='joined', init=False)
    name: Mapped[str] = mapped_column(String(100), index=True)
    meta_data: Mapped["ItemMetaData"] = relationship('ItemMetaData', back_populates='item', uselist=False,
                                                     lazy='selectin', cascade='all, delete-orphan',
                                                     passive_deletes=True, single_parent=True, init=False)
    domain: Mapped["Domain"] = relationship('Domain', back_populates='items', lazy='joined', uselist=False, init=False)
    item_class: Mapped["ItemClass"] = relationship("ItemClass", back_populates='items', uselist=False,
                                                   lazy='joined', init=False)
    visual_identity: Mapped["ItemVisualIdentity"] = relationship("ItemVisualIdentity",
                                                                 back_populates='items', uselist=False,
                                                                 lazy='joined', init=False)
    item_meta_data_id: Mapped[int] = mapped_column(ForeignKey('item_meta_data.id'), init=False)
    domain_id: Mapped[int] = mapped_column(ForeignKey('domains.id'), nullable=False, init=False)
    item_class_id: Mapped[int] = mapped_column(ForeignKey('item_classes.id'), nullable=False, init=False)
    visual_identity_id: Mapped[int] = mapped_column(ForeignKey('item_visual_identities.id'), nullable=False,
                                                    init=False)
    release_state_id: Mapped[int] = mapped_column(ForeignKey('item_release_states.id'), nullable=False, init=False)
    
    id: Mapped[intpk] = mapped_column(init=False)
    
    # One-to-Many Relationships
    implicits: Mapped[List["Mod"]] = relationship('Mod', secondary=item_implicits_association, default_factory=list,
                                                  back_populates='items', lazy='selectin', init=False)
    tags: Mapped[List["Tag"]] = relationship('Tag', secondary=item_tags_association, default_factory=list,
                                             back_populates='items', lazy='selectin', init=False)
    properties: Mapped[List["ItemProperty"]] = relationship("ItemProperty", back_populates='item', lazy='selectin',
                                                            default_factory=list, init=False)
    requirements: Mapped[List["ItemRequirement"]] = relationship("ItemRequirement", back_populates='item',
                                                                 lazy='selectin', default_factory=list, init=False)
    
    @classmethod
    def get_property_value(cls, item_properties, attrs):
        """
        Get the value of a property from the item properties.

        Args:
            item_properties (ItemProperties): The properties of the item.
            attrs (Union[tuple, str]): The attribute(s) to retrieve the value from.

        Returns:
            Union[None, Any]: The value of the property, or None if not found.
        """
        if isinstance(attrs, tuple):
            values = [getattr(item_properties, attr, None) for attr in attrs]
            if all(v is not None for v in values):
                return values
        elif isinstance(attrs, str):
            return getattr(item_properties, attrs, None)
        return None
    
    @classmethod
    def get_requirement_value(cls, item_requirements, attrs):
        """
        Get the value of a property from the item properties.

        Args:
            item_requirements (ItemRequirements): The properties of the item.
            attrs (Union[tuple, str]): The attribute(s) to retrieve the value from.

        Returns:
            Union[None, Any]: The value of the property, or None if not found.
        """
        if isinstance(attrs, tuple):
            values = [getattr(item_requirements, attr, None) for attr in attrs]
            if all(v is not None for v in values):
                return values
        elif isinstance(attrs, str):
            return getattr(item_requirements, attrs, None)
        return None
    
    def get_requirements(self, item_requirements):
        """
        Get the requirements of the item.

        Args:
            item_requirements (ItemRequirements): The properties of the item.

        Returns:
            dict: A dictionary of requirements.
        """
        requirements = {}
        for name, attrs, color in ITEM_REQUIREMENTS:
            value = self.get_requirement_value(item_requirements, attrs)
            if value is not None:
                requirements[name] = (value, color)
        return requirements
    
    def formatted_requirements(self):
        """
        Gets the formatted requirements of the item.

        Returns:
            str: The formatted requirements of the item.
        """
        item_requirements = self.requirements
        if item_requirements is not None:
            item_requirements = self.get_requirements(item_requirements)
            return self.format_requirements_string(item_requirements)
        return ''
    
    def formatted_properties(self):
        """
        Gets the formatted properties of the item.

        Returns:
            str: The formatted properties of the item.
        """
        item_properties = self.properties
        if item_properties:
            properties = self.get_properties(item_properties)
            return self.format_properties_string(properties)
        return ''
    
    def get_properties(self, item_properties):
        """
        Get the properties of the item.

        Args:
            item_properties (ItemProperties): The properties of the item.

        Returns:
            dict: A dictionary of properties.
        """
        properties = {}
        for name, attrs, color in ITEM_PROPERTIES:
            value = self.get_property_value(item_properties, attrs)
            if value is not None:
                properties[name] = (value, color)
        return properties
    
    def get_implicits(self):
        return self.implicits.Mod.name
    
    @staticmethod
    def format_requirements_string(requirements):
        """
        Formats the requirements of an item for display in the GUI.

        Args:
            requirements (dict): A dictionary of requirements.

        Returns:
            str: A string containing the formatted requirements, ready to be displayed in the GUI.
        """
        template = Template("""
            <p align="center">
            {% for requirement_name, (value, color) in requirements.items() %}
                {% if value and value != "0" %}
                    {% if requirement_name == 'Requires Level' %}
                        <span style=" font-size:11pt; color:#827a6c;">{{ requirement_name }}: </span>
                        <span style=" font-size:11pt; font-weight:bold; color:{{ color }};">{{ value }}</span>
                    {% else %}
                        <span style=" font-size:11pt; font-weight:bold; color:{{ color }};">{{ value }} </span>
                        <span style=" font-size:11pt; color:#827a6c;">{{ requirement_name }}</span>
                    {% endif %}
                {% endif %}
            {% endfor %}
            </p>
        """)
        return template.render(requirements=requirements)
    
    @staticmethod
    def format_properties_string(properties):
        """
        Formats the properties of an item for display in the GUI.

        Args:
            properties (dict): A dictionary of properties, where each key is the name of a property and each value
                is a tuple containing the value of the property and the color to display the value in.

        Returns:
            str: A string containing the formatted properties, ready to be displayed in the GUI.
        """
        template = Template("""
            {% for property_name, (value, color) in properties.items() %}
                {% if value and value != "0" %}
                    {% if property_name == "Physical Damage" %}
                        {% set min_damage, max_damage = value %}
                        <p style="line-height:0.8; padding-bottom:0.2em;" align="center">
                            <span style=" font-size:11pt; font-weight:bold; color:{{ color }};">{{ min_damage }} </span>
                            <span style=" font-size:11pt; color:#827a6c;">To </span>
                            <span style=" font-size:11pt; font-weight:bold; color:{{ color }};">{{ max_damage }} </span>
                            <span style=" font-size:11pt; color:#827a6c;">{{ property_name }}</span>
                        </p>
                    {% else %}
                        <p style="line-height:0.8; padding-bottom:0.2em;" align="center">
                            <span style=" font-size:11pt; color:#827a6c;">{{ property_name }}: </span>
                            <span style=" font-size:11pt; font-weight:bold; color:{{ color }};">{{ value }}</span>
                        </p>
                    {% endif %}
                {% endif %}
            {% endfor %}
        """)
        return template.render(properties=properties)


class CustomItem(Item, InfluencedItemMixin):
    __tablename__ = "custom_items"
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(ForeignKey('items.id'), primary_key=True, init=False)
    prefix1: Mapped[Optional[str50]] = mapped_column(default=None)
    prefix2: Mapped[Optional[str50]] = mapped_column(default=None)
    prefix3: Mapped[Optional[str50]] = mapped_column(default=None)
    suffix1: Mapped[Optional[str50]] = mapped_column(default=None)
    suffix2: Mapped[Optional[str50]] = mapped_column(default=None)
    suffix3: Mapped[Optional[str50]] = mapped_column(default=None)
    quality = mapped_column(Integer, default=0)
    enchantment: Mapped[Optional[str50]] = mapped_column(default=None)
    
    # Relationships
    base_item = relationship("Item")
    
    def __init__(self, prefix1: str50, prefix2: str50, prefix3: str50, suffix1: str50, suffix2: str50,
                 suffix3: str50, quality: int, enchantment: str50, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.prefix1 = prefix1
        self.prefix2 = prefix2
        self.prefix3 = prefix3
        self.suffix1 = suffix1
        self.suffix2 = suffix2
        self.suffix3 = suffix3
        self.quality = quality
        self.enchantment = enchantment


class ItemRequirement(Base):
    __tablename__ = "item_requirements"
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(ForeignKey('items.id'), init=False)
    item: Mapped["Item"] = relationship("Item", back_populates="requirements", uselist=False, lazy='selectin',
                                        init=False)
    requirement_type: Mapped[str] = mapped_column(String(50), insert_default=None, default=None)
    _value: Mapped[int] = mapped_column(Integer, insert_default=None, default=None)
    
    @hybrid_property
    def value(self) -> Optional[int]:
        return self._value
    
    @value.setter
    def value(self, value: Optional[int]):
        self._value = int(value)
    
    @value.expression
    def value(cls):
        return cls._value


class ItemProperty(Base):
    __tablename__ = "item_properties"
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(ForeignKey('items.id'), init=False)
    item: Mapped["Item"] = relationship("Item", back_populates="properties", uselist=False, lazy='selectin', init=False)
    property_type: Mapped[str] = mapped_column(String(100), insert_default=None, default=None)
    _value: Mapped[Optional[float]] = mapped_column(Float, insert_default=None, default=None)
    
    @hybrid_property
    def value(self) -> Optional[Union[int, float]]:
        return self._value
    
    @value.setter
    def value(self, value: Optional[Union[int, float]]):
        self._value = float(value)
    
    @value.expression
    def value(cls):
        return cls._value


class ItemVisualIdentity(Base):
    __tablename__ = "item_visual_identities"
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(init=False)
    dds_file: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    # Many-to-one Relationships
    items: Mapped[List["Item"]] = relationship("Item", back_populates="visual_identity", lazy='selectin',
                                               default_factory=list, init=False)


class ItemMetaData(Base):
    """Represents the metadata of an item.
    
    Attributes:
        id (int): The ID of the item.
        drop_level (int): The level at which the item can drop.
        is_corrupted (bool): Whether the item is corrupted.
        
        item (Item): The item this metadata belongs to.
    """
    __tablename__ = 'item_meta_data'
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(init=False)
    
    metadata_name: Mapped[str] = mapped_column(String(300), nullable=False, unique=True)
    drop_level: Mapped[int] = mapped_column(insert_default=0, default=0)
    is_corrupted: Mapped[bool] = mapped_column(insert_default=False, default=False)
    
    # One-to-One Relationships
    item: Mapped["Item"] = relationship("Item", back_populates='meta_data', uselist=False,
                                        cascade="all, delete-orphan", passive_deletes=True, passive_updates=True,
                                        init=False, single_parent=True)


class ItemReleaseState(Base):
    """Represents the release state of an item.
    
    Attributes:
        id (int): The ID of the release state.
        name (str): The name of the release state.
    """
    __tablename__ = 'item_release_states'
    
    # Table Columns
    name: Mapped[str] = mapped_column(String(50), unique=True)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # One-to-Many Relationships
    items: Mapped[List["Item"]] = relationship("Item", back_populates='release_state',
                                               cascade="all, delete-orphan", passive_deletes=True,
                                               passive_updates=True, default_factory=list, init=False,
                                               lazy='selectin')


class ItemClass(Base):
    """Represents the class of an item.
    
    Attributes:
        id (int): The ID of the class.
        name (str): The name of the class.
        display_name (str): The display name of the class.
    """
    __tablename__ = 'item_classes'
    
    # Table Columns
    name: Mapped[str] = mapped_column(String(180))
    display_name: Mapped[str] = mapped_column(String(180))
    id: Mapped[intpk] = mapped_column(init=False)
    
    # One-to-Many Relationships
    items: Mapped[List["Item"]] = relationship("Item", back_populates='item_class',
                                               cascade="all, delete-orphan", passive_deletes=True,
                                               passive_updates=True, init=False, lazy='selectin', default_factory=list)

# ########################################################################################################################
# # EVENT LISTENERS
# ########################################################################################################################
#
#
# @event.listens_for(ItemClass, 'after_insert')
# def receive_after_insert(mapper, connection, target):
#     session = Session(bind=connection)
#     item_class_id = target.id
#     item_class_name = target.name
#     item_class_display_name = target.display_name
#     with session.begin():
#         if item_class_name in armour_subtypes:
#             for subtype in armour_subtypes[item_class_name]:
#                 display_name = subtype_display_names.get(subtype, "")
#                 if not display_name:
#                     logging.warning("No display name found for subtype %s, skipping this subtype", subtype)
#                     continue
#
#                 if display_name is not None and '{}' in display_name:
#                     formatted_display_name = display_name.format(item_class_name)
#                 else:
#                     formatted_display_name = display_name
#
#                 item_class_subtype = {
#                     "item_class_id": item_class_id,
#                     "name": subtype,
#                     "display_name": formatted_display_name
#                 }
#                 new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
#                 session.add(new_item_class_subtype)
#
#         elif item_class_name in one_hand_weapon_types:
#             item_class_subtype = {
#                 "item_class_id": item_class_id,
#                 "name": 'one_hand_weapon',
#                 "display_name": item_class_display_name
#             }
#             new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
#             session.add(new_item_class_subtype)
#
#         elif item_class_name in two_hand_weapon_types:
#             item_class_subtype = {
#                 "item_class_id": item_class_id,
#                 "name": 'two_hand_weapon',
#                 "display_name": item_class_display_name
#             }
#             new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
#             session.add(new_item_class_subtype)
#
#         elif item_class_name in flask_types:
#             item_class_subtype = {
#                 "item_class_id": item_class_id,
#                 "name": 'flask',
#                 "display_name": item_class_display_name
#             }
#             new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
#             session.add(new_item_class_subtype)
#         else:
#             item_class_subtype = {
#                 "item_class_id": item_class_id,
#                 "name": 'other',
#                 "display_name": item_class_display_name
#             }
#             new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
#             session.add(new_item_class_subtype)
#     session.commit()
#
#
# @event.listens_for(ItemClassSubtype, 'after_insert')
# def receive_after_insert(mapper, connection, target):
#     session = Session(bind=connection)
#     item_class_subtype_id = target.id
#     item_class_subtype_tag = target.name
#     tag = session.query(Tag).filter(Tag.tag == item_class_subtype_tag).first()
#
#     # Check if the tag exists
#     if tag:
#         tag_id = tag.id
#         # Insert into the association table
#         insert_stmt = insert(item_class_subtype_association).values(item_class_subtype_id=item_class_subtype_id,
#                                                                     tag_id=tag_id)
#         connection.execute(insert_stmt)
#         session.commit()
