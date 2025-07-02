"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


class mediainsights_metric_enum_param(str, Enum):
    """mediainsights_metric_enum_param enum values."""

    clips_replays_count = "clips_replays_count"
    comments = "comments"
    content_views = "content_views"
    follows = "follows"
    ig_reels_aggregated_all_plays_count = "ig_reels_aggregated_all_plays_count"
    ig_reels_avg_watch_time = "ig_reels_avg_watch_time"
    ig_reels_video_view_total_time = "ig_reels_video_view_total_time"
    impressions = "impressions"
    likes = "likes"
    navigation = "navigation"
    plays = "plays"
    profile_activity = "profile_activity"
    profile_visits = "profile_visits"
    quotes = "quotes"
    reach = "reach"
    replies = "replies"
    reposts = "reposts"
    saved = "saved"
    shares = "shares"
    thread_replies = "thread_replies"
    thread_shares = "thread_shares"
    threads_media_clicks = "threads_media_clicks"
    threads_views = "threads_views"
    total_interactions = "total_interactions"
    views = "views"


class mediainsights_period_enum_param(str, Enum):
    """mediainsights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class mediainsights_breakdown_enum_param(str, Enum):
    """mediainsights_breakdown_enum_param enum values."""

    action_type = "action_type"
    follow_type = "follow_type"
    story_navigation_action_type = "story_navigation_action_type"
    surface_type = "surface_type"


# Field literal type
IGMediaForIGOnlyAPIField = Literal[
    "alt_text",
    "caption",
    "comments_count",
    "id",
    "is_comment_enabled",
    "is_shared_to_feed",
    "like_count",
    "media_product_type",
    "media_type",
    "media_url",
    "owner",
    "permalink",
    "shortcode",
    "thumbnail_url",
    "timestamp",
    "username",
]


class IGMediaForIGOnlyAPIFields(BaseModel):
    """Pydantic model for IGMediaForIGOnlyAPI fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    alt_text: str = Field(None, alias="alt_text")
    caption: str = Field(None, alias="caption")
    comments_count: int = Field(None, alias="comments_count")
    id: str = Field(None, alias="id")
    is_comment_enabled: bool = Field(None, alias="is_comment_enabled")
    is_shared_to_feed: bool = Field(None, alias="is_shared_to_feed")
    like_count: int = Field(None, alias="like_count")
    media_product_type: str = Field(None, alias="media_product_type")
    media_type: str = Field(None, alias="media_type")
    media_url: str = Field(None, alias="media_url")
    owner: UserFields = Field(None, alias="owner")
    permalink: str = Field(None, alias="permalink")
    shortcode: str = Field(None, alias="shortcode")
    thumbnail_url: str = Field(None, alias="thumbnail_url")
    timestamp: datetime = Field(None, alias="timestamp")
    username: str = Field(None, alias="username")


class IGMediaForIGOnlyAPICreateCommentParams(BaseModel):
    """Parameters for IGMediaForIGOnlyAPI.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    message: str | None = Field(None, description="message parameter")


class IGMediaForIGOnlyAPIGetInsightsParams(BaseModel):
    """Parameters for IGMediaForIGOnlyAPI.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    breakdown: list[mediainsights_breakdown_enum_param] | None = Field(
        None, description="breakdown parameter"
    )
    metric: list[mediainsights_metric_enum_param] | None = Field(
        None, description="metric parameter"
    )
    period: list[mediainsights_period_enum_param] | None = Field(
        None, description="period parameter"
    )
