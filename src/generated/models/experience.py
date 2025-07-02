"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
ExperienceField = Literal["description", "from", "id", "name", "with"]


class ExperienceFields(BaseModel):
    """Pydantic model for Experience fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    from_: dict[str, Any] = Field(None, alias="from")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    with_: list[UserFields] = Field(None, alias="with")
