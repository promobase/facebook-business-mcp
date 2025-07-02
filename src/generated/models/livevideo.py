"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .advideo import AdVideoFields
    from .livevideoadbreakconfig import LiveVideoAdBreakConfigFields
    from .livevideoinputstream import LiveVideoInputStreamFields
    from .livevideorecommendedencodersettings import LiveVideoRecommendedEncoderSettingsFields
    from .livevideotargeting import LiveVideoTargetingFields
    from .videocopyright import VideoCopyrightFields


class livevideocomments_order_enum_param(str, Enum):
    """livevideocomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


class livevideoreactions_type_enum_param(str, Enum):
    """livevideoreactions_type_enum_param enum values."""

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


class livevideocomments_live_filter_enum_param(str, Enum):
    """livevideocomments_live_filter_enum_param enum values."""

    filter_low_quality = "filter_low_quality"
    no_filter = "no_filter"


class livevideocomments_filter_enum_param(str, Enum):
    """livevideocomments_filter_enum_param enum values."""

    stream = "stream"
    toplevel = "toplevel"


# Field literal type
LiveVideoField = Literal[
    "ad_break_config",
    "ad_break_failure_reason",
    "broadcast_start_time",
    "copyright",
    "creation_time",
    "dash_ingest_url",
    "dash_preview_url",
    "description",
    "embed_html",
    "from",
    "id",
    "ingest_streams",
    "is_manual_mode",
    "is_reference_only",
    "live_views",
    "overlay_url",
    "permalink_url",
    "planned_start_time",
    "recommended_encoder_settings",
    "seconds_left",
    "secure_stream_url",
    "status",
    "stream_url",
    "targeting",
    "title",
    "total_views",
    "video",
]


class LiveVideoFields(BaseModel):
    """Pydantic model for LiveVideo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_break_config: LiveVideoAdBreakConfigFields = Field(None, alias="ad_break_config")
    ad_break_failure_reason: str = Field(None, alias="ad_break_failure_reason")
    broadcast_start_time: datetime = Field(None, alias="broadcast_start_time")
    copyright: VideoCopyrightFields = Field(None, alias="copyright")
    creation_time: datetime = Field(None, alias="creation_time")
    dash_ingest_url: str = Field(None, alias="dash_ingest_url")
    dash_preview_url: str = Field(None, alias="dash_preview_url")
    description: str = Field(None, alias="description")
    embed_html: dict[str, Any] = Field(None, alias="embed_html")
    from_: dict[str, Any] = Field(None, alias="from")
    id: str = Field(None, alias="id")
    ingest_streams: list[LiveVideoInputStreamFields] = Field(None, alias="ingest_streams")
    is_manual_mode: bool = Field(None, alias="is_manual_mode")
    is_reference_only: bool = Field(None, alias="is_reference_only")
    live_views: int = Field(None, alias="live_views")
    overlay_url: str = Field(None, alias="overlay_url")
    permalink_url: str = Field(None, alias="permalink_url")
    planned_start_time: datetime = Field(None, alias="planned_start_time")
    recommended_encoder_settings: LiveVideoRecommendedEncoderSettingsFields = Field(
        None, alias="recommended_encoder_settings"
    )
    seconds_left: int = Field(None, alias="seconds_left")
    secure_stream_url: str = Field(None, alias="secure_stream_url")
    status: str = Field(None, alias="status")
    stream_url: str = Field(None, alias="stream_url")
    targeting: LiveVideoTargetingFields = Field(None, alias="targeting")
    title: str = Field(None, alias="title")
    total_views: str = Field(None, alias="total_views")
    video: AdVideoFields = Field(None, alias="video")


class LiveVideoGetBlockedUsersParams(BaseModel):
    """Parameters for LiveVideo.get_blocked_users()."""

    model_config = ConfigDict(extra="forbid")
    uid: str | None = Field(None, description="uid parameter")


class LiveVideoGetCommentsParams(BaseModel):
    """Parameters for LiveVideo.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    filter: livevideocomments_filter_enum_param | None = Field(None, description="filter parameter")
    live_filter: livevideocomments_live_filter_enum_param | None = Field(
        None, description="live_filter parameter"
    )
    order: livevideocomments_order_enum_param | None = Field(None, description="order parameter")
    since: datetime | None = Field(None, description="since parameter")


class LiveVideoCreatePollParams(BaseModel):
    """Parameters for LiveVideo.create_poll()."""

    model_config = ConfigDict(extra="forbid")
    close_after_voting: bool | None = Field(None, description="close_after_voting parameter")
    correct_option: int | None = Field(None, description="correct_option parameter")
    default_open: bool | None = Field(None, description="default_open parameter")
    options: list[str] | None = Field(None, description="options parameter")
    question: str | None = Field(None, description="question parameter")
    show_gradient: bool | None = Field(None, description="show_gradient parameter")
    show_results: bool | None = Field(None, description="show_results parameter")


class LiveVideoGetReactionsParams(BaseModel):
    """Parameters for LiveVideo.get_reactions()."""

    model_config = ConfigDict(extra="forbid")
    type: livevideoreactions_type_enum_param | None = Field(None, description="type parameter")
