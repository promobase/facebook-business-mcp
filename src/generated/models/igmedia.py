"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .igmediaboosteligibilityinfo import IGMediaBoostEligibilityInfoFields
    from .iguser import IGUserFields
    from .igvideocopyrightcheckmatchesinformation import (
        IGVideoCopyrightCheckMatchesInformationFields,
    )


class shadowigmediainsights_metric_enum_param(str, Enum):
    """shadowigmediainsights_metric_enum_param enum values."""

    clips_replays_count = "clips_replays_count"
    comments = "comments"
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
    reach = "reach"
    replies = "replies"
    saved = "saved"
    shares = "shares"
    total_interactions = "total_interactions"
    video_views = "video_views"
    views = "views"


class shadowigmediainsights_period_enum_param(str, Enum):
    """shadowigmediainsights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class shadowigmediainsights_breakdown_enum_param(str, Enum):
    """shadowigmediainsights_breakdown_enum_param enum values."""

    action_type = "action_type"
    follow_type = "follow_type"
    story_navigation_action_type = "story_navigation_action_type"
    surface_type = "surface_type"


# Field literal type
IGMediaField = Literal[
    "alt_text",
    "boost_eligibility_info",
    "caption",
    "comments_count",
    "copyright_check_information",
    "id",
    "ig_id",
    "is_comment_enabled",
    "is_shared_to_feed",
    "legacy_instagram_media_id",
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
    "view_count",
]


class IGMediaFields(BaseModel):
    """Pydantic model for IGMedia fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    alt_text: str = Field(None, alias="alt_text")
    boost_eligibility_info: IGMediaBoostEligibilityInfoFields = Field(
        None, alias="boost_eligibility_info"
    )
    caption: str = Field(None, alias="caption")
    comments_count: int = Field(None, alias="comments_count")
    copyright_check_information: IGVideoCopyrightCheckMatchesInformationFields = Field(
        None, alias="copyright_check_information"
    )
    id: str = Field(None, alias="id")
    ig_id: str = Field(None, alias="ig_id")
    is_comment_enabled: bool = Field(None, alias="is_comment_enabled")
    is_shared_to_feed: bool = Field(None, alias="is_shared_to_feed")
    legacy_instagram_media_id: str = Field(None, alias="legacy_instagram_media_id")
    like_count: int = Field(None, alias="like_count")
    media_product_type: str = Field(None, alias="media_product_type")
    media_type: str = Field(None, alias="media_type")
    media_url: str = Field(None, alias="media_url")
    owner: IGUserFields = Field(None, alias="owner")
    permalink: str = Field(None, alias="permalink")
    shortcode: str = Field(None, alias="shortcode")
    thumbnail_url: str = Field(None, alias="thumbnail_url")
    timestamp: datetime = Field(None, alias="timestamp")
    username: str = Field(None, alias="username")
    view_count: int = Field(None, alias="view_count")


class IGMediaCreateBrandedContentPartnerPromoteParams(BaseModel):
    """Parameters for IGMedia.create_branded_content_partner_promote()."""

    model_config = ConfigDict(extra="forbid")
    permission: bool | None = Field(None, description="permission parameter")
    sponsor_id: int | None = Field(None, description="sponsor_id parameter")


class IGMediaCreateCommentParams(BaseModel):
    """Parameters for IGMedia.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    ad_id: str | None = Field(None, description="ad_id parameter")
    message: str | None = Field(None, description="message parameter")


class IGMediaGetInsightsParams(BaseModel):
    """Parameters for IGMedia.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    breakdown: list[shadowigmediainsights_breakdown_enum_param] | None = Field(
        None, description="breakdown parameter"
    )
    metric: list[shadowigmediainsights_metric_enum_param] | None = Field(
        None, description="metric parameter"
    )
    period: list[shadowigmediainsights_period_enum_param] | None = Field(
        None, description="period parameter"
    )


class IGMediaCreateProductTagParams(BaseModel):
    """Parameters for IGMedia.create_product_tag()."""

    model_config = ConfigDict(extra="forbid")
    child_index: int | None = Field(None, description="child_index parameter")
    updated_tags: list[dict[str, Any]] | None = Field(None, description="updated_tags parameter")
