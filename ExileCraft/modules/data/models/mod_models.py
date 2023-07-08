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
import json
import os

from pathlib import Path
from typing import Optional, List

from sqlalchemy import String, ForeignKey, Integer, Boolean, event
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session, joinedload

from modules.data.models.association_models import mod_tags_association, item_implicits_association, \
    mod_implicit_tags_association, mod_stats_association, mod_adds_tags_association, mod_spawn_weights_association, \
    fossil_mods_association
from modules.data.models.base_model import Base, intpk
from modules.data.models.fossil_models import Fossil
from modules.data.models.stat_models import StatTranslation, Stat

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


class Mod(Base):
    __tablename__ = 'mods'
    
    # Table Columns
    mod: Mapped[str] = mapped_column(String)
    level_req: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    is_essence_only: Mapped[bool] = mapped_column(Boolean, default=False)
    domain_id: Mapped[int] = mapped_column(Integer, ForeignKey('domains.id'))
    generation_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation_types.id'))
    mod_group_id: Mapped[int] = mapped_column(Integer, ForeignKey('mod_groups.id'))
    mod_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('mod_types.id'))
    
    @hybrid_method
    def get_translation(self):
        for mod_stat in self.mod_stats:
            stat_id = mod_stat.stat_id
            stat_min_value = mod_stat.stat_min_value
            stat_max_value = mod_stat.stat_max_value
            
            stat = Stat.query.get(stat_id)
            for stat_translation in stat.stat_translations:
                for english_translation in stat_translation.english_translations:
                    conditions = english_translation.conditions
                    formats = english_translation.formats
                    
                for value in range(stat_min_value, stat_max_value + 1):
                    if self.check_conditions(conditions, value):
                        for format in formats:
                            yield self.format_translation(format, value)
                        
    @hybrid_method
    def check_conditions(self, conditions, value):
        for condition in conditions:
            if (condition.min or float('-inf')) <= value <= (condition.max or float('inf')):
                return not condition.negated
        return False
    
    @hybrid_method
    def format_translation(self, translation, value):
        for format in translation.formats:
            return format.format.format(value)

    # Relationships
    domain = relationship('Domain', back_populates='mods')  # Many-to-one relationship
    generation_type = relationship('GenerationType', back_populates='mods')  # Many-to-one relationship
    mod_groups: Mapped["ModGroup"] = relationship('ModGroup', back_populates='mods', foreign_keys=[mod_group_id])
    mod_types: Mapped["ModType"] = relationship('ModType', back_populates='mods', foreign_keys=[mod_type_id])
    
    # Relationships with a secondary association table included
    items: Mapped[List["Item"]] = relationship(secondary=item_implicits_association, back_populates='item_implicits')
    implicit_tags = relationship('Tag', secondary=mod_implicit_tags_association, back_populates='mod_implicit_tags')
    tags = relationship('Tag', secondary=mod_tags_association, back_populates='mods')
    mod_stats: Mapped[List["Stat"]] = relationship(secondary=mod_stats_association, back_populates='mods')
    added_tags = relationship('Tag', secondary=mod_adds_tags_association, back_populates='mod_adds_tags')
    tag_weights = relationship('Tag', secondary=mod_spawn_weights_association, back_populates='mod_spawn_weights')
    # essences = relationship('Essences', secondary=essence_mods_association, back_populates='mods')
    fossils: Mapped["Fossil"] = relationship('Fossil', secondary=fossil_mods_association, back_populates='mods')


class ModType(Base):
    __tablename__ = 'mod_types'
    
    id: Mapped[intpk]
    mod_type: Mapped[str] = mapped_column(String(180))
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship('Mod', back_populates='mod_types', foreign_keys=[Mod.mod_type_id])


class ModGroup(Base):
    __tablename__ = 'mod_groups'
    
    id: Mapped[intpk]
    group: Mapped[str] = mapped_column(String(255))
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship('Mod', back_populates='mod_groups', foreign_keys=[Mod.mod_group_id])
