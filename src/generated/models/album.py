"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .event import EventFields
    from .photo import PhotoFields
    from .place import PlaceFields


class albumphotos_backdated_time_granularity_enum_param(str, Enum):
    """albumphotos_backdated_time_granularity_enum_param enum values."""

    day = "day"
    hour = "hour"
    min = "min"
    month = "month"
    none = "none"
    year = "year"


class albumcomments_filter_enum_param(str, Enum):
    """albumcomments_filter_enum_param enum values."""

    stream = "stream"
    toplevel = "toplevel"


class albumcomments_comment_privacy_value_enum_param(str, Enum):
    """albumcomments_comment_privacy_value_enum_param enum values."""

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


class albumphotos_unpublished_content_type_enum_param(str, Enum):
    """albumphotos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class albumcomments_live_filter_enum_param(str, Enum):
    """albumcomments_live_filter_enum_param enum values."""

    filter_low_quality = "filter_low_quality"
    no_filter = "no_filter"


class albumcomments_order_enum_param(str, Enum):
    """albumcomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


class albumpicture_type_enum_param(str, Enum):
    """albumpicture_type_enum_param enum values."""

    album = "album"
    small = "small"
    thumbnail = "thumbnail"


# Field literal type
AlbumField = Literal[
    "backdated_time",
    "backdated_time_granularity",
    "can_backdate",
    "can_upload",
    "count",
    "cover_photo",
    "created_time",
    "description",
    "edit_link",
    "event",
    "from",
    "id",
    "is_user_facing",
    "link",
    "location",
    "modified_major",
    "name",
    "photo_count",
    "place",
    "privacy",
    "type",
    "updated_time",
    "video_count",
]


class AlbumFields(BaseModel):
    """Pydantic model for Album fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    backdated_time: datetime = Field(None, alias="backdated_time")
    backdated_time_granularity: str = Field(None, alias="backdated_time_granularity")
    can_backdate: bool = Field(None, alias="can_backdate")
    can_upload: bool = Field(None, alias="can_upload")
    count: int = Field(None, alias="count")
    cover_photo: PhotoFields = Field(None, alias="cover_photo")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    edit_link: str = Field(None, alias="edit_link")
    event: EventFields = Field(None, alias="event")
    from_: dict[str, Any] = Field(None, alias="from")
    id: str = Field(None, alias="id")
    is_user_facing: bool = Field(None, alias="is_user_facing")
    link: str = Field(None, alias="link")
    location: str = Field(None, alias="location")
    modified_major: datetime = Field(None, alias="modified_major")
    name: str = Field(None, alias="name")
    photo_count: int = Field(None, alias="photo_count")
    place: PlaceFields = Field(None, alias="place")
    privacy: str = Field(None, alias="privacy")
    type: str = Field(None, alias="type")
    updated_time: datetime = Field(None, alias="updated_time")
    video_count: int = Field(None, alias="video_count")


class AlbumGetCommentsParams(BaseModel):
    """Parameters for Album.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    filter: albumcomments_filter_enum_param | None = Field(None, description="filter parameter")
    live_filter: albumcomments_live_filter_enum_param | None = Field(
        None, description="live_filter parameter"
    )
    order: albumcomments_order_enum_param | None = Field(None, description="order parameter")
    since: datetime | None = Field(None, description="since parameter")


class AlbumCreateCommentParams(BaseModel):
    """Parameters for Album.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    attachment_id: str | None = Field(None, description="attachment_id parameter")
    attachment_share_url: str | None = Field(None, description="attachment_share_url parameter")
    attachment_url: str | None = Field(None, description="attachment_url parameter")
    comment_privacy_value: albumcomments_comment_privacy_value_enum_param | None = Field(
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


class AlbumCreateLikeParams(BaseModel):
    """Parameters for Album.create_like()."""

    model_config = ConfigDict(extra="forbid")
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    notify: bool | None = Field(None, description="notify parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class AlbumCreatePhotoParams(BaseModel):
    """Parameters for Album.create_photo()."""

    model_config = ConfigDict(extra="forbid")
    aid: str | None = Field(None, description="aid parameter")
    allow_spherical_photo: bool | None = Field(None, description="allow_spherical_photo parameter")
    alt_text_custom: str | None = Field(None, description="alt_text_custom parameter")
    android_key_hash: str | None = Field(None, description="android_key_hash parameter")
    application_id: str | None = Field(None, description="application_id parameter")
    attempt: int | None = Field(None, description="attempt parameter")
    audience_exp: bool | None = Field(None, description="audience_exp parameter")
    backdated_time: datetime | None = Field(None, description="backdated_time parameter")
    backdated_time_granularity: albumphotos_backdated_time_granularity_enum_param | None = Field(
        None, description="backdated_time_granularity parameter"
    )
    caption: str | None = Field(None, description="caption parameter")
    composer_session_id: str | None = Field(None, description="composer_session_id parameter")
    direct_share_status: int | None = Field(None, description="direct_share_status parameter")
    feed_targeting: dict[str, Any] | None = Field(None, description="feed_targeting parameter")
    filter_type: int | None = Field(None, description="filter_type parameter")
    full_res_is_coming_later: bool | None = Field(
        None, description="full_res_is_coming_later parameter"
    )
    initial_view_heading_override_degrees: int | None = Field(
        None, description="initial_view_heading_override_degrees parameter"
    )
    initial_view_pitch_override_degrees: int | None = Field(
        None, description="initial_view_pitch_override_degrees parameter"
    )
    initial_view_vertical_fov_override_degrees: int | None = Field(
        None, description="initial_view_vertical_fov_override_degrees parameter"
    )
    ios_bundle_id: str | None = Field(None, description="ios_bundle_id parameter")
    is_explicit_location: bool | None = Field(None, description="is_explicit_location parameter")
    is_explicit_place: bool | None = Field(None, description="is_explicit_place parameter")
    manual_privacy: bool | None = Field(None, description="manual_privacy parameter")
    message: str | None = Field(None, description="message parameter")
    name: str | None = Field(None, description="name parameter")
    no_story: bool | None = Field(None, description="no_story parameter")
    offline_id: int | None = Field(None, description="offline_id parameter")
    og_action_type_id: str | None = Field(None, description="og_action_type_id parameter")
    og_icon_id: str | None = Field(None, description="og_icon_id parameter")
    og_object_id: str | None = Field(None, description="og_object_id parameter")
    og_phrase: str | None = Field(None, description="og_phrase parameter")
    og_set_profile_badge: bool | None = Field(None, description="og_set_profile_badge parameter")
    og_suggestion_mechanism: str | None = Field(
        None, description="og_suggestion_mechanism parameter"
    )
    place: dict[str, Any] | None = Field(None, description="place parameter")
    privacy: str | None = Field(None, description="privacy parameter")
    profile_id: int | None = Field(None, description="profile_id parameter")
    provenance_info: dict[str, Any] | None = Field(None, description="provenance_info parameter")
    proxied_app_id: str | None = Field(None, description="proxied_app_id parameter")
    published: bool | None = Field(None, description="published parameter")
    qn: str | None = Field(None, description="qn parameter")
    spherical_metadata: dict[str, Any] | None = Field(
        None, description="spherical_metadata parameter"
    )
    sponsor_id: str | None = Field(None, description="sponsor_id parameter")
    sponsor_relationship: int | None = Field(None, description="sponsor_relationship parameter")
    tags: list[dict[str, Any]] | None = Field(None, description="tags parameter")
    target_id: int | None = Field(None, description="target_id parameter")
    targeting: dict[str, Any] | None = Field(None, description="targeting parameter")
    time_since_original_post: int | None = Field(
        None, description="time_since_original_post parameter"
    )
    uid: int | None = Field(None, description="uid parameter")
    unpublished_content_type: albumphotos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    url: str | None = Field(None, description="url parameter")
    user_selected_tags: bool | None = Field(None, description="user_selected_tags parameter")
    vault_image_id: str | None = Field(None, description="vault_image_id parameter")


class AlbumGetPictureParams(BaseModel):
    """Parameters for Album.get_picture()."""

    model_config = ConfigDict(extra="forbid")
    redirect: bool | None = Field(None, description="redirect parameter")
    type: albumpicture_type_enum_param | None = Field(None, description="type parameter")
