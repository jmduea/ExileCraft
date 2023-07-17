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

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.association_models import item_tags_association, mod_tags_association, \
    mod_implicit_tags_association, mod_adds_tags_association, mod_tag_weights_association
from modules.data.models.base_model import Base, intpk

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


@dataclass
class Tag(Base):
    __tablename__ = 'tags'
    
    id: Mapped[intpk] = mapped_column(init=False)
    tag: Mapped[str] = mapped_column(unique=True)
    
    # Relationships
    
    items: Mapped[List["Item"]] = relationship("Item", secondary=item_tags_association,
                                               back_populates='tags', default_factory=list, lazy='selectin')
    added_by_mods: Mapped[List["Mod"]] = relationship("Mod", secondary=mod_adds_tags_association,
                                                      back_populates='adds_tags',
                                                      default_factory=list, lazy='selectin')
    mod_implicit_tags: Mapped[List["Mod"]] = relationship("Mod", secondary=mod_implicit_tags_association,
                                                          back_populates='implicit_tags', default_factory=list,
                                                          lazy='selectin')
    mod_weights: Mapped[List["TagWeight"]] = relationship("TagWeight", back_populates='tag', default_factory=list,
                                                          lazy='selectin')


@dataclass
class TagWeight(Base):
    __tablename__ = 'tag_weights'
    
    # Table columns
    id: Mapped[intpk] = mapped_column(init=False)
    mod_id: Mapped[int] = mapped_column(Integer, ForeignKey('mods.id'))
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey('tags.id'))
    tag: Mapped["Tag"] = relationship("Tag", back_populates='mod_weights', lazy='selectin', uselist=False)
    mod_weight: Mapped["Mod"] = relationship("Mod", back_populates='tag_weights', lazy='selectin', uselist=False)
    
    weight: Mapped[int] = mapped_column(Integer, nullable=False, insert_default=0, default=0)
    
    