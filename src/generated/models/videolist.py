"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoListField = Literal[
    "creation_time",
    "description",
    "id",
    "last_modified",
    "owner",
    "season_number",
    "thumbnail",
    "title",
    "videos_count",
]


class VideoListFields(BaseModel):
    """Pydantic model for VideoList fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    last_modified: datetime = Field(None, alias="last_modified")
    owner: dict[str, Any] = Field(None, alias="owner")
    season_number: int = Field(None, alias="season_number")
    thumbnail: str = Field(None, alias="thumbnail")
    title: str = Field(None, alias="title")
    videos_count: int = Field(None, alias="videos_count")
