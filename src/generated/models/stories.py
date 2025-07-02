"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class storiesinsights_metric_enum_param(str, Enum):
    """storiesinsights_metric_enum_param enum values."""

    PAGES_FB_STORY_REPLIES = "PAGES_FB_STORY_REPLIES"
    PAGES_FB_STORY_SHARES = "PAGES_FB_STORY_SHARES"
    PAGES_FB_STORY_STICKER_INTERACTIONS = "PAGES_FB_STORY_STICKER_INTERACTIONS"
    PAGES_FB_STORY_THREAD_LIGHTWEIGHT_REACTIONS = "PAGES_FB_STORY_THREAD_LIGHTWEIGHT_REACTIONS"
    PAGE_STORY_IMPRESSIONS_BY_STORY_ID = "PAGE_STORY_IMPRESSIONS_BY_STORY_ID"
    PAGE_STORY_IMPRESSIONS_BY_STORY_ID_UNIQUE = "PAGE_STORY_IMPRESSIONS_BY_STORY_ID_UNIQUE"
    STORY_INTERACTION = "STORY_INTERACTION"


# Field literal type
StoriesField = Literal["creation_time", "media_id", "media_type", "post_id", "status", "url"]


class StoriesFields(BaseModel):
    """Pydantic model for Stories fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: str = Field(None, alias="creation_time")
    media_id: str = Field(None, alias="media_id")
    media_type: str = Field(None, alias="media_type")
    post_id: str = Field(None, alias="post_id")
    status: str = Field(None, alias="status")
    url: str = Field(None, alias="url")


class StoriesGetInsightsParams(BaseModel):
    """Parameters for Stories.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    metric: list[storiesinsights_metric_enum_param] | None = Field(
        None, description="metric parameter"
    )
