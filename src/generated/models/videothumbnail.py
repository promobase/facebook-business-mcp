"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoThumbnailField = Literal["height", "id", "is_preferred", "name", "scale", "uri", "width"]


class VideoThumbnailFields(BaseModel):
    """Pydantic model for VideoThumbnail fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    height: int = Field(None, alias="height")
    id: str = Field(None, alias="id")
    is_preferred: bool = Field(None, alias="is_preferred")
    name: str = Field(None, alias="name")
    scale: float = Field(None, alias="scale")
    uri: str = Field(None, alias="uri")
    width: int = Field(None, alias="width")
