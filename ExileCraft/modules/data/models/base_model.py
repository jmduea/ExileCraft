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
import math
import re
from dataclasses import dataclass
from typing import Annotated, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column, declared_attr, Mapped, relationship

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
str50 = Annotated[str, mapped_column(String(50), default=None)]


@dataclass
class Base(MappedAsDataclass, DeclarativeBase):
    pass


class TableNameMixIn:
    """
    Provides a method for generating the name of a database table based on the name of the class.
    
    Uses regular expressions to convert the class name from CamelCase to snake_case and appends an 's' to the end of
    the resulting string to form the table name.
    
    Methods:
    -__tablename__(cls) -> Optional[str]:
        Class method that returns the name of the database table that corresponds to the class that uses the
        TableNameMixin mixin. Uses regular expressions to convert the class name from CamelCase to snake_case.
    
    """
    
    @declared_attr
    def __tablename__(cls) -> Optional[str]:
        name = cls.__name__
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
        return name + 's'
    
    
@dataclass
class ItemClassMixin(MappedAsDataclass):
    item_class_id: Mapped[int] = mapped_column("ItemClass", ForeignKey('item_classes.id'))
    
    @declared_attr
    def item_class(cls) -> Mapped["ItemClass"]:
        return relationship('ItemClass', init=False)


@dataclass
class ItemClassSubtypeMixin(MappedAsDataclass):
    item_class_subtype_id: Mapped[Optional[int]] = mapped_column("ItemClassSubtype", ForeignKey(
        'item_class_subtypes.id'),
                                                                                init=False)
    
    @declared_attr
    def item_class_subtype(cls) -> Mapped["ItemClassSubtype"]:
        return relationship('ItemClassSubtype', init=False)


@dataclass
class InfluencedItemMixin(MappedAsDataclass):
    has_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_crusader_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_hunter_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_redeemer_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_warlord_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_shaper_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    has_elder_influence: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    is_eater_of_worlds_item: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    is_searing_exarch_item: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    is_synthesis_item: Mapped[bool] = mapped_column(deferred=True, deferred_group='influence_flags')
    

@dataclass
class FlaskPropertiesMixin(MappedAsDataclass):
    buff_id: Mapped[Optional[str]] = mapped_column(nullable=False)
    buff_stat: Mapped[Optional[str]] = mapped_column(nullable=False)
    implicits: Mapped[Optional[str]] = mapped_column(nullable=False)
    charges_max: Mapped[Optional[int]] = mapped_column(nullable=False)
    charges_per_use: Mapped[Optional[int]] = mapped_column(nullable=False)
    duration: Mapped[Optional[int]] = mapped_column(nullable=False)
    life_per_use: Mapped[Optional[int]] = mapped_column(nullable=False)
    mana_per_use: Mapped[Optional[int]] = mapped_column(nullable=False)


@dataclass
class JewelleryPropertiesMixIn(MappedAsDataclass):
    catalyst_quality_type: Mapped[Optional[str]] = mapped_column(use_existing_column=True, nullable=False, default=None)
    catalyst_quality_value: Mapped[Optional[int]] = mapped_column(use_existing_column=True, nullable=False,
                                                                  default=None)


@dataclass
class AnointmentPropertyMixin(MappedAsDataclass):
    pass
