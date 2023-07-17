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

from sqlalchemy import ForeignKey, Table, Column, Integer
from modules.data.models.base_model import Base

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'

# item_class_subtype_association = Table('item_class_subtype_association', Base.metadata,
#                                        Column('item_class_subtype_id', Integer, ForeignKey('item_class_subtypes.id')),
#                                        Column('tag_id', Integer, ForeignKey('tags.id'))
#                                        )

item_tags_association = Table('item_tags_association', Base.metadata,
                              Column('item_id', Integer, ForeignKey('items.id')),
                              Column('tag_id', Integer, ForeignKey('tags.id'))
                              )

item_implicits_association = Table('item_implicits_association', Base.metadata,
                                   Column('item_id', Integer, ForeignKey('items.id')),
                                   Column('mod_id', Integer, ForeignKey('mods.id'))
                                   )

mod_types_association = Table('mod_types_association', Base.metadata,
                              Column('mod_id', Integer, ForeignKey('mods.id')),
                              Column('mod_type_id', Integer, ForeignKey('mod_types.id'))
                              )

mod_groups_association = Table('mod_groups_association', Base.metadata,
                               Column('mod_id', Integer, ForeignKey('mods.id')),
                               Column('mod_group_id', Integer, ForeignKey('mod_groups.id'))
                               )

mod_generation_types_association = Table('mod_generation_types_association', Base.metadata,
                                         Column('mod_id', Integer, ForeignKey('mods.id')),
                                         Column('generation_type_id', Integer,
                                                ForeignKey('generation_types.id'))
                                         )

mod_adds_tags_association = Table('mod_adds_tags_association', Base.metadata,
                                  Column('mod_id', Integer, ForeignKey('mods.id')),
                                  Column('tag_id', Integer, ForeignKey('tags.id'))
                                  )

mod_implicit_tags_association = Table('mod_implicit_tags_association', Base.metadata,
                                      Column('mod_id', Integer, ForeignKey('mods.id')),
                                      Column('tag_id', Integer, ForeignKey('tags.id'))
                                      )
