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

import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.association_models import mod_tags_association, item_implicits_association, \
    mod_implicit_tags_association, mod_adds_tags_association, mod_spawn_weights_association, \
    fossil_mods_association
from modules.data.models.base_model import Base, intpk, str50
from modules.data.models.fossil_models import Fossil

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'

MOD_MAX_STATS = 6
MOD_STATS_RANGE = range(1, MOD_MAX_STATS + 1)


@dataclass
class Mod(Base):
    __tablename__ = 'mods'
    
    # Table Columns
    mod: Mapped[str]
    level_req: Mapped[int]
    name: Mapped[str]
    is_essence_only: Mapped[bool]
    domain_id: Mapped[int] = mapped_column(ForeignKey('mod_domains.id'), deferred=True, deferred_group='mod_details')
    generation_type_id: Mapped[int] = mapped_column(ForeignKey('mod_generation_types.id'), deferred=True,
                                                    deferred_group='mod_details')
    mod_group_id: Mapped[int] = mapped_column(ForeignKey('mod_groups.id'), deferred=True, deferred_group='mod_details')
    mod_type_id: Mapped[int] = mapped_column(ForeignKey('mod_types.id'), deferred=True, deferred_group='mod_details')
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    domain = relationship("ModDomain", back_populates='mods')
    generation_type = relationship("ModGenerationType", back_populates='mods')
    mod_group = relationship("ModGroup", back_populates='mods')
    mod_type = relationship("ModType", back_populates='mods')
    translation: Mapped["Translation"] = relationship("Translation", back_populates='mod')
    
    # Many-to-Many Relationships
    mod_stat_values: Mapped[List["ModStatValue"]] = relationship(default_factory=list, back_populates='mod')
    items: Mapped[List["Item"]] = relationship(default_factory=list, secondary=item_implicits_association,
                                               back_populates='item_implicits', lazy='dynamic')
    implicit_tags: Mapped[List["Tag"]] = relationship(default_factory=list, secondary=mod_implicit_tags_association,
                                                      back_populates='mod_implicit_tags', lazy='dynamic')
    tags: Mapped[List["Tag"]] = relationship(default_factory=list, secondary=mod_tags_association,
                                             back_populates='mods', lazy='dynamic')
    mod_stats: Mapped[List["Stat"]] = relationship(default_factory=list, secondary='mod_stat_values',
                                                   back_populates='mods', lazy='dynamic')
    added_tags: Mapped[List["Tag"]] = relationship(default_factory=list, secondary=mod_adds_tags_association,
                                                   back_populates='mod_adds_tags', lazy='dynamic')
    tag_weights: Mapped[List["Tag"]] = relationship(default_factory=list, secondary=mod_spawn_weights_association,
                                                    back_populates='mod_spawn_weights', lazy='dynamic')
    # essences = relationship('Essences', secondary=essence_mods_association, back_populates='mods')
    fossils: Mapped[List["Fossil"]] = relationship(default_factory=list, secondary=fossil_mods_association,
                                                   back_populates='mods', lazy='dynamic')


@dataclass
class ModType(Base):
    __tablename__ = 'mod_types'
    
    # Table Columns
    mod_type: Mapped[str50]
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship(default_factory=list, back_populates='mod_type', foreign_keys=[
        Mod.mod_type_id], init=False)


@dataclass
class ModGenerationType(Base):
    __tablename__ = 'mod_generation_types'
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(init=False)
    generation_type: Mapped[str] = mapped_column(unique=True)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship(default_factory=list, back_populates='generation_type', init=False)


@dataclass
class ModDomain(Base):
    __tablename__ = 'mod_domains'
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(init=False)
    domain: Mapped[str] = mapped_column(unique=True)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship(default_factory=list, back_populates='domain', init=False)
    items: Mapped[List["Item"]] = relationship(default_factory=list, back_populates='domain', init=False)


@dataclass
class ModGroup(Base):
    __tablename__ = 'mod_groups'
    
    # Table Columns
    group: Mapped[str50]
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship(default_factory=list, back_populates='mod_group', foreign_keys=[
        Mod.mod_group_id], init=False)


@dataclass
class ModStatValue(Base):
    __tablename__ = 'mod_stat_values'
    
    # Table Columns
    stat_min_value: Mapped[int]
    stat_max_value: Mapped[int]
    stat_id: Mapped[int] = mapped_column(ForeignKey('stats.id'))
    mod_id: Mapped[int] = mapped_column(ForeignKey('mods.id'))
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    mod = relationship("Mod", back_populates='mod_stat_values', init=False)
    stat = relationship("Stat", back_populates='mod_stat_values', init=False)
