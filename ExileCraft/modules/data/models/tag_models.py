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

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.association_models import mod_tags_association, item_tags_association, \
    mod_adds_tags_association, mod_spawn_weights_association, mod_implicit_tags_association, item_class_association, \
    item_class_subtype_association
from modules.data.models.base_model import Base

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


class Tag(Base):
    __tablename__ = 'tags'
    
    tag: Mapped[str] = mapped_column(unique=True)
    
    # Relationships
    
    # Relationships with a secondary association table included
    mods: Mapped[List["Mod"]] = relationship(secondary=mod_tags_association, back_populates='tags')
    mod_implicit_tags = relationship('Mod', secondary=mod_implicit_tags_association, back_populates='implicit_tags')
    mod_adds_tags = relationship('Mod', secondary=mod_adds_tags_association, back_populates='added_tags')
    mod_spawn_weights = relationship('Mod', secondary=mod_spawn_weights_association, back_populates='tag_weights')
    
    items: Mapped[List["Item"]] = relationship(secondary=item_tags_association, back_populates='tags')
    item_class: Mapped[List["ItemClass"]] = relationship(secondary=item_class_association, back_populates='tags')
    item_class_subtypes: Mapped[List["ItemClassSubtype"]] = relationship(secondary=item_class_subtype_association,
                                                                         back_populates='tags')
    
    def __repr__(self):
        return f"Tags(id={self.id!r}, tag={self.tag!r})"
