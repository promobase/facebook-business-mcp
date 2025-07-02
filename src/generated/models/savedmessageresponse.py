"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
SavedMessageResponseField = Literal["id", "image", "is_enabled", "message", "title"]


class SavedMessageResponseFields(BaseModel):
    """Pydantic model for SavedMessageResponse fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    image: str = Field(None, alias="image")
    is_enabled: bool = Field(None, alias="is_enabled")
    message: str = Field(None, alias="message")
    title: str = Field(None, alias="title")
