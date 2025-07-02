"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PrivacyOptionField = Literal[
    "description", "icon_src", "id", "is_currently_selected", "type", "user_id"
]


class PrivacyOptionFields(BaseModel):
    """Pydantic model for PrivacyOption fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    icon_src: str = Field(None, alias="icon_src")
    id: str = Field(None, alias="id")
    is_currently_selected: bool = Field(None, alias="is_currently_selected")
    type: str = Field(None, alias="type")
    user_id: str = Field(None, alias="user_id")
