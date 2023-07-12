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
import math
import typing
from typing import Annotated, Optional

import sqlalchemy.orm.exc
from sqlalchemy import ForeignKey, String, Integer, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column, declared_attr, Mapped, relationship

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class Base(DeclarativeBase):
    
    def __repr__(self) -> str:
        return self._repr(id=self.id)
    
    def _repr(self, **fields: typing.Dict[str, typing.Any]) -> str:
        """
        Helper for __repr__
        Args:
            **fields ():

        Returns:

        """
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                field_strings.append(f'{key}={field!r}')
            except sqlalchemy.orm.exc.DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"
    
    id: Mapped[intpk]


class ItemClassMixin:
    item_class_id: Mapped[int] = mapped_column(Integer, ForeignKey('item_classes.id'))
    
    @declared_attr
    def item_class(cls) -> Mapped["ItemClass"]:
        return relationship('ItemClass')


class ItemClassSubtypeMixin:
    item_class_subtype_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('item_class_subtypes.id'),
                                                                 nullable=True)
    
    @declared_attr
    def item_class_subtype(cls) -> Mapped["ItemClassSubtype"]:
        return relationship('ItemClassSubtype')


@dataclass
class InfluencedItemMixin(MappedAsDataclass):
    has_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_crusader_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_hunter_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_redeemer_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_warlord_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_shaper_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_elder_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    is_eater_of_worlds_item: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    is_searing_exarch_item: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    is_synthesis_item: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')


class ArmourBaseMixin:
    armour_min: Mapped[int] = mapped_column(use_existing_column=True)
    armour_max: Mapped[int] = mapped_column(use_existing_column=True)
    
    @hybrid_property
    def average_armour(self) -> int:
        return math.floor((self.armour_min + self.armour_max) / 2)
    

class EvasionBaseMixin:
    evasion_min: Mapped[int] = mapped_column(use_existing_column=True)
    evasion_max: Mapped[int] = mapped_column(use_existing_column=True)
    
    @hybrid_property
    def average_evasion(self) -> int:
        return math.floor((self.evasion_min + self.evasion_max) / 2)
    
    
class EnergyShieldBaseMixin:
    energy_shield_min: Mapped[int] = mapped_column(use_existing_column=True)
    energy_shield_max: Mapped[int] = mapped_column(use_existing_column=True)
    
    @hybrid_property
    def average_energy_shield(self) -> int:
        return math.floor((self.energy_shield_min + self.energy_shield_max) / 2)


class WardBaseMixin:
    ward_min: Mapped[int] = mapped_column(use_existing_column=True)
    ward_max: Mapped[int] = mapped_column(use_existing_column=True)
    
    @hybrid_property
    def average_ward(self) -> int:
        return math.floor((self.ward_min + self.ward_max) / 2)
    
    
class ShieldMixin:
    block: Mapped[Optional[int]] = mapped_column(use_existing_column=True, nullable=True)


class MovementPenaltyMixin:
    movement_penalty: Mapped[Optional[int]] = mapped_column(use_existing_column=True, nullable=True)


class WeaponPropertiesMixin:
    critical_strike_chance: Mapped[float]
    attack_time: Mapped[float]
    physical_damage_min: Mapped[int]
    physical_damage_max: Mapped[int]
    fire_damage_min: Mapped[Optional[int]] = mapped_column(nullable=True)
    fire_damage_max: Mapped[Optional[int]] = mapped_column(nullable=True)
    lightning_damage_min: Mapped[Optional[int]] = mapped_column(nullable=True)
    lightning_damage_max: Mapped[Optional[int]] = mapped_column(nullable=True)
    cold_damage_min: Mapped[Optional[int]] = mapped_column(nullable=True)
    cold_damage_max: Mapped[Optional[int]] = mapped_column(nullable=True)
    chaos_damage_min: Mapped[Optional[int]] = mapped_column(nullable=True)
    chaos_damage_max: Mapped[Optional[int]] = mapped_column(nullable=True)
    range: Mapped[int]
    
    @hybrid_property
    def average_physical_damage(self) -> int:
        return math.floor((self.physical_damage_min + self.physical_damage_max) / 2)
    
    @hybrid_property
    def average_fire_damage(self) -> int:
        return math.floor((self.fire_damage_min + self.fire_damage_max) / 2)
    
    @hybrid_property
    def average_lightning_damage(self) -> int:
        return math.floor((self.lightning_damage_min + self.lightning_damage_max) / 2)
    
    @hybrid_property
    def average_cold_damage(self) -> int:
        return math.floor((self.cold_damage_min + self.cold_damage_max) / 2)
    
    @hybrid_property
    def average_chaos_damage(self) -> int:
        return math.floor((self.chaos_damage_min + self.chaos_damage_max) / 2)
    
    @hybrid_property
    def attacks_per_second(self) -> str:
        """
        Calculates the attacks per second of an item.

        This method takes the attack time of an item and calculates the attacks per second.

        Returns:
            attacks_per_second (str): The attacks per second of the item, formatted as a string with two decimal places.
        """
        attack_time = (1000 / float(self.attack_time))
        attacks_per_second = "{:.2f}".format(attack_time)
        return attacks_per_second
    
    @hybrid_property
    def critical_strike_chance_percentage(self):
        critical_strike_chance_percentage = (float(self.critical_strike_chance) / 100)
        critical_strike_chance_percentage = "{:.2f}".format(critical_strike_chance_percentage)
        return critical_strike_chance_percentage


class RequirementsMixin:
    level: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    strength: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=None)
    dexterity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=None)
    intelligence: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=None)


class FlaskPropertiesMixin:
    buff_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    buff_stat: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    implicits: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    charges_max: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    charges_per_use: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    
    life_per_use: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    mana_per_use: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
