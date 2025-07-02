"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .coverphoto import CoverPhotoFields
    from .location import LocationFields


class groupphotos_unpublished_content_type_enum_param(str, Enum):
    """groupphotos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class groupfeed_formatting_enum_param(str, Enum):
    """groupfeed_formatting_enum_param enum values."""

    MARKDOWN = "MARKDOWN"
    PLAINTEXT = "PLAINTEXT"


class groupvideos_swap_mode_enum_param(str, Enum):
    """groupvideos_swap_mode_enum_param enum values."""

    replace = "replace"


class groupfeed_backdated_time_granularity_enum_param(str, Enum):
    """groupfeed_backdated_time_granularity_enum_param enum values."""

    day = "day"
    hour = "hour"
    min = "min"
    month = "month"
    none = "none"
    year = "year"


class grouplive_videos_projection_enum_param(str, Enum):
    """grouplive_videos_projection_enum_param enum values."""

    CUBEMAP = "CUBEMAP"
    EQUIRECTANGULAR = "EQUIRECTANGULAR"
    HALF_EQUIRECTANGULAR = "HALF_EQUIRECTANGULAR"


class groupvideos_original_projection_type_enum_param(str, Enum):
    """groupvideos_original_projection_type_enum_param enum values."""

    cubemap = "cubemap"
    equirectangular = "equirectangular"
    half_equirectangular = "half_equirectangular"


class grouplive_videos_status_enum_param(str, Enum):
    """grouplive_videos_status_enum_param enum values."""

    LIVE_NOW = "LIVE_NOW"
    SCHEDULED_CANCELED = "SCHEDULED_CANCELED"
    SCHEDULED_LIVE = "SCHEDULED_LIVE"
    SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"


class grouplive_videos_broadcast_status_enum_param(str, Enum):
    """grouplive_videos_broadcast_status_enum_param enum values."""

    LIVE = "LIVE"
    LIVE_STOPPED = "LIVE_STOPPED"
    PROCESSING = "PROCESSING"
    SCHEDULED_CANCELED = "SCHEDULED_CANCELED"
    SCHEDULED_EXPIRED = "SCHEDULED_EXPIRED"
    SCHEDULED_LIVE = "SCHEDULED_LIVE"
    SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"
    VOD = "VOD"


class groupvideos_content_category_enum_param(str, Enum):
    """groupvideos_content_category_enum_param enum values."""

    BEAUTY_FASHION = "BEAUTY_FASHION"
    BUSINESS = "BUSINESS"
    CARS_TRUCKS = "CARS_TRUCKS"
    COMEDY = "COMEDY"
    CUTE_ANIMALS = "CUTE_ANIMALS"
    ENTERTAINMENT = "ENTERTAINMENT"
    FAMILY = "FAMILY"
    FOOD_HEALTH = "FOOD_HEALTH"
    HOME = "HOME"
    LIFESTYLE = "LIFESTYLE"
    MUSIC = "MUSIC"
    NEWS = "NEWS"
    OTHER = "OTHER"
    POLITICS = "POLITICS"
    SCIENCE = "SCIENCE"
    SPORTS = "SPORTS"
    TECHNOLOGY = "TECHNOLOGY"
    VIDEO_GAMING = "VIDEO_GAMING"


class groupfeed_target_surface_enum_param(str, Enum):
    """groupfeed_target_surface_enum_param enum values."""

    STORY = "STORY"
    TIMELINE = "TIMELINE"


class grouplive_videos_spatial_audio_format_enum_param(str, Enum):
    """grouplive_videos_spatial_audio_format_enum_param enum values."""

    ambiX_4 = "ambiX_4"


class groupfeed_unpublished_content_type_enum_param(str, Enum):
    """groupfeed_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class grouplive_videos_stream_type_enum_param(str, Enum):
    """grouplive_videos_stream_type_enum_param enum values."""

    AMBIENT = "AMBIENT"
    REGULAR = "REGULAR"


class groupvideos_type_enum_param(str, Enum):
    """groupvideos_type_enum_param enum values."""

    tagged = "tagged"
    uploaded = "uploaded"


class groupgroups_group_type_enum_param(str, Enum):
    """groupgroups_group_type_enum_param enum values."""

    CASUAL = "CASUAL"
    COWORKERS = "COWORKERS"
    CUSTOM = "CUSTOM"
    FOR_SALE = "FOR_SALE"
    FOR_WORK = "FOR_WORK"
    GAME = "GAME"
    HEALTH_SUPPORT = "HEALTH_SUPPORT"
    JOBS = "JOBS"
    LEARNING = "LEARNING"
    NONE = "NONE"
    PARENTING = "PARENTING"
    STREAMER = "STREAMER"
    WORK_ANNOUNCEMENT = "WORK_ANNOUNCEMENT"
    WORK_DEMO_GROUP = "WORK_DEMO_GROUP"
    WORK_DISCUSSION = "WORK_DISCUSSION"
    WORK_EPHEMERAL = "WORK_EPHEMERAL"
    WORK_FEEDBACK = "WORK_FEEDBACK"
    WORK_FOR_SALE = "WORK_FOR_SALE"
    WORK_GARDEN = "WORK_GARDEN"
    WORK_INTEGRITY = "WORK_INTEGRITY"
    WORK_LEARNING = "WORK_LEARNING"
    WORK_MENTORSHIP = "WORK_MENTORSHIP"
    WORK_MULTI_COMPANY = "WORK_MULTI_COMPANY"
    WORK_RECRUITING = "WORK_RECRUITING"
    WORK_SOCIAL = "WORK_SOCIAL"
    WORK_STAGES = "WORK_STAGES"
    WORK_TEAM = "WORK_TEAM"
    WORK_TEAMWORK = "WORK_TEAMWORK"


class grouplive_videos_source_enum_param(str, Enum):
    """grouplive_videos_source_enum_param enum values."""

    owner = "owner"
    target = "target"


class groupfeed_posting_to_redspace_enum_param(str, Enum):
    """groupfeed_posting_to_redspace_enum_param enum values."""

    disabled = "disabled"
    enabled = "enabled"


class groupfeed_place_attachment_setting_enum_param(str, Enum):
    """groupfeed_place_attachment_setting_enum_param enum values."""

    VALUE_1 = "1"
    VALUE_2 = "2"


class groupgroups_join_setting_enum_param(str, Enum):
    """groupgroups_join_setting_enum_param enum values."""

    ADMIN_ONLY = "ADMIN_ONLY"
    ANYONE = "ANYONE"
    NONE = "NONE"


class grouppicture_type_enum_param(str, Enum):
    """grouppicture_type_enum_param enum values."""

    album = "album"
    large = "large"
    normal = "normal"
    small = "small"
    square = "square"


class groupphotos_backdated_time_granularity_enum_param(str, Enum):
    """groupphotos_backdated_time_granularity_enum_param enum values."""

    day = "day"
    hour = "hour"
    min = "min"
    month = "month"
    none = "none"
    year = "year"


class groupvideos_formatting_enum_param(str, Enum):
    """groupvideos_formatting_enum_param enum values."""

    MARKDOWN = "MARKDOWN"
    PLAINTEXT = "PLAINTEXT"


class groupvideos_container_type_enum_param(str, Enum):
    """groupvideos_container_type_enum_param enum values."""

    ACO_VIDEO_VARIATION = "ACO_VIDEO_VARIATION"
    ADS_AI_GENERATED = "ADS_AI_GENERATED"
    AD_BREAK_PREVIEW = "AD_BREAK_PREVIEW"
    AD_DERIVATIVE = "AD_DERIVATIVE"
    AD_LIBRARY_WATERMARK = "AD_LIBRARY_WATERMARK"
    ALBUM_MULTIMEDIA_POST = "ALBUM_MULTIMEDIA_POST"
    ALOHA_SUPERFRAME = "ALOHA_SUPERFRAME"
    APP_REREVIEW_SCREENCAST = "APP_REREVIEW_SCREENCAST"
    APP_REVIEW_SCREENCAST = "APP_REVIEW_SCREENCAST"
    ASSET_MANAGER = "ASSET_MANAGER"
    ATLAS_VIDEO = "ATLAS_VIDEO"
    AUDIO_BROADCAST = "AUDIO_BROADCAST"
    AUDIO_COMMENT = "AUDIO_COMMENT"
    BROADCAST = "BROADCAST"
    CANVAS = "CANVAS"
    CMS_MEDIA_MANAGER = "CMS_MEDIA_MANAGER"
    CONTAINED_POST_ATTACHMENT = "CONTAINED_POST_ATTACHMENT"
    CONTAINED_POST_AUDIO_BROADCAST = "CONTAINED_POST_AUDIO_BROADCAST"
    CONTAINED_POST_COPYRIGHT_REFERENCE_BROADCAST = "CONTAINED_POST_COPYRIGHT_REFERENCE_BROADCAST"
    COPYRIGHT_REFERENCE_BROADCAST = "COPYRIGHT_REFERENCE_BROADCAST"
    COPYRIGHT_REFERENCE_IG_XPOST_VIDEO = "COPYRIGHT_REFERENCE_IG_XPOST_VIDEO"
    COPYRIGHT_REFERENCE_VIDEO = "COPYRIGHT_REFERENCE_VIDEO"
    CREATION_ML_PRECREATION = "CREATION_ML_PRECREATION"
    CREATOR_FAN_CHALLENGE = "CREATOR_FAN_CHALLENGE"
    CREATOR_STOREFRONT_PERSONALIZED_VIDEO = "CREATOR_STOREFRONT_PERSONALIZED_VIDEO"
    DATAGENIX_VIDEO = "DATAGENIX_VIDEO"
    DCO_AD_ASSET_FEED = "DCO_AD_ASSET_FEED"
    DCO_AUTOGEN_VIDEO = "DCO_AUTOGEN_VIDEO"
    DCO_TRIMMED_VIDEO = "DCO_TRIMMED_VIDEO"
    DIM_SUM = "DIM_SUM"
    DIRECTED_POST_ATTACHMENT = "DIRECTED_POST_ATTACHMENT"
    DIRECT_INBOX = "DIRECT_INBOX"
    DROPS_SHOPPING_EVENT_PAGE = "DROPS_SHOPPING_EVENT_PAGE"
    DYNAMIC_ITEM_VIDEO = "DYNAMIC_ITEM_VIDEO"
    DYNAMIC_TEMPLATE_VIDEO = "DYNAMIC_TEMPLATE_VIDEO"
    EVENT_COVER_VIDEO = "EVENT_COVER_VIDEO"
    EVENT_TOUR = "EVENT_TOUR"
    FACECAST_DVR = "FACECAST_DVR"
    FB_AVATAR_ANIMATED_SATP = "FB_AVATAR_ANIMATED_SATP"
    FB_COLLECTIBLE_VIDEO = "FB_COLLECTIBLE_VIDEO"
    FB_SHORTS = "FB_SHORTS"
    FB_SHORTS_CONTENT_REMIXABLE = "FB_SHORTS_CONTENT_REMIXABLE"
    FB_SHORTS_GROUP_POST = "FB_SHORTS_GROUP_POST"
    FB_SHORTS_LINKED_PRODUCT = "FB_SHORTS_LINKED_PRODUCT"
    FB_SHORTS_PMV_POST = "FB_SHORTS_PMV_POST"
    FB_SHORTS_POST = "FB_SHORTS_POST"
    FB_SHORTS_REMIX_POST = "FB_SHORTS_REMIX_POST"
    FUNDRAISER_COVER_VIDEO = "FUNDRAISER_COVER_VIDEO"
    GAME_CLIP = "GAME_CLIP"
    GIF_TO_VIDEO = "GIF_TO_VIDEO"
    GOODWILL_ANNIVERSARY_DEPRECATED = "GOODWILL_ANNIVERSARY_DEPRECATED"
    GOODWILL_ANNIVERSARY_PROMOTION_DEPRECATED = "GOODWILL_ANNIVERSARY_PROMOTION_DEPRECATED"
    GOODWILL_VIDEO_CONTAINED_SHARE = "GOODWILL_VIDEO_CONTAINED_SHARE"
    GOODWILL_VIDEO_PROMOTION = "GOODWILL_VIDEO_PROMOTION"
    GOODWILL_VIDEO_SHARE = "GOODWILL_VIDEO_SHARE"
    GOODWILL_VIDEO_TOKEN_REQUIRED = "GOODWILL_VIDEO_TOKEN_REQUIRED"
    GROUP_POST = "GROUP_POST"
    HEURISTIC_CLUSTER_VIDEO = "HEURISTIC_CLUSTER_VIDEO"
    HIGHLIGHT_CLIP_VIDEO = "HIGHLIGHT_CLIP_VIDEO"
    HORIZON_WORLDS_TV = "HORIZON_WORLDS_TV"
    HUDDLE_BROADCAST = "HUDDLE_BROADCAST"
    IG_REELS_XPV = "IG_REELS_XPV"
    IG_STORIES_READER = "IG_STORIES_READER"
    INJECTABLE = "INJECTABLE"
    INSPIRATION_VIDEO = "INSPIRATION_VIDEO"
    INSTAGRAM_VIDEO_COPY = "INSTAGRAM_VIDEO_COPY"
    INSTANT_APPLICATION_PREVIEW = "INSTANT_APPLICATION_PREVIEW"
    INSTANT_ARTICLE = "INSTANT_ARTICLE"
    ISSUE_MODULE = "ISSUE_MODULE"
    LEARN = "LEARN"
    LEGACY = "LEGACY"
    LEGACY_CONTAINED_POST_BROADCAST = "LEGACY_CONTAINED_POST_BROADCAST"
    LIVE_AUDIO_ROOM_BROADCAST = "LIVE_AUDIO_ROOM_BROADCAST"
    LIVE_CLIP_PREVIEW = "LIVE_CLIP_PREVIEW"
    LIVE_CLIP_WORKCHAT = "LIVE_CLIP_WORKCHAT"
    LIVE_CREATIVE_KIT_VIDEO = "LIVE_CREATIVE_KIT_VIDEO"
    LIVE_PHOTO = "LIVE_PHOTO"
    LOOK_NOW_DEPRECATED = "LOOK_NOW_DEPRECATED"
    MARKETPLACE_LISTING_VIDEO = "MARKETPLACE_LISTING_VIDEO"
    MARKETPLACE_PRE_RECORDED_VIDEO = "MARKETPLACE_PRE_RECORDED_VIDEO"
    MOMENTS_VIDEO = "MOMENTS_VIDEO"
    MUSIC_CLIP = "MUSIC_CLIP"
    MUSIC_CLIP_IN_COMMENT = "MUSIC_CLIP_IN_COMMENT"
    MUSIC_CLIP_IN_LIGHTWEIGHT_STATUS = "MUSIC_CLIP_IN_LIGHTWEIGHT_STATUS"
    MUSIC_CLIP_IN_MSGR_NOTE = "MUSIC_CLIP_IN_MSGR_NOTE"
    MUSIC_CLIP_IN_POLL_OPTION = "MUSIC_CLIP_IN_POLL_OPTION"
    MUSIC_CLIP_ON_DATING_PROFILE = "MUSIC_CLIP_ON_DATING_PROFILE"
    NEO_ASYNC_GAME_VIDEO = "NEO_ASYNC_GAME_VIDEO"
    NEW_CONTAINED_POST_BROADCAST = "NEW_CONTAINED_POST_BROADCAST"
    NO_STORY = "NO_STORY"
    OCULUS_CREATOR_PORTAL = "OCULUS_CREATOR_PORTAL"
    OCULUS_VENUES_BROADCAST = "OCULUS_VENUES_BROADCAST"
    ORIGINALITY_SELF_ADVOCACY = "ORIGINALITY_SELF_ADVOCACY"
    PAGES_COVER_VIDEO = "PAGES_COVER_VIDEO"
    PAGE_REVIEW_SCREENCAST = "PAGE_REVIEW_SCREENCAST"
    PAGE_SLIDESHOW_VIDEO = "PAGE_SLIDESHOW_VIDEO"
    PAID_CONTENT_PREVIEW = "PAID_CONTENT_PREVIEW"
    PAID_CONTENT_VIDEO = "PAID_CONTENT_VIDEO"
    PAID_CONTENT_VIDEO__POST = "PAID_CONTENT_VIDEO__POST"
    PIXELCLOUD = "PIXELCLOUD"
    PODCAST_HIGHLIGHT = "PODCAST_HIGHLIGHT"
    PODCAST_ML_PREVIEW = "PODCAST_ML_PREVIEW"
    PODCAST_ML_PREVIEW_NO_NEWSFEED_STORY = "PODCAST_ML_PREVIEW_NO_NEWSFEED_STORY"
    PODCAST_RSS = "PODCAST_RSS"
    PODCAST_RSS_EPHEMERAL = "PODCAST_RSS_EPHEMERAL"
    PODCAST_RSS_NO_NEWSFEED_STORY = "PODCAST_RSS_NO_NEWSFEED_STORY"
    PODCAST_VOICES = "PODCAST_VOICES"
    PODCAST_VOICES_NO_NEWSFEED_STORY = "PODCAST_VOICES_NO_NEWSFEED_STORY"
    PREMIERE_SOURCE = "PREMIERE_SOURCE"
    PREMIUM_MUSIC_VIDEO_CLIP = "PREMIUM_MUSIC_VIDEO_CLIP"
    PREMIUM_MUSIC_VIDEO_CROPPED_CLIP = "PREMIUM_MUSIC_VIDEO_CROPPED_CLIP"
    PREMIUM_MUSIC_VIDEO_NO_NEWSFEED_STORY = "PREMIUM_MUSIC_VIDEO_NO_NEWSFEED_STORY"
    PREMIUM_MUSIC_VIDEO_WITH_NEWSFEED_STORY = "PREMIUM_MUSIC_VIDEO_WITH_NEWSFEED_STORY"
    PRIVATE_GALLERY_VIDEO = "PRIVATE_GALLERY_VIDEO"
    PRODUCT_VIDEO = "PRODUCT_VIDEO"
    PROFILE_COVER_VIDEO = "PROFILE_COVER_VIDEO"
    PROFILE_INTRO_CARD = "PROFILE_INTRO_CARD"
    PROFILE_VIDEO = "PROFILE_VIDEO"
    PROTON = "PROTON"
    QUICK_CLIP_WORKPLACE_POST = "QUICK_CLIP_WORKPLACE_POST"
    QUICK_PROMOTION = "QUICK_PROMOTION"
    REPLACE_VIDEO = "REPLACE_VIDEO"
    SALES_CLIENT_INTERACTION = "SALES_CLIENT_INTERACTION"
    SHOWREEL_NATIVE_DUMMY_VIDEO = "SHOWREEL_NATIVE_DUMMY_VIDEO"
    SLIDESHOW_ANIMOTO = "SLIDESHOW_ANIMOTO"
    SLIDESHOW_SHAKR = "SLIDESHOW_SHAKR"
    SLIDESHOW_VARIATION_VIDEO = "SLIDESHOW_VARIATION_VIDEO"
    SOUND_PLATFORM_STREAM = "SOUND_PLATFORM_STREAM"
    SRT_ATTACHMENT = "SRT_ATTACHMENT"
    STORIES_VIDEO = "STORIES_VIDEO"
    STORYLINE = "STORYLINE"
    STORYLINE_WITH_EXTERNAL_MUSIC = "STORYLINE_WITH_EXTERNAL_MUSIC"
    STORY_ARCHIVE_VIDEO = "STORY_ARCHIVE_VIDEO"
    STORY_CARD_TEMPLATE = "STORY_CARD_TEMPLATE"
    STREAM_HIGHLIGHTS_VIDEO = "STREAM_HIGHLIGHTS_VIDEO"
    TAROT_DIGEST = "TAROT_DIGEST"
    TEMPORARY_UNLISTED = "TEMPORARY_UNLISTED"
    TEMP_VIDEO_COPYRIGHT_SCAN = "TEMP_VIDEO_COPYRIGHT_SCAN"
    UNLISTED = "UNLISTED"
    UNLISTED_OCULUS = "UNLISTED_OCULUS"
    VIDEO_COMMENT = "VIDEO_COMMENT"
    VIDEO_COMPOSITION_VARIATION = "VIDEO_COMPOSITION_VARIATION"
    VIDEO_CREATIVE_EDITOR_AUTOGEN_AD_VIDEO = "VIDEO_CREATIVE_EDITOR_AUTOGEN_AD_VIDEO"
    VIDEO_SUPERRES = "VIDEO_SUPERRES"
    VOICES_ARTICLE_VIDEO = "VOICES_ARTICLE_VIDEO"
    VU_GENERATED_VIDEO = "VU_GENERATED_VIDEO"
    WOODHENGE = "WOODHENGE"
    WORK_KNOWLEDGE_VIDEO = "WORK_KNOWLEDGE_VIDEO"
    YOUR_DAY = "YOUR_DAY"


class groupvideos_upload_phase_enum_param(str, Enum):
    """groupvideos_upload_phase_enum_param enum values."""

    cancel = "cancel"
    finish = "finish"
    start = "start"
    transfer = "transfer"


class groupgroups_post_permissions_enum_param(str, Enum):
    """groupgroups_post_permissions_enum_param enum values."""

    ADMIN_ONLY = "ADMIN_ONLY"
    ANYONE = "ANYONE"
    NONE = "NONE"


class groupvideos_unpublished_content_type_enum_param(str, Enum):
    """groupvideos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class groupfeed_post_surfaces_blacklist_enum_param(str, Enum):
    """groupfeed_post_surfaces_blacklist_enum_param enum values."""

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class grouplive_videos_stereoscopic_mode_enum_param(str, Enum):
    """grouplive_videos_stereoscopic_mode_enum_param enum values."""

    LEFT_RIGHT = "LEFT_RIGHT"
    MONO = "MONO"
    TOP_BOTTOM = "TOP_BOTTOM"


# Field literal type
GroupField = Literal[
    "archived",
    "cover",
    "created_time",
    "description",
    "email",
    "icon",
    "id",
    "install",
    "link",
    "member_count",
    "member_request_count",
    "name",
    "parent",
    "permissions",
    "privacy",
    "purpose",
    "subdomain",
    "updated_time",
    "venue",
]


class GroupFields(BaseModel):
    """Pydantic model for Group fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    archived: bool = Field(None, alias="archived")
    cover: CoverPhotoFields = Field(None, alias="cover")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    email: str = Field(None, alias="email")
    icon: str = Field(None, alias="icon")
    id: str = Field(None, alias="id")
    install: dict[str, Any] = Field(None, alias="install")
    link: str = Field(None, alias="link")
    member_count: int = Field(None, alias="member_count")
    member_request_count: int = Field(None, alias="member_request_count")
    name: str = Field(None, alias="name")
    parent: dict[str, Any] = Field(None, alias="parent")
    permissions: list[str] = Field(None, alias="permissions")
    privacy: str = Field(None, alias="privacy")
    purpose: str = Field(None, alias="purpose")
    subdomain: str = Field(None, alias="subdomain")
    updated_time: datetime = Field(None, alias="updated_time")
    venue: LocationFields = Field(None, alias="venue")


class GroupDeleteAdMinsParams(BaseModel):
    """Parameters for Group.delete_ad_mins()."""

    model_config = ConfigDict(extra="forbid")
    uid: int | None = Field(None, description="uid parameter")


class GroupCreateAdMinParams(BaseModel):
    """Parameters for Group.create_ad_min()."""

    model_config = ConfigDict(extra="forbid")
    uid: int | None = Field(None, description="uid parameter")


class GroupGetFeedParams(BaseModel):
    """Parameters for Group.get_feed()."""

    model_config = ConfigDict(extra="forbid")
    include_hidden: bool | None = Field(None, description="include_hidden parameter")
    q: str | None = Field(None, description="q parameter")
    show_expired: bool | None = Field(None, description="show_expired parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")
    with_: str | None = Field(None, alias="with", description="with parameter")


class GroupCreateFeedParams(BaseModel):
    """Parameters for Group.create_feed()."""

    model_config = ConfigDict(extra="forbid")
    actions: dict[str, Any] | None = Field(None, description="actions parameter")
    album_id: str | None = Field(None, description="album_id parameter")
    android_key_hash: str | None = Field(None, description="android_key_hash parameter")
    application_id: str | None = Field(None, description="application_id parameter")
    asked_fun_fact_prompt_id: int | None = Field(
        None, description="asked_fun_fact_prompt_id parameter"
    )
    asset3d_id: str | None = Field(None, description="asset3d_id parameter")
    associated_id: str | None = Field(None, description="associated_id parameter")
    attach_place_suggestion: bool | None = Field(
        None, description="attach_place_suggestion parameter"
    )
    attached_media: list[dict[str, Any]] | None = Field(
        None, description="attached_media parameter"
    )
    audience_exp: bool | None = Field(None, description="audience_exp parameter")
    backdated_time: datetime | None = Field(None, description="backdated_time parameter")
    backdated_time_granularity: groupfeed_backdated_time_granularity_enum_param | None = Field(
        None, description="backdated_time_granularity parameter"
    )
    breaking_news: bool | None = Field(None, description="breaking_news parameter")
    breaking_news_expiration: int | None = Field(
        None, description="breaking_news_expiration parameter"
    )
    call_to_action: dict[str, Any] | None = Field(None, description="call_to_action parameter")
    caption: str | None = Field(None, description="caption parameter")
    child_attachments: list[dict[str, Any]] | None = Field(
        None, description="child_attachments parameter"
    )
    client_mutation_id: str | None = Field(None, description="client_mutation_id parameter")
    composer_entry_picker: str | None = Field(None, description="composer_entry_picker parameter")
    composer_entry_point: str | None = Field(None, description="composer_entry_point parameter")
    composer_entry_time: int | None = Field(None, description="composer_entry_time parameter")
    composer_session_events_log: str | None = Field(
        None, description="composer_session_events_log parameter"
    )
    composer_session_id: str | None = Field(None, description="composer_session_id parameter")
    composer_source_surface: str | None = Field(
        None, description="composer_source_surface parameter"
    )
    composer_type: str | None = Field(None, description="composer_type parameter")
    connection_class: str | None = Field(None, description="connection_class parameter")
    content_attachment: str | None = Field(None, description="content_attachment parameter")
    coordinates: dict[str, Any] | None = Field(None, description="coordinates parameter")
    cta_link: str | None = Field(None, description="cta_link parameter")
    cta_type: str | None = Field(None, description="cta_type parameter")
    description: str | None = Field(None, description="description parameter")
    direct_share_status: int | None = Field(None, description="direct_share_status parameter")
    expanded_height: int | None = Field(None, description="expanded_height parameter")
    expanded_width: int | None = Field(None, description="expanded_width parameter")
    feed_targeting: dict[str, Any] | None = Field(None, description="feed_targeting parameter")
    formatting: groupfeed_formatting_enum_param | None = Field(
        None, description="formatting parameter"
    )
    fun_fact_prompt_id: str | None = Field(None, description="fun_fact_prompt_id parameter")
    fun_fact_toastee_id: int | None = Field(None, description="fun_fact_toastee_id parameter")
    height: int | None = Field(None, description="height parameter")
    home_checkin_city_id: dict[str, Any] | None = Field(
        None, description="home_checkin_city_id parameter"
    )
    image_crops: dict[str, Any] | None = Field(None, description="image_crops parameter")
    implicit_with_tags: list[int] | None = Field(None, description="implicit_with_tags parameter")
    instant_game_entry_point_data: str | None = Field(
        None, description="instant_game_entry_point_data parameter"
    )
    ios_bundle_id: str | None = Field(None, description="ios_bundle_id parameter")
    is_backout_draft: bool | None = Field(None, description="is_backout_draft parameter")
    is_boost_intended: bool | None = Field(None, description="is_boost_intended parameter")
    is_explicit_location: bool | None = Field(None, description="is_explicit_location parameter")
    is_explicit_share: bool | None = Field(None, description="is_explicit_share parameter")
    is_group_linking_post: bool | None = Field(None, description="is_group_linking_post parameter")
    is_photo_container: bool | None = Field(None, description="is_photo_container parameter")
    link: str | None = Field(None, description="link parameter")
    location_source_id: str | None = Field(None, description="location_source_id parameter")
    manual_privacy: bool | None = Field(None, description="manual_privacy parameter")
    message: str | None = Field(None, description="message parameter")
    multi_share_end_card: bool | None = Field(None, description="multi_share_end_card parameter")
    multi_share_optimized: bool | None = Field(None, description="multi_share_optimized parameter")
    name: str | None = Field(None, description="name parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    object_attachment: str | None = Field(None, description="object_attachment parameter")
    og_action_type_id: str | None = Field(None, description="og_action_type_id parameter")
    og_hide_object_attachment: bool | None = Field(
        None, description="og_hide_object_attachment parameter"
    )
    og_icon_id: str | None = Field(None, description="og_icon_id parameter")
    og_object_id: str | None = Field(None, description="og_object_id parameter")
    og_phrase: str | None = Field(None, description="og_phrase parameter")
    og_set_profile_badge: bool | None = Field(None, description="og_set_profile_badge parameter")
    og_suggestion_mechanism: str | None = Field(
        None, description="og_suggestion_mechanism parameter"
    )
    page_recommendation: str | None = Field(None, description="page_recommendation parameter")
    picture: str | None = Field(None, description="picture parameter")
    place: dict[str, Any] | None = Field(None, description="place parameter")
    place_attachment_setting: groupfeed_place_attachment_setting_enum_param | None = Field(
        None, description="place_attachment_setting parameter"
    )
    place_list: str | None = Field(None, description="place_list parameter")
    place_list_data: dict[str, Any] | None = Field(None, description="place_list_data parameter")
    post_surfaces_blacklist: list[groupfeed_post_surfaces_blacklist_enum_param] | None = Field(
        None, description="post_surfaces_blacklist parameter"
    )
    posting_to_redspace: groupfeed_posting_to_redspace_enum_param | None = Field(
        None, description="posting_to_redspace parameter"
    )
    privacy: str | None = Field(None, description="privacy parameter")
    prompt_id: str | None = Field(None, description="prompt_id parameter")
    prompt_tracking_string: str | None = Field(None, description="prompt_tracking_string parameter")
    properties: dict[str, Any] | None = Field(None, description="properties parameter")
    proxied_app_id: str | None = Field(None, description="proxied_app_id parameter")
    publish_event_id: int | None = Field(None, description="publish_event_id parameter")
    published: bool | None = Field(None, description="published parameter")
    quote: str | None = Field(None, description="quote parameter")
    ref: list[str] | None = Field(None, description="ref parameter")
    referenceable_image_ids: list[str] | None = Field(
        None, description="referenceable_image_ids parameter"
    )
    referral_id: str | None = Field(None, description="referral_id parameter")
    scheduled_publish_time: datetime | None = Field(
        None, description="scheduled_publish_time parameter"
    )
    source: str | None = Field(None, description="source parameter")
    sponsor_id: str | None = Field(None, description="sponsor_id parameter")
    sponsor_relationship: int | None = Field(None, description="sponsor_relationship parameter")
    suggested_place_id: dict[str, Any] | None = Field(
        None, description="suggested_place_id parameter"
    )
    tags: list[int] | None = Field(None, description="tags parameter")
    target_surface: groupfeed_target_surface_enum_param | None = Field(
        None, description="target_surface parameter"
    )
    targeting: dict[str, Any] | None = Field(None, description="targeting parameter")
    text_format_metadata: str | None = Field(None, description="text_format_metadata parameter")
    text_format_preset_id: str | None = Field(None, description="text_format_preset_id parameter")
    text_only_place: str | None = Field(None, description="text_only_place parameter")
    thumbnail: dict[str, Any] | None = Field(None, description="thumbnail parameter")
    time_since_original_post: int | None = Field(
        None, description="time_since_original_post parameter"
    )
    title: str | None = Field(None, description="title parameter")
    tracking_info: str | None = Field(None, description="tracking_info parameter")
    unpublished_content_type: groupfeed_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    user_selected_tags: bool | None = Field(None, description="user_selected_tags parameter")
    video_start_time_ms: int | None = Field(None, description="video_start_time_ms parameter")
    viewer_coordinates: dict[str, Any] | None = Field(
        None, description="viewer_coordinates parameter"
    )
    width: int | None = Field(None, description="width parameter")


class GroupCreateGroupParams(BaseModel):
    """Parameters for Group.create_group()."""

    model_config = ConfigDict(extra="forbid")
    admin: int | None = Field(None, description="admin parameter")
    description: str | None = Field(None, description="description parameter")
    group_icon_id: str | None = Field(None, description="group_icon_id parameter")
    group_type: groupgroups_group_type_enum_param | None = Field(
        None, description="group_type parameter"
    )
    join_setting: groupgroups_join_setting_enum_param | None = Field(
        None, description="join_setting parameter"
    )
    name: str | None = Field(None, description="name parameter")
    parent_id: str | None = Field(None, description="parent_id parameter")
    post_permissions: groupgroups_post_permissions_enum_param | None = Field(
        None, description="post_permissions parameter"
    )
    post_requires_admin_approval: bool | None = Field(
        None, description="post_requires_admin_approval parameter"
    )
    privacy: str | None = Field(None, description="privacy parameter")
    ref: str | None = Field(None, description="ref parameter")


class GroupGetLiveVideosParams(BaseModel):
    """Parameters for Group.get_live_videos()."""

    model_config = ConfigDict(extra="forbid")
    broadcast_status: list[grouplive_videos_broadcast_status_enum_param] | None = Field(
        None, description="broadcast_status parameter"
    )
    source: grouplive_videos_source_enum_param | None = Field(None, description="source parameter")


class GroupCreateLiveVideoParams(BaseModel):
    """Parameters for Group.create_live_video()."""

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
    projection: grouplive_videos_projection_enum_param | None = Field(
        None, description="projection parameter"
    )
    published: bool | None = Field(None, description="published parameter")
    schedule_custom_profile_image: dict[str, Any] | None = Field(
        None, description="schedule_custom_profile_image parameter"
    )
    spatial_audio_format: grouplive_videos_spatial_audio_format_enum_param | None = Field(
        None, description="spatial_audio_format parameter"
    )
    status: grouplive_videos_status_enum_param | None = Field(None, description="status parameter")
    stereoscopic_mode: grouplive_videos_stereoscopic_mode_enum_param | None = Field(
        None, description="stereoscopic_mode parameter"
    )
    stop_on_delete_stream: bool | None = Field(None, description="stop_on_delete_stream parameter")
    stream_type: grouplive_videos_stream_type_enum_param | None = Field(
        None, description="stream_type parameter"
    )
    title: str | None = Field(None, description="title parameter")


class GroupDeleteMembersParams(BaseModel):
    """Parameters for Group.delete_members()."""

    model_config = ConfigDict(extra="forbid")
    email: str | None = Field(None, description="email parameter")
    member: int | None = Field(None, description="member parameter")


class GroupCreateMemberParams(BaseModel):
    """Parameters for Group.create_member()."""

    model_config = ConfigDict(extra="forbid")
    email: str | None = Field(None, description="email parameter")
    from_: int | None = Field(None, alias="from", description="from parameter")
    member: int | None = Field(None, description="member parameter")
    rate: int | None = Field(None, description="rate parameter")
    source: str | None = Field(None, description="source parameter")


class GroupCreatePhotoParams(BaseModel):
    """Parameters for Group.create_photo()."""

    model_config = ConfigDict(extra="forbid")
    aid: str | None = Field(None, description="aid parameter")
    allow_spherical_photo: bool | None = Field(None, description="allow_spherical_photo parameter")
    alt_text_custom: str | None = Field(None, description="alt_text_custom parameter")
    android_key_hash: str | None = Field(None, description="android_key_hash parameter")
    application_id: str | None = Field(None, description="application_id parameter")
    attempt: int | None = Field(None, description="attempt parameter")
    audience_exp: bool | None = Field(None, description="audience_exp parameter")
    backdated_time: datetime | None = Field(None, description="backdated_time parameter")
    backdated_time_granularity: groupphotos_backdated_time_granularity_enum_param | None = Field(
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
    unpublished_content_type: groupphotos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    url: str | None = Field(None, description="url parameter")
    user_selected_tags: bool | None = Field(None, description="user_selected_tags parameter")
    vault_image_id: str | None = Field(None, description="vault_image_id parameter")


class GroupGetPictureParams(BaseModel):
    """Parameters for Group.get_picture()."""

    model_config = ConfigDict(extra="forbid")
    height: int | None = Field(None, description="height parameter")
    redirect: bool | None = Field(None, description="redirect parameter")
    type: grouppicture_type_enum_param | None = Field(None, description="type parameter")
    width: int | None = Field(None, description="width parameter")


class GroupGetVideosParams(BaseModel):
    """Parameters for Group.get_videos()."""

    model_config = ConfigDict(extra="forbid")
    type: groupvideos_type_enum_param | None = Field(None, description="type parameter")


class GroupCreateVideoParams(BaseModel):
    """Parameters for Group.create_video()."""

    model_config = ConfigDict(extra="forbid")
    application_id: str | None = Field(None, description="application_id parameter")
    asked_fun_fact_prompt_id: int | None = Field(
        None, description="asked_fun_fact_prompt_id parameter"
    )
    audio_story_wave_animation_handle: str | None = Field(
        None, description="audio_story_wave_animation_handle parameter"
    )
    composer_entry_picker: str | None = Field(None, description="composer_entry_picker parameter")
    composer_entry_point: str | None = Field(None, description="composer_entry_point parameter")
    composer_entry_time: int | None = Field(None, description="composer_entry_time parameter")
    composer_session_events_log: str | None = Field(
        None, description="composer_session_events_log parameter"
    )
    composer_session_id: str | None = Field(None, description="composer_session_id parameter")
    composer_source_surface: str | None = Field(
        None, description="composer_source_surface parameter"
    )
    composer_type: str | None = Field(None, description="composer_type parameter")
    container_type: groupvideos_container_type_enum_param | None = Field(
        None, description="container_type parameter"
    )
    content_category: groupvideos_content_category_enum_param | None = Field(
        None, description="content_category parameter"
    )
    creative_tools: str | None = Field(None, description="creative_tools parameter")
    description: str | None = Field(None, description="description parameter")
    embeddable: bool | None = Field(None, description="embeddable parameter")
    end_offset: int | None = Field(None, description="end_offset parameter")
    fbuploader_video_file_chunk: str | None = Field(
        None, description="fbuploader_video_file_chunk parameter"
    )
    file_size: int | None = Field(None, description="file_size parameter")
    file_url: str | None = Field(None, description="file_url parameter")
    fisheye_video_cropped: bool | None = Field(None, description="fisheye_video_cropped parameter")
    formatting: groupvideos_formatting_enum_param | None = Field(
        None, description="formatting parameter"
    )
    fov: int | None = Field(None, description="fov parameter")
    front_z_rotation: float | None = Field(None, description="front_z_rotation parameter")
    fun_fact_prompt_id: str | None = Field(None, description="fun_fact_prompt_id parameter")
    fun_fact_toastee_id: int | None = Field(None, description="fun_fact_toastee_id parameter")
    guide: list[list[int]] | None = Field(None, description="guide parameter")
    guide_enabled: bool | None = Field(None, description="guide_enabled parameter")
    initial_heading: int | None = Field(None, description="initial_heading parameter")
    initial_pitch: int | None = Field(None, description="initial_pitch parameter")
    instant_game_entry_point_data: str | None = Field(
        None, description="instant_game_entry_point_data parameter"
    )
    is_boost_intended: bool | None = Field(None, description="is_boost_intended parameter")
    is_explicit_share: bool | None = Field(None, description="is_explicit_share parameter")
    is_group_linking_post: bool | None = Field(None, description="is_group_linking_post parameter")
    is_partnership_ad: bool | None = Field(None, description="is_partnership_ad parameter")
    is_voice_clip: bool | None = Field(None, description="is_voice_clip parameter")
    location_source_id: str | None = Field(None, description="location_source_id parameter")
    manual_privacy: bool | None = Field(None, description="manual_privacy parameter")
    og_action_type_id: str | None = Field(None, description="og_action_type_id parameter")
    og_icon_id: str | None = Field(None, description="og_icon_id parameter")
    og_object_id: str | None = Field(None, description="og_object_id parameter")
    og_phrase: str | None = Field(None, description="og_phrase parameter")
    og_suggestion_mechanism: str | None = Field(
        None, description="og_suggestion_mechanism parameter"
    )
    original_fov: int | None = Field(None, description="original_fov parameter")
    original_projection_type: groupvideos_original_projection_type_enum_param | None = Field(
        None, description="original_projection_type parameter"
    )
    partnership_ad_ad_code: str | None = Field(None, description="partnership_ad_ad_code parameter")
    publish_event_id: int | None = Field(None, description="publish_event_id parameter")
    published: bool | None = Field(None, description="published parameter")
    referenced_sticker_id: str | None = Field(None, description="referenced_sticker_id parameter")
    replace_video_id: str | None = Field(None, description="replace_video_id parameter")
    scheduled_publish_time: int | None = Field(None, description="scheduled_publish_time parameter")
    slideshow_spec: dict[str, Any] | None = Field(None, description="slideshow_spec parameter")
    source: str | None = Field(None, description="source parameter")
    source_instagram_media_id: str | None = Field(
        None, description="source_instagram_media_id parameter"
    )
    spherical: bool | None = Field(None, description="spherical parameter")
    start_offset: int | None = Field(None, description="start_offset parameter")
    swap_mode: groupvideos_swap_mode_enum_param | None = Field(
        None, description="swap_mode parameter"
    )
    text_format_metadata: str | None = Field(None, description="text_format_metadata parameter")
    thumb: dict[str, Any] | None = Field(None, description="thumb parameter")
    time_since_original_post: int | None = Field(
        None, description="time_since_original_post parameter"
    )
    title: str | None = Field(None, description="title parameter")
    transcode_setting_properties: str | None = Field(
        None, description="transcode_setting_properties parameter"
    )
    unpublished_content_type: groupvideos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    upload_phase: groupvideos_upload_phase_enum_param | None = Field(
        None, description="upload_phase parameter"
    )
    upload_session_id: str | None = Field(None, description="upload_session_id parameter")
    upload_setting_properties: str | None = Field(
        None, description="upload_setting_properties parameter"
    )
    video_file_chunk: str | None = Field(None, description="video_file_chunk parameter")
    video_id_original: str | None = Field(None, description="video_id_original parameter")
    video_start_time_ms: int | None = Field(None, description="video_start_time_ms parameter")
    waterfall_id: str | None = Field(None, description="waterfall_id parameter")
