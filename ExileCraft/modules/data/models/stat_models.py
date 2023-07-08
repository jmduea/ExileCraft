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
from typing import Optional

from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.association_models import mod_stats_association
from modules.data.models.base_model import Base, intpk

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
target_dir = script_dir.parent / 'json'


class Stat(Base):
    __tablename__ = 'stats'

    id: Mapped[intpk]
    stat: Mapped[str] = mapped_column(String, unique=True)
    alias: Mapped[str] = mapped_column(String, default='')
    is_aliased: Mapped[bool] = mapped_column(Boolean, default=False)
    is_local: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationships
    mods = relationship('Mod', secondary=mod_stats_association, back_populates='mod_stats')
    stat_translations = relationship('StatTranslation', back_populates='stats')
    stat_values = relationship('StatValue', back_populates='stats')


class StatValue(Base):
    __tablename__ = 'stat_values'

    id: Mapped[intpk]
    stat_id: Mapped[int] = mapped_column(Integer, ForeignKey('stats.id'))
    stat_min_value: Mapped[int] = mapped_column(Integer)
    stat_max_value: Mapped[int] = mapped_column(Integer)

    # Relationships
    stats = relationship('Stat', back_populates='stat_values')


class StatTranslation(Base):
    __tablename__ = 'stat_translations'

    id: Mapped[intpk]
    stat_id: Mapped[int] = mapped_column(String, ForeignKey('stats.id'))
    hidden: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationships
    stats = relationship('Stat', back_populates='stat_translations')
    english_translations = relationship("EnglishTranslation", back_populates='stat_translations')


class EnglishTranslation(Base):
    __tablename__ = 'english_translations'

    id: Mapped[intpk]
    stat_translation_id: Mapped[int] = mapped_column(Integer, ForeignKey('stat_translations.id'))
    stat_string: Mapped[str] = mapped_column(String, nullable=False)

    # Relationships
    stat_translations = relationship('StatTranslation', back_populates='english_translations')
    conditions = relationship('StatCondition', back_populates='english_translations')
    formats = relationship('StatFormat', back_populates='english_translations')
    index_handlers = relationship('StatIndexHandler', back_populates='english_translations')


class StatCondition(Base):
    __tablename__ = 'stat_conditions'

    id: Mapped[intpk]
    english_translation_id: Mapped[int] = mapped_column(Integer, ForeignKey('english_translations.id'))
    min: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    max: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    negated: Mapped[bool] = mapped_column(Boolean, default=False)

    english_translations = relationship("EnglishTranslation", back_populates="conditions")


class StatFormat(Base):
    __tablename__ = 'stat_formats'

    id: Mapped[intpk]
    english_translation_id: Mapped[int] = mapped_column(Integer, ForeignKey('english_translations.id'))
    format: Mapped[str] = mapped_column(String, nullable=False)

    english_translations = relationship("EnglishTranslation", back_populates="formats")


class StatIndexHandler(Base):
    __tablename__ = 'stat_index_handlers'

    id: Mapped[intpk]
    english_translation_id: Mapped[int] = mapped_column(Integer, ForeignKey('english_translations.id'))
    handler: Mapped[str] = mapped_column(String, nullable=False)

    english_translations = relationship("EnglishTranslation", back_populates="index_handlers")
