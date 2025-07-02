"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PremiumMusicVideoField = Literal[
    "creation_time",
    "cross_post_videos",
    "eligible_cross_post_pages",
    "id",
    "preferred_video_thumbnail_image_uri",
    "premium_music_video_metadata",
    "scheduled_publish_time",
    "title",
]


class PremiumMusicVideoFields(BaseModel):
    """Pydantic model for PremiumMusicVideo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: str = Field(None, alias="creation_time")
    cross_post_videos: list[dict[str, Any]] = Field(None, alias="cross_post_videos")
    eligible_cross_post_pages: list[dict[str, Any]] = Field(None, alias="eligible_cross_post_pages")
    id: str = Field(None, alias="id")
    preferred_video_thumbnail_image_uri: str = Field(
        None, alias="preferred_video_thumbnail_image_uri"
    )
    premium_music_video_metadata: dict[str, Any] = Field(None, alias="premium_music_video_metadata")
    scheduled_publish_time: int = Field(None, alias="scheduled_publish_time")
    title: str = Field(None, alias="title")
