"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessCreativeField = Literal[
    "creation_time",
    "duration",
    "hash",
    "height",
    "id",
    "name",
    "thumbnail",
    "type",
    "url",
    "video_id",
    "width",
]


class BusinessCreativeFields(BaseModel):
    """Pydantic model for BusinessCreative fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    duration: int = Field(None, alias="duration")
    hash: str = Field(None, alias="hash")
    height: int = Field(None, alias="height")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    thumbnail: str = Field(None, alias="thumbnail")
    type: str = Field(None, alias="type")
    url: str = Field(None, alias="url")
    video_id: str = Field(None, alias="video_id")
    width: int = Field(None, alias="width")
