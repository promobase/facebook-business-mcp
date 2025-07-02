"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


# Field literal type
PlayableContentField = Literal["id", "name", "owner"]


class PlayableContentFields(BaseModel):
    """Pydantic model for PlayableContent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    owner: ProfileFields = Field(None, alias="owner")
