"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


class EntityAtTextRange_type(str, Enum):
    """EntityAtTextRange_type enum values."""

    application = "application"
    event = "event"
    group = "group"
    page = "page"
    user = "user"


# Field literal type
EntityAtTextRangeField = Literal["id", "length", "name", "object", "offset", "type"]


class EntityAtTextRangeFields(BaseModel):
    """Pydantic model for EntityAtTextRange fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    length: int = Field(None, alias="length")
    name: str = Field(None, alias="name")
    object: ProfileFields = Field(None, alias="object")
    offset: int = Field(None, alias="offset")
    type: dict[str, Any] = Field(None, alias="type")
