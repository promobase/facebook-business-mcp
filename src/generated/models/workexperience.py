"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields
    from .user import UserFields


# Field literal type
WorkExperienceField = Literal[
    "description",
    "employer",
    "end_date",
    "from",
    "id",
    "location",
    "position",
    "projects",
    "start_date",
    "with",
]


class WorkExperienceFields(BaseModel):
    """Pydantic model for WorkExperience fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    employer: PageFields = Field(None, alias="employer")
    end_date: str = Field(None, alias="end_date")
    from_: UserFields = Field(None, alias="from")
    id: str = Field(None, alias="id")
    location: PageFields = Field(None, alias="location")
    position: PageFields = Field(None, alias="position")
    projects: list[dict[str, Any]] = Field(None, alias="projects")
    start_date: str = Field(None, alias="start_date")
    with_: list[UserFields] = Field(None, alias="with")
