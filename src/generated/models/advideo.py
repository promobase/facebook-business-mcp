"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .audioisrc import AudioIsrcFields
    from .event import EventFields
    from .musicvideocopyright import MusicVideoCopyrightFields
    from .place import PlaceFields
    from .privacy import PrivacyFields
    from .user import UserFields
    from .videocopyright import VideoCopyrightFields
    from .videostatus import VideoStatusFields


class videocomments_filter_enum_param(str, Enum):
    """videocomments_filter_enum_param enum values."""

    stream = "stream"
    toplevel = "toplevel"


class videocomments_comment_privacy_value_enum_param(str, Enum):
    """videocomments_comment_privacy_value_enum_param enum values."""

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


class videovideo_insights_period_enum_param(str, Enum):
    """videovideo_insights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class videocomments_order_enum_param(str, Enum):
    """videocomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


class videocomments_live_filter_enum_param(str, Enum):
    """videocomments_live_filter_enum_param enum values."""

    filter_low_quality = "filter_low_quality"
    no_filter = "no_filter"


# Field literal type
AdVideoField = Literal[
    "ad_breaks",
    "admin_creator",
    "audio_isrc",
    "backdated_time",
    "backdated_time_granularity",
    "boost_eligibility_info",
    "content_category",
    "content_tags",
    "copyright",
    "copyright_check_information",
    "copyright_monitoring_status",
    "created_time",
    "custom_labels",
    "description",
    "embed_html",
    "embeddable",
    "event",
    "expiration",
    "format",
    "from",
    "icon",
    "id",
    "is_crosspost_video",
    "is_crossposting_eligible",
    "is_episode",
    "is_instagram_eligible",
    "is_reference_only",
    "length",
    "live_audience_count",
    "live_status",
    "music_video_copyright",
    "permalink_url",
    "picture",
    "place",
    "post_id",
    "post_views",
    "premiere_living_room_status",
    "privacy",
    "published",
    "scheduled_publish_time",
    "source",
    "spherical",
    "status",
    "title",
    "universal_video_id",
    "updated_time",
    "views",
]


class AdVideoFields(BaseModel):
    """Pydantic model for AdVideo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_breaks: list[int] = Field(None, alias="ad_breaks")
    admin_creator: UserFields = Field(None, alias="admin_creator")
    audio_isrc: AudioIsrcFields = Field(None, alias="audio_isrc")
    backdated_time: datetime = Field(None, alias="backdated_time")
    backdated_time_granularity: str = Field(None, alias="backdated_time_granularity")
    boost_eligibility_info: dict[str, Any] = Field(None, alias="boost_eligibility_info")
    content_category: str = Field(None, alias="content_category")
    content_tags: list[str] = Field(None, alias="content_tags")
    copyright: VideoCopyrightFields = Field(None, alias="copyright")
    copyright_check_information: dict[str, Any] = Field(None, alias="copyright_check_information")
    copyright_monitoring_status: str = Field(None, alias="copyright_monitoring_status")
    created_time: datetime = Field(None, alias="created_time")
    custom_labels: list[str] = Field(None, alias="custom_labels")
    description: str = Field(None, alias="description")
    embed_html: dict[str, Any] = Field(None, alias="embed_html")
    embeddable: bool = Field(None, alias="embeddable")
    event: EventFields = Field(None, alias="event")
    expiration: dict[str, Any] = Field(None, alias="expiration")
    format: list[dict[str, Any]] = Field(None, alias="format")
    from_: dict[str, Any] = Field(None, alias="from")
    icon: str = Field(None, alias="icon")
    id: str = Field(None, alias="id")
    is_crosspost_video: bool = Field(None, alias="is_crosspost_video")
    is_crossposting_eligible: bool = Field(None, alias="is_crossposting_eligible")
    is_episode: bool = Field(None, alias="is_episode")
    is_instagram_eligible: bool = Field(None, alias="is_instagram_eligible")
    is_reference_only: bool = Field(None, alias="is_reference_only")
    length: float = Field(None, alias="length")
    live_audience_count: int = Field(None, alias="live_audience_count")
    live_status: str = Field(None, alias="live_status")
    music_video_copyright: MusicVideoCopyrightFields = Field(None, alias="music_video_copyright")
    permalink_url: str = Field(None, alias="permalink_url")
    picture: str = Field(None, alias="picture")
    place: PlaceFields = Field(None, alias="place")
    post_id: str = Field(None, alias="post_id")
    post_views: int = Field(None, alias="post_views")
    premiere_living_room_status: str = Field(None, alias="premiere_living_room_status")
    privacy: PrivacyFields = Field(None, alias="privacy")
    published: bool = Field(None, alias="published")
    scheduled_publish_time: datetime = Field(None, alias="scheduled_publish_time")
    source: str = Field(None, alias="source")
    spherical: bool = Field(None, alias="spherical")
    status: VideoStatusFields = Field(None, alias="status")
    title: str = Field(None, alias="title")
    universal_video_id: str = Field(None, alias="universal_video_id")
    updated_time: datetime = Field(None, alias="updated_time")
    views: int = Field(None, alias="views")


class AdVideoCreateCaptionParams(BaseModel):
    """Parameters for AdVideo.create_caption()."""

    model_config = ConfigDict(extra="forbid")
    captions_file: dict[str, Any] | None = Field(None, description="captions_file parameter")
    default_locale: str | None = Field(None, description="default_locale parameter")
    locales_to_delete: list[str] | None = Field(None, description="locales_to_delete parameter")


class AdVideoCreateCollaboratorParams(BaseModel):
    """Parameters for AdVideo.create_collaborator()."""

    model_config = ConfigDict(extra="forbid")
    target_id: str | None = Field(None, description="target_id parameter")


class AdVideoGetCommentsParams(BaseModel):
    """Parameters for AdVideo.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    filter: videocomments_filter_enum_param | None = Field(None, description="filter parameter")
    live_filter: videocomments_live_filter_enum_param | None = Field(
        None, description="live_filter parameter"
    )
    order: videocomments_order_enum_param | None = Field(None, description="order parameter")
    since: datetime | None = Field(None, description="since parameter")


class AdVideoCreateCommentParams(BaseModel):
    """Parameters for AdVideo.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    attachment_id: str | None = Field(None, description="attachment_id parameter")
    attachment_share_url: str | None = Field(None, description="attachment_share_url parameter")
    attachment_url: str | None = Field(None, description="attachment_url parameter")
    comment_privacy_value: videocomments_comment_privacy_value_enum_param | None = Field(
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


class AdVideoCreateGamingClipCreateParams(BaseModel):
    """Parameters for AdVideo.create_gaming_clip_create()."""

    model_config = ConfigDict(extra="forbid")
    duration_seconds: float | None = Field(None, description="duration_seconds parameter")


class AdVideoCreateLikeParams(BaseModel):
    """Parameters for AdVideo.create_like()."""

    model_config = ConfigDict(extra="forbid")
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    notify: bool | None = Field(None, description="notify parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class AdVideoCreatePollParams(BaseModel):
    """Parameters for AdVideo.create_poll()."""

    model_config = ConfigDict(extra="forbid")
    close_after_voting: bool | None = Field(None, description="close_after_voting parameter")
    correct_option: int | None = Field(None, description="correct_option parameter")
    default_open: bool | None = Field(None, description="default_open parameter")
    options: list[str] | None = Field(None, description="options parameter")
    question: str | None = Field(None, description="question parameter")
    show_gradient: bool | None = Field(None, description="show_gradient parameter")
    show_results: bool | None = Field(None, description="show_results parameter")


class AdVideoCreateThumbnailParams(BaseModel):
    """Parameters for AdVideo.create_thumbnail()."""

    model_config = ConfigDict(extra="forbid")
    is_preferred: bool | None = Field(None, description="is_preferred parameter")
    source: dict[str, Any] | None = Field(None, description="source parameter")


class AdVideoGetVideoInsightsParams(BaseModel):
    """Parameters for AdVideo.get_video_insights()."""

    model_config = ConfigDict(extra="forbid")
    metric: list[dict[str, Any]] | None = Field(None, description="metric parameter")
    period: videovideo_insights_period_enum_param | None = Field(
        None, description="period parameter"
    )
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")
