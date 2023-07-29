# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"),
#  to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE
#  SOFTWARE.
# ##############################################################################
"""

Module: modules.data.models.tag

This module contains the `Tag` class, which represents a tag in the application.

Classes:
    - Tag

"""
from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.data.models.base_model import Base


@dataclass
class Tag(Base):
    """
    This class represents a Tag in the system.

    Attributes:
        tag (Mapped[str]): The unique tag associated with the Tag object.
        spawn_weights (Relationship): The relationship to ModSpawnWeight objects.

    """
    tag: Mapped[str] = mapped_column(unique=True)

    # Relationships
    spawn_weights = relationship(
        "ModSpawnWeight", back_populates="tag", default_factory=list, init=False
    )
