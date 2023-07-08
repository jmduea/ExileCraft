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
from typing import List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.base_model import Base
from modules.data.models.mod_models import Mod

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


class Domain(Base):
    __tablename__ = 'domains'
    
    # Table Columns
    domain: Mapped[str] = mapped_column(String, unique=True, default='item')
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship(back_populates='domain')
    items: Mapped[List["Item"]] = relationship(back_populates='domain')


class GenerationType(Base):
    __tablename__ = 'generation_types'
    
    # Table Columns
    generation_type: Mapped[str] = mapped_column(String, unique=True)
    
    # Relationships
    mods: Mapped[List["Mod"]] = relationship(back_populates='generation_type')
