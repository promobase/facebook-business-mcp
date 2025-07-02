"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .album import AlbumFields
    from .entityattextrange import EntityAtTextRangeFields
    from .event import EventFields
    from .place import PlaceFields
    from .platformimagesource import PlatformImageSourceFields
    from .profile import ProfileFields


class photocomments_live_filter_enum_param(str, Enum):
    """photocomments_live_filter_enum_param enum values."""

    filter_low_quality = "filter_low_quality"
    no_filter = "no_filter"


class photoinsights_period_enum_param(str, Enum):
    """photoinsights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class photoinsights_date_preset_enum_param(str, Enum):
    """photoinsights_date_preset_enum_param enum values."""

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


class photocomments_order_enum_param(str, Enum):
    """photocomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


class photocomments_comment_privacy_value_enum_param(str, Enum):
    """photocomments_comment_privacy_value_enum_param enum values."""

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


class photocomments_filter_enum_param(str, Enum):
    """photocomments_filter_enum_param enum values."""

    stream = "stream"
    toplevel = "toplevel"


# Field literal type
PhotoField = Literal[
    "album",
    "alt_text",
    "alt_text_custom",
    "backdated_time",
    "backdated_time_granularity",
    "can_backdate",
    "can_delete",
    "can_tag",
    "created_time",
    "event",
    "from",
    "height",
    "icon",
    "id",
    "images",
    "link",
    "name",
    "name_tags",
    "page_story_id",
    "picture",
    "place",
    "position",
    "source",
    "target",
    "updated_time",
    "webp_images",
    "width",
]


class PhotoFields(BaseModel):
    """Pydantic model for Photo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    album: AlbumFields = Field(None, alias="album")
    alt_text: str = Field(None, alias="alt_text")
    alt_text_custom: str = Field(None, alias="alt_text_custom")
    backdated_time: datetime = Field(None, alias="backdated_time")
    backdated_time_granularity: str = Field(None, alias="backdated_time_granularity")
    can_backdate: bool = Field(None, alias="can_backdate")
    can_delete: bool = Field(None, alias="can_delete")
    can_tag: bool = Field(None, alias="can_tag")
    created_time: datetime = Field(None, alias="created_time")
    event: EventFields = Field(None, alias="event")
    from_: dict[str, Any] = Field(None, alias="from")
    height: int = Field(None, alias="height")
    icon: str = Field(None, alias="icon")
    id: str = Field(None, alias="id")
    images: list[PlatformImageSourceFields] = Field(None, alias="images")
    link: str = Field(None, alias="link")
    name: str = Field(None, alias="name")
    name_tags: list[EntityAtTextRangeFields] = Field(None, alias="name_tags")
    page_story_id: str = Field(None, alias="page_story_id")
    picture: str = Field(None, alias="picture")
    place: PlaceFields = Field(None, alias="place")
    position: int = Field(None, alias="position")
    source: str = Field(None, alias="source")
    target: ProfileFields = Field(None, alias="target")
    updated_time: datetime = Field(None, alias="updated_time")
    webp_images: list[PlatformImageSourceFields] = Field(None, alias="webp_images")
    width: int = Field(None, alias="width")


class PhotoGetCommentsParams(BaseModel):
    """Parameters for Photo.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    filter: photocomments_filter_enum_param | None = Field(None, description="filter parameter")
    live_filter: photocomments_live_filter_enum_param | None = Field(
        None, description="live_filter parameter"
    )
    order: photocomments_order_enum_param | None = Field(None, description="order parameter")
    since: datetime | None = Field(None, description="since parameter")


class PhotoCreateCommentParams(BaseModel):
    """Parameters for Photo.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    attachment_id: str | None = Field(None, description="attachment_id parameter")
    attachment_share_url: str | None = Field(None, description="attachment_share_url parameter")
    attachment_url: str | None = Field(None, description="attachment_url parameter")
    comment_privacy_value: photocomments_comment_privacy_value_enum_param | None = Field(
        None, description="comment_privacy_value parameter"
    )
    facepile_mentioned_ids: list[str] | None = Field(
        None, description="facepile_mentioned_ids parameter"
    )
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    is_offline: bool | None = Field(None, description="is_offline parameter")
    message: str | None = Field(None, description="message parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    object_id: str | None = Field(None, description="object_id parameter")
    parent_comment_id: dict[str, Any] | None = Field(
        None, description="parent_comment_id parameter"
    )
    text: str | None = Field(None, description="text parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class PhotoGetInsightsParams(BaseModel):
    """Parameters for Photo.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: photoinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    metric: list[dict[str, Any]] | None = Field(None, description="metric parameter")
    period: photoinsights_period_enum_param | None = Field(None, description="period parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class PhotoCreateLikeParams(BaseModel):
    """Parameters for Photo.create_like()."""

    model_config = ConfigDict(extra="forbid")
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    notify: bool | None = Field(None, description="notify parameter")
    tracking: str | None = Field(None, description="tracking parameter")
