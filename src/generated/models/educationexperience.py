"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .experience import ExperienceFields
    from .page import PageFields
    from .user import UserFields


# Field literal type
EducationExperienceField = Literal[
    "classes", "concentration", "degree", "id", "school", "type", "with", "year"
]


class EducationExperienceFields(BaseModel):
    """Pydantic model for EducationExperience fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    classes: list[ExperienceFields] = Field(None, alias="classes")
    concentration: list[PageFields] = Field(None, alias="concentration")
    degree: PageFields = Field(None, alias="degree")
    id: str = Field(None, alias="id")
    school: PageFields = Field(None, alias="school")
    type: str = Field(None, alias="type")
    with_: list[UserFields] = Field(None, alias="with")
    year: PageFields = Field(None, alias="year")
