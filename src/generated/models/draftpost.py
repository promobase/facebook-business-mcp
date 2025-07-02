"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .place import PlaceFields
    from .targeting import TargetingFields
    from .user import UserFields


# Field literal type
DraftPostField = Literal[
    "admin_creator",
    "creation_time",
    "feed_audience_description",
    "feed_targeting",
    "id",
    "is_post_in_good_state",
    "message",
    "modified_time",
    "og_action_summary",
    "permalink_url",
    "place",
    "privacy_description",
    "scheduled_failure_notice",
    "scheduled_publish_time",
    "story_token",
    "thumbnail",
    "video_id",
]


class DraftPostFields(BaseModel):
    """Pydantic model for DraftPost fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    admin_creator: UserFields = Field(None, alias="admin_creator")
    creation_time: datetime = Field(None, alias="creation_time")
    feed_audience_description: str = Field(None, alias="feed_audience_description")
    feed_targeting: TargetingFields = Field(None, alias="feed_targeting")
    id: str = Field(None, alias="id")
    is_post_in_good_state: bool = Field(None, alias="is_post_in_good_state")
    message: str = Field(None, alias="message")
    modified_time: datetime = Field(None, alias="modified_time")
    og_action_summary: str = Field(None, alias="og_action_summary")
    permalink_url: str = Field(None, alias="permalink_url")
    place: PlaceFields = Field(None, alias="place")
    privacy_description: str = Field(None, alias="privacy_description")
    scheduled_failure_notice: str = Field(None, alias="scheduled_failure_notice")
    scheduled_publish_time: datetime = Field(None, alias="scheduled_publish_time")
    story_token: str = Field(None, alias="story_token")
    thumbnail: str = Field(None, alias="thumbnail")
    video_id: str = Field(None, alias="video_id")
