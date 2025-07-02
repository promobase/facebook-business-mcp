"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CoverPhotoField = Literal["cover_id", "id", "offset_x", "offset_y", "source"]


class CoverPhotoFields(BaseModel):
    """Pydantic model for CoverPhoto fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    cover_id: str = Field(None, alias="cover_id")
    id: str = Field(None, alias="id")
    offset_x: float = Field(None, alias="offset_x")
    offset_y: float = Field(None, alias="offset_y")
    source: str = Field(None, alias="source")
