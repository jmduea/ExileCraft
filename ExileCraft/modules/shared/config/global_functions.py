# ##################################################################################################
#   MIT License                                                                                    #
#                                                                                                  #
#   Copyright (c) 2023 Jon Duea                                                                    #
#                                                                                                  #
#   Permission is hereby granted, free of charge, to any person obtaining a copy                   #
#   of this software and associated documentation files (the "Software"), to deal                  #
#   in the Software without restriction, including without limitation the rights                   #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                      #
#   copies of the Software, and to permit persons to whom the Software is                          #
#   furnished to do so, subject to the following conditions:                                       #
#                                                                                                  #
#   The above copyright notice and this permission notice shall be included in all                 #
#   copies or substantial portions of the Software.                                                #
#                                                                                                  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                     #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                       #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                    #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                         #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                  #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                  #
#   SOFTWARE.                                                                                      #
# ##################################################################################################
import re


def snake_case(name):
    # Convert CamelCase to snake_case
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def round_with_2_decimal_places(value):
    if value is not None:
        return round(value, 2)
    return None


def round_with_no_decimal_places(value):
    if value is not None:
        return round(value)
    return None
