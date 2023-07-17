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
from dataclasses import dataclass
from pathlib import Path
from typing import List

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.association_models import mod_stats_association
from modules.data.models.base_model import Base, intpk

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


@dataclass
class Stat(Base):
    __tablename__ = 'stats'
    
    # Table Columns
    is_aliased: Mapped[bool]
    is_local: Mapped[bool]
    name: Mapped[str] = mapped_column(String(250), unique=True)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    values: Mapped[List["StatValue"]] = relationship("StatValue", back_populates='stat', default_factory=list,
                                                     lazy='selectin')



@dataclass
class StatValue(Base):
    __tablename__ = 'stat_values'
    
    id: Mapped[intpk] = mapped_column(init=False)
    mod_id: Mapped[int] = mapped_column(ForeignKey('mods.id'), init=False, nullable=False)
    stat_id: Mapped[int] = mapped_column(ForeignKey('stats.id'), init=False, nullable=False)
    stat: Mapped["Stat"] = relationship("Stat", back_populates='values', lazy='selectin')
    mod: Mapped["Mod"] = relationship("Mod", back_populates='stat_values', lazy='selectin')
    
    stat_min_value: Mapped[int] = mapped_column(Integer, nullable=False, insert_default=0, default=0)
    stat_max_value: Mapped[int] = mapped_column(Integer, nullable=False, insert_default=0, default=0)
    translations: Mapped[List["Translation"]] = relationship("Translation", back_populates='stat_values',
                                                             default_factory=list, lazy='selectin')
    