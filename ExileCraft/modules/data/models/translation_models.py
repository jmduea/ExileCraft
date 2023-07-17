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
from ast import literal_eval
from dataclasses import dataclass
from itertools import zip_longest
from typing import List, Union

from sqlalchemy import ForeignKey, PickleType, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.base_model import Base, intpk


class Translation(Base):
    __tablename__ = 'translations'
    
    # Table Columns
    string: Mapped[str] = mapped_column(String(250))
    hidden: Mapped[bool] = mapped_column(init=False)
    stat_id: Mapped[int] = mapped_column(ForeignKey('stat_values.id'), init=False)
    mod_id: Mapped[int] = mapped_column(ForeignKey('mods.id'), init=False)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    conditions: Mapped[List["TranslationCondition"]] = relationship("TranslationCondition",
                                                                    back_populates='translation_conditions')
    formats: Mapped[List["TranslationFormat"]] = relationship("TranslationFormat", back_populates='translation_formats')
    index_handlers: Mapped[List["TranslationIndexHandler"]] = relationship("TranslationIndexHandler",
                                                                           back_populates='translation_index_handlers')
    mod: Mapped["Mod"] = relationship("Mod", back_populates='translation', init=False)
    stat_values: Mapped[List["StatValue"]] = relationship("StatValue", back_populates='translations',
                                                          default_factory=list,
                                                          init=False)
    
    def match_conditions(self, stat):
        for condition, value in zip_longest(self.conditions, stat.values):
            min_value = condition.get('min', -float('inf'))
            max_value = condition.get('max', float('inf'))
            
            if not (min_value <= value <= max_value):
                return False
        return True
    
    def apply_index_handlers(self, values):
        for handler, value in zip_longest(self.index_handlers, values):
            if handler:
                values[values.index(value)] = literal_eval(handler.replace('v', str(value)))
        
        return values
    
    def format_values(self, values):
        return [f'+{value}' if value > 0 else f'{value}' if index == '+#' else '' if index == 'ignored' else value for
                index, value in zip_longest(self.format, values)]
    
    def insert_values_into_string(self, values):
        string = self.string
        
        for i, value in enumerate(values):
            string = string.replace(f'{{{i}}}', str(value))
        return string


class TranslationCondition(Base):
    __tablename__ = 'translation_conditions'
    
    # Table Columns
    condition_data = mapped_column(PickleType)
    translation_id: Mapped[int] = mapped_column(ForeignKey('translations.id'), init=False)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    translation_conditions: Mapped["Translation"] = relationship("Translation", back_populates='conditions',
                                                                 uselist=False, init=False)
    
    @hybrid_property
    def condition(self):
        return self.condition_data
    
    @condition.setter
    def condition(self, value: Union[bytes, str]):
        try:
            self.condition_data = bytes(value, 'utf-8')
        except TypeError:
            raise ValueError("Condition must be a string or bytes object.")
        except UnicodeDecodeError:
            raise ValueError("Condition must be a valid utf-8 encoded string")


class TranslationFormat(Base):
    __tablename__ = 'translation_formats'
    
    # Table Columns
    format_data = mapped_column(PickleType)
    translation_id: Mapped[int] = mapped_column(ForeignKey('translations.id'), init=False)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    translation_formats: Mapped["Translation"] = relationship("Translation", back_populates='formats', uselist=False,
                                                              init=False)
    
    @hybrid_property
    def format(self):
        return self.format_data
    
    @format.setter
    def format(self, value):
        try:
            self.format_data = bytes(value, 'utf-8')
        except TypeError:
            raise ValueError("Condition must be a string or bytes object.")
        except UnicodeDecodeError:
            raise ValueError("Condition must be a valid utf-8 encoded string")


@dataclass
class TranslationIndexHandler(Base):
    __tablename__ = 'translation_index_handlers'
    
    # Table Columns
    index_handler_data = mapped_column(PickleType)
    translation_id: Mapped[int] = mapped_column(ForeignKey('translations.id'), init=False)
    id: Mapped[intpk] = mapped_column(init=False)
    
    # Relationships
    translation_index_handlers: Mapped["Translation"] = relationship("Translation", back_populates='index_handlers',
                                                                     uselist=False, init=False)
    
    @hybrid_property
    def index_handler(self):
        return self.index_handler_data
    
    @index_handler.setter
    def index_handler(self, value):
        try:
            self.index_handler_data = bytes(value, 'utf-8')
        except TypeError:
            raise ValueError("Condition must be a string or bytes object.")
        except UnicodeDecodeError:
            raise ValueError("Condition must be a valid utf-8 encoded string")
