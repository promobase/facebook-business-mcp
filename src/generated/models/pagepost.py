"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields
    from .event import EventFields
    from .place import PlaceFields
    from .privacy import PrivacyFields
    from .profile import ProfileFields


class pagepostcomments_filter_enum_param(str, Enum):
    """pagepostcomments_filter_enum_param enum values."""

    stream = "stream"
    toplevel = "toplevel"


class pagepostinsights_period_enum_param(str, Enum):
    """pagepostinsights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class pagepostinsights_date_preset_enum_param(str, Enum):
    """pagepostinsights_date_preset_enum_param enum values."""

    data_maximum = "data_maximum"
    last_14d = "last_14d"
    last_28d = "last_28d"
    last_30d = "last_30d"
    last_3d = "last_3d"
    last_7d = "last_7d"
    last_90d = "last_90d"
    last_month = "last_month"
    last_quarter = "last_quarter"
    last_week_mon_sun = "last_week_mon_sun"
    last_week_sun_sat = "last_week_sun_sat"
    last_year = "last_year"
    maximum = "maximum"
    this_month = "this_month"
    this_quarter = "this_quarter"
    this_week_mon_today = "this_week_mon_today"
    this_week_sun_today = "this_week_sun_today"
    this_year = "this_year"
    today = "today"
    yesterday = "yesterday"


class pagepostcomments_live_filter_enum_param(str, Enum):
    """pagepostcomments_live_filter_enum_param enum values."""

    filter_low_quality = "filter_low_quality"
    no_filter = "no_filter"


class pagepostreactions_type_enum_param(str, Enum):
    """pagepostreactions_type_enum_param enum values."""

    ANGRY = "ANGRY"
    CARE = "CARE"
    FIRE = "FIRE"
    HAHA = "HAHA"
    HUNDRED = "HUNDRED"
    LIKE = "LIKE"
    LOVE = "LOVE"
    NONE = "NONE"
    PRIDE = "PRIDE"
    SAD = "SAD"
    THANKFUL = "THANKFUL"
    WOW = "WOW"


class pagepostcomments_order_enum_param(str, Enum):
    """pagepostcomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


class pagepostcomments_comment_privacy_value_enum_param(str, Enum):
    """pagepostcomments_comment_privacy_value_enum_param enum values."""

    DECLINED_BY_ADMIN_ASSISTANT = "DECLINED_BY_ADMIN_ASSISTANT"
    DEFAULT_PRIVACY = "DEFAULT_PRIVACY"
    FRIENDS_AND_POST_OWNER = "FRIENDS_AND_POST_OWNER"
    FRIENDS_ONLY = "FRIENDS_ONLY"
    GRAPHQL_MULTIPLE_VALUE_HACK_DO_NOT_USE = "GRAPHQL_MULTIPLE_VALUE_HACK_DO_NOT_USE"
    OWNER_OR_COMMENTER = "OWNER_OR_COMMENTER"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    REMOVED_BY_ADMIN_ASSISTANT = "REMOVED_BY_ADMIN_ASSISTANT"
    SIDE_CONVERSATION = "SIDE_CONVERSATION"
    SIDE_CONVERSATION_AND_POST_OWNER = "SIDE_CONVERSATION_AND_POST_OWNER"
    SPOTLIGHT_TAB = "SPOTLIGHT_TAB"


# Field literal type
PagePostField = Literal[
    "actions",
    "admin_creator",
    "allowed_advertising_objectives",
    "application",
    "backdated_time",
    "call_to_action",
    "can_reply_privately",
    "child_attachments",
    "comments_mirroring_domain",
    "coordinates",
    "created_time",
    "event",
    "expanded_height",
    "expanded_width",
    "feed_targeting",
    "from",
    "full_picture",
    "height",
    "icon",
    "id",
    "instagram_eligibility",
    "is_app_share",
    "is_eligible_for_promotion",
    "is_expired",
    "is_hidden",
    "is_inline_created",
    "is_instagram_eligible",
    "is_popular",
    "is_published",
    "is_spherical",
    "message",
    "message_tags",
    "multi_share_end_card",
    "multi_share_optimized",
    "parent_id",
    "permalink_url",
    "picture",
    "place",
    "privacy",
    "promotable_id",
    "promotion_status",
    "properties",
    "scheduled_publish_time",
    "shares",
    "status_type",
    "story",
    "story_tags",
    "subscribed",
    "target",
    "targeting",
    "timeline_visibility",
    "updated_time",
    "via",
    "video_buying_eligibility",
    "width",
]


class PagePostFields(BaseModel):
    """Pydantic model for PagePost fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actions: dict[str, Any] = Field(None, alias="actions")
    admin_creator: dict[str, Any] = Field(None, alias="admin_creator")
    allowed_advertising_objectives: list[str] = Field(None, alias="allowed_advertising_objectives")
    application: ApplicationFields = Field(None, alias="application")
    backdated_time: datetime = Field(None, alias="backdated_time")
    call_to_action: dict[str, Any] = Field(None, alias="call_to_action")
    can_reply_privately: bool = Field(None, alias="can_reply_privately")
    child_attachments: dict[str, Any] = Field(None, alias="child_attachments")
    comments_mirroring_domain: str = Field(None, alias="comments_mirroring_domain")
    coordinates: dict[str, Any] = Field(None, alias="coordinates")
    created_time: datetime = Field(None, alias="created_time")
    event: EventFields = Field(None, alias="event")
    expanded_height: int = Field(None, alias="expanded_height")
    expanded_width: int = Field(None, alias="expanded_width")
    feed_targeting: dict[str, Any] = Field(None, alias="feed_targeting")
    from_: dict[str, Any] = Field(None, alias="from")
    full_picture: str = Field(None, alias="full_picture")
    height: int = Field(None, alias="height")
    icon: str = Field(None, alias="icon")
    id: str = Field(None, alias="id")
    instagram_eligibility: str = Field(None, alias="instagram_eligibility")
    is_app_share: bool = Field(None, alias="is_app_share")
    is_eligible_for_promotion: bool = Field(None, alias="is_eligible_for_promotion")
    is_expired: bool = Field(None, alias="is_expired")
    is_hidden: bool = Field(None, alias="is_hidden")
    is_inline_created: bool = Field(None, alias="is_inline_created")
    is_instagram_eligible: bool = Field(None, alias="is_instagram_eligible")
    is_popular: bool = Field(None, alias="is_popular")
    is_published: bool = Field(None, alias="is_published")
    is_spherical: bool = Field(None, alias="is_spherical")
    message: str = Field(None, alias="message")
    message_tags: dict[str, Any] = Field(None, alias="message_tags")
    multi_share_end_card: bool = Field(None, alias="multi_share_end_card")
    multi_share_optimized: bool = Field(None, alias="multi_share_optimized")
    parent_id: str = Field(None, alias="parent_id")
    permalink_url: str = Field(None, alias="permalink_url")
    picture: str = Field(None, alias="picture")
    place: PlaceFields = Field(None, alias="place")
    privacy: PrivacyFields = Field(None, alias="privacy")
    promotable_id: str = Field(None, alias="promotable_id")
    promotion_status: str = Field(None, alias="promotion_status")
    properties: dict[str, Any] = Field(None, alias="properties")
    scheduled_publish_time: float = Field(None, alias="scheduled_publish_time")
    shares: dict[str, Any] = Field(None, alias="shares")
    status_type: str = Field(None, alias="status_type")
    story: str = Field(None, alias="story")
    story_tags: dict[str, Any] = Field(None, alias="story_tags")
    subscribed: bool = Field(None, alias="subscribed")
    target: ProfileFields = Field(None, alias="target")
    targeting: dict[str, Any] = Field(None, alias="targeting")
    timeline_visibility: str = Field(None, alias="timeline_visibility")
    updated_time: datetime = Field(None, alias="updated_time")
    via: dict[str, Any] = Field(None, alias="via")
    video_buying_eligibility: list[str] = Field(None, alias="video_buying_eligibility")
    width: int = Field(None, alias="width")


class PagePostGetCommentsParams(BaseModel):
    """Parameters for PagePost.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    filter: pagepostcomments_filter_enum_param | None = Field(None, description="filter parameter")
    live_filter: pagepostcomments_live_filter_enum_param | None = Field(
        None, description="live_filter parameter"
    )
    order: pagepostcomments_order_enum_param | None = Field(None, description="order parameter")
    since: datetime | None = Field(None, description="since parameter")


class PagePostCreateCommentParams(BaseModel):
    """Parameters for PagePost.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    attachment_id: str | None = Field(None, description="attachment_id parameter")
    attachment_share_url: str | None = Field(None, description="attachment_share_url parameter")
    attachment_url: str | None = Field(None, description="attachment_url parameter")
    comment: str | None = Field(None, description="comment parameter")
    comment_privacy_value: pagepostcomments_comment_privacy_value_enum_param | None = Field(
        None, description="comment_privacy_value parameter"
    )
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    message: str | None = Field(None, description="message parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    parent_comment_id: dict[str, Any] | None = Field(
        None, description="parent_comment_id parameter"
    )
    post_id: str | None = Field(None, description="post_id parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class PagePostGetInsightsParams(BaseModel):
    """Parameters for PagePost.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: pagepostinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    metric: list[dict[str, Any]] | None = Field(None, description="metric parameter")
    period: pagepostinsights_period_enum_param | None = Field(None, description="period parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class PagePostDeleteLikesParams(BaseModel):
    """Parameters for PagePost.delete_likes()."""

    model_config = ConfigDict(extra="forbid")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class PagePostCreateLikeParams(BaseModel):
    """Parameters for PagePost.create_like()."""

    model_config = ConfigDict(extra="forbid")
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class PagePostGetReactionsParams(BaseModel):
    """Parameters for PagePost.get_reactions()."""

    model_config = ConfigDict(extra="forbid")
    type: pagepostreactions_type_enum_param | None = Field(None, description="type parameter")
