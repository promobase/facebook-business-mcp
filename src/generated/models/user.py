"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .agerange import AgeRangeFields
    from .avatarprofilepicture import AvatarProfilePictureFields
    from .currency import CurrencyFields
    from .educationexperience import EducationExperienceFields
    from .experience import ExperienceFields
    from .group import GroupFields
    from .page import PageFields
    from .paymentpricepoints import PaymentPricepointsFields
    from .usercoverphoto import UserCoverPhotoFields
    from .videouploadlimits import VideoUploadLimitsFields


class userphotos_type_enum_param(str, Enum):
    """userphotos_type_enum_param enum values."""

    tagged = "tagged"
    uploaded = "uploaded"


class uservideos_swap_mode_enum_param(str, Enum):
    """uservideos_swap_mode_enum_param enum values."""

    replace = "replace"


class userphotos_unpublished_content_type_enum_param(str, Enum):
    """userphotos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class uservideos_unpublished_content_type_enum_param(str, Enum):
    """uservideos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class userconversations_platform_enum_param(str, Enum):
    """userconversations_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class userfeed_target_surface_enum_param(str, Enum):
    """userfeed_target_surface_enum_param enum values."""

    STORY = "STORY"
    TIMELINE = "TIMELINE"


class userfeed_place_attachment_setting_enum_param(str, Enum):
    """userfeed_place_attachment_setting_enum_param enum values."""

    VALUE_1 = "1"
    VALUE_2 = "2"


class userpermissions_status_enum_param(str, Enum):
    """userpermissions_status_enum_param enum values."""

    declined = "declined"
    expired = "expired"
    granted = "granted"


class uservideos_original_projection_type_enum_param(str, Enum):
    """uservideos_original_projection_type_enum_param enum values."""

    cubemap = "cubemap"
    equirectangular = "equirectangular"
    half_equirectangular = "half_equirectangular"


class usernotifications_type_enum_param(str, Enum):
    """usernotifications_type_enum_param enum values."""

    content_update = "content_update"
    generic = "generic"


class uservideos_type_enum_param(str, Enum):
    """uservideos_type_enum_param enum values."""

    TAGGED = "TAGGED"
    UPLOADED = "UPLOADED"


class userfeed_backdated_time_granularity_enum_param(str, Enum):
    """userfeed_backdated_time_granularity_enum_param enum values."""

    day = "day"
    hour = "hour"
    min = "min"
    month = "month"
    none = "none"
    year = "year"


class userfeed_posting_to_redspace_enum_param(str, Enum):
    """userfeed_posting_to_redspace_enum_param enum values."""

    disabled = "disabled"
    enabled = "enabled"


class userlive_videos_projection_enum_param(str, Enum):
    """userlive_videos_projection_enum_param enum values."""

    CUBEMAP = "CUBEMAP"
    EQUIRECTANGULAR = "EQUIRECTANGULAR"
    HALF_EQUIRECTANGULAR = "HALF_EQUIRECTANGULAR"


class uservideos_content_category_enum_param(str, Enum):
    """uservideos_content_category_enum_param enum values."""

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


class uservideos_upload_phase_enum_param(str, Enum):
    """uservideos_upload_phase_enum_param enum values."""

    cancel = "cancel"
    finish = "finish"
    start = "start"
    transfer = "transfer"


class usernotifications_filtering_enum_param(str, Enum):
    """usernotifications_filtering_enum_param enum values."""

    ema = "ema"
    groups = "groups"
    groups_social = "groups_social"


class userlive_videos_status_enum_param(str, Enum):
    """userlive_videos_status_enum_param enum values."""

    LIVE_NOW = "LIVE_NOW"
    SCHEDULED_CANCELED = "SCHEDULED_CANCELED"
    SCHEDULED_LIVE = "SCHEDULED_LIVE"
    SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"


class userfeed_formatting_enum_param(str, Enum):
    """userfeed_formatting_enum_param enum values."""

    MARKDOWN = "MARKDOWN"
    PLAINTEXT = "PLAINTEXT"


class userlive_videos_stream_type_enum_param(str, Enum):
    """userlive_videos_stream_type_enum_param enum values."""

    AMBIENT = "AMBIENT"
    REGULAR = "REGULAR"


class userlive_videos_broadcast_status_enum_param(str, Enum):
    """userlive_videos_broadcast_status_enum_param enum values."""

    LIVE = "LIVE"
    LIVE_STOPPED = "LIVE_STOPPED"
    PROCESSING = "PROCESSING"
    SCHEDULED_CANCELED = "SCHEDULED_CANCELED"
    SCHEDULED_EXPIRED = "SCHEDULED_EXPIRED"
    SCHEDULED_LIVE = "SCHEDULED_LIVE"
    SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"
    VOD = "VOD"


class userevents_type_enum_param(str, Enum):
    """userevents_type_enum_param enum values."""

    attending = "attending"
    created = "created"
    declined = "declined"
    maybe = "maybe"
    not_replied = "not_replied"


class userlive_videos_source_enum_param(str, Enum):
    """userlive_videos_source_enum_param enum values."""

    owner = "owner"
    target = "target"


class userbusinesses_survey_business_type_enum_param(str, Enum):
    """userbusinesses_survey_business_type_enum_param enum values."""

    ADVERTISER = "ADVERTISER"
    AGENCY = "AGENCY"
    APP_DEVELOPER = "APP_DEVELOPER"
    PUBLISHER = "PUBLISHER"


class userlive_videos_stereoscopic_mode_enum_param(str, Enum):
    """userlive_videos_stereoscopic_mode_enum_param enum values."""

    LEFT_RIGHT = "LEFT_RIGHT"
    MONO = "MONO"
    TOP_BOTTOM = "TOP_BOTTOM"


class uservideos_formatting_enum_param(str, Enum):
    """uservideos_formatting_enum_param enum values."""

    MARKDOWN = "MARKDOWN"
    PLAINTEXT = "PLAINTEXT"


class userphotos_backdated_time_granularity_enum_param(str, Enum):
    """userphotos_backdated_time_granularity_enum_param enum values."""

    day = "day"
    hour = "hour"
    min = "min"
    month = "month"
    none = "none"
    year = "year"


class userlive_videos_spatial_audio_format_enum_param(str, Enum):
    """userlive_videos_spatial_audio_format_enum_param enum values."""

    ambiX_4 = "ambiX_4"


class uservideos_container_type_enum_param(str, Enum):
    """uservideos_container_type_enum_param enum values."""

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


class userad_studies_type_enum_param(str, Enum):
    """userad_studies_type_enum_param enum values."""

    BACKEND_AB_TESTING = "BACKEND_AB_TESTING"
    CONTINUOUS_LIFT_CONFIG = "CONTINUOUS_LIFT_CONFIG"
    GEO_LIFT = "GEO_LIFT"
    LIFT = "LIFT"
    SPLIT_TEST = "SPLIT_TEST"


class userfeed_post_surfaces_blacklist_enum_param(str, Enum):
    """userfeed_post_surfaces_blacklist_enum_param enum values."""

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class userfeed_unpublished_content_type_enum_param(str, Enum):
    """userfeed_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class userbusinesses_vertical_enum_param(str, Enum):
    """userbusinesses_vertical_enum_param enum values."""

    ADVERTISING = "ADVERTISING"
    AUTOMOTIVE = "AUTOMOTIVE"
    CONSUMER_PACKAGED_GOODS = "CONSUMER_PACKAGED_GOODS"
    ECOMMERCE = "ECOMMERCE"
    EDUCATION = "EDUCATION"
    ENERGY_AND_UTILITIES = "ENERGY_AND_UTILITIES"
    ENTERTAINMENT_AND_MEDIA = "ENTERTAINMENT_AND_MEDIA"
    FINANCIAL_SERVICES = "FINANCIAL_SERVICES"
    GAMING = "GAMING"
    GOVERNMENT_AND_POLITICS = "GOVERNMENT_AND_POLITICS"
    HEALTH = "HEALTH"
    LUXURY = "LUXURY"
    MARKETING = "MARKETING"
    NON_PROFIT = "NON_PROFIT"
    NOT_SET = "NOT_SET"
    ORGANIZATIONS_AND_ASSOCIATIONS = "ORGANIZATIONS_AND_ASSOCIATIONS"
    OTHER = "OTHER"
    PROFESSIONAL_SERVICES = "PROFESSIONAL_SERVICES"
    RESTAURANT = "RESTAURANT"
    RETAIL = "RETAIL"
    TECHNOLOGY = "TECHNOLOGY"
    TELECOM = "TELECOM"
    TRAVEL = "TRAVEL"


class userpicture_type_enum_param(str, Enum):
    """userpicture_type_enum_param enum values."""

    album = "album"
    large = "large"
    normal = "normal"
    small = "small"
    square = "square"


class userbusinesses_timezone_id_enum_param(str, Enum):
    """userbusinesses_timezone_id_enum_param enum values."""

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_57 = "57"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_68 = "68"
    VALUE_69 = "69"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_76 = "76"
    VALUE_77 = "77"
    VALUE_78 = "78"
    VALUE_79 = "79"
    VALUE_80 = "80"
    VALUE_81 = "81"
    VALUE_82 = "82"
    VALUE_83 = "83"
    VALUE_84 = "84"
    VALUE_85 = "85"
    VALUE_86 = "86"
    VALUE_87 = "87"
    VALUE_88 = "88"
    VALUE_89 = "89"
    VALUE_90 = "90"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_98 = "98"
    VALUE_99 = "99"
    VALUE_100 = "100"
    VALUE_101 = "101"
    VALUE_102 = "102"
    VALUE_103 = "103"
    VALUE_104 = "104"
    VALUE_105 = "105"
    VALUE_106 = "106"
    VALUE_107 = "107"
    VALUE_108 = "108"
    VALUE_109 = "109"
    VALUE_110 = "110"
    VALUE_111 = "111"
    VALUE_112 = "112"
    VALUE_113 = "113"
    VALUE_114 = "114"
    VALUE_115 = "115"
    VALUE_116 = "116"
    VALUE_117 = "117"
    VALUE_118 = "118"
    VALUE_119 = "119"
    VALUE_120 = "120"
    VALUE_121 = "121"
    VALUE_122 = "122"
    VALUE_123 = "123"
    VALUE_124 = "124"
    VALUE_125 = "125"
    VALUE_126 = "126"
    VALUE_127 = "127"
    VALUE_128 = "128"
    VALUE_129 = "129"
    VALUE_130 = "130"
    VALUE_131 = "131"
    VALUE_132 = "132"
    VALUE_133 = "133"
    VALUE_134 = "134"
    VALUE_135 = "135"
    VALUE_136 = "136"
    VALUE_137 = "137"
    VALUE_138 = "138"
    VALUE_139 = "139"
    VALUE_140 = "140"
    VALUE_141 = "141"
    VALUE_142 = "142"
    VALUE_143 = "143"
    VALUE_144 = "144"
    VALUE_145 = "145"
    VALUE_146 = "146"
    VALUE_147 = "147"
    VALUE_148 = "148"
    VALUE_149 = "149"
    VALUE_150 = "150"
    VALUE_151 = "151"
    VALUE_152 = "152"
    VALUE_153 = "153"
    VALUE_154 = "154"
    VALUE_155 = "155"
    VALUE_156 = "156"
    VALUE_157 = "157"
    VALUE_158 = "158"
    VALUE_159 = "159"
    VALUE_160 = "160"
    VALUE_161 = "161"
    VALUE_162 = "162"
    VALUE_163 = "163"
    VALUE_164 = "164"
    VALUE_165 = "165"
    VALUE_166 = "166"
    VALUE_167 = "167"
    VALUE_168 = "168"
    VALUE_169 = "169"
    VALUE_170 = "170"
    VALUE_171 = "171"
    VALUE_172 = "172"
    VALUE_173 = "173"
    VALUE_174 = "174"
    VALUE_175 = "175"
    VALUE_176 = "176"
    VALUE_177 = "177"
    VALUE_178 = "178"
    VALUE_179 = "179"
    VALUE_180 = "180"
    VALUE_181 = "181"
    VALUE_182 = "182"
    VALUE_183 = "183"
    VALUE_184 = "184"
    VALUE_185 = "185"
    VALUE_186 = "186"
    VALUE_187 = "187"
    VALUE_188 = "188"
    VALUE_189 = "189"
    VALUE_190 = "190"
    VALUE_191 = "191"
    VALUE_192 = "192"
    VALUE_193 = "193"
    VALUE_194 = "194"
    VALUE_195 = "195"
    VALUE_196 = "196"
    VALUE_197 = "197"
    VALUE_198 = "198"
    VALUE_199 = "199"
    VALUE_200 = "200"
    VALUE_201 = "201"
    VALUE_202 = "202"
    VALUE_203 = "203"
    VALUE_204 = "204"
    VALUE_205 = "205"
    VALUE_206 = "206"
    VALUE_207 = "207"
    VALUE_208 = "208"
    VALUE_209 = "209"
    VALUE_210 = "210"
    VALUE_211 = "211"
    VALUE_212 = "212"
    VALUE_213 = "213"
    VALUE_214 = "214"
    VALUE_215 = "215"
    VALUE_216 = "216"
    VALUE_217 = "217"
    VALUE_218 = "218"
    VALUE_219 = "219"
    VALUE_220 = "220"
    VALUE_221 = "221"
    VALUE_222 = "222"
    VALUE_223 = "223"
    VALUE_224 = "224"
    VALUE_225 = "225"
    VALUE_226 = "226"
    VALUE_227 = "227"
    VALUE_228 = "228"
    VALUE_229 = "229"
    VALUE_230 = "230"
    VALUE_231 = "231"
    VALUE_232 = "232"
    VALUE_233 = "233"
    VALUE_234 = "234"
    VALUE_235 = "235"
    VALUE_236 = "236"
    VALUE_237 = "237"
    VALUE_238 = "238"
    VALUE_239 = "239"
    VALUE_240 = "240"
    VALUE_241 = "241"
    VALUE_242 = "242"
    VALUE_243 = "243"
    VALUE_244 = "244"
    VALUE_245 = "245"
    VALUE_246 = "246"
    VALUE_247 = "247"
    VALUE_248 = "248"
    VALUE_249 = "249"
    VALUE_250 = "250"
    VALUE_251 = "251"
    VALUE_252 = "252"
    VALUE_253 = "253"
    VALUE_254 = "254"
    VALUE_255 = "255"
    VALUE_256 = "256"
    VALUE_257 = "257"
    VALUE_258 = "258"
    VALUE_259 = "259"
    VALUE_260 = "260"
    VALUE_261 = "261"
    VALUE_262 = "262"
    VALUE_263 = "263"
    VALUE_264 = "264"
    VALUE_265 = "265"
    VALUE_266 = "266"
    VALUE_267 = "267"
    VALUE_268 = "268"
    VALUE_269 = "269"
    VALUE_270 = "270"
    VALUE_271 = "271"
    VALUE_272 = "272"
    VALUE_273 = "273"
    VALUE_274 = "274"
    VALUE_275 = "275"
    VALUE_276 = "276"
    VALUE_277 = "277"
    VALUE_278 = "278"
    VALUE_279 = "279"
    VALUE_280 = "280"
    VALUE_281 = "281"
    VALUE_282 = "282"
    VALUE_283 = "283"
    VALUE_284 = "284"
    VALUE_285 = "285"
    VALUE_286 = "286"
    VALUE_287 = "287"
    VALUE_288 = "288"
    VALUE_289 = "289"
    VALUE_290 = "290"
    VALUE_291 = "291"
    VALUE_292 = "292"
    VALUE_293 = "293"
    VALUE_294 = "294"
    VALUE_295 = "295"
    VALUE_296 = "296"
    VALUE_297 = "297"
    VALUE_298 = "298"
    VALUE_299 = "299"
    VALUE_300 = "300"
    VALUE_301 = "301"
    VALUE_302 = "302"
    VALUE_303 = "303"
    VALUE_304 = "304"
    VALUE_305 = "305"
    VALUE_306 = "306"
    VALUE_307 = "307"
    VALUE_308 = "308"
    VALUE_309 = "309"
    VALUE_310 = "310"
    VALUE_311 = "311"
    VALUE_312 = "312"
    VALUE_313 = "313"
    VALUE_314 = "314"
    VALUE_315 = "315"
    VALUE_316 = "316"
    VALUE_317 = "317"
    VALUE_318 = "318"
    VALUE_319 = "319"
    VALUE_320 = "320"
    VALUE_321 = "321"
    VALUE_322 = "322"
    VALUE_323 = "323"
    VALUE_324 = "324"
    VALUE_325 = "325"
    VALUE_326 = "326"
    VALUE_327 = "327"
    VALUE_328 = "328"
    VALUE_329 = "329"
    VALUE_330 = "330"
    VALUE_331 = "331"
    VALUE_332 = "332"
    VALUE_333 = "333"
    VALUE_334 = "334"
    VALUE_335 = "335"
    VALUE_336 = "336"
    VALUE_337 = "337"
    VALUE_338 = "338"
    VALUE_339 = "339"
    VALUE_340 = "340"
    VALUE_341 = "341"
    VALUE_342 = "342"
    VALUE_343 = "343"
    VALUE_344 = "344"
    VALUE_345 = "345"
    VALUE_346 = "346"
    VALUE_347 = "347"
    VALUE_348 = "348"
    VALUE_349 = "349"
    VALUE_350 = "350"
    VALUE_351 = "351"
    VALUE_352 = "352"
    VALUE_353 = "353"
    VALUE_354 = "354"
    VALUE_355 = "355"
    VALUE_356 = "356"
    VALUE_357 = "357"
    VALUE_358 = "358"
    VALUE_359 = "359"
    VALUE_360 = "360"
    VALUE_361 = "361"
    VALUE_362 = "362"
    VALUE_363 = "363"
    VALUE_364 = "364"
    VALUE_365 = "365"
    VALUE_366 = "366"
    VALUE_367 = "367"
    VALUE_368 = "368"
    VALUE_369 = "369"
    VALUE_370 = "370"
    VALUE_371 = "371"
    VALUE_372 = "372"
    VALUE_373 = "373"
    VALUE_374 = "374"
    VALUE_375 = "375"
    VALUE_376 = "376"
    VALUE_377 = "377"
    VALUE_378 = "378"
    VALUE_379 = "379"
    VALUE_380 = "380"
    VALUE_381 = "381"
    VALUE_382 = "382"
    VALUE_383 = "383"
    VALUE_384 = "384"
    VALUE_385 = "385"
    VALUE_386 = "386"
    VALUE_387 = "387"
    VALUE_388 = "388"
    VALUE_389 = "389"
    VALUE_390 = "390"
    VALUE_391 = "391"
    VALUE_392 = "392"
    VALUE_393 = "393"
    VALUE_394 = "394"
    VALUE_395 = "395"
    VALUE_396 = "396"
    VALUE_397 = "397"
    VALUE_398 = "398"
    VALUE_399 = "399"
    VALUE_400 = "400"
    VALUE_401 = "401"
    VALUE_402 = "402"
    VALUE_403 = "403"
    VALUE_404 = "404"
    VALUE_405 = "405"
    VALUE_406 = "406"
    VALUE_407 = "407"
    VALUE_408 = "408"
    VALUE_409 = "409"
    VALUE_410 = "410"
    VALUE_411 = "411"
    VALUE_412 = "412"
    VALUE_413 = "413"
    VALUE_414 = "414"
    VALUE_415 = "415"
    VALUE_416 = "416"
    VALUE_417 = "417"
    VALUE_418 = "418"
    VALUE_419 = "419"
    VALUE_420 = "420"
    VALUE_421 = "421"
    VALUE_422 = "422"
    VALUE_423 = "423"
    VALUE_424 = "424"
    VALUE_425 = "425"
    VALUE_426 = "426"
    VALUE_427 = "427"
    VALUE_428 = "428"
    VALUE_429 = "429"
    VALUE_430 = "430"
    VALUE_431 = "431"
    VALUE_432 = "432"
    VALUE_433 = "433"
    VALUE_434 = "434"
    VALUE_435 = "435"
    VALUE_436 = "436"
    VALUE_437 = "437"
    VALUE_438 = "438"
    VALUE_439 = "439"
    VALUE_440 = "440"
    VALUE_441 = "441"
    VALUE_442 = "442"
    VALUE_443 = "443"
    VALUE_444 = "444"
    VALUE_445 = "445"
    VALUE_446 = "446"
    VALUE_447 = "447"
    VALUE_448 = "448"
    VALUE_449 = "449"
    VALUE_450 = "450"
    VALUE_451 = "451"
    VALUE_452 = "452"
    VALUE_453 = "453"
    VALUE_454 = "454"
    VALUE_455 = "455"
    VALUE_456 = "456"
    VALUE_457 = "457"
    VALUE_458 = "458"
    VALUE_459 = "459"
    VALUE_460 = "460"
    VALUE_461 = "461"
    VALUE_462 = "462"
    VALUE_463 = "463"
    VALUE_464 = "464"
    VALUE_465 = "465"
    VALUE_466 = "466"
    VALUE_467 = "467"
    VALUE_468 = "468"
    VALUE_469 = "469"
    VALUE_470 = "470"
    VALUE_471 = "471"
    VALUE_472 = "472"
    VALUE_473 = "473"
    VALUE_474 = "474"
    VALUE_475 = "475"
    VALUE_476 = "476"
    VALUE_477 = "477"
    VALUE_478 = "478"
    VALUE_479 = "479"
    VALUE_480 = "480"


class userfundraisers_fundraiser_type_enum_param(str, Enum):
    """userfundraisers_fundraiser_type_enum_param enum values."""

    person_for_charity = "person_for_charity"


# Field literal type
UserField = Literal[
    "about",
    "age_range",
    "avatar_2d_profile_picture",
    "birthday",
    "client_business_id",
    "community",
    "cover",
    "currency",
    "education",
    "email",
    "favorite_athletes",
    "favorite_teams",
    "first_name",
    "gender",
    "hometown",
    "id",
    "id_for_avatars",
    "inspirational_people",
    "install_type",
    "installed",
    "is_guest_user",
    "is_work_account",
    "languages",
    "last_name",
    "link",
    "local_news_megaphone_dismiss_status",
    "local_news_subscription_status",
    "locale",
    "location",
    "meeting_for",
    "middle_name",
    "name",
    "name_format",
    "payment_pricepoints",
    "political",
    "profile_pic",
    "quotes",
    "relationship_status",
    "religion",
    "shared_login_upgrade_required_by",
    "short_name",
    "significant_other",
    "sports",
    "supports_donate_button_in_live_video",
    "third_party_id",
    "timezone",
    "token_for_business",
    "updated_time",
    "verified",
    "video_upload_limits",
    "website",
]


class UserFields(BaseModel):
    """Pydantic model for User fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    about: str = Field(None, alias="about")
    age_range: AgeRangeFields = Field(None, alias="age_range")
    avatar_2d_profile_picture: AvatarProfilePictureFields = Field(
        None, alias="avatar_2d_profile_picture"
    )
    birthday: str = Field(None, alias="birthday")
    client_business_id: str = Field(None, alias="client_business_id")
    community: GroupFields = Field(None, alias="community")
    cover: UserCoverPhotoFields = Field(None, alias="cover")
    currency: CurrencyFields = Field(None, alias="currency")
    education: list[EducationExperienceFields] = Field(None, alias="education")
    email: str = Field(None, alias="email")
    favorite_athletes: list[ExperienceFields] = Field(None, alias="favorite_athletes")
    favorite_teams: list[ExperienceFields] = Field(None, alias="favorite_teams")
    first_name: str = Field(None, alias="first_name")
    gender: str = Field(None, alias="gender")
    hometown: PageFields = Field(None, alias="hometown")
    id: str = Field(None, alias="id")
    id_for_avatars: str = Field(None, alias="id_for_avatars")
    inspirational_people: list[ExperienceFields] = Field(None, alias="inspirational_people")
    install_type: str = Field(None, alias="install_type")
    installed: bool = Field(None, alias="installed")
    is_guest_user: bool = Field(None, alias="is_guest_user")
    is_work_account: bool = Field(None, alias="is_work_account")
    languages: list[ExperienceFields] = Field(None, alias="languages")
    last_name: str = Field(None, alias="last_name")
    link: str = Field(None, alias="link")
    local_news_megaphone_dismiss_status: bool = Field(
        None, alias="local_news_megaphone_dismiss_status"
    )
    local_news_subscription_status: bool = Field(None, alias="local_news_subscription_status")
    locale: str = Field(None, alias="locale")
    location: PageFields = Field(None, alias="location")
    meeting_for: list[str] = Field(None, alias="meeting_for")
    middle_name: str = Field(None, alias="middle_name")
    name: str = Field(None, alias="name")
    name_format: str = Field(None, alias="name_format")
    payment_pricepoints: PaymentPricepointsFields = Field(None, alias="payment_pricepoints")
    political: str = Field(None, alias="political")
    profile_pic: str = Field(None, alias="profile_pic")
    quotes: str = Field(None, alias="quotes")
    relationship_status: str = Field(None, alias="relationship_status")
    religion: str = Field(None, alias="religion")
    shared_login_upgrade_required_by: datetime = Field(
        None, alias="shared_login_upgrade_required_by"
    )
    short_name: str = Field(None, alias="short_name")
    significant_other: UserFields = Field(None, alias="significant_other")
    sports: list[ExperienceFields] = Field(None, alias="sports")
    supports_donate_button_in_live_video: bool = Field(
        None, alias="supports_donate_button_in_live_video"
    )
    third_party_id: str = Field(None, alias="third_party_id")
    timezone: float = Field(None, alias="timezone")
    token_for_business: str = Field(None, alias="token_for_business")
    updated_time: datetime = Field(None, alias="updated_time")
    verified: bool = Field(None, alias="verified")
    video_upload_limits: VideoUploadLimitsFields = Field(None, alias="video_upload_limits")
    website: str = Field(None, alias="website")


class UserCreateAccessTokenParams(BaseModel):
    """Parameters for User.create_access_token()."""

    model_config = ConfigDict(extra="forbid")
    business_app: str | None = Field(None, description="business_app parameter")
    page_id: str | None = Field(None, description="page_id parameter")
    scope: list[str] | None = Field(None, description="scope parameter")
    set_token_expires_in_60_days: bool | None = Field(
        None, description="set_token_expires_in_60_days parameter"
    )


class UserGetAccountsParams(BaseModel):
    """Parameters for User.get_accounts()."""

    model_config = ConfigDict(extra="forbid")
    ad_id: str | None = Field(None, description="ad_id parameter")
    is_place: bool | None = Field(None, description="is_place parameter")
    is_promotable: bool | None = Field(None, description="is_promotable parameter")


class UserCreateAccountParams(BaseModel):
    """Parameters for User.create_account()."""

    model_config = ConfigDict(extra="forbid")
    about: str | None = Field(None, description="about parameter")
    address: str | None = Field(None, description="address parameter")
    category: int | None = Field(None, description="category parameter")
    category_enum: str | None = Field(None, description="category_enum parameter")
    category_list: list[str] | None = Field(None, description="category_list parameter")
    city_id: str | None = Field(None, description="city_id parameter")
    coordinates: dict[str, Any] | None = Field(None, description="coordinates parameter")
    cover_photo: dict[str, Any] | None = Field(None, description="cover_photo parameter")
    description: str | None = Field(None, description="description parameter")
    ignore_coordinate_warnings: bool | None = Field(
        None, description="ignore_coordinate_warnings parameter"
    )
    location: dict[str, Any] | None = Field(None, description="location parameter")
    name: str | None = Field(None, description="name parameter")
    phone: str | None = Field(None, description="phone parameter")
    picture: str | None = Field(None, description="picture parameter")
    website: str | None = Field(None, description="website parameter")
    zip: str | None = Field(None, description="zip parameter")


class UserCreateAdStudieParams(BaseModel):
    """Parameters for User.create_ad_studie()."""

    model_config = ConfigDict(extra="forbid")
    cells: list[dict[str, Any]] | None = Field(None, description="cells parameter")
    client_business: str | None = Field(None, description="client_business parameter")
    confidence_level: float | None = Field(None, description="confidence_level parameter")
    cooldown_start_time: int | None = Field(None, description="cooldown_start_time parameter")
    description: str | None = Field(None, description="description parameter")
    end_time: int | None = Field(None, description="end_time parameter")
    name: str | None = Field(None, description="name parameter")
    objectives: list[dict[str, Any]] | None = Field(None, description="objectives parameter")
    observation_end_time: int | None = Field(None, description="observation_end_time parameter")
    start_time: int | None = Field(None, description="start_time parameter")
    type: userad_studies_type_enum_param | None = Field(None, description="type parameter")
    viewers: list[int] | None = Field(None, description="viewers parameter")


class UserCreateApplicationParams(BaseModel):
    """Parameters for User.create_application()."""

    model_config = ConfigDict(extra="forbid")
    business_app: int | None = Field(None, description="business_app parameter")


class UserGetAssignedBusinessAssetGroupsParams(BaseModel):
    """Parameters for User.get_assigned_business_asset_groups()."""

    model_config = ConfigDict(extra="forbid")
    contained_asset_id: str | None = Field(None, description="contained_asset_id parameter")


class UserGetAssignedPagesParams(BaseModel):
    """Parameters for User.get_assigned_pages()."""

    model_config = ConfigDict(extra="forbid")
    pages: list[int] | None = Field(None, description="pages parameter")


class UserDeleteBusinessesParams(BaseModel):
    """Parameters for User.delete_businesses()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class UserCreateBusinesseParams(BaseModel):
    """Parameters for User.create_businesse()."""

    model_config = ConfigDict(extra="forbid")
    child_business_external_id: str | None = Field(
        None, description="child_business_external_id parameter"
    )
    email: str | None = Field(None, description="email parameter")
    name: str | None = Field(None, description="name parameter")
    primary_page: str | None = Field(None, description="primary_page parameter")
    sales_rep_email: str | None = Field(None, description="sales_rep_email parameter")
    survey_business_type: userbusinesses_survey_business_type_enum_param | None = Field(
        None, description="survey_business_type parameter"
    )
    survey_num_assets: int | None = Field(None, description="survey_num_assets parameter")
    survey_num_people: int | None = Field(None, description="survey_num_people parameter")
    timezone_id: userbusinesses_timezone_id_enum_param | None = Field(
        None, description="timezone_id parameter"
    )
    vertical: userbusinesses_vertical_enum_param | None = Field(
        None, description="vertical parameter"
    )


class UserGetConversationsParams(BaseModel):
    """Parameters for User.get_conversations()."""

    model_config = ConfigDict(extra="forbid")
    folder: str | None = Field(None, description="folder parameter")
    platform: userconversations_platform_enum_param | None = Field(
        None, description="platform parameter"
    )
    tags: list[str] | None = Field(None, description="tags parameter")
    user_id: str | None = Field(None, description="user_id parameter")


class UserGetEventsParams(BaseModel):
    """Parameters for User.get_events()."""

    model_config = ConfigDict(extra="forbid")
    include_canceled: bool | None = Field(None, description="include_canceled parameter")
    type: userevents_type_enum_param | None = Field(None, description="type parameter")


class UserGetFeedParams(BaseModel):
    """Parameters for User.get_feed()."""

    model_config = ConfigDict(extra="forbid")
    include_hidden: bool | None = Field(None, description="include_hidden parameter")
    q: str | None = Field(None, description="q parameter")
    show_expired: bool | None = Field(None, description="show_expired parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")
    with_: str | None = Field(None, alias="with", description="with parameter")


class UserCreateFeedParams(BaseModel):
    """Parameters for User.create_feed()."""

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
    backdated_time_granularity: userfeed_backdated_time_granularity_enum_param | None = Field(
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
    formatting: userfeed_formatting_enum_param | None = Field(
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
    place_attachment_setting: userfeed_place_attachment_setting_enum_param | None = Field(
        None, description="place_attachment_setting parameter"
    )
    place_list: str | None = Field(None, description="place_list parameter")
    place_list_data: dict[str, Any] | None = Field(None, description="place_list_data parameter")
    post_surfaces_blacklist: list[userfeed_post_surfaces_blacklist_enum_param] | None = Field(
        None, description="post_surfaces_blacklist parameter"
    )
    posting_to_redspace: userfeed_posting_to_redspace_enum_param | None = Field(
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
    target_surface: userfeed_target_surface_enum_param | None = Field(
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
    unpublished_content_type: userfeed_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    user_selected_tags: bool | None = Field(None, description="user_selected_tags parameter")
    video_start_time_ms: int | None = Field(None, description="video_start_time_ms parameter")
    viewer_coordinates: dict[str, Any] | None = Field(
        None, description="viewer_coordinates parameter"
    )
    width: int | None = Field(None, description="width parameter")


class UserGetFriendsParams(BaseModel):
    """Parameters for User.get_friends()."""

    model_config = ConfigDict(extra="forbid")
    uid: int | None = Field(None, description="uid parameter")


class UserCreateFundraiserParams(BaseModel):
    """Parameters for User.create_fundraiser()."""

    model_config = ConfigDict(extra="forbid")
    charity_id: str | None = Field(None, description="charity_id parameter")
    cover_photo: dict[str, Any] | None = Field(None, description="cover_photo parameter")
    currency: str | None = Field(None, description="currency parameter")
    description: str | None = Field(None, description="description parameter")
    end_time: datetime | None = Field(None, description="end_time parameter")
    external_event_name: str | None = Field(None, description="external_event_name parameter")
    external_event_start_time: datetime | None = Field(
        None, description="external_event_start_time parameter"
    )
    external_event_uri: str | None = Field(None, description="external_event_uri parameter")
    external_fundraiser_uri: str | None = Field(
        None, description="external_fundraiser_uri parameter"
    )
    external_id: str | None = Field(None, description="external_id parameter")
    fundraiser_type: userfundraisers_fundraiser_type_enum_param | None = Field(
        None, description="fundraiser_type parameter"
    )
    goal_amount: int | None = Field(None, description="goal_amount parameter")
    name: str | None = Field(None, description="name parameter")
    page_id: str | None = Field(None, description="page_id parameter")


class UserGetGroupsParams(BaseModel):
    """Parameters for User.get_groups()."""

    model_config = ConfigDict(extra="forbid")
    admin_only: bool | None = Field(None, description="admin_only parameter")
    parent: str | None = Field(None, description="parent parameter")


class UserGetIdsForAppsParams(BaseModel):
    """Parameters for User.get_ids_for_apps()."""

    model_config = ConfigDict(extra="forbid")
    app: int | None = Field(None, description="app parameter")


class UserGetIdsForBusinessParams(BaseModel):
    """Parameters for User.get_ids_for_business()."""

    model_config = ConfigDict(extra="forbid")
    app: int | None = Field(None, description="app parameter")


class UserGetIdsForPagesParams(BaseModel):
    """Parameters for User.get_ids_for_pages()."""

    model_config = ConfigDict(extra="forbid")
    page: int | None = Field(None, description="page parameter")


class UserGetLikesParams(BaseModel):
    """Parameters for User.get_likes()."""

    model_config = ConfigDict(extra="forbid")
    target_id: str | None = Field(None, description="target_id parameter")


class UserGetLiveVideosParams(BaseModel):
    """Parameters for User.get_live_videos()."""

    model_config = ConfigDict(extra="forbid")
    broadcast_status: list[userlive_videos_broadcast_status_enum_param] | None = Field(
        None, description="broadcast_status parameter"
    )
    source: userlive_videos_source_enum_param | None = Field(None, description="source parameter")


class UserCreateLiveVideoParams(BaseModel):
    """Parameters for User.create_live_video()."""

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
    projection: userlive_videos_projection_enum_param | None = Field(
        None, description="projection parameter"
    )
    published: bool | None = Field(None, description="published parameter")
    schedule_custom_profile_image: dict[str, Any] | None = Field(
        None, description="schedule_custom_profile_image parameter"
    )
    spatial_audio_format: userlive_videos_spatial_audio_format_enum_param | None = Field(
        None, description="spatial_audio_format parameter"
    )
    status: userlive_videos_status_enum_param | None = Field(None, description="status parameter")
    stereoscopic_mode: userlive_videos_stereoscopic_mode_enum_param | None = Field(
        None, description="stereoscopic_mode parameter"
    )
    stop_on_delete_stream: bool | None = Field(None, description="stop_on_delete_stream parameter")
    stream_type: userlive_videos_stream_type_enum_param | None = Field(
        None, description="stream_type parameter"
    )
    title: str | None = Field(None, description="title parameter")


class UserCreateMessengerKidsAccountsUnreadBadgeParams(BaseModel):
    """Parameters for User.create_messenger_kids_accounts_unread_badge()."""

    model_config = ConfigDict(extra="forbid")
    proxied_app_id: int | None = Field(None, description="proxied_app_id parameter")


class UserGetMusicParams(BaseModel):
    """Parameters for User.get_music()."""

    model_config = ConfigDict(extra="forbid")
    target_id: str | None = Field(None, description="target_id parameter")


class UserCreateNotificationParams(BaseModel):
    """Parameters for User.create_notification()."""

    model_config = ConfigDict(extra="forbid")
    bot_message_payload_elements: str | None = Field(
        None, description="bot_message_payload_elements parameter"
    )
    filtering: list[usernotifications_filtering_enum_param] | None = Field(
        None, description="filtering parameter"
    )
    href: dict[str, Any] | None = Field(None, description="href parameter")
    label: str | None = Field(None, description="label parameter")
    message: dict[str, Any] | None = Field(None, description="message parameter")
    notif_ids: list[str] | None = Field(None, description="notif_ids parameter")
    payload: str | None = Field(None, description="payload parameter")
    read: bool | None = Field(None, description="read parameter")
    ref: str | None = Field(None, description="ref parameter")
    schedule_interval: int | None = Field(None, description="schedule_interval parameter")
    seen: bool | None = Field(None, description="seen parameter")
    template: dict[str, Any] | None = Field(None, description="template parameter")
    type: usernotifications_type_enum_param | None = Field(None, description="type parameter")


class UserDeletePermissionsParams(BaseModel):
    """Parameters for User.delete_permissions()."""

    model_config = ConfigDict(extra="forbid")
    permission: str | None = Field(None, description="permission parameter")


class UserGetPermissionsParams(BaseModel):
    """Parameters for User.get_permissions()."""

    model_config = ConfigDict(extra="forbid")
    permission: str | None = Field(None, description="permission parameter")
    status: userpermissions_status_enum_param | None = Field(None, description="status parameter")


class UserGetPhotosParams(BaseModel):
    """Parameters for User.get_photos()."""

    model_config = ConfigDict(extra="forbid")
    type: userphotos_type_enum_param | None = Field(None, description="type parameter")


class UserCreatePhotoParams(BaseModel):
    """Parameters for User.create_photo()."""

    model_config = ConfigDict(extra="forbid")
    aid: str | None = Field(None, description="aid parameter")
    allow_spherical_photo: bool | None = Field(None, description="allow_spherical_photo parameter")
    alt_text_custom: str | None = Field(None, description="alt_text_custom parameter")
    android_key_hash: str | None = Field(None, description="android_key_hash parameter")
    application_id: str | None = Field(None, description="application_id parameter")
    attempt: int | None = Field(None, description="attempt parameter")
    audience_exp: bool | None = Field(None, description="audience_exp parameter")
    backdated_time: datetime | None = Field(None, description="backdated_time parameter")
    backdated_time_granularity: userphotos_backdated_time_granularity_enum_param | None = Field(
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
    scheduled_publish_time: int | None = Field(None, description="scheduled_publish_time parameter")
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
    unpublished_content_type: userphotos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    url: str | None = Field(None, description="url parameter")
    user_selected_tags: bool | None = Field(None, description="user_selected_tags parameter")
    vault_image_id: str | None = Field(None, description="vault_image_id parameter")


class UserGetPictureParams(BaseModel):
    """Parameters for User.get_picture()."""

    model_config = ConfigDict(extra="forbid")
    height: int | None = Field(None, description="height parameter")
    redirect: bool | None = Field(None, description="redirect parameter")
    type: userpicture_type_enum_param | None = Field(None, description="type parameter")
    width: int | None = Field(None, description="width parameter")


class UserGetPostsParams(BaseModel):
    """Parameters for User.get_posts()."""

    model_config = ConfigDict(extra="forbid")
    include_hidden: bool | None = Field(None, description="include_hidden parameter")
    q: str | None = Field(None, description="q parameter")
    show_expired: bool | None = Field(None, description="show_expired parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")
    with_: str | None = Field(None, alias="with", description="with parameter")


class UserGetRichMediaDocumentsParams(BaseModel):
    """Parameters for User.get_rich_media_documents()."""

    model_config = ConfigDict(extra="forbid")
    query: str | None = Field(None, description="query parameter")


class UserCreateStagingResourceParams(BaseModel):
    """Parameters for User.create_staging_resource()."""

    model_config = ConfigDict(extra="forbid")
    file: dict[str, Any] | None = Field(None, description="file parameter")


class UserGetVideosParams(BaseModel):
    """Parameters for User.get_videos()."""

    model_config = ConfigDict(extra="forbid")
    type: uservideos_type_enum_param | None = Field(None, description="type parameter")


class UserCreateVideoParams(BaseModel):
    """Parameters for User.create_video()."""

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
    container_type: uservideos_container_type_enum_param | None = Field(
        None, description="container_type parameter"
    )
    content_category: uservideos_content_category_enum_param | None = Field(
        None, description="content_category parameter"
    )
    creative_tools: str | None = Field(None, description="creative_tools parameter")
    description: str | None = Field(None, description="description parameter")
    direct_share_status: int | None = Field(None, description="direct_share_status parameter")
    embeddable: bool | None = Field(None, description="embeddable parameter")
    end_offset: int | None = Field(None, description="end_offset parameter")
    fbuploader_video_file_chunk: str | None = Field(
        None, description="fbuploader_video_file_chunk parameter"
    )
    file_size: int | None = Field(None, description="file_size parameter")
    file_url: str | None = Field(None, description="file_url parameter")
    fisheye_video_cropped: bool | None = Field(None, description="fisheye_video_cropped parameter")
    formatting: uservideos_formatting_enum_param | None = Field(
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
    no_story: bool | None = Field(None, description="no_story parameter")
    og_action_type_id: str | None = Field(None, description="og_action_type_id parameter")
    og_icon_id: str | None = Field(None, description="og_icon_id parameter")
    og_object_id: str | None = Field(None, description="og_object_id parameter")
    og_phrase: str | None = Field(None, description="og_phrase parameter")
    og_suggestion_mechanism: str | None = Field(
        None, description="og_suggestion_mechanism parameter"
    )
    original_fov: int | None = Field(None, description="original_fov parameter")
    original_projection_type: uservideos_original_projection_type_enum_param | None = Field(
        None, description="original_projection_type parameter"
    )
    partnership_ad_ad_code: str | None = Field(None, description="partnership_ad_ad_code parameter")
    privacy: str | None = Field(None, description="privacy parameter")
    publish_event_id: int | None = Field(None, description="publish_event_id parameter")
    referenced_sticker_id: str | None = Field(None, description="referenced_sticker_id parameter")
    replace_video_id: str | None = Field(None, description="replace_video_id parameter")
    slideshow_spec: dict[str, Any] | None = Field(None, description="slideshow_spec parameter")
    source: str | None = Field(None, description="source parameter")
    source_instagram_media_id: str | None = Field(
        None, description="source_instagram_media_id parameter"
    )
    spherical: bool | None = Field(None, description="spherical parameter")
    sponsor_id: str | None = Field(None, description="sponsor_id parameter")
    start_offset: int | None = Field(None, description="start_offset parameter")
    swap_mode: uservideos_swap_mode_enum_param | None = Field(
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
    unpublished_content_type: uservideos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    upload_phase: uservideos_upload_phase_enum_param | None = Field(
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
