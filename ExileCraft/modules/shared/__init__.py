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


# =============================================================================
# Imports
# =============================================================================

# Python

# 3rd-party

# self

# =============================================================================
# Globals
# =============================================================================

__all__ = []

# =============================================================================
# Classes
# =============================================================================


class InheritedDocStringsMeta(type):
    def __new__(cls, name, args, attrs):
        if not ('__doc__' in attrs and attrs['__doc__']):
            for mro in cls.mro(cls):
                docstring = mro.__doc__
                if docstring is not None:
                    cls.__doc__ = docstring
                    #attrs['__doc__'] = docstring
                    break
        for attr, attribute in attrs.items():
            if attribute.__doc__:
                continue

            for mro in cls.mro(cls):
                if not hasattr(mro, attr):
                    break
                docstring = getattr(mro, attr).__doc__
                if docstring is not None:
                    attribute.__doc__ = docstring
                    break

        return type.__new__(cls, name, args, attrs)

# =============================================================================
# Functions
# =============================================================================
