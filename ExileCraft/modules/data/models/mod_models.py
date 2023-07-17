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
from typing import List, Optional

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.association_models import item_implicits_association, mod_tags_association, \
    mod_stats_association, mod_types_association, mod_groups_association, mod_generation_types_association, \
    mod_adds_tags_association, mod_implicit_tags_association, mod_tag_weights_association
from modules.data.models.base_model import Base, intpk
from modules.data.models.shared_models import Domain
from modules.data.models.stat_models import StatValue
from modules.data.models.translation_models import Translation

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


@dataclass
class Mod(Base):
    __tablename__ = 'mods'
    
    # Table Columns
    id: Mapped[intpk] = mapped_column(init=False)
    mod_name: Mapped[str] = mapped_column(String(190), nullable=False)
    name: Mapped[str] = mapped_column(String(180))
    level_req: Mapped[int] = mapped_column(Integer, nullable=False, insert_default=0, default=0)
    essence_only: Mapped[bool] = mapped_column(nullable=False, insert_default=False, default=False)
    domain_id: Mapped[int] = mapped_column(ForeignKey('domains.id'), insert_default=None, default=None)
    generation_type_id: Mapped[int] = mapped_column(ForeignKey('generation_types.id'), insert_default=None,
                                                    default=None)
    mod_type_id: Mapped[int] = mapped_column(ForeignKey('mod_types.id'), insert_default=None, default=None)
    mod_group_id: Mapped[int] = mapped_column(ForeignKey('mod_groups.id'), insert_default=None, default=None)
    
    # Relationships
    domain: Mapped["Domain"] = relationship("Domain", back_populates='mods', uselist=False, default='item')
    items: Mapped[List["Item"]] = relationship("Item", secondary=item_implicits_association,
                                               back_populates='implicits', default_factory=list,
                                               lazy='selectin')
    stat_values: Mapped[List["StatValue"]] = relationship("StatValue", back_populates='mod',
                                                          default_factory=list, lazy='selectin')
    translation: Mapped[List["Translation"]] = relationship("Translation", back_populates='mod', default_factory=list,
                                                            lazy='selectin')
    mod_type: Mapped["ModType"] = relationship("ModType", back_populates='mods', default='', lazy='selectin')
    mod_group: Mapped["ModGroup"] = relationship("ModGroup", back_populates='mods', default='', lazy='selectin')
    generation_type: Mapped["GenerationType"] = relationship("GenerationType",
                                                             back_populates='mods', default='', lazy='selectin')
    adds_tags: Mapped[List["Tag"]] = relationship("Tag", secondary=mod_adds_tags_association,
                                                  back_populates='added_by_mods',
                                                  default_factory=list, lazy='selectin')
    implicit_tags: Mapped[List["Tag"]] = relationship("Tag", secondary=mod_implicit_tags_association,
                                                      back_populates='mod_implicit_tags', default_factory=list,
                                                      lazy='selectin')
    tag_weights: Mapped[List["TagWeight"]] = relationship("TagWeight", back_populates='mod_weight',
                                                          default_factory=list, lazy='selectin')


class ModType(Base):
    __tablename__ = 'mod_types'
    
    # Table Columns
    type: Mapped[str] = mapped_column(String(60), unique=True)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship("Mod", secondary=mod_types_association, back_populates='mod_type',
                                             init=False, default_factory=list, lazy='selectin')


class GenerationType(Base):
    __tablename__ = 'generation_types'
    
    # Table Columns
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    generation_type: Mapped[str] = mapped_column(String(60), unique=True)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship("Mod", secondary=mod_generation_types_association,
                                             back_populates='generation_type', default_factory=list, lazy='selectin',
                                             init=False)


class ModGroup(Base):
    __tablename__ = 'mod_groups'
    
    # Table Columns
    group: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship("Mod", secondary=mod_groups_association, back_populates='mod_group',
                                             default_factory=list, lazy='selectin', init=False)
    
    def __init__(self, group) -> None:
        super().__init__()
        self.group = group if group else None
