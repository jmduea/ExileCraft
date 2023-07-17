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

#   MIT License
#
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#
import inspect
import re
from typing import Optional

from sqlalchemy.orm import declared_attr
from sqlalchemy.util import OrderedDict


class ReprMixin:
    """
    Add to a class to get semi-universal repr of the form:

    ClassName<memoryaddr>(arg1=val1, ..., argn=valn, extrakey1=extraval1, ...,
    extrakeyn=extravaln)


    :cvar _REPR_PRIVATE_ATTRIBUTES: If set, also consider attributes with _
    :type _REPR_PRIVATE_ATTRIBUTES: bool

    :cvar _REPR_ARGUMENTS_IGNORE_MISSING: Whether to ignore missing attributes
    if _REPR_ARGUMENTS_TO_ATTRIBUTES is specified
    :type _REPR_ARGUMENTS_IGNORE_MISSING: bool

    :cvar _REPR_ARGUMENTS_TO_ATTRIBUTES: Match arguments against this directory
    and if found as key, use the value to determine the instance attribute
    to retrieve the value for the attribute
    :type _REPR_ARGUMENTS_TO_ATTRIBUTES: dict[str, str]

    :cvar _REPR_ARGUMENTS_IGNORE: Ignore these arguments entirely
    :type _REPR_ARGUMENTS_IGNORE: set

    :cvar _REPR_EXTRA_ATTRIBUTES: Adds those extra attributes, even if they are
    not __init__ arguments.
    The keys are used for the name displayed, the values for retrieving the
    attribute from the instance. If the value is None, the key is used instead.
    :type _REPR_EXTRA_ATTRIBUTES: OrderedDict[str, str]
    """
    
    _REPR_PRIVATE_ATTRIBUTES = False
    _REPR_ARGUMENTS_IGNORE_MISSING = False
    _REPR_ARGUMENTS_TO_ATTRIBUTES = {}
    _REPR_ARGUMENTS_IGNORE = set()
    _REPR_EXTRA_ATTRIBUTES = OrderedDict()
    
    def __get_repr_obj(self, name, test_private):
        if not hasattr(self, name):
            if test_private and self._REPR_PRIVATE_ATTRIBUTES:
                name = '_' + name
                if not hasattr(self, name):
                    return
            else:
                return
        
        return repr(getattr(self, name))
    
    def __repr__(self):
        args = []
        for name, parameter in inspect.signature(self.__init__).parameters.items():
            if parameter.kind == inspect.Parameter.POSITIONAL_ONLY:
                continue
            
            if name in self._REPR_ARGUMENTS_IGNORE:
                continue
            
            test_private = True
            if self._REPR_ARGUMENTS_TO_ATTRIBUTES:
                if name in self._REPR_ARGUMENTS_TO_ATTRIBUTES:
                    name = self._REPR_ARGUMENTS_TO_ATTRIBUTES[name]
                    test_private = False
                elif self._REPR_ARGUMENTS_IGNORE_MISSING:
                    continue
            s = self.__get_repr_obj(name, test_private)
            
            if s is None:
                continue
            
            args.append('%s=%s' % (parameter.name, s))
        
        for k, v in self._REPR_EXTRA_ATTRIBUTES.items():
            args.append('%s=%s' % (k, self.__get_repr_obj(v or k, False)))
        
        return '%s<%s>(%s)' % (
            self.__class__.__name__,
            hex(id(self)),
            ', '.join(args),
        )


class TranslationReprMixin(ReprMixin):
    _REPR_ARGUMENTS_TO_ATTRIBUTES = {
        'parent': '_parent_repr',
    }
    
    @property
    def _parent_repr(self):
        return '%s<%s>' % (self.parent.__class__.__name__, hex(id(self.parent)))


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