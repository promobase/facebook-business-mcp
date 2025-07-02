"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
InstagramThreadField = Literal["folder", "id", "participants", "updated_time"]


class InstagramThreadFields(BaseModel):
    """Pydantic model for InstagramThread fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    folder: str = Field(None, alias="folder")
    id: str = Field(None, alias="id")
    participants: dict[str, Any] = Field(None, alias="participants")
    updated_time: datetime = Field(None, alias="updated_time")
