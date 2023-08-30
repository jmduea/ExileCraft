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
from dataclasses import dataclass
from typing import Any


@dataclass
class Translation:
    """

    The `Translation` class represents a translation object that provides a way to obtain translations based on given conditions and input values.

    Attributes:
        ids (list): A list of identifiers used to reference the input values.
        translations (list): A list of translation objects containing conditions and strings.
        hidden (bool): Indicates whether the translation is hidden or not.

    Methods:
        __init__(self, **kw: Any)
            Initializes a new instance of the `Translation` class.

        get_translation(self, stat_values)
            Retrieves the translation string based on the given input values.

        format_translation(self, translation, stat_values)
            Formats the translation string by replacing placeholders with actual values.

    """

    def __init__(self, **kw: Any):
        super().__init__(**kw)
        self.ids = self.data.get("ids", [])
        self.translations = self.data.get("translations", [])
        self.hidden = self.data.get("hidden", False)

    def get_translation(self, stat_values):
        """
        Parameters
        ----------
        stat_values : dict
            A dictionary containing the values of the statistical data. The dictionary should have the following structure:
            {
                "stat1": {
                    "min": float,  # Minimum value of stat1
                    "max": float   # Maximum value of stat1
                },
                "stat2": {
                    "min": float,  # Minimum value of stat2
                    "max": float   # Maximum value of stat2
                },
                ...
            }
            The keys should correspond to the IDs used in the translation conditions.

        Returns
        -------
        str
            The formatted translation string if a match is found in the translations list. Otherwise, returns "Translation not available".
        """
        for translation in self.translations:
            conditions = translation["condition"]
            matches = True

            for i, condition in enumerate(conditions):
                if stat_values.get(self.ids[i]) is None:
                    matches = False
                    break
                stat_min_value = stat_values.get(self.ids[i]).get("min")
                stat_max_value = stat_values.get(self.ids[i]).get("max")
                min_value = condition.get("min", float("-inf"))
                max_value = condition.get("max", float("inf"))
                negated = condition.get("negated", False)

                if negated:
                    condition_result = not (
                        min_value <= stat_min_value <= max_value
                    ) and not (min_value <= stat_max_value <= max_value)
                else:
                    condition_result = (
                        min_value <= stat_min_value <= max_value
                        and min_value <= stat_max_value <= max_value
                    )

                if not condition_result:
                    matches = False
                    break

            if matches:
                formatted_value = self.format_translation(translation, stat_values)
                if formatted_value is not None:
                    return formatted_value

        return "Translation not available"

    def format_translation(self, translation, stat_values):
        """
        Parameters
        ----------
        translation : dict
            The translation containing the string, index handlers, and formats.
        stat_values : dict
            The dictionary containing the statistical values.

        Returns
        -------
        str
            The formatted translation string."""
        string = translation["string"]
        index_handlers = translation["index_handlers"]
        formats = translation["format"]

        for i in range(len(index_handlers)):
            min_value = stat_values.get(self.ids[i]).get("min")
            max_value = stat_values.get(self.ids[i]).get("max")
            value = stat_values.get(self.ids[i], 0)
            if min_value != max_value:
                for handler in index_handlers[i]:
                    min_value = apply_index_handler(handler, min_value)
                    max_value = apply_index_handler(handler, max_value)
                value = format_range_value(min_value, max_value)
            if min_value == max_value:
                value = min_value
                for handler in index_handlers[i]:
                    value = apply_index_handler(handler, value)

            formatted_value = apply_format(formats[i], value)

            if formatted_value is not None:
                string = string.replace("{" + str(i) + "}", formatted_value)
            else:
                string = string.replace("{" + str(i) + "}", "")

        return string


def apply_index_handler(handler: str, value: float) -> float:
    """
    Apply an index handler to a value.

    Parameters
    ----------
    handler : str
        The ID of the handler to be applied.

    value : float
        The value to which the handler will be applied.

    Returns
    -------
    float
        The result of applying the handler to the value.

    """
    # Check if the handler matches any of the quantifier IDs
    for quantifier in quantifiers:
        if handler == quantifier.id:
            # Apply the corresponding handler function and return the result
            return quantifier.handler(value)

    # If the handler doesn't match any of the quantifier IDs, return the value unchanged
    return value


def apply_format(format_str, value):
    """
    Apply formatting to a value.

    Parameters
    ----------
    format_str : str
        The format string to apply.
    value : Any
        The value to format.

    Returns
    -------
    str
        The formatted value.

    """
    if format_str == "+#":
        if isinstance(value, str):
            return "+" + str(value)
        elif value >= 0:
            return "+" + str(value)
        else:
            return str(value)
    elif format_str == "ignored":
        return ""
    elif format_str == "#":
        return str(value)


def format_range_value(min_value, max_value):
    """
    Parameters
    ----------
    min_value : Any
        The minimum value of the range.
    max_value : Any
        The maximum value of the range.

    Returns
    -------
    str
        The formatted range value.

    """
    if min_value >= 0 and max_value >= 0:
        return f"({min_value}-{max_value})"
    elif min_value < 0 and max_value < 0:
        return f"-({abs(min_value)}-{abs(max_value)})"
    else:
        return f"({min_value}-{max_value})"


class TranslationQuantifier:
    """
    A class representing a translation quantifier.

    Attributes:
        id (Any): The identifier of the quantifier.
        handler (Any): The handler function for translating values.
        reverse_handler (Any): The handler function for reverse translating values.
    """

    def __init__(self, id, handler, reverse_handler):
        self.id = id
        self.handler = handler
        self.reverse_handler = reverse_handler


quantifiers = [
    TranslationQuantifier(
        id="30%_of_value", handler=lambda v: v * 0.3, reverse_handler=lambda v: v / 0.3
    ),
    TranslationQuantifier(
        id="60%_of_value", handler=lambda v: v * 0.6, reverse_handler=lambda v: v / 0.6
    ),
    TranslationQuantifier(
        id="deciseconds_to_seconds",
        handler=lambda v: v / 10,
        reverse_handler=lambda v: float(v) * 10,
    ),
    TranslationQuantifier(
        id="divide_by_three",
        handler=lambda v: v / 3,
        reverse_handler=lambda v: float(v) * 3,
    ),
    TranslationQuantifier(
        id="divide_by_five",
        handler=lambda v: v / 5,
        reverse_handler=lambda v: float(v) * 5,
    ),
    TranslationQuantifier(
        id="divide_by_one_hundred",
        handler=lambda v: v / 100,
        reverse_handler=lambda v: float(v) * 100,
    ),
    TranslationQuantifier(
        id="divide_by_one_hundred_and_negate",
        handler=lambda v: -v / 100,
        reverse_handler=lambda v: -float(v) * 100,
    ),
    TranslationQuantifier(
        id="divide_by_one_hundred_0dp",
        handler=lambda v: round(v / 100, 0),
        reverse_handler=lambda v: float(v) * 100,
    ),
    TranslationQuantifier(
        id="divide_by_one_hundred_1dp",
        handler=lambda v: round(v / 100, 1),
        reverse_handler=lambda v: float(v) * 100,
    ),
    TranslationQuantifier(
        id="divide_by_one_hundred_2dp",
        handler=lambda v: round(v / 100, 2),
        reverse_handler=lambda v: float(v) * 100,
    ),
    TranslationQuantifier(
        id="divide_by_one_hundred_2dp_if_required",
        handler=lambda v: round(v / 100, 2),
        reverse_handler=lambda v: float(v) * 100,
    ),
    TranslationQuantifier(
        id="divide_by_two_0dp",
        handler=lambda v: v // 2,
        reverse_handler=lambda v: int(v) * 2,
    ),
    TranslationQuantifier(
        id="divide_by_six",
        handler=lambda v: v / 6,
        reverse_handler=lambda v: int(v) * 6,
    ),
    TranslationQuantifier(
        id="divide_by_ten_0dp",
        handler=lambda v: v // 10,
        reverse_handler=lambda v: int(v) * 10,
    ),
    TranslationQuantifier(
        id="divide_by_ten_1dp",
        handler=lambda v: round(v / 10, 1),
        reverse_handler=lambda v: int(v) * 10,
    ),
    TranslationQuantifier(
        id="divide_by_twelve",
        handler=lambda v: v / 12,
        reverse_handler=lambda v: int(v) * 12,
    ),
    TranslationQuantifier(
        id="divide_by_fifteen_0dp",
        handler=lambda v: v // 15,
        reverse_handler=lambda v: int(v) * 15,
    ),
    TranslationQuantifier(
        id="divide_by_twenty_then_double_0dp",
        handler=lambda v: v // 20 * 2,
        reverse_handler=lambda v: int(v) * 20 // 2,
    ),
    TranslationQuantifier(
        id="milliseconds_to_seconds",
        handler=lambda v: v / 1000,
        reverse_handler=lambda v: float(v) * 1000,
    ),
    TranslationQuantifier(
        id="milliseconds_to_seconds_halved",
        handler=lambda v: v / 500,
        reverse_handler=lambda v: float(v) * 500,
    ),
    TranslationQuantifier(
        id="milliseconds_to_seconds_0dp",
        handler=lambda v: int(round(v / 1000, 0)),
        reverse_handler=lambda v: float(v) * 1000,
    ),
    TranslationQuantifier(
        id="milliseconds_to_seconds_1dp",
        handler=lambda v: round(v / 1000, 1),
        reverse_handler=lambda v: float(v) * 1000,
    ),
    TranslationQuantifier(
        id="milliseconds_to_seconds_2dp",
        handler=lambda v: round(v / 1000, 2),
        reverse_handler=lambda v: float(v) * 1000,
    ),
    TranslationQuantifier(
        id="milliseconds_to_seconds_2dp_if_required",
        handler=lambda v: round(v / 1000, 2),
        reverse_handler=lambda v: float(v) * 1000,
    ),
    TranslationQuantifier(
        id="multiplicative_damage_modifier",
        handler=lambda v: v + 100,
        reverse_handler=lambda v: float(v) - 100,
    ),
    TranslationQuantifier(
        id="multiplicative_permyriad_damage_modifier",
        handler=lambda v: v / 100 + 100,
        reverse_handler=lambda v: (float(v) - 100) * 100,
    ),
    TranslationQuantifier(
        id="multiply_by_four",
        handler=lambda v: v * 4,
        reverse_handler=lambda v: int(v) // 4,
    ),
    TranslationQuantifier(
        id="multiply_by_four_and_",
        handler=lambda v: v * 4,
        reverse_handler=lambda v: int(v) // 4,
    ),
    TranslationQuantifier(
        id="negate", handler=lambda v: -v, reverse_handler=lambda v: -float(v)
    ),
    TranslationQuantifier(
        id="old_leech_percent",
        handler=lambda v: v / 5,
        reverse_handler=lambda v: float(v) * 5,
    ),
    TranslationQuantifier(
        id="old_leech_permyriad",
        handler=lambda v: v / 500,
        reverse_handler=lambda v: float(v) * 500,
    ),
    TranslationQuantifier(
        id="per_minute_to_per_second",
        handler=lambda v: round(v / 60, 1),
        reverse_handler=lambda v: float(v) * 60,
    ),
    TranslationQuantifier(
        id="per_minute_to_per_second_0dp",
        handler=lambda v: int(round(v / 60, 0)),
        reverse_handler=lambda v: float(v) * 60,
    ),
    TranslationQuantifier(
        id="per_minute_to_per_second_1dp",
        handler=lambda v: round(v / 60, 1),
        reverse_handler=lambda v: float(v) * 60,
    ),
    TranslationQuantifier(
        id="per_minute_to_per_second_2dp",
        handler=lambda v: round(v / 60, 2),
        reverse_handler=lambda v: float(v) * 60,
    ),
    TranslationQuantifier(
        id="per_minute_to_per_second_2dp_if_required",
        handler=lambda v: round(v / 60, 2) if v % 60 != 0 else v // 60,
        reverse_handler=lambda v: float(v) * 60,
    ),
    TranslationQuantifier(
        id="times_twenty",
        handler=lambda v: v * 20,
        reverse_handler=lambda v: int(v) // 20,
    ),
    TranslationQuantifier(
        id="times_one_point_five",
        handler=lambda v: v * 1.5,
        reverse_handler=lambda v: int(v / 1.5),
    ),
    TranslationQuantifier(
        id="double", handler=lambda v: v * 2, reverse_handler=lambda v: int(v) // 2
    ),
    TranslationQuantifier(
        id="negate_and_double",
        handler=lambda v: -v * 2,
        reverse_handler=lambda v: int(-v) // 2,
    ),
    TranslationQuantifier(
        id="divide_by_four", handler=lambda v: v / 4, reverse_handler=lambda v: v * 4
    ),
    TranslationQuantifier(
        id="divide_by_ten_1dp_if_required",
        handler=lambda v: round(v / 10, 1),
        reverse_handler=lambda v: v * 10,
    ),
    TranslationQuantifier(
        id="divide_by_fifty", handler=lambda v: v / 50, reverse_handler=lambda v: v * 50
    ),
    TranslationQuantifier(
        id="multiply_by_ten", handler=lambda v: v * 10, reverse_handler=lambda v: v / 10
    ),
    TranslationQuantifier(
        id="divide_by_one_thousand",
        handler=lambda v: v / 1000,
        reverse_handler=lambda v: v * 1000,
    ),
    TranslationQuantifier(
        id="plus_two_hundred",
        handler=lambda v: v + 200,
        reverse_handler=lambda v: v - 200,
    ),
]
