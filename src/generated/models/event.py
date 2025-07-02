"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .childevent import ChildEventFields
    from .coverphoto import CoverPhotoFields
    from .eventregistrationsetting import EventRegistrationSettingFields
    from .eventticketsetting import EventTicketSettingFields
    from .group import GroupFields
    from .place import PlaceFields


class Event_category(str, Enum):
    """Event_category enum values."""

    CLASSIC_LITERATURE = "CLASSIC_LITERATURE"
    COMEDY = "COMEDY"
    CRAFTS = "CRAFTS"
    DANCE = "DANCE"
    DRINKS = "DRINKS"
    FITNESS_AND_WORKOUTS = "FITNESS_AND_WORKOUTS"
    FOODS = "FOODS"
    GAMES = "GAMES"
    GARDENING = "GARDENING"
    HEALTHY_LIVING_AND_SELF_CARE = "HEALTHY_LIVING_AND_SELF_CARE"
    HEALTH_AND_MEDICAL = "HEALTH_AND_MEDICAL"
    HOME_AND_GARDEN = "HOME_AND_GARDEN"
    MUSIC_AND_AUDIO = "MUSIC_AND_AUDIO"
    PARTIES = "PARTIES"
    PROFESSIONAL_NETWORKING = "PROFESSIONAL_NETWORKING"
    RELIGIONS = "RELIGIONS"
    SHOPPING_EVENT = "SHOPPING_EVENT"
    SOCIAL_ISSUES = "SOCIAL_ISSUES"
    SPORTS = "SPORTS"
    THEATER = "THEATER"
    TV_AND_MOVIES = "TV_AND_MOVIES"
    VISUAL_ARTS = "VISUAL_ARTS"


class Event_online_event_format(str, Enum):
    """Event_online_event_format enum values."""

    fb_live = "fb_live"
    horizon_event = "horizon_event"
    horizon_world = "horizon_world"
    messenger_room = "messenger_room"
    none = "none"
    other = "other"
    third_party = "third_party"


class Event_type(str, Enum):
    """Event_type enum values."""

    community = "community"
    friends = "friends"
    group = "group"
    messenger_community = "messenger_community"
    private = "private"
    public = "public"
    work_company = "work_company"


class eventlive_videos_stereoscopic_mode_enum_param(str, Enum):
    """eventlive_videos_stereoscopic_mode_enum_param enum values."""

    LEFT_RIGHT = "LEFT_RIGHT"
    MONO = "MONO"
    TOP_BOTTOM = "TOP_BOTTOM"


class eventlive_videos_projection_enum_param(str, Enum):
    """eventlive_videos_projection_enum_param enum values."""

    CUBEMAP = "CUBEMAP"
    EQUIRECTANGULAR = "EQUIRECTANGULAR"
    HALF_EQUIRECTANGULAR = "HALF_EQUIRECTANGULAR"


class eventlive_videos_stream_type_enum_param(str, Enum):
    """eventlive_videos_stream_type_enum_param enum values."""

    AMBIENT = "AMBIENT"
    REGULAR = "REGULAR"


class eventlive_videos_status_enum_param(str, Enum):
    """eventlive_videos_status_enum_param enum values."""

    LIVE_NOW = "LIVE_NOW"
    SCHEDULED_CANCELED = "SCHEDULED_CANCELED"
    SCHEDULED_LIVE = "SCHEDULED_LIVE"
    SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"


class eventlive_videos_spatial_audio_format_enum_param(str, Enum):
    """eventlive_videos_spatial_audio_format_enum_param enum values."""

    ambiX_4 = "ambiX_4"


# Field literal type
EventField = Literal[
    "attending_count",
    "can_guests_invite",
    "category",
    "cover",
    "created_time",
    "declined_count",
    "description",
    "discount_code_enabled",
    "end_time",
    "event_times",
    "guest_list_enabled",
    "id",
    "interested_count",
    "is_canceled",
    "is_draft",
    "is_online",
    "is_page_owned",
    "maybe_count",
    "name",
    "noreply_count",
    "online_event_format",
    "online_event_third_party_url",
    "owner",
    "parent_group",
    "place",
    "registration_setting",
    "scheduled_publish_time",
    "start_time",
    "sub_categories",
    "ticket_selling_status",
    "ticket_setting",
    "ticket_uri",
    "ticket_uri_start_sales_time",
    "ticketing_privacy_uri",
    "ticketing_terms_uri",
    "timezone",
    "type",
    "updated_time",
]


class EventFields(BaseModel):
    """Pydantic model for Event fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    attending_count: int = Field(None, alias="attending_count")
    can_guests_invite: bool = Field(None, alias="can_guests_invite")
    category: dict[str, Any] = Field(None, alias="category")
    cover: CoverPhotoFields = Field(None, alias="cover")
    created_time: datetime = Field(None, alias="created_time")
    declined_count: int = Field(None, alias="declined_count")
    description: str = Field(None, alias="description")
    discount_code_enabled: bool = Field(None, alias="discount_code_enabled")
    end_time: str = Field(None, alias="end_time")
    event_times: list[ChildEventFields] = Field(None, alias="event_times")
    guest_list_enabled: bool = Field(None, alias="guest_list_enabled")
    id: str = Field(None, alias="id")
    interested_count: int = Field(None, alias="interested_count")
    is_canceled: bool = Field(None, alias="is_canceled")
    is_draft: bool = Field(None, alias="is_draft")
    is_online: bool = Field(None, alias="is_online")
    is_page_owned: bool = Field(None, alias="is_page_owned")
    maybe_count: int = Field(None, alias="maybe_count")
    name: str = Field(None, alias="name")
    noreply_count: int = Field(None, alias="noreply_count")
    online_event_format: dict[str, Any] = Field(None, alias="online_event_format")
    online_event_third_party_url: str = Field(None, alias="online_event_third_party_url")
    owner: dict[str, Any] = Field(None, alias="owner")
    parent_group: GroupFields = Field(None, alias="parent_group")
    place: PlaceFields = Field(None, alias="place")
    registration_setting: EventRegistrationSettingFields = Field(None, alias="registration_setting")
    scheduled_publish_time: str = Field(None, alias="scheduled_publish_time")
    start_time: str = Field(None, alias="start_time")
    sub_categories: list[str] = Field(None, alias="sub_categories")
    ticket_selling_status: str = Field(None, alias="ticket_selling_status")
    ticket_setting: EventTicketSettingFields = Field(None, alias="ticket_setting")
    ticket_uri: str = Field(None, alias="ticket_uri")
    ticket_uri_start_sales_time: str = Field(None, alias="ticket_uri_start_sales_time")
    ticketing_privacy_uri: str = Field(None, alias="ticketing_privacy_uri")
    ticketing_terms_uri: str = Field(None, alias="ticketing_terms_uri")
    timezone: str = Field(None, alias="timezone")
    type: dict[str, Any] = Field(None, alias="type")
    updated_time: datetime = Field(None, alias="updated_time")


class EventCreateLiveVideoParams(BaseModel):
    """Parameters for Event.create_live_video()."""

    model_config = ConfigDict(extra="forbid")
    content_tags: list[str] | None = Field(None, description="content_tags parameter")
    description: str | None = Field(None, description="description parameter")
    enable_backup_ingest: bool | None = Field(None, description="enable_backup_ingest parameter")
    encoding_settings: str | None = Field(None, description="encoding_settings parameter")
    event_params: dict[str, Any] | None = Field(None, description="event_params parameter")
    fisheye_video_cropped: bool | None = Field(None, description="fisheye_video_cropped parameter")
    front_z_rotation: float | None = Field(None, description="front_z_rotation parameter")
    is_audio_only: bool | None = Field(None, description="is_audio_only parameter")
    is_spherical: bool | None = Field(None, description="is_spherical parameter")
    original_fov: int | None = Field(None, description="original_fov parameter")
    privacy: str | None = Field(None, description="privacy parameter")
    projection: eventlive_videos_projection_enum_param | None = Field(
        None, description="projection parameter"
    )
    published: bool | None = Field(None, description="published parameter")
    schedule_custom_profile_image: dict[str, Any] | None = Field(
        None, description="schedule_custom_profile_image parameter"
    )
    spatial_audio_format: eventlive_videos_spatial_audio_format_enum_param | None = Field(
        None, description="spatial_audio_format parameter"
    )
    status: eventlive_videos_status_enum_param | None = Field(None, description="status parameter")
    stereoscopic_mode: eventlive_videos_stereoscopic_mode_enum_param | None = Field(
        None, description="stereoscopic_mode parameter"
    )
    stop_on_delete_stream: bool | None = Field(None, description="stop_on_delete_stream parameter")
    stream_type: eventlive_videos_stream_type_enum_param | None = Field(
        None, description="stream_type parameter"
    )
    title: str | None = Field(None, description="title parameter")
