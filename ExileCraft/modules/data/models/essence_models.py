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
from typing import Optional

from sqlalchemy import String, ForeignKey, Integer, Boolean, event
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session

from modules.data.models.base_model import Base, intpk

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


class Essences(Base):
    __tablename__ = 'essences'
    
    id: Mapped[intpk]
    essence: Mapped[str] = mapped_column(String(255), unique=True)
    item_level_restriction: Mapped[int] = mapped_column(Integer, default=None)
    
    # Relationships
    mods = relationship('Mods', secondary=essence_mods_association, back_populates='essences')
    essence_tiers: Mapped["EssenceTiers"] = relationship('EssenceTiers', back_populates='essences')
    item_class = relationship('ItemClass', secondary=essence_mods_association, back_populates='essences')
    

class EssenceTiers(Base):
    __tablename__ = 'essence_tiers'
    
    id: Mapped[int] = mapped_column(Integer, ForeignKey('essences.id'), primary_key=True)
    tier: Mapped[int] = mapped_column(Integer)
    
    # Relationships
    essences: Mapped["Essences"] = relationship('Essences', back_populates='essence_tiers')
