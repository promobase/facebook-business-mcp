"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoGroupField = Literal[
    "created_time",
    "description",
    "disable_reason",
    "id",
    "ig_profile_ids",
    "is_disabled",
    "is_fb_video_group",
    "last_used_time",
    "length",
    "name",
    "page_id",
    "page_ids",
    "picture",
    "placements",
    "video_group_types",
    "videos",
    "views",
]


class VideoGroupFields(BaseModel):
    """Pydantic model for VideoGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_time: str = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    disable_reason: str = Field(None, alias="disable_reason")
    id: str = Field(None, alias="id")
    ig_profile_ids: list[str] = Field(None, alias="ig_profile_ids")
    is_disabled: bool = Field(None, alias="is_disabled")
    is_fb_video_group: bool = Field(None, alias="is_fb_video_group")
    last_used_time: str = Field(None, alias="last_used_time")
    length: float = Field(None, alias="length")
    name: str = Field(None, alias="name")
    page_id: str = Field(None, alias="page_id")
    page_ids: list[str] = Field(None, alias="page_ids")
    picture: str = Field(None, alias="picture")
    placements: list[str] = Field(None, alias="placements")
    video_group_types: list[str] = Field(None, alias="video_group_types")
    videos: list[str] = Field(None, alias="videos")
    views: int = Field(None, alias="views")
