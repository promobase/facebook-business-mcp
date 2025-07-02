"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProfilePictureSourceField = Literal[
    "bottom", "cache_key", "height", "is_silhouette", "left", "right", "top", "url", "width"
]


class ProfilePictureSourceFields(BaseModel):
    """Pydantic model for ProfilePictureSource fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    bottom: int = Field(None, alias="bottom")
    cache_key: str = Field(None, alias="cache_key")
    height: int = Field(None, alias="height")
    is_silhouette: bool = Field(None, alias="is_silhouette")
    left: int = Field(None, alias="left")
    right: int = Field(None, alias="right")
    top: int = Field(None, alias="top")
    url: str = Field(None, alias="url")
    width: int = Field(None, alias="width")
