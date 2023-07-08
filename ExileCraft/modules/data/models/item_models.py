
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
import logging
import os
from jinja2 import Template
from pathlib import Path
from typing import List, Dict, Any, Optional

from sqlalchemy import String, ForeignKey, Integer, Boolean, event, text
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session, declared_attr

from modules.config.constants import armour_subtypes, subtype_display_names, one_hand_weapon_types, \
    two_hand_weapon_types, flask_types, ITEM_PROPERTIES, ITEM_REQUIREMENTS
from modules.data.models.association_models import item_implicits_association, \
    item_class_association, item_class_subtype_association
from modules.data.models.base_model import Base, EvasionBaseMixin, ArmourBaseMixin, EnergyShieldBaseMixin, \
    WardBaseMixin, RequirementsMixin, WeaponPropertiesMixin, ItemClassMixin, FlaskPropertiesMixin, ShieldMixin, \
    MovementPenaltyMixin, ItemClassSubtypeMixin
from modules.data.models.global_models import Domain
from modules.data.models.mod_models import Mod
from modules.data.models.tag_models import Tag

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


class Item(Base):
    """
    Represents an item base.

    Attributes:
        visual_identity_id (int): The ID of the visual identity associated with the item.
        name (str): The name of the item.
        meta_data_id (str): The unique metadata ID of the item.
        item_class_id (int): The ID of the item's class.
        item_class_subtype_id (int, optional): The ID of the item's subclass, if applicable.
        domain_id (int): The ID of the domain to which the item belongs.
        drop_level (int): The drop level of the item.
        rarity (str): The rarity of the item.
        is_corrupted (bool): Indicates if the item is corrupted or not.
        domain (Domain): The domain to which the item belongs.
        item_class (ItemClass): The class of the item.
        item_class_subtype (ItemClassSubtype): The subclass of the item, if applicable.
        item_properties (ItemProperties): The properties of the item.
        item_implicits (List[Mod]): The implicit mods of the item.
        visual_identity (VisualIdentity): The visual identity associated with the item.
        tags (List[Tag]): The tags associated with the item.
    """
    
    __tablename__ = 'items'
    
    # Table Columns
    visual_identity_id: Mapped[int] = mapped_column(Integer, ForeignKey('visual_identities.id'))
    name: Mapped[str] = mapped_column(String, index=True)
    meta_data_id: Mapped[str] = mapped_column(String(255), unique=True)
    item_class_id: Mapped[int] = mapped_column(Integer, ForeignKey('item_classes.id'), index=True)
    item_class_subtype_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('item_class_subtypes.id'),
                                                                 nullable=True)
    domain_id: Mapped[int] = mapped_column(Integer, ForeignKey('domains.id'))
    drop_level: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    rarity: Mapped[str] = mapped_column(String(50), nullable=False, default='normal')
    is_corrupted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    
    # Relationships
    domain: Mapped["Domain"] = relationship(back_populates='items')
    item_class: Mapped["ItemClass"] = relationship('ItemClass', back_populates='items', uselist=False, foreign_keys=[
        item_class_id])
    item_class_subtype: Mapped["ItemClassSubtype"] = relationship('ItemClassSubtype', back_populates='items',
                                                                  uselist=False, foreign_keys=[item_class_subtype_id])
    item_properties: Mapped["ItemProperties"] = relationship(back_populates='item', lazy='selectin')
    item_implicits: Mapped[List["Mod"]] = relationship(secondary=item_implicits_association, back_populates='items',
                                                       lazy='joined')
    visual_identity: Mapped["VisualIdentity"] = relationship('VisualIdentity', back_populates='items', uselist=False,
                                                             foreign_keys=[visual_identity_id])
    tags = relationship('Tag', secondary='item_tags_association', back_populates='items')
    
    def __repr__(self):
        """
        Returns a string representation of the item.

        Returns:
            str: The string representation of the item.
        """
        logging.debug(f'Item __repr__ called with id={self.id}')
        return self._repr(id=self.id,
                          name=self.name,
                          item_class=self.item_class,
                          item_class_subtyp=self.item_class_subtype,
                          item_implicits=self.item_implicits,
                          item_properties=self.item_properties.formatted_properties,
                          visual_identity=self.visual_identity,
                          tags=self.tags
                          )
    
    @hybrid_property
    def formatted_requirements(self):
        """
        Gets the formatted requirements of the item.

        Returns:
            str: The formatted requirements of the item.
        """
        item_properties = self.item_properties
        if item_properties:
            requirements = self.get_requirements(item_properties)
            return self.format_requirements_string(requirements)
        return ''
    
    @hybrid_property
    def formatted_properties(self):
        """
        Gets the formatted properties of the item.

        Returns:
            str: The formatted properties of the item.
        """
        item_properties = self.item_properties
        if item_properties:
            properties = self.get_properties(item_properties)
            return self.format_properties_string(properties)
        return ''
    
    def get_requirements(self, item_properties):
        """
        Get the requirements of the item.

        Args:
            item_properties (ItemProperties): The properties of the item.

        Returns:
            dict: A dictionary of requirements.
        """
        requirements = {}
        for name, attrs, color in ITEM_REQUIREMENTS:
            value = self.get_property_value(item_properties, attrs)
            if value is not None:
                requirements[name] = (value, color)
        return requirements
    
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
    
    @staticmethod
    def get_property_value(item_properties, attrs):
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


class CustomItem(Item):
    __tablename__ = "custom_items"
    
    # Table Columns
    id: Mapped[int] = mapped_column(Integer, ForeignKey('items.id'), primary_key=True)
    quality: Mapped[int] = mapped_column(Integer, default=0)


class ItemClass(Base):
    __tablename__ = 'item_classes'
    
    # Table Columns
    name: Mapped[str] = mapped_column(String, index=True)
    display_name: Mapped[str] = mapped_column(String, index=True)
    
    # Relationships
    items: Mapped[List["Item"]] = relationship("Item", back_populates="item_class")
    subtypes: Mapped[List["ItemClassSubtype"]] = relationship(back_populates="item_class")
    tags = relationship('Tag', secondary=item_class_association, back_populates="item_class")


class ItemClassSubtype(Base, ItemClassMixin):
    __tablename__ = 'item_class_subtypes'
    
    # Table Columns
    name: Mapped[str] = mapped_column(String, index=True)
    display_name: Mapped[str] = mapped_column(String, index=True)
    
    # Relationships
    items: Mapped[List["Item"]] = relationship('Item', back_populates="item_class_subtype")
    tags = relationship('Tag', secondary=item_class_subtype_association, back_populates="item_class_subtypes")


class ItemProperties(Base, RequirementsMixin, ItemClassSubtypeMixin):
    __tablename__ = 'item_properties'
    
    @declared_attr.directive
    def __mapper_args__(self) -> Dict[str, Any]:
        if self.__name__ == 'ItemProperties':
            return {
                'polymorphic_identity': 'other',
                'polymorphic_on': self.type
            }
        else:
            return {
                'polymorphic_load': 'selectin'
            }
    
    id: Mapped[int] = mapped_column(Integer, ForeignKey('items.id'), primary_key=True)
    type: Mapped[str] = mapped_column(String)
    
    # Relationships
    item: Mapped["Item"] = relationship(back_populates='item_properties')


class EvasionBase(ItemProperties, EvasionBaseMixin, ShieldMixin, MovementPenaltyMixin):
    __tablename__ = 'evasion_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'dex_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class ArmourBase(ItemProperties, ArmourBaseMixin, ShieldMixin, MovementPenaltyMixin):
    __tablename__ = 'armour_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'str_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class EnergyShieldBase(ItemProperties, EnergyShieldBaseMixin, ShieldMixin, MovementPenaltyMixin):
    __tablename__ = 'energy_shield_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'int_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class ArmourEvasionBase(ItemProperties, ArmourBaseMixin, EvasionBaseMixin, ShieldMixin, MovementPenaltyMixin):
    __tablename__ = 'armour_evasion_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'str_dex_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class ArmourEnergyShieldBase(ItemProperties, ArmourBaseMixin, EnergyShieldBaseMixin, ShieldMixin, MovementPenaltyMixin):
    __tablename__ = 'armour_energy_shield_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'str_int_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class ArmourEvasionEnergyShieldBase(ItemProperties, ArmourBaseMixin, EvasionBaseMixin, EnergyShieldBaseMixin,
                                    ShieldMixin, MovementPenaltyMixin):
    __tablename__ = 'armour_evasion_energy_shield_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'str_dex_int_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class EvasionEnergyShieldBase(ItemProperties, EvasionBaseMixin, EnergyShieldBaseMixin, ShieldMixin,
                              MovementPenaltyMixin):
    __tablename__ = 'evasion_energy_shield_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'dex_int_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class WardBase(ItemProperties, WardBaseMixin):
    __tablename__ = 'ward_base'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'ward_armour'
    }
    
    # Table Columns
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class OneHandWeapon(ItemProperties, WeaponPropertiesMixin):
    __tablename__ = 'one_hand_weapons'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'one_hand_weapon'
    }
    
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class TwoHandWeapon(ItemProperties, WeaponPropertiesMixin):
    __tablename__ = 'two_hand_weapons'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'two_hand_weapon'
    }
    
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class Flask(ItemProperties, FlaskPropertiesMixin):
    __tablename__ = 'flasks'
    
    # Mapper Arguments
    __mapper_args__ = {
        'polymorphic_identity': 'flask'
    }
    
    id: Mapped["ItemProperties"] = mapped_column(ForeignKey('item_properties.id'), primary_key=True)


class VisualIdentity(Base):
    __tablename__ = 'visual_identities'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    visual_identity: Mapped[str]
    
    # Relationships
    items: Mapped[List["Item"]] = relationship('Item', back_populates='visual_identity')


########################################################################################################################
# EVENT LISTENERS
########################################################################################################################


@event.listens_for(ItemClass, 'after_insert')
def receive_after_insert(mapper, connection, target):
    session = Session(bind=connection)
    item_class_id = target.id
    item_class_name = target.name
    item_class_display_name = target.display_name
    if item_class_name in armour_subtypes:
        for subtype in armour_subtypes[item_class_name]:
            display_name = subtype_display_names.get(subtype, "")
            if not display_name:
                print(f"No display name found for subtype {subtype}, skipping this subtype")
                continue
            
            if display_name is not None and '{}' in display_name:
                formatted_display_name = display_name.format(item_class_name)
            else:
                formatted_display_name = display_name
            
            item_class_subtype = {
                "item_class_id": item_class_id,
                "name": subtype,
                "display_name": formatted_display_name
            }
            new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
            session.add(new_item_class_subtype)
            session.commit()
    
    elif item_class_name in one_hand_weapon_types:
        item_class_subtype = {
            "item_class_id": item_class_id,
            "name": 'one_hand_weapon',
            "display_name": item_class_display_name
        }
        new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
        session.add(new_item_class_subtype)
        session.commit()
    
    elif item_class_name in two_hand_weapon_types:
        item_class_subtype = {
            "item_class_id": item_class_id,
            "name": 'two_hand_weapon',
            "display_name": item_class_display_name
        }
        new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
        session.add(new_item_class_subtype)
        session.commit()
    
    elif item_class_name in flask_types:
        item_class_subtype = {
            "item_class_id": item_class_id,
            "name": 'flask',
            "display_name": item_class_display_name
        }
        new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
        session.add(new_item_class_subtype)
        session.commit()
    else:
        item_class_subtype = {
            "item_class_id": item_class_id,
            "name": 'other',
            "display_name": item_class_display_name
        }
        new_item_class_subtype = ItemClassSubtype(**item_class_subtype)
        session.add(new_item_class_subtype)
        session.commit()


@event.listens_for(ItemClassSubtype, 'after_insert')
def receive_after_insert(mapper, connection, target):
    session = Session(bind=connection)
    item_class_subtype_id = target.id
    item_class_subtype_tag = target.name
    tag = session.query(Tag).filter(Tag.tag == item_class_subtype_tag).first()
    
    # Check if the tag exists
    if tag:
        tag_id = tag.id
        # Insert into the association table
        insert_stmt = insert(item_class_subtype_association).values(item_class_subtype_id=item_class_subtype_id,
                                                                    tag_id=tag_id)
        connection.execute(insert_stmt)
        session.commit()