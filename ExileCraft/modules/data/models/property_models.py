#   MIT License
#
#   Copyright (c) 2023 Jon Duea
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
import math

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column

from modules.data.models.base_model import Base, intpk


class Armour(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    armour_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    armour_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_armour(self) -> int:
        return math.floor((self.armour_min + self.armour_max) / 2)


class EnergyShield(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    energy_shield_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    energy_shield_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_energy_shield(self) -> int:
        return math.floor((self.energy_shield_min + self.energy_shield_max) / 2)


class Evasion(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    evasion_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    evasion_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_evasion(self) -> int:
        return math.floor((self.evasion_min + self.evasion_max) / 2)
    
    
class Ward(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    ward_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    ward_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_ward(self) -> int:
        return math.floor((self.ward_min + self.ward_max) / 2)


class Block(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    block_chance_value: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)


class MovementPenalty(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    movement_penalty_value: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    
class CriticalStrikeChance(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    critical_strike_chance_value: Mapped[float] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def critical_strike_chance_percentage(self):
        critical_strike_chance_percentage = (float(self.critical_strike_chance_value) / 100)
        critical_strike_chance_percentage = "{:.2f}".format(critical_strike_chance_percentage)
        return critical_strike_chance_percentage
    
    
class AttackTime(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    attack_time_value: Mapped[float] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def attacks_per_second(self) -> str:
        """
        Calculates the attacks per second of an item.

        This method takes the attack time of an item and calculates the attacks per second.

        Returns:
            attacks_per_second (str): The attacks per second of the item, formatted as a string with two decimal places.
        """
        attack_time = (1000 / float(self.attack_time_value))
        attacks_per_second = "{:.2f}".format(attack_time)
        return attacks_per_second
    
    
class Range(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    range_value: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    
class PhysicalDamage(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    physical_damage_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    physical_damage_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_physical_damage(self) -> int:
        return math.floor((self.physical_damage_min + self.physical_damage_max) / 2)
    
    
class FireDamage(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    fire_damage_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    fire_damage_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_fire_damage(self) -> int:
        return math.floor((self.fire_damage_min + self.fire_damage_max) / 2)
    
    
class LightningDamage(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    lightning_damage_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    lightning_damage_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_lightning_damage(self) -> int:
        return math.floor((self.lightning_damage_min + self.lightning_damage_max) / 2)
    
    
class ColdDamage(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    cold_damage_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    cold_damage_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    
    @hybrid_property
    def average_cold_damage(self) -> int:
        return math.floor((self.cold_damage_min + self.cold_damage_max) / 2)
    
    
class ChaosDamage(Base):
    id: Mapped[intpk] = mapped_column(nullable=False, init=False)
    chaos_damage_min: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)
    chaos_damage_max: Mapped[int] = mapped_column(nullable=False, insert_default=0, default=0)

    @hybrid_property
    def average_chaos_damage(self) -> int:
        return math.floor((self.chaos_damage_min + self.chaos_damage_max) / 2)
    
    