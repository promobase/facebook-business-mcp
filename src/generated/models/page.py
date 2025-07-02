"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adset import AdSetFields
    from .advideo import AdVideoFields
    from .business import BusinessFields
    from .coverphoto import CoverPhotoFields
    from .engagement import EngagementFields
    from .hasleadaccess import HasLeadAccessFields
    from .iguser import IGUserFields
    from .location import LocationFields
    from .mailingaddress import MailingAddressFields
    from .messagingfeaturestatus import MessagingFeatureStatusFields
    from .pagecategory import PageCategoryFields
    from .pageparking import PageParkingFields
    from .pagepaymentoptions import PagePaymentOptionsFields
    from .pagerestaurantservices import PageRestaurantServicesFields
    from .pagerestaurantspecialties import PageRestaurantSpecialtiesFields
    from .pagestartinfo import PageStartInfoFields
    from .shop import ShopFields
    from .targeting import TargetingFields
    from .user import UserFields
    from .voipinfo import VoipInfoFields


class pageimage_copyrights_geo_ownership_enum_param(str, Enum):
    """pageimage_copyrights_geo_ownership_enum_param enum values."""

    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TP = "TP"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    XK = "XK"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


class pagevideo_reels_video_state_enum_param(str, Enum):
    """pagevideo_reels_video_state_enum_param enum values."""

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    SCHEDULED = "SCHEDULED"


class pagecustom_user_settings_params_enum_param(str, Enum):
    """pagecustom_user_settings_params_enum_param enum values."""

    PERSISTENT_MENU = "PERSISTENT_MENU"


class pagelive_videos_source_enum_param(str, Enum):
    """pagelive_videos_source_enum_param enum values."""

    owner = "owner"
    target = "target"


class pagestories_status_enum_param(str, Enum):
    """pagestories_status_enum_param enum values."""

    ARCHIVED = "ARCHIVED"
    PUBLISHED = "PUBLISHED"


class pagevideos_formatting_enum_param(str, Enum):
    """pagevideos_formatting_enum_param enum values."""

    MARKDOWN = "MARKDOWN"
    PLAINTEXT = "PLAINTEXT"


class pagemedia_fingerprints_fingerprint_content_type_enum_param(str, Enum):
    """pagemedia_fingerprints_fingerprint_content_type_enum_param enum values."""

    AM_SONGTRACK = "AM_SONGTRACK"
    EPISODE = "EPISODE"
    MOVIE = "MOVIE"
    OTHER = "OTHER"
    SONGTRACK = "SONGTRACK"


class pagenotification_messages_dev_support_developer_action_enum_param(str, Enum):
    """pagenotification_messages_dev_support_developer_action_enum_param enum values."""

    ENABLE_FOLLOWUP_MESSAGE = "ENABLE_FOLLOWUP_MESSAGE"


class pagemessage_templates_status_enum_param(str, Enum):
    """pagemessage_templates_status_enum_param enum values."""

    APPROVED = "APPROVED"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    DISABLED = "DISABLED"
    IN_APPEAL = "IN_APPEAL"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"
    PAUSED = "PAUSED"
    PENDING = "PENDING"
    PENDING_DELETION = "PENDING_DELETION"
    REJECTED = "REJECTED"


class pagemessages_messaging_type_enum_param(str, Enum):
    """pagemessages_messaging_type_enum_param enum values."""

    MESSAGE_TAG = "MESSAGE_TAG"
    RESPONSE = "RESPONSE"
    UPDATE = "UPDATE"
    UTILITY = "UTILITY"


class pagemessenger_profile_fields_enum_param(str, Enum):
    """pagemessenger_profile_fields_enum_param enum values."""

    ACCOUNT_LINKING_URL = "ACCOUNT_LINKING_URL"
    COMMANDS = "COMMANDS"
    DESCRIPTION = "DESCRIPTION"
    GET_STARTED = "GET_STARTED"
    GREETING = "GREETING"
    HOME_URL = "HOME_URL"
    ICE_BREAKERS = "ICE_BREAKERS"
    PERSISTENT_MENU = "PERSISTENT_MENU"
    PLATFORM = "PLATFORM"
    SUBJECT_TO_NEW_EU_PRIVACY_RULES = "SUBJECT_TO_NEW_EU_PRIVACY_RULES"
    TITLE = "TITLE"
    WHITELISTED_DOMAINS = "WHITELISTED_DOMAINS"


class pagelive_videos_projection_enum_param(str, Enum):
    """pagelive_videos_projection_enum_param enum values."""

    CUBEMAP = "CUBEMAP"
    EQUIRECTANGULAR = "EQUIRECTANGULAR"
    HALF_EQUIRECTANGULAR = "HALF_EQUIRECTANGULAR"


class pageab_tests_optimization_goal_enum_param(str, Enum):
    """pageab_tests_optimization_goal_enum_param enum values."""

    AUTO_RESOLVE_TO_CONTROL = "AUTO_RESOLVE_TO_CONTROL"
    AVG_TIME_WATCHED = "AVG_TIME_WATCHED"
    COMMENTS = "COMMENTS"
    IMPRESSIONS = "IMPRESSIONS"
    IMPRESSIONS_UNIQUE = "IMPRESSIONS_UNIQUE"
    LINK_CLICKS = "LINK_CLICKS"
    OTHER = "OTHER"
    REACTIONS = "REACTIONS"
    REELS_PLAYS = "REELS_PLAYS"
    SHARES = "SHARES"
    VIDEO_VIEWS_60S = "VIDEO_VIEWS_60S"


class pagevideos_swap_mode_enum_param(str, Enum):
    """pagevideos_swap_mode_enum_param enum values."""

    replace = "replace"


class pagevideo_copyright_rules_source_enum_param(str, Enum):
    """pagevideo_copyright_rules_source_enum_param enum values."""

    MATCH_SETTINGS_DIALOG = "MATCH_SETTINGS_DIALOG"
    RULES_SELECTOR = "RULES_SELECTOR"
    RULES_TAB = "RULES_TAB"


class pageagencies_permitted_tasks_enum_param(str, Enum):
    """pageagencies_permitted_tasks_enum_param enum values."""

    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    CASHIER_ROLE = "CASHIER_ROLE"
    CREATE_CONTENT = "CREATE_CONTENT"
    GLOBAL_STRUCTURE_MANAGEMENT = "GLOBAL_STRUCTURE_MANAGEMENT"
    MANAGE = "MANAGE"
    MANAGE_JOBS = "MANAGE_JOBS"
    MANAGE_LEADS = "MANAGE_LEADS"
    MESSAGING = "MESSAGING"
    MODERATE = "MODERATE"
    MODERATE_COMMUNITY = "MODERATE_COMMUNITY"
    PAGES_MESSAGING = "PAGES_MESSAGING"
    PAGES_MESSAGING_SUBSCRIPTIONS = "PAGES_MESSAGING_SUBSCRIPTIONS"
    PROFILE_PLUS_ADVERTISE = "PROFILE_PLUS_ADVERTISE"
    PROFILE_PLUS_ANALYZE = "PROFILE_PLUS_ANALYZE"
    PROFILE_PLUS_CREATE_CONTENT = "PROFILE_PLUS_CREATE_CONTENT"
    PROFILE_PLUS_FACEBOOK_ACCESS = "PROFILE_PLUS_FACEBOOK_ACCESS"
    PROFILE_PLUS_FULL_CONTROL = "PROFILE_PLUS_FULL_CONTROL"
    PROFILE_PLUS_MANAGE = "PROFILE_PLUS_MANAGE"
    PROFILE_PLUS_MANAGE_LEADS = "PROFILE_PLUS_MANAGE_LEADS"
    PROFILE_PLUS_MESSAGING = "PROFILE_PLUS_MESSAGING"
    PROFILE_PLUS_MODERATE = "PROFILE_PLUS_MODERATE"
    PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY = "PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY"
    PROFILE_PLUS_REVENUE = "PROFILE_PLUS_REVENUE"
    READ_PAGE_MAILBOXES = "READ_PAGE_MAILBOXES"
    VIEW_MONETIZATION_INSIGHTS = "VIEW_MONETIZATION_INSIGHTS"


class pagevideos_container_type_enum_param(str, Enum):
    """pagevideos_container_type_enum_param enum values."""

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


class pagecopyright_manual_claims_match_content_type_enum_param(str, Enum):
    """pagecopyright_manual_claims_match_content_type_enum_param enum values."""

    AUDIO_ONLY = "AUDIO_ONLY"
    VIDEO_AND_AUDIO = "VIDEO_AND_AUDIO"
    VIDEO_ONLY = "VIDEO_ONLY"


class pagephotos_backdated_time_granularity_enum_param(str, Enum):
    """pagephotos_backdated_time_granularity_enum_param enum values."""

    day = "day"
    hour = "hour"
    min = "min"
    month = "month"
    none = "none"
    year = "year"


class pagefeed_unpublished_content_type_enum_param(str, Enum):
    """pagefeed_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class pagemessage_templates_category_enum_param(str, Enum):
    """pagemessage_templates_category_enum_param enum values."""

    UTILITY = "UTILITY"


class pagenlp_configs_model_enum_param(str, Enum):
    """pagenlp_configs_model_enum_param enum values."""

    ARABIC = "ARABIC"
    CHINESE = "CHINESE"
    CROATIAN = "CROATIAN"
    CUSTOM = "CUSTOM"
    DANISH = "DANISH"
    DUTCH = "DUTCH"
    ENGLISH = "ENGLISH"
    FRENCH_STANDARD = "FRENCH_STANDARD"
    GEORGIAN = "GEORGIAN"
    GERMAN_STANDARD = "GERMAN_STANDARD"
    GREEK = "GREEK"
    HEBREW = "HEBREW"
    HUNGARIAN = "HUNGARIAN"
    IRISH = "IRISH"
    ITALIAN_STANDARD = "ITALIAN_STANDARD"
    KOREAN = "KOREAN"
    NORWEGIAN_BOKMAL = "NORWEGIAN_BOKMAL"
    POLISH = "POLISH"
    PORTUGUESE = "PORTUGUESE"
    ROMANIAN = "ROMANIAN"
    SPANISH = "SPANISH"
    SWEDISH = "SWEDISH"
    VIETNAMESE = "VIETNAMESE"


class pagephotos_unpublished_content_type_enum_param(str, Enum):
    """pagephotos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class pagefeed_target_surface_enum_param(str, Enum):
    """pagefeed_target_surface_enum_param enum values."""

    STORY = "STORY"
    TIMELINE = "TIMELINE"


class pagefeed_post_surfaces_blacklist_enum_param(str, Enum):
    """pagefeed_post_surfaces_blacklist_enum_param enum values."""

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class pagevideo_copyrights_content_category_enum_param(str, Enum):
    """pagevideo_copyrights_content_category_enum_param enum values."""

    episode = "episode"
    movie = "movie"
    web = "web"


class pagemessage_attachments_platform_enum_param(str, Enum):
    """pagemessage_attachments_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class pagevideo_stories_upload_phase_enum_param(str, Enum):
    """pagevideo_stories_upload_phase_enum_param enum values."""

    FINISH = "FINISH"
    START = "START"


class pagevideos_content_category_enum_param(str, Enum):
    """pagevideos_content_category_enum_param enum values."""

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


class pagepicture_type_enum_param(str, Enum):
    """pagepicture_type_enum_param enum values."""

    album = "album"
    large = "large"
    normal = "normal"
    small = "small"
    square = "square"


class pagevideo_copyrights_monitoring_type_enum_param(str, Enum):
    """pagevideo_copyrights_monitoring_type_enum_param enum values."""

    AUDIO_ONLY = "AUDIO_ONLY"
    VIDEO_AND_AUDIO = "VIDEO_AND_AUDIO"
    VIDEO_ONLY = "VIDEO_ONLY"


class pagelive_videos_stream_type_enum_param(str, Enum):
    """pagelive_videos_stream_type_enum_param enum values."""

    AMBIENT = "AMBIENT"
    REGULAR = "REGULAR"


class pagefeed_formatting_enum_param(str, Enum):
    """pagefeed_formatting_enum_param enum values."""

    MARKDOWN = "MARKDOWN"
    PLAINTEXT = "PLAINTEXT"


class pagemessages_sender_action_enum_param(str, Enum):
    """pagemessages_sender_action_enum_param enum values."""

    MARK_SEEN = "MARK_SEEN"
    REACT = "REACT"
    TYPING_OFF = "TYPING_OFF"
    TYPING_ON = "TYPING_ON"
    UNREACT = "UNREACT"


class pagethreads_platform_enum_param(str, Enum):
    """pagethreads_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class pagevideos_unpublished_content_type_enum_param(str, Enum):
    """pagevideos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class pagelive_videos_status_enum_param(str, Enum):
    """pagelive_videos_status_enum_param enum values."""

    LIVE_NOW = "LIVE_NOW"
    SCHEDULED_CANCELED = "SCHEDULED_CANCELED"
    SCHEDULED_LIVE = "SCHEDULED_LIVE"
    SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"


class pagepublished_posts_with_enum_param(str, Enum):
    """pagepublished_posts_with_enum_param enum values."""

    LOCATION = "LOCATION"


class pageconversations_platform_enum_param(str, Enum):
    """pageconversations_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class pageinsights_date_preset_enum_param(str, Enum):
    """pageinsights_date_preset_enum_param enum values."""

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


class pagefeed_with_enum_param(str, Enum):
    """pagefeed_with_enum_param enum values."""

    LOCATION = "LOCATION"


class pagecommerce_orders_filters_enum_param(str, Enum):
    """pagecommerce_orders_filters_enum_param enum values."""

    HAS_CANCELLATIONS = "HAS_CANCELLATIONS"
    HAS_FULFILLMENTS = "HAS_FULFILLMENTS"
    HAS_REFUNDS = "HAS_REFUNDS"
    NO_CANCELLATIONS = "NO_CANCELLATIONS"
    NO_REFUNDS = "NO_REFUNDS"
    NO_SHIPMENTS = "NO_SHIPMENTS"


class pagecopyright_manual_claims_action_enum_param(str, Enum):
    """pagecopyright_manual_claims_action_enum_param enum values."""

    BLOCK = "BLOCK"
    CLAIM_AD_EARNINGS = "CLAIM_AD_EARNINGS"
    MANUAL_REVIEW = "MANUAL_REVIEW"
    MONITOR = "MONITOR"
    REQUEST_TAKEDOWN = "REQUEST_TAKEDOWN"


class pageinsights_period_enum_param(str, Enum):
    """pageinsights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class pagemessages_notification_type_enum_param(str, Enum):
    """pagemessages_notification_type_enum_param enum values."""

    NO_PUSH = "NO_PUSH"
    REGULAR = "REGULAR"
    SILENT_PUSH = "SILENT_PUSH"


class pageposts_with_enum_param(str, Enum):
    """pageposts_with_enum_param enum values."""

    LOCATION = "LOCATION"


class pagesecondary_receivers_platform_enum_param(str, Enum):
    """pagesecondary_receivers_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class pagecalls_platform_enum_param(str, Enum):
    """pagecalls_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class pagelive_videos_stereoscopic_mode_enum_param(str, Enum):
    """pagelive_videos_stereoscopic_mode_enum_param enum values."""

    LEFT_RIGHT = "LEFT_RIGHT"
    MONO = "MONO"
    TOP_BOTTOM = "TOP_BOTTOM"


class pagesubscribed_apps_subscribed_fields_enum_param(str, Enum):
    """pagesubscribed_apps_subscribed_fields_enum_param enum values."""

    affiliation = "affiliation"
    attire = "attire"
    awards = "awards"
    bio = "bio"
    birthday = "birthday"
    call_permission_reply = "call_permission_reply"
    calls = "calls"
    category = "category"
    checkins = "checkins"
    company_overview = "company_overview"
    conversations = "conversations"
    culinary_team = "culinary_team"
    current_location = "current_location"
    description = "description"
    email = "email"
    feature_access_list = "feature_access_list"
    feed = "feed"
    founded = "founded"
    general_info = "general_info"
    general_manager = "general_manager"
    group_feed = "group_feed"
    hometown = "hometown"
    hours = "hours"
    inbox_labels = "inbox_labels"
    invalid_topic_placeholder = "invalid_topic_placeholder"
    invoice_access_bank_slip_events = "invoice_access_bank_slip_events"
    invoice_access_invoice_change = "invoice_access_invoice_change"
    invoice_access_invoice_draft_change = "invoice_access_invoice_draft_change"
    invoice_access_onboarding_status_active = "invoice_access_onboarding_status_active"
    leadgen = "leadgen"
    leadgen_fat = "leadgen_fat"
    live_videos = "live_videos"
    local_delivery = "local_delivery"
    location = "location"
    marketing_message_delivery_failed = "marketing_message_delivery_failed"
    mcom_invoice_change = "mcom_invoice_change"
    members = "members"
    mention = "mention"
    merchant_review = "merchant_review"
    message_context = "message_context"
    message_deliveries = "message_deliveries"
    message_echoes = "message_echoes"
    message_edits = "message_edits"
    message_mention = "message_mention"
    message_reactions = "message_reactions"
    message_reads = "message_reads"
    message_template_status_update = "message_template_status_update"
    messages = "messages"
    messaging_account_linking = "messaging_account_linking"
    messaging_appointments = "messaging_appointments"
    messaging_checkout_updates = "messaging_checkout_updates"
    messaging_customer_information = "messaging_customer_information"
    messaging_direct_sends = "messaging_direct_sends"
    messaging_fblogin_account_linking = "messaging_fblogin_account_linking"
    messaging_feedback = "messaging_feedback"
    messaging_game_plays = "messaging_game_plays"
    messaging_handovers = "messaging_handovers"
    messaging_in_thread_lead_form_submit = "messaging_in_thread_lead_form_submit"
    messaging_integrity = "messaging_integrity"
    messaging_optins = "messaging_optins"
    messaging_optouts = "messaging_optouts"
    messaging_payments = "messaging_payments"
    messaging_policy_enforcement = "messaging_policy_enforcement"
    messaging_postbacks = "messaging_postbacks"
    messaging_pre_checkouts = "messaging_pre_checkouts"
    messaging_referrals = "messaging_referrals"
    mission = "mission"
    name = "name"
    page_about_story = "page_about_story"
    page_change_proposal = "page_change_proposal"
    page_upcoming_change = "page_upcoming_change"
    parking = "parking"
    payment_options = "payment_options"
    payment_request_update = "payment_request_update"
    personal_info = "personal_info"
    personal_interests = "personal_interests"
    phone = "phone"
    picture = "picture"
    price_range = "price_range"
    product_review = "product_review"
    products = "products"
    public_transit = "public_transit"
    publisher_subscriptions = "publisher_subscriptions"
    ratings = "ratings"
    registration = "registration"
    response_feedback = "response_feedback"
    send_cart = "send_cart"
    standby = "standby"
    user_action = "user_action"
    video_text_question_responses = "video_text_question_responses"
    videos = "videos"
    website = "website"


class pageevents_time_filter_enum_param(str, Enum):
    """pageevents_time_filter_enum_param enum values."""

    past = "past"
    upcoming = "upcoming"


class pagefeed_backdated_time_granularity_enum_param(str, Enum):
    """pagefeed_backdated_time_granularity_enum_param enum values."""

    day = "day"
    hour = "hour"
    min = "min"
    month = "month"
    none = "none"
    year = "year"


class pagewelcome_message_flows_eligible_platforms_enum_param(str, Enum):
    """pagewelcome_message_flows_eligible_platforms_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"
    WHATSAPP = "WHATSAPP"


class pagecommerce_orders_state_enum_param(str, Enum):
    """pagecommerce_orders_state_enum_param enum values."""

    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    FB_PROCESSING = "FB_PROCESSING"
    IN_PROGRESS = "IN_PROGRESS"


class pagemoderate_conversations_actions_enum_param(str, Enum):
    """pagemoderate_conversations_actions_enum_param enum values."""

    BAN_USER = "BAN_USER"
    BLOCK_USER = "BLOCK_USER"
    MOVE_TO_SPAM = "MOVE_TO_SPAM"
    UNBAN_USER = "UNBAN_USER"
    UNBLOCK_USER = "UNBLOCK_USER"


class pageevents_event_state_filter_enum_param(str, Enum):
    """pageevents_event_state_filter_enum_param enum values."""

    canceled = "canceled"
    draft = "draft"
    published = "published"
    scheduled_draft_for_publication = "scheduled_draft_for_publication"


class pagevideos_type_enum_param(str, Enum):
    """pagevideos_type_enum_param enum values."""

    TAGGED = "TAGGED"
    UPLOADED = "UPLOADED"


class pagevideos_upload_phase_enum_param(str, Enum):
    """pagevideos_upload_phase_enum_param enum values."""

    cancel = "cancel"
    finish = "finish"
    start = "start"
    transfer = "transfer"


class pagevideos_original_projection_type_enum_param(str, Enum):
    """pagevideos_original_projection_type_enum_param enum values."""

    cubemap = "cubemap"
    equirectangular = "equirectangular"
    half_equirectangular = "half_equirectangular"


class pagefeed_posting_to_redspace_enum_param(str, Enum):
    """pagefeed_posting_to_redspace_enum_param enum values."""

    disabled = "disabled"
    enabled = "enabled"


class pagevideo_reels_upload_phase_enum_param(str, Enum):
    """pagevideo_reels_upload_phase_enum_param enum values."""

    FINISH = "FINISH"
    START = "START"


class pageassigned_users_tasks_enum_param(str, Enum):
    """pageassigned_users_tasks_enum_param enum values."""

    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    CASHIER_ROLE = "CASHIER_ROLE"
    CREATE_CONTENT = "CREATE_CONTENT"
    GLOBAL_STRUCTURE_MANAGEMENT = "GLOBAL_STRUCTURE_MANAGEMENT"
    MANAGE = "MANAGE"
    MANAGE_JOBS = "MANAGE_JOBS"
    MANAGE_LEADS = "MANAGE_LEADS"
    MESSAGING = "MESSAGING"
    MODERATE = "MODERATE"
    MODERATE_COMMUNITY = "MODERATE_COMMUNITY"
    PAGES_MESSAGING = "PAGES_MESSAGING"
    PAGES_MESSAGING_SUBSCRIPTIONS = "PAGES_MESSAGING_SUBSCRIPTIONS"
    PROFILE_PLUS_ADVERTISE = "PROFILE_PLUS_ADVERTISE"
    PROFILE_PLUS_ANALYZE = "PROFILE_PLUS_ANALYZE"
    PROFILE_PLUS_CREATE_CONTENT = "PROFILE_PLUS_CREATE_CONTENT"
    PROFILE_PLUS_FACEBOOK_ACCESS = "PROFILE_PLUS_FACEBOOK_ACCESS"
    PROFILE_PLUS_FULL_CONTROL = "PROFILE_PLUS_FULL_CONTROL"
    PROFILE_PLUS_MANAGE = "PROFILE_PLUS_MANAGE"
    PROFILE_PLUS_MANAGE_LEADS = "PROFILE_PLUS_MANAGE_LEADS"
    PROFILE_PLUS_MESSAGING = "PROFILE_PLUS_MESSAGING"
    PROFILE_PLUS_MODERATE = "PROFILE_PLUS_MODERATE"
    PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY = "PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY"
    PROFILE_PLUS_REVENUE = "PROFILE_PLUS_REVENUE"
    READ_PAGE_MAILBOXES = "READ_PAGE_MAILBOXES"
    VIEW_MONETIZATION_INSIGHTS = "VIEW_MONETIZATION_INSIGHTS"


class pagelocations_temporary_status_enum_param(str, Enum):
    """pagelocations_temporary_status_enum_param enum values."""

    DIFFERENTLY_OPEN = "DIFFERENTLY_OPEN"
    NO_DATA = "NO_DATA"
    OPERATING_AS_USUAL = "OPERATING_AS_USUAL"
    TEMPORARILY_CLOSED = "TEMPORARILY_CLOSED"


class pagevisitor_posts_with_enum_param(str, Enum):
    """pagevisitor_posts_with_enum_param enum values."""

    LOCATION = "LOCATION"


class pagelive_videos_broadcast_status_enum_param(str, Enum):
    """pagelive_videos_broadcast_status_enum_param enum values."""

    LIVE = "LIVE"
    LIVE_STOPPED = "LIVE_STOPPED"
    PROCESSING = "PROCESSING"
    SCHEDULED_CANCELED = "SCHEDULED_CANCELED"
    SCHEDULED_EXPIRED = "SCHEDULED_EXPIRED"
    SCHEDULED_LIVE = "SCHEDULED_LIVE"
    SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"
    VOD = "VOD"


class pageleadgen_forms_locale_enum_param(str, Enum):
    """pageleadgen_forms_locale_enum_param enum values."""

    AR_AR = "AR_AR"
    CS_CZ = "CS_CZ"
    DA_DK = "DA_DK"
    DE_DE = "DE_DE"
    EL_GR = "EL_GR"
    EN_GB = "EN_GB"
    EN_US = "EN_US"
    ES_ES = "ES_ES"
    ES_LA = "ES_LA"
    FI_FI = "FI_FI"
    FR_FR = "FR_FR"
    HE_IL = "HE_IL"
    HI_IN = "HI_IN"
    HU_HU = "HU_HU"
    ID_ID = "ID_ID"
    IT_IT = "IT_IT"
    JA_JP = "JA_JP"
    KO_KR = "KO_KR"
    NB_NO = "NB_NO"
    NL_NL = "NL_NL"
    PL_PL = "PL_PL"
    PT_BR = "PT_BR"
    PT_PT = "PT_PT"
    RO_RO = "RO_RO"
    RU_RU = "RU_RU"
    SV_SE = "SV_SE"
    TH_TH = "TH_TH"
    TR_TR = "TR_TR"
    VI_VN = "VI_VN"
    ZH_CN = "ZH_CN"
    ZH_HK = "ZH_HK"
    ZH_TW = "ZH_TW"


class pagemessenger_profile_platform_enum_param(str, Enum):
    """pagemessenger_profile_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class pagecalls_action_enum_param(str, Enum):
    """pagecalls_action_enum_param enum values."""

    ACCEPT = "ACCEPT"
    CONNECT = "CONNECT"
    MEDIA_UPDATE = "MEDIA_UPDATE"
    REJECT = "REJECT"
    TERMINATE = "TERMINATE"


class pagelocations_pickup_options_enum_param(str, Enum):
    """pagelocations_pickup_options_enum_param enum values."""

    CURBSIDE = "CURBSIDE"
    IN_STORE = "IN_STORE"
    OTHER = "OTHER"


class pagemessages_suggestion_action_enum_param(str, Enum):
    """pagemessages_suggestion_action_enum_param enum values."""

    ACCEPT = "ACCEPT"
    DISMISS = "DISMISS"
    IMPRESSION = "IMPRESSION"


class pagelive_videos_spatial_audio_format_enum_param(str, Enum):
    """pagelive_videos_spatial_audio_format_enum_param enum values."""

    ambiX_4 = "ambiX_4"


class pagephotos_type_enum_param(str, Enum):
    """pagephotos_type_enum_param enum values."""

    profile = "profile"
    tagged = "tagged"
    uploaded = "uploaded"


class pagevideo_stories_video_state_enum_param(str, Enum):
    """pagevideo_stories_video_state_enum_param enum values."""

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    SCHEDULED = "SCHEDULED"


class pageevents_type_enum_param(str, Enum):
    """pageevents_type_enum_param enum values."""

    attending = "attending"
    created = "created"
    declined = "declined"
    maybe = "maybe"
    not_replied = "not_replied"


class pagefeed_place_attachment_setting_enum_param(str, Enum):
    """pagefeed_place_attachment_setting_enum_param enum values."""

    VALUE_1 = "1"
    VALUE_2 = "2"


class pagecopyright_manual_claims_action_reason_enum_param(str, Enum):
    """pagecopyright_manual_claims_action_reason_enum_param enum values."""

    ARTICLE_17_PREFLAGGING = "ARTICLE_17_PREFLAGGING"
    ARTIST_OBJECTION = "ARTIST_OBJECTION"
    OBJECTIONABLE_CONTENT = "OBJECTIONABLE_CONTENT"
    PREMIUM_MUSIC_VIDEO = "PREMIUM_MUSIC_VIDEO"
    PRERELEASE_CONTENT = "PRERELEASE_CONTENT"
    PRODUCT_PARAMETERS = "PRODUCT_PARAMETERS"
    RESTRICTED_CONTENT = "RESTRICTED_CONTENT"
    UNAUTHORIZED_COMMERCIAL_USE = "UNAUTHORIZED_COMMERCIAL_USE"


# Field literal type
PageField = Literal[
    "about",
    "access_token",
    "ad_campaign",
    "affiliation",
    "app_id",
    "artists_we_like",
    "attire",
    "available_promo_offer_ids",
    "awards",
    "band_interests",
    "band_members",
    "best_page",
    "bio",
    "birthday",
    "booking_agent",
    "breaking_news_usage",
    "built",
    "business",
    "can_checkin",
    "can_post",
    "category",
    "category_list",
    "checkins",
    "company_overview",
    "connected_instagram_account",
    "connected_page_backed_instagram_account",
    "contact_address",
    "copyright_whitelisted_ig_partners",
    "country_page_likes",
    "cover",
    "culinary_team",
    "current_location",
    "delivery_and_pickup_option_info",
    "description",
    "description_html",
    "differently_open_offerings",
    "directed_by",
    "display_subtext",
    "displayed_message_response_time",
    "does_viewer_have_page_permission_link_ig",
    "emails",
    "engagement",
    "fan_count",
    "featured_video",
    "features",
    "followers_count",
    "food_styles",
    "founded",
    "general_info",
    "general_manager",
    "genre",
    "global_brand_page_name",
    "global_brand_root_id",
    "has_added_app",
    "has_lead_access",
    "has_transitioned_to_new_page_experience",
    "has_whatsapp_business_number",
    "has_whatsapp_number",
    "hometown",
    "hours",
    "id",
    "impressum",
    "influences",
    "instagram_business_account",
    "is_always_open",
    "is_calling_eligible",
    "is_chain",
    "is_community_page",
    "is_eligible_for_branded_content",
    "is_eligible_for_disable_connect_ig_btn_for_non_page_admin_am_web",
    "is_messenger_bot_get_started_enabled",
    "is_messenger_platform_bot",
    "is_owned",
    "is_permanently_closed",
    "is_published",
    "is_unclaimed",
    "is_verified",
    "is_webhooks_subscribed",
    "keywords",
    "leadgen_tos_acceptance_time",
    "leadgen_tos_accepted",
    "leadgen_tos_accepting_user",
    "link",
    "location",
    "members",
    "merchant_id",
    "merchant_review_status",
    "messaging_feature_status",
    "messenger_ads_default_icebreakers",
    "messenger_ads_default_quick_replies",
    "messenger_ads_quick_replies_type",
    "mini_shop_storefront",
    "mission",
    "mpg",
    "name",
    "name_with_location_descriptor",
    "network",
    "new_like_count",
    "offer_eligible",
    "overall_star_rating",
    "owner_business",
    "page_token",
    "parent_page",
    "parking",
    "payment_options",
    "personal_info",
    "personal_interests",
    "pharma_safety_info",
    "phone",
    "pickup_options",
    "place_type",
    "plot_outline",
    "preferred_audience",
    "press_contact",
    "price_range",
    "privacy_info_url",
    "produced_by",
    "products",
    "promotion_eligible",
    "promotion_ineligible_reason",
    "public_transit",
    "rating_count",
    "recipient",
    "record_label",
    "release_date",
    "restaurant_services",
    "restaurant_specialties",
    "schedule",
    "screenplay_by",
    "season",
    "single_line_address",
    "starring",
    "start_info",
    "store_code",
    "store_location_descriptor",
    "store_number",
    "studio",
    "supports_donate_button_in_live_video",
    "talking_about_count",
    "temporary_status",
    "unread_message_count",
    "unread_notif_count",
    "unseen_message_count",
    "user_access_expire_time",
    "username",
    "verification_status",
    "voip_info",
    "website",
    "were_here_count",
    "whatsapp_number",
    "written_by",
]


class PageFields(BaseModel):
    """Pydantic model for Page fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    about: str = Field(None, alias="about")
    access_token: str = Field(None, alias="access_token")
    ad_campaign: AdSetFields = Field(None, alias="ad_campaign")
    affiliation: str = Field(None, alias="affiliation")
    app_id: str = Field(None, alias="app_id")
    artists_we_like: str = Field(None, alias="artists_we_like")
    attire: str = Field(None, alias="attire")
    available_promo_offer_ids: list[dict[str, list[dict[str, str]]]] = Field(
        None, alias="available_promo_offer_ids"
    )
    awards: str = Field(None, alias="awards")
    band_interests: str = Field(None, alias="band_interests")
    band_members: str = Field(None, alias="band_members")
    best_page: PageFields = Field(None, alias="best_page")
    bio: str = Field(None, alias="bio")
    birthday: str = Field(None, alias="birthday")
    booking_agent: str = Field(None, alias="booking_agent")
    breaking_news_usage: dict[str, Any] = Field(None, alias="breaking_news_usage")
    built: str = Field(None, alias="built")
    business: dict[str, Any] = Field(None, alias="business")
    can_checkin: bool = Field(None, alias="can_checkin")
    can_post: bool = Field(None, alias="can_post")
    category: str = Field(None, alias="category")
    category_list: list[PageCategoryFields] = Field(None, alias="category_list")
    checkins: int = Field(None, alias="checkins")
    company_overview: str = Field(None, alias="company_overview")
    connected_instagram_account: IGUserFields = Field(None, alias="connected_instagram_account")
    connected_page_backed_instagram_account: IGUserFields = Field(
        None, alias="connected_page_backed_instagram_account"
    )
    contact_address: MailingAddressFields = Field(None, alias="contact_address")
    copyright_whitelisted_ig_partners: list[str] = Field(
        None, alias="copyright_whitelisted_ig_partners"
    )
    country_page_likes: int = Field(None, alias="country_page_likes")
    cover: CoverPhotoFields = Field(None, alias="cover")
    culinary_team: str = Field(None, alias="culinary_team")
    current_location: str = Field(None, alias="current_location")
    delivery_and_pickup_option_info: list[str] = Field(
        None, alias="delivery_and_pickup_option_info"
    )
    description: str = Field(None, alias="description")
    description_html: str = Field(None, alias="description_html")
    differently_open_offerings: list[dict[str, bool]] = Field(
        None, alias="differently_open_offerings"
    )
    directed_by: str = Field(None, alias="directed_by")
    display_subtext: str = Field(None, alias="display_subtext")
    displayed_message_response_time: str = Field(None, alias="displayed_message_response_time")
    does_viewer_have_page_permission_link_ig: bool = Field(
        None, alias="does_viewer_have_page_permission_link_ig"
    )
    emails: list[str] = Field(None, alias="emails")
    engagement: EngagementFields = Field(None, alias="engagement")
    fan_count: int = Field(None, alias="fan_count")
    featured_video: AdVideoFields = Field(None, alias="featured_video")
    features: str = Field(None, alias="features")
    followers_count: int = Field(None, alias="followers_count")
    food_styles: list[str] = Field(None, alias="food_styles")
    founded: str = Field(None, alias="founded")
    general_info: str = Field(None, alias="general_info")
    general_manager: str = Field(None, alias="general_manager")
    genre: str = Field(None, alias="genre")
    global_brand_page_name: str = Field(None, alias="global_brand_page_name")
    global_brand_root_id: str = Field(None, alias="global_brand_root_id")
    has_added_app: bool = Field(None, alias="has_added_app")
    has_lead_access: HasLeadAccessFields = Field(None, alias="has_lead_access")
    has_transitioned_to_new_page_experience: bool = Field(
        None, alias="has_transitioned_to_new_page_experience"
    )
    has_whatsapp_business_number: bool = Field(None, alias="has_whatsapp_business_number")
    has_whatsapp_number: bool = Field(None, alias="has_whatsapp_number")
    hometown: str = Field(None, alias="hometown")
    hours: dict[str, str] = Field(None, alias="hours")
    id: str = Field(None, alias="id")
    impressum: str = Field(None, alias="impressum")
    influences: str = Field(None, alias="influences")
    instagram_business_account: IGUserFields = Field(None, alias="instagram_business_account")
    is_always_open: bool = Field(None, alias="is_always_open")
    is_calling_eligible: bool = Field(None, alias="is_calling_eligible")
    is_chain: bool = Field(None, alias="is_chain")
    is_community_page: bool = Field(None, alias="is_community_page")
    is_eligible_for_branded_content: bool = Field(None, alias="is_eligible_for_branded_content")
    is_eligible_for_disable_connect_ig_btn_for_non_page_admin_am_web: bool = Field(
        None, alias="is_eligible_for_disable_connect_ig_btn_for_non_page_admin_am_web"
    )
    is_messenger_bot_get_started_enabled: bool = Field(
        None, alias="is_messenger_bot_get_started_enabled"
    )
    is_messenger_platform_bot: bool = Field(None, alias="is_messenger_platform_bot")
    is_owned: bool = Field(None, alias="is_owned")
    is_permanently_closed: bool = Field(None, alias="is_permanently_closed")
    is_published: bool = Field(None, alias="is_published")
    is_unclaimed: bool = Field(None, alias="is_unclaimed")
    is_verified: bool = Field(None, alias="is_verified")
    is_webhooks_subscribed: bool = Field(None, alias="is_webhooks_subscribed")
    keywords: dict[str, Any] = Field(None, alias="keywords")
    leadgen_tos_acceptance_time: datetime = Field(None, alias="leadgen_tos_acceptance_time")
    leadgen_tos_accepted: bool = Field(None, alias="leadgen_tos_accepted")
    leadgen_tos_accepting_user: UserFields = Field(None, alias="leadgen_tos_accepting_user")
    link: str = Field(None, alias="link")
    location: LocationFields = Field(None, alias="location")
    members: str = Field(None, alias="members")
    merchant_id: str = Field(None, alias="merchant_id")
    merchant_review_status: str = Field(None, alias="merchant_review_status")
    messaging_feature_status: MessagingFeatureStatusFields = Field(
        None, alias="messaging_feature_status"
    )
    messenger_ads_default_icebreakers: list[str] = Field(
        None, alias="messenger_ads_default_icebreakers"
    )
    messenger_ads_default_quick_replies: list[str] = Field(
        None, alias="messenger_ads_default_quick_replies"
    )
    messenger_ads_quick_replies_type: str = Field(None, alias="messenger_ads_quick_replies_type")
    mini_shop_storefront: ShopFields = Field(None, alias="mini_shop_storefront")
    mission: str = Field(None, alias="mission")
    mpg: str = Field(None, alias="mpg")
    name: str = Field(None, alias="name")
    name_with_location_descriptor: str = Field(None, alias="name_with_location_descriptor")
    network: str = Field(None, alias="network")
    new_like_count: int = Field(None, alias="new_like_count")
    offer_eligible: bool = Field(None, alias="offer_eligible")
    overall_star_rating: float = Field(None, alias="overall_star_rating")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    page_token: str = Field(None, alias="page_token")
    parent_page: PageFields = Field(None, alias="parent_page")
    parking: PageParkingFields = Field(None, alias="parking")
    payment_options: PagePaymentOptionsFields = Field(None, alias="payment_options")
    personal_info: str = Field(None, alias="personal_info")
    personal_interests: str = Field(None, alias="personal_interests")
    pharma_safety_info: str = Field(None, alias="pharma_safety_info")
    phone: str = Field(None, alias="phone")
    pickup_options: list[str] = Field(None, alias="pickup_options")
    place_type: str = Field(None, alias="place_type")
    plot_outline: str = Field(None, alias="plot_outline")
    preferred_audience: TargetingFields = Field(None, alias="preferred_audience")
    press_contact: str = Field(None, alias="press_contact")
    price_range: str = Field(None, alias="price_range")
    privacy_info_url: str = Field(None, alias="privacy_info_url")
    produced_by: str = Field(None, alias="produced_by")
    products: str = Field(None, alias="products")
    promotion_eligible: bool = Field(None, alias="promotion_eligible")
    promotion_ineligible_reason: str = Field(None, alias="promotion_ineligible_reason")
    public_transit: str = Field(None, alias="public_transit")
    rating_count: int = Field(None, alias="rating_count")
    recipient: str = Field(None, alias="recipient")
    record_label: str = Field(None, alias="record_label")
    release_date: str = Field(None, alias="release_date")
    restaurant_services: PageRestaurantServicesFields = Field(None, alias="restaurant_services")
    restaurant_specialties: PageRestaurantSpecialtiesFields = Field(
        None, alias="restaurant_specialties"
    )
    schedule: str = Field(None, alias="schedule")
    screenplay_by: str = Field(None, alias="screenplay_by")
    season: str = Field(None, alias="season")
    single_line_address: str = Field(None, alias="single_line_address")
    starring: str = Field(None, alias="starring")
    start_info: PageStartInfoFields = Field(None, alias="start_info")
    store_code: str = Field(None, alias="store_code")
    store_location_descriptor: str = Field(None, alias="store_location_descriptor")
    store_number: int = Field(None, alias="store_number")
    studio: str = Field(None, alias="studio")
    supports_donate_button_in_live_video: bool = Field(
        None, alias="supports_donate_button_in_live_video"
    )
    talking_about_count: int = Field(None, alias="talking_about_count")
    temporary_status: str = Field(None, alias="temporary_status")
    unread_message_count: int = Field(None, alias="unread_message_count")
    unread_notif_count: int = Field(None, alias="unread_notif_count")
    unseen_message_count: int = Field(None, alias="unseen_message_count")
    user_access_expire_time: datetime = Field(None, alias="user_access_expire_time")
    username: str = Field(None, alias="username")
    verification_status: str = Field(None, alias="verification_status")
    voip_info: VoipInfoFields = Field(None, alias="voip_info")
    website: str = Field(None, alias="website")
    were_here_count: int = Field(None, alias="were_here_count")
    whatsapp_number: str = Field(None, alias="whatsapp_number")
    written_by: str = Field(None, alias="written_by")


class PageCreateAbTestParams(BaseModel):
    """Parameters for Page.create_ab_test()."""

    model_config = ConfigDict(extra="forbid")
    control_video_id: str | None = Field(None, description="control_video_id parameter")
    description: str | None = Field(None, description="description parameter")
    duration: int | None = Field(None, description="duration parameter")
    experiment_video_ids: list[str] | None = Field(
        None, description="experiment_video_ids parameter"
    )
    name: str | None = Field(None, description="name parameter")
    optimization_goal: pageab_tests_optimization_goal_enum_param | None = Field(
        None, description="optimization_goal parameter"
    )
    scheduled_experiment_timestamp: int | None = Field(
        None, description="scheduled_experiment_timestamp parameter"
    )


class PageCreateAcknowledgeOrderParams(BaseModel):
    """Parameters for Page.create_acknowledge_order()."""

    model_config = ConfigDict(extra="forbid")
    idempotency_key: str | None = Field(None, description="idempotency_key parameter")
    orders: list[dict[str, Any]] | None = Field(None, description="orders parameter")


class PageGetAdsPostsParams(BaseModel):
    """Parameters for Page.get_ads_posts()."""

    model_config = ConfigDict(extra="forbid")
    exclude_dynamic_ads: bool | None = Field(None, description="exclude_dynamic_ads parameter")
    include_inline_create: bool | None = Field(None, description="include_inline_create parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class PageDeleteAgenciesParams(BaseModel):
    """Parameters for Page.delete_agencies()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class PageCreateAgencieParams(BaseModel):
    """Parameters for Page.create_agencie()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")
    permitted_tasks: list[pageagencies_permitted_tasks_enum_param] | None = Field(
        None, description="permitted_tasks parameter"
    )


class PageDeleteAssignedUsersParams(BaseModel):
    """Parameters for Page.delete_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    user: int | None = Field(None, description="user parameter")


class PageGetAssignedUsersParams(BaseModel):
    """Parameters for Page.get_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class PageCreateAssignedUserParams(BaseModel):
    """Parameters for Page.create_assigned_user()."""

    model_config = ConfigDict(extra="forbid")
    tasks: list[pageassigned_users_tasks_enum_param] | None = Field(
        None, description="tasks parameter"
    )
    user: int | None = Field(None, description="user parameter")


class PageDeleteBlockedParams(BaseModel):
    """Parameters for Page.delete_blocked()."""

    model_config = ConfigDict(extra="forbid")
    asid: str | None = Field(None, description="asid parameter")
    psid: int | None = Field(None, description="psid parameter")
    uid: int | None = Field(None, description="uid parameter")
    user: int | None = Field(None, description="user parameter")


class PageGetBlockedParams(BaseModel):
    """Parameters for Page.get_blocked()."""

    model_config = ConfigDict(extra="forbid")
    uid: int | None = Field(None, description="uid parameter")
    user: int | None = Field(None, description="user parameter")


class PageCreateBlockedParams(BaseModel):
    """Parameters for Page.create_blocked()."""

    model_config = ConfigDict(extra="forbid")
    asid: list[str] | None = Field(None, description="asid parameter")
    psid: list[int] | None = Field(None, description="psid parameter")
    uid: list[str] | None = Field(None, description="uid parameter")
    user: list[str] | None = Field(None, description="user parameter")


class PageCreateBusinessDataParams(BaseModel):
    """Parameters for Page.create_business_data()."""

    model_config = ConfigDict(extra="forbid")
    data: list[str] | None = Field(None, description="data parameter")
    partner_agent: str | None = Field(None, description="partner_agent parameter")
    processing_type: str | None = Field(None, description="processing_type parameter")


class PageGetBusinessprojectsParams(BaseModel):
    """Parameters for Page.get_businessprojects()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class PageCreateCallParams(BaseModel):
    """Parameters for Page.create_call()."""

    model_config = ConfigDict(extra="forbid")
    action: pagecalls_action_enum_param | None = Field(None, description="action parameter")
    call_id: str | None = Field(None, description="call_id parameter")
    platform: pagecalls_platform_enum_param | None = Field(None, description="platform parameter")
    session: dict[str, Any] | None = Field(None, description="session parameter")
    to: str | None = Field(None, description="to parameter")


class PageCreateCanvasElementParams(BaseModel):
    """Parameters for Page.create_canvas_element()."""

    model_config = ConfigDict(extra="forbid")
    canvas_button: dict[str, Any] | None = Field(None, description="canvas_button parameter")
    canvas_carousel: dict[str, Any] | None = Field(None, description="canvas_carousel parameter")
    canvas_footer: dict[str, Any] | None = Field(None, description="canvas_footer parameter")
    canvas_header: dict[str, Any] | None = Field(None, description="canvas_header parameter")
    canvas_lead_form: dict[str, Any] | None = Field(None, description="canvas_lead_form parameter")
    canvas_photo: dict[str, Any] | None = Field(None, description="canvas_photo parameter")
    canvas_product_list: dict[str, Any] | None = Field(
        None, description="canvas_product_list parameter"
    )
    canvas_product_set: dict[str, Any] | None = Field(
        None, description="canvas_product_set parameter"
    )
    canvas_store_locator: dict[str, Any] | None = Field(
        None, description="canvas_store_locator parameter"
    )
    canvas_template_video: dict[str, Any] | None = Field(
        None, description="canvas_template_video parameter"
    )
    canvas_text: dict[str, Any] | None = Field(None, description="canvas_text parameter")
    canvas_video: dict[str, Any] | None = Field(None, description="canvas_video parameter")


class PageGetCanvasesParams(BaseModel):
    """Parameters for Page.get_canvases()."""

    model_config = ConfigDict(extra="forbid")
    is_hidden: bool | None = Field(None, description="is_hidden parameter")
    is_published: bool | None = Field(None, description="is_published parameter")


class PageCreateCanvaseParams(BaseModel):
    """Parameters for Page.create_canvase()."""

    model_config = ConfigDict(extra="forbid")
    background_color: str | None = Field(None, description="background_color parameter")
    body_element_ids: list[str] | None = Field(None, description="body_element_ids parameter")
    enable_swipe_to_open: bool | None = Field(None, description="enable_swipe_to_open parameter")
    is_hidden: bool | None = Field(None, description="is_hidden parameter")
    is_published: bool | None = Field(None, description="is_published parameter")
    name: str | None = Field(None, description="name parameter")
    source_template_id: str | None = Field(None, description="source_template_id parameter")


class PageGetCommerceOrdersParams(BaseModel):
    """Parameters for Page.get_commerce_orders()."""

    model_config = ConfigDict(extra="forbid")
    filters: list[pagecommerce_orders_filters_enum_param] | None = Field(
        None, description="filters parameter"
    )
    state: list[pagecommerce_orders_state_enum_param] | None = Field(
        None, description="state parameter"
    )
    updated_after: datetime | None = Field(None, description="updated_after parameter")
    updated_before: datetime | None = Field(None, description="updated_before parameter")


class PageGetCommercePayoutsParams(BaseModel):
    """Parameters for Page.get_commerce_payouts()."""

    model_config = ConfigDict(extra="forbid")
    end_time: datetime | None = Field(None, description="end_time parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")


class PageGetCommerceTransactionsParams(BaseModel):
    """Parameters for Page.get_commerce_transactions()."""

    model_config = ConfigDict(extra="forbid")
    end_time: datetime | None = Field(None, description="end_time parameter")
    payout_reference_id: str | None = Field(None, description="payout_reference_id parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")


class PageGetConversationsParams(BaseModel):
    """Parameters for Page.get_conversations()."""

    model_config = ConfigDict(extra="forbid")
    folder: str | None = Field(None, description="folder parameter")
    platform: pageconversations_platform_enum_param | None = Field(
        None, description="platform parameter"
    )
    tags: list[str] | None = Field(None, description="tags parameter")
    user_id: str | None = Field(None, description="user_id parameter")


class PageCreateCopyrightManualClaimParams(BaseModel):
    """Parameters for Page.create_copyright_manual_claim()."""

    model_config = ConfigDict(extra="forbid")
    action: pagecopyright_manual_claims_action_enum_param | None = Field(
        None, description="action parameter"
    )
    action_reason: pagecopyright_manual_claims_action_reason_enum_param | None = Field(
        None, description="action_reason parameter"
    )
    countries: dict[str, Any] | None = Field(None, description="countries parameter")
    match_content_type: pagecopyright_manual_claims_match_content_type_enum_param | None = Field(
        None, description="match_content_type parameter"
    )
    matched_asset_id: str | None = Field(None, description="matched_asset_id parameter")
    reference_asset_id: str | None = Field(None, description="reference_asset_id parameter")
    selected_segments: list[dict[str, Any]] | None = Field(
        None, description="selected_segments parameter"
    )


class PageCreateCustomLabelParams(BaseModel):
    """Parameters for Page.create_custom_label()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")
    page_label_name: str | None = Field(None, description="page_label_name parameter")


class PageDeleteCustomUserSettingsParams(BaseModel):
    """Parameters for Page.delete_custom_user_settings()."""

    model_config = ConfigDict(extra="forbid")
    params: list[pagecustom_user_settings_params_enum_param] | None = Field(
        None, description="params parameter"
    )
    psid: str | None = Field(None, description="psid parameter")


class PageGetCustomUserSettingsParams(BaseModel):
    """Parameters for Page.get_custom_user_settings()."""

    model_config = ConfigDict(extra="forbid")
    psid: str | None = Field(None, description="psid parameter")


class PageCreateCustomUserSettingParams(BaseModel):
    """Parameters for Page.create_custom_user_setting()."""

    model_config = ConfigDict(extra="forbid")
    persistent_menu: list[dict[str, Any]] | None = Field(
        None, description="persistent_menu parameter"
    )
    psid: str | None = Field(None, description="psid parameter")


class PageCreateDatasetParams(BaseModel):
    """Parameters for Page.create_dataset()."""

    model_config = ConfigDict(extra="forbid")
    dataset_name: str | None = Field(None, description="dataset_name parameter")


class PageGetEventsParams(BaseModel):
    """Parameters for Page.get_events()."""

    model_config = ConfigDict(extra="forbid")
    event_state_filter: list[pageevents_event_state_filter_enum_param] | None = Field(
        None, description="event_state_filter parameter"
    )
    include_canceled: bool | None = Field(None, description="include_canceled parameter")
    time_filter: pageevents_time_filter_enum_param | None = Field(
        None, description="time_filter parameter"
    )
    type: pageevents_type_enum_param | None = Field(None, description="type parameter")


class PageCreateExtendThreadControlParams(BaseModel):
    """Parameters for Page.create_extend_thread_control()."""

    model_config = ConfigDict(extra="forbid")
    duration: int | None = Field(None, description="duration parameter")
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")


class PageGetFeedParams(BaseModel):
    """Parameters for Page.get_feed()."""

    model_config = ConfigDict(extra="forbid")
    include_hidden: bool | None = Field(None, description="include_hidden parameter")
    limit: int | None = Field(None, description="limit parameter")
    show_expired: bool | None = Field(None, description="show_expired parameter")
    with_: pagefeed_with_enum_param | None = Field(None, alias="with", description="with parameter")


class PageCreateFeedParams(BaseModel):
    """Parameters for Page.create_feed()."""

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
    backdated_time_granularity: pagefeed_backdated_time_granularity_enum_param | None = Field(
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
    enforce_link_ownership: bool | None = Field(
        None, description="enforce_link_ownership parameter"
    )
    expanded_height: int | None = Field(None, description="expanded_height parameter")
    expanded_width: int | None = Field(None, description="expanded_width parameter")
    feed_targeting: dict[str, Any] | None = Field(None, description="feed_targeting parameter")
    formatting: pagefeed_formatting_enum_param | None = Field(
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
    place_attachment_setting: pagefeed_place_attachment_setting_enum_param | None = Field(
        None, description="place_attachment_setting parameter"
    )
    place_list: str | None = Field(None, description="place_list parameter")
    place_list_data: dict[str, Any] | None = Field(None, description="place_list_data parameter")
    post_surfaces_blacklist: list[pagefeed_post_surfaces_blacklist_enum_param] | None = Field(
        None, description="post_surfaces_blacklist parameter"
    )
    posting_to_redspace: pagefeed_posting_to_redspace_enum_param | None = Field(
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
    target_surface: pagefeed_target_surface_enum_param | None = Field(
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
    unpublished_content_type: pagefeed_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    user_selected_tags: bool | None = Field(None, description="user_selected_tags parameter")
    video_start_time_ms: int | None = Field(None, description="video_start_time_ms parameter")
    viewer_coordinates: dict[str, Any] | None = Field(
        None, description="viewer_coordinates parameter"
    )
    width: int | None = Field(None, description="width parameter")


class PageCreateImageCopyrightParams(BaseModel):
    """Parameters for Page.create_image_copyright()."""

    model_config = ConfigDict(extra="forbid")
    artist: str | None = Field(None, description="artist parameter")
    attribution_link: str | None = Field(None, description="attribution_link parameter")
    creator: str | None = Field(None, description="creator parameter")
    custom_id: str | None = Field(None, description="custom_id parameter")
    description: str | None = Field(None, description="description parameter")
    filename: str | None = Field(None, description="filename parameter")
    geo_ownership: list[pageimage_copyrights_geo_ownership_enum_param] | None = Field(
        None, description="geo_ownership parameter"
    )
    original_content_creation_date: int | None = Field(
        None, description="original_content_creation_date parameter"
    )
    reference_photo: str | None = Field(None, description="reference_photo parameter")
    title: str | None = Field(None, description="title parameter")


class PageGetInsightsParams(BaseModel):
    """Parameters for Page.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    breakdown: list[dict[str, Any]] | None = Field(None, description="breakdown parameter")
    date_preset: pageinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    metric: list[dict[str, Any]] | None = Field(None, description="metric parameter")
    period: pageinsights_period_enum_param | None = Field(None, description="period parameter")
    show_description_from_api_doc: bool | None = Field(
        None, description="show_description_from_api_doc parameter"
    )
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class PageCreateLeadgenFormParams(BaseModel):
    """Parameters for Page.create_leadgen_form()."""

    model_config = ConfigDict(extra="forbid")
    allow_organic_lead_retrieval: bool | None = Field(
        None, description="allow_organic_lead_retrieval parameter"
    )
    block_display_for_non_targeted_viewer: bool | None = Field(
        None, description="block_display_for_non_targeted_viewer parameter"
    )
    context_card: dict[str, Any] | None = Field(None, description="context_card parameter")
    cover_photo: dict[str, Any] | None = Field(None, description="cover_photo parameter")
    custom_disclaimer: dict[str, Any] | None = Field(
        None, description="custom_disclaimer parameter"
    )
    follow_up_action_url: str | None = Field(None, description="follow_up_action_url parameter")
    is_for_canvas: bool | None = Field(None, description="is_for_canvas parameter")
    is_optimized_for_quality: bool | None = Field(
        None, description="is_optimized_for_quality parameter"
    )
    locale: pageleadgen_forms_locale_enum_param | None = Field(None, description="locale parameter")
    name: str | None = Field(None, description="name parameter")
    privacy_policy: dict[str, Any] | None = Field(None, description="privacy_policy parameter")
    question_page_custom_headline: str | None = Field(
        None, description="question_page_custom_headline parameter"
    )
    questions: list[dict[str, Any]] | None = Field(None, description="questions parameter")
    thank_you_page: dict[str, Any] | None = Field(None, description="thank_you_page parameter")
    tracking_parameters: dict[str, Any] | None = Field(
        None, description="tracking_parameters parameter"
    )
    upload_gated_file: dict[str, Any] | None = Field(
        None, description="upload_gated_file parameter"
    )


class PageGetLikesParams(BaseModel):
    """Parameters for Page.get_likes()."""

    model_config = ConfigDict(extra="forbid")
    target_id: str | None = Field(None, description="target_id parameter")


class PageGetLiveVideosParams(BaseModel):
    """Parameters for Page.get_live_videos()."""

    model_config = ConfigDict(extra="forbid")
    broadcast_status: list[pagelive_videos_broadcast_status_enum_param] | None = Field(
        None, description="broadcast_status parameter"
    )
    source: pagelive_videos_source_enum_param | None = Field(None, description="source parameter")


class PageCreateLiveVideoParams(BaseModel):
    """Parameters for Page.create_live_video()."""

    model_config = ConfigDict(extra="forbid")
    content_tags: list[str] | None = Field(None, description="content_tags parameter")
    crossposting_actions: list[dict[str, Any]] | None = Field(
        None, description="crossposting_actions parameter"
    )
    custom_labels: list[str] | None = Field(None, description="custom_labels parameter")
    description: str | None = Field(None, description="description parameter")
    enable_backup_ingest: bool | None = Field(None, description="enable_backup_ingest parameter")
    encoding_settings: str | None = Field(None, description="encoding_settings parameter")
    event_params: dict[str, Any] | None = Field(None, description="event_params parameter")
    fisheye_video_cropped: bool | None = Field(None, description="fisheye_video_cropped parameter")
    front_z_rotation: float | None = Field(None, description="front_z_rotation parameter")
    game_show: dict[str, Any] | None = Field(None, description="game_show parameter")
    is_audio_only: bool | None = Field(None, description="is_audio_only parameter")
    is_spherical: bool | None = Field(None, description="is_spherical parameter")
    original_fov: int | None = Field(None, description="original_fov parameter")
    privacy: str | None = Field(None, description="privacy parameter")
    projection: pagelive_videos_projection_enum_param | None = Field(
        None, description="projection parameter"
    )
    published: bool | None = Field(None, description="published parameter")
    schedule_custom_profile_image: dict[str, Any] | None = Field(
        None, description="schedule_custom_profile_image parameter"
    )
    spatial_audio_format: pagelive_videos_spatial_audio_format_enum_param | None = Field(
        None, description="spatial_audio_format parameter"
    )
    status: pagelive_videos_status_enum_param | None = Field(None, description="status parameter")
    stereoscopic_mode: pagelive_videos_stereoscopic_mode_enum_param | None = Field(
        None, description="stereoscopic_mode parameter"
    )
    stop_on_delete_stream: bool | None = Field(None, description="stop_on_delete_stream parameter")
    stream_type: pagelive_videos_stream_type_enum_param | None = Field(
        None, description="stream_type parameter"
    )
    targeting: dict[str, Any] | None = Field(None, description="targeting parameter")
    title: str | None = Field(None, description="title parameter")


class PageDeleteLocationsParams(BaseModel):
    """Parameters for Page.delete_locations()."""

    model_config = ConfigDict(extra="forbid")
    location_page_ids: list[str] | None = Field(None, description="location_page_ids parameter")
    store_numbers: list[int] | None = Field(None, description="store_numbers parameter")


class PageCreateLocationParams(BaseModel):
    """Parameters for Page.create_location()."""

    model_config = ConfigDict(extra="forbid")
    always_open: bool | None = Field(None, description="always_open parameter")
    delivery_and_pickup_option_info: list[str] | None = Field(
        None, description="delivery_and_pickup_option_info parameter"
    )
    differently_open_offerings: dict[str, Any] | None = Field(
        None, description="differently_open_offerings parameter"
    )
    hours: dict[str, Any] | None = Field(None, description="hours parameter")
    ignore_warnings: bool | None = Field(None, description="ignore_warnings parameter")
    location: dict[str, Any] | None = Field(None, description="location parameter")
    location_page_id: str | None = Field(None, description="location_page_id parameter")
    old_store_number: int | None = Field(None, description="old_store_number parameter")
    page_username: str | None = Field(None, description="page_username parameter")
    permanently_closed: bool | None = Field(None, description="permanently_closed parameter")
    phone: str | None = Field(None, description="phone parameter")
    pickup_options: list[pagelocations_pickup_options_enum_param] | None = Field(
        None, description="pickup_options parameter"
    )
    place_topics: list[str] | None = Field(None, description="place_topics parameter")
    price_range: str | None = Field(None, description="price_range parameter")
    store_code: str | None = Field(None, description="store_code parameter")
    store_location_descriptor: str | None = Field(
        None, description="store_location_descriptor parameter"
    )
    store_name: str | None = Field(None, description="store_name parameter")
    store_number: int | None = Field(None, description="store_number parameter")
    temporary_status: pagelocations_temporary_status_enum_param | None = Field(
        None, description="temporary_status parameter"
    )
    website: str | None = Field(None, description="website parameter")


class PageGetMediaFingerprintsParams(BaseModel):
    """Parameters for Page.get_media_fingerprints()."""

    model_config = ConfigDict(extra="forbid")
    universal_content_id: str | None = Field(None, description="universal_content_id parameter")


class PageCreateMediaFingerprintParams(BaseModel):
    """Parameters for Page.create_media_fingerprint()."""

    model_config = ConfigDict(extra="forbid")
    fingerprint_content_type: pagemedia_fingerprints_fingerprint_content_type_enum_param | None = (
        Field(None, description="fingerprint_content_type parameter")
    )
    metadata: dict[str, Any] | None = Field(None, description="metadata parameter")
    source: str | None = Field(None, description="source parameter")
    title: str | None = Field(None, description="title parameter")
    universal_content_id: str | None = Field(None, description="universal_content_id parameter")


class PageCreateMessageAttachmentParams(BaseModel):
    """Parameters for Page.create_message_attachment()."""

    model_config = ConfigDict(extra="forbid")
    message: dict[str, Any] | None = Field(None, description="message parameter")
    platform: pagemessage_attachments_platform_enum_param | None = Field(
        None, description="platform parameter"
    )


class PageDeleteMessageTemplatesParams(BaseModel):
    """Parameters for Page.delete_message_templates()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")
    template_id: str | None = Field(None, description="template_id parameter")


class PageGetMessageTemplatesParams(BaseModel):
    """Parameters for Page.get_message_templates()."""

    model_config = ConfigDict(extra="forbid")
    category: list[pagemessage_templates_category_enum_param] | None = Field(
        None, description="category parameter"
    )
    content: str | None = Field(None, description="content parameter")
    language: list[str] | None = Field(None, description="language parameter")
    name: str | None = Field(None, description="name parameter")
    name_or_content: str | None = Field(None, description="name_or_content parameter")
    status: list[pagemessage_templates_status_enum_param] | None = Field(
        None, description="status parameter"
    )


class PageCreateMessageTemplateParams(BaseModel):
    """Parameters for Page.create_message_template()."""

    model_config = ConfigDict(extra="forbid")
    category: pagemessage_templates_category_enum_param | None = Field(
        None, description="category parameter"
    )
    components: list[dict[str, Any]] | None = Field(None, description="components parameter")
    language: str | None = Field(None, description="language parameter")
    library_template_button_inputs: list[dict[str, Any]] | None = Field(
        None, description="library_template_button_inputs parameter"
    )
    library_template_name: str | None = Field(None, description="library_template_name parameter")
    name: str | None = Field(None, description="name parameter")


class PageCreateMessageParams(BaseModel):
    """Parameters for Page.create_message()."""

    model_config = ConfigDict(extra="forbid")
    message: dict[str, Any] | None = Field(None, description="message parameter")
    messaging_type: pagemessages_messaging_type_enum_param | None = Field(
        None, description="messaging_type parameter"
    )
    notification_type: pagemessages_notification_type_enum_param | None = Field(
        None, description="notification_type parameter"
    )
    payload: str | None = Field(None, description="payload parameter")
    persona_id: str | None = Field(None, description="persona_id parameter")
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")
    reply_to: str | None = Field(None, description="reply_to parameter")
    sender_action: pagemessages_sender_action_enum_param | None = Field(
        None, description="sender_action parameter"
    )
    suggestion_action: pagemessages_suggestion_action_enum_param | None = Field(
        None, description="suggestion_action parameter"
    )
    tag: dict[str, Any] | None = Field(None, description="tag parameter")
    thread_control: dict[str, Any] | None = Field(None, description="thread_control parameter")


class PageCreateMessengerCallSettingParams(BaseModel):
    """Parameters for Page.create_messenger_call_setting()."""

    model_config = ConfigDict(extra="forbid")
    audio_enabled: bool | None = Field(None, description="audio_enabled parameter")
    call_hours: dict[str, Any] | None = Field(None, description="call_hours parameter")
    call_routing: dict[str, Any] | None = Field(None, description="call_routing parameter")
    icon_enabled: bool | None = Field(None, description="icon_enabled parameter")


class PageCreateMessengerLeadFormParams(BaseModel):
    """Parameters for Page.create_messenger_lead_form()."""

    model_config = ConfigDict(extra="forbid")
    account_id: int | None = Field(None, description="account_id parameter")
    block_send_api: bool | None = Field(None, description="block_send_api parameter")
    exit_keyphrases: str | None = Field(None, description="exit_keyphrases parameter")
    handover_app_id: int | None = Field(None, description="handover_app_id parameter")
    handover_summary: bool | None = Field(None, description="handover_summary parameter")
    privacy_url: str | None = Field(None, description="privacy_url parameter")
    reminder_text: str | None = Field(None, description="reminder_text parameter")
    step_list: list[dict[str, Any]] | None = Field(None, description="step_list parameter")
    stop_question_message: str | None = Field(None, description="stop_question_message parameter")
    template_name: str | None = Field(None, description="template_name parameter")
    tracking_parameters: dict[str, Any] | None = Field(
        None, description="tracking_parameters parameter"
    )


class PageDeleteMessengerProfileParams(BaseModel):
    """Parameters for Page.delete_messenger_profile()."""

    model_config = ConfigDict(extra="forbid")
    fields: list[pagemessenger_profile_fields_enum_param] | None = Field(
        None, description="fields parameter"
    )
    platform: pagemessenger_profile_platform_enum_param | None = Field(
        None, description="platform parameter"
    )


class PageGetMessengerProfileParams(BaseModel):
    """Parameters for Page.get_messenger_profile()."""

    model_config = ConfigDict(extra="forbid")
    platform: pagemessenger_profile_platform_enum_param | None = Field(
        None, description="platform parameter"
    )


class PageCreateMessengerProfileParams(BaseModel):
    """Parameters for Page.create_messenger_profile()."""

    model_config = ConfigDict(extra="forbid")
    account_linking_url: str | None = Field(None, description="account_linking_url parameter")
    commands: list[dict[str, Any]] | None = Field(None, description="commands parameter")
    description: list[dict[str, Any]] | None = Field(None, description="description parameter")
    get_started: dict[str, Any] | None = Field(None, description="get_started parameter")
    greeting: list[dict[str, Any]] | None = Field(None, description="greeting parameter")
    ice_breakers: list[dict[str, Any]] | None = Field(None, description="ice_breakers parameter")
    persistent_menu: list[dict[str, Any]] | None = Field(
        None, description="persistent_menu parameter"
    )
    platform: pagemessenger_profile_platform_enum_param | None = Field(
        None, description="platform parameter"
    )
    title: list[dict[str, Any]] | None = Field(None, description="title parameter")
    whitelisted_domains: list[str] | None = Field(None, description="whitelisted_domains parameter")


class PageCreateModerateConversationParams(BaseModel):
    """Parameters for Page.create_moderate_conversation()."""

    model_config = ConfigDict(extra="forbid")
    actions: list[pagemoderate_conversations_actions_enum_param] | None = Field(
        None, description="actions parameter"
    )
    user_ids: list[dict[str, Any]] | None = Field(None, description="user_ids parameter")


class PageCreateNlpConfigParams(BaseModel):
    """Parameters for Page.create_nlp_config()."""

    model_config = ConfigDict(extra="forbid")
    api_version: dict[str, Any] | None = Field(None, description="api_version parameter")
    custom_token: str | None = Field(None, description="custom_token parameter")
    model: pagenlp_configs_model_enum_param | None = Field(None, description="model parameter")
    n_best: int | None = Field(None, description="n_best parameter")
    nlp_enabled: bool | None = Field(None, description="nlp_enabled parameter")
    other_language_support: dict[str, Any] | None = Field(
        None, description="other_language_support parameter"
    )
    verbose: bool | None = Field(None, description="verbose parameter")


class PageCreateNotificationMessagesDevSupportParams(BaseModel):
    """Parameters for Page.create_notification_messages_dev_support()."""

    model_config = ConfigDict(extra="forbid")
    developer_action: pagenotification_messages_dev_support_developer_action_enum_param | None = (
        Field(None, description="developer_action parameter")
    )
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")


class PageCreatePageWhatsappNumberVerificationParams(BaseModel):
    """Parameters for Page.create_page_whatsapp_number_verification()."""

    model_config = ConfigDict(extra="forbid")
    verification_code: str | None = Field(None, description="verification_code parameter")
    whatsapp_number: str | None = Field(None, description="whatsapp_number parameter")


class PageCreatePassThreadControlParams(BaseModel):
    """Parameters for Page.create_pass_thread_control()."""

    model_config = ConfigDict(extra="forbid")
    metadata: str | None = Field(None, description="metadata parameter")
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")
    target_app_id: str | None = Field(None, description="target_app_id parameter")


class PageCreatePersonaParams(BaseModel):
    """Parameters for Page.create_persona()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")
    profile_picture_url: str | None = Field(None, description="profile_picture_url parameter")


class PageCreatePhotoStorieParams(BaseModel):
    """Parameters for Page.create_photo_storie()."""

    model_config = ConfigDict(extra="forbid")
    photo_id: str | None = Field(None, description="photo_id parameter")


class PageGetPhotosParams(BaseModel):
    """Parameters for Page.get_photos()."""

    model_config = ConfigDict(extra="forbid")
    biz_tag_id: int | None = Field(None, description="biz_tag_id parameter")
    business_id: str | None = Field(None, description="business_id parameter")
    type: pagephotos_type_enum_param | None = Field(None, description="type parameter")


class PageCreatePhotoParams(BaseModel):
    """Parameters for Page.create_photo()."""

    model_config = ConfigDict(extra="forbid")
    aid: str | None = Field(None, description="aid parameter")
    allow_spherical_photo: bool | None = Field(None, description="allow_spherical_photo parameter")
    alt_text_custom: str | None = Field(None, description="alt_text_custom parameter")
    android_key_hash: str | None = Field(None, description="android_key_hash parameter")
    application_id: str | None = Field(None, description="application_id parameter")
    attempt: int | None = Field(None, description="attempt parameter")
    audience_exp: bool | None = Field(None, description="audience_exp parameter")
    backdated_time: datetime | None = Field(None, description="backdated_time parameter")
    backdated_time_granularity: pagephotos_backdated_time_granularity_enum_param | None = Field(
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
    location_source_id: str | None = Field(None, description="location_source_id parameter")
    manual_privacy: bool | None = Field(None, description="manual_privacy parameter")
    message: str | None = Field(None, description="message parameter")
    name: str | None = Field(None, description="name parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
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
    parent_media_id: int | None = Field(None, description="parent_media_id parameter")
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
    temporary: bool | None = Field(None, description="temporary parameter")
    time_since_original_post: int | None = Field(
        None, description="time_since_original_post parameter"
    )
    uid: int | None = Field(None, description="uid parameter")
    unpublished_content_type: pagephotos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    url: str | None = Field(None, description="url parameter")
    user_selected_tags: bool | None = Field(None, description="user_selected_tags parameter")
    vault_image_id: str | None = Field(None, description="vault_image_id parameter")


class PageGetPictureParams(BaseModel):
    """Parameters for Page.get_picture()."""

    model_config = ConfigDict(extra="forbid")
    height: int | None = Field(None, description="height parameter")
    redirect: bool | None = Field(None, description="redirect parameter")
    type: pagepicture_type_enum_param | None = Field(None, description="type parameter")
    width: int | None = Field(None, description="width parameter")


class PageCreatePictureParams(BaseModel):
    """Parameters for Page.create_picture()."""

    model_config = ConfigDict(extra="forbid")
    android_key_hash: str | None = Field(None, description="android_key_hash parameter")
    burn_media_effect: bool | None = Field(None, description="burn_media_effect parameter")
    caption: str | None = Field(None, description="caption parameter")
    composer_session_id: str | None = Field(None, description="composer_session_id parameter")
    frame_entrypoint: str | None = Field(None, description="frame_entrypoint parameter")
    has_umg: bool | None = Field(None, description="has_umg parameter")
    height: int | None = Field(None, description="height parameter")
    ios_bundle_id: str | None = Field(None, description="ios_bundle_id parameter")
    media_effect_ids: list[int] | None = Field(None, description="media_effect_ids parameter")
    media_effect_source_object_id: int | None = Field(
        None, description="media_effect_source_object_id parameter"
    )
    msqrd_mask_id: str | None = Field(None, description="msqrd_mask_id parameter")
    photo: str | None = Field(None, description="photo parameter")
    picture: str | None = Field(None, description="picture parameter")
    profile_pic_method: str | None = Field(None, description="profile_pic_method parameter")
    profile_pic_source: str | None = Field(None, description="profile_pic_source parameter")
    proxied_app_id: int | None = Field(None, description="proxied_app_id parameter")
    qn: str | None = Field(None, description="qn parameter")
    reuse: bool | None = Field(None, description="reuse parameter")
    scaled_crop_rect: dict[str, Any] | None = Field(None, description="scaled_crop_rect parameter")
    set_profile_photo_shield: str | None = Field(
        None, description="set_profile_photo_shield parameter"
    )
    sticker_id: int | None = Field(None, description="sticker_id parameter")
    sticker_source_object_id: int | None = Field(
        None, description="sticker_source_object_id parameter"
    )
    suppress_stories: bool | None = Field(None, description="suppress_stories parameter")
    width: int | None = Field(None, description="width parameter")
    x: int | None = Field(None, description="x parameter")
    y: int | None = Field(None, description="y parameter")


class PageGetPostsParams(BaseModel):
    """Parameters for Page.get_posts()."""

    model_config = ConfigDict(extra="forbid")
    include_hidden: bool | None = Field(None, description="include_hidden parameter")
    limit: int | None = Field(None, description="limit parameter")
    q: str | None = Field(None, description="q parameter")
    show_expired: bool | None = Field(None, description="show_expired parameter")
    with_: pageposts_with_enum_param | None = Field(
        None, alias="with", description="with parameter"
    )


class PageGetPublishedPostsParams(BaseModel):
    """Parameters for Page.get_published_posts()."""

    model_config = ConfigDict(extra="forbid")
    include_hidden: bool | None = Field(None, description="include_hidden parameter")
    limit: int | None = Field(None, description="limit parameter")
    show_expired: bool | None = Field(None, description="show_expired parameter")
    with_: pagepublished_posts_with_enum_param | None = Field(
        None, alias="with", description="with parameter"
    )


class PageCreateReleaseThreadControlParams(BaseModel):
    """Parameters for Page.create_release_thread_control()."""

    model_config = ConfigDict(extra="forbid")
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")


class PageCreateRequestThreadControlParams(BaseModel):
    """Parameters for Page.create_request_thread_control()."""

    model_config = ConfigDict(extra="forbid")
    metadata: str | None = Field(None, description="metadata parameter")
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")


class PageGetRolesParams(BaseModel):
    """Parameters for Page.get_roles()."""

    model_config = ConfigDict(extra="forbid")
    include_deactivated: bool | None = Field(None, description="include_deactivated parameter")
    uid: int | None = Field(None, description="uid parameter")


class PageGetSecondaryReceiversParams(BaseModel):
    """Parameters for Page.get_secondary_receivers()."""

    model_config = ConfigDict(extra="forbid")
    platform: pagesecondary_receivers_platform_enum_param | None = Field(
        None, description="platform parameter"
    )


class PageCreateSettingParams(BaseModel):
    """Parameters for Page.create_setting()."""

    model_config = ConfigDict(extra="forbid")
    option: dict[str, Any] | None = Field(None, description="option parameter")


class PageGetStoriesParams(BaseModel):
    """Parameters for Page.get_stories()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")
    status: list[pagestories_status_enum_param] | None = Field(None, description="status parameter")
    until: datetime | None = Field(None, description="until parameter")


class PageCreateSubscribedAppParams(BaseModel):
    """Parameters for Page.create_subscribed_app()."""

    model_config = ConfigDict(extra="forbid")
    subscribed_fields: list[pagesubscribed_apps_subscribed_fields_enum_param] | None = Field(
        None, description="subscribed_fields parameter"
    )


class PageGetTabsParams(BaseModel):
    """Parameters for Page.get_tabs()."""

    model_config = ConfigDict(extra="forbid")
    tab: list[str] | None = Field(None, description="tab parameter")


class PageCreateTakeThreadControlParams(BaseModel):
    """Parameters for Page.create_take_thread_control()."""

    model_config = ConfigDict(extra="forbid")
    metadata: str | None = Field(None, description="metadata parameter")
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")


class PageGetThreadOwnerParams(BaseModel):
    """Parameters for Page.get_thread_owner()."""

    model_config = ConfigDict(extra="forbid")
    recipient: str | None = Field(None, description="recipient parameter")


class PageGetThreadsParams(BaseModel):
    """Parameters for Page.get_threads()."""

    model_config = ConfigDict(extra="forbid")
    folder: str | None = Field(None, description="folder parameter")
    platform: pagethreads_platform_enum_param | None = Field(None, description="platform parameter")
    tags: list[str] | None = Field(None, description="tags parameter")
    user_id: str | None = Field(None, description="user_id parameter")


class PageCreateUnlinkAccountParams(BaseModel):
    """Parameters for Page.create_unlink_account()."""

    model_config = ConfigDict(extra="forbid")
    psid: str | None = Field(None, description="psid parameter")


class PageGetVideoCopyrightRulesParams(BaseModel):
    """Parameters for Page.get_video_copyright_rules()."""

    model_config = ConfigDict(extra="forbid")
    selected_rule_id: str | None = Field(None, description="selected_rule_id parameter")
    source: pagevideo_copyright_rules_source_enum_param | None = Field(
        None, description="source parameter"
    )


class PageCreateVideoCopyrightRuleParams(BaseModel):
    """Parameters for Page.create_video_copyright_rule()."""

    model_config = ConfigDict(extra="forbid")
    condition_groups: list[dict[str, Any]] | None = Field(
        None, description="condition_groups parameter"
    )
    name: str | None = Field(None, description="name parameter")


class PageCreateVideoCopyrightParams(BaseModel):
    """Parameters for Page.create_video_copyright()."""

    model_config = ConfigDict(extra="forbid")
    attribution_id: str | None = Field(None, description="attribution_id parameter")
    content_category: pagevideo_copyrights_content_category_enum_param | None = Field(
        None, description="content_category parameter"
    )
    copyright_content_id: str | None = Field(None, description="copyright_content_id parameter")
    excluded_ownership_countries: list[str] | None = Field(
        None, description="excluded_ownership_countries parameter"
    )
    excluded_ownership_segments: list[dict[str, Any]] | None = Field(
        None, description="excluded_ownership_segments parameter"
    )
    is_reference_disabled: bool | None = Field(None, description="is_reference_disabled parameter")
    is_reference_video: bool | None = Field(None, description="is_reference_video parameter")
    monitoring_type: pagevideo_copyrights_monitoring_type_enum_param | None = Field(
        None, description="monitoring_type parameter"
    )
    ownership_countries: list[str] | None = Field(None, description="ownership_countries parameter")
    rule_id: str | None = Field(None, description="rule_id parameter")
    tags: list[str] | None = Field(None, description="tags parameter")
    whitelisted_ids: list[str] | None = Field(None, description="whitelisted_ids parameter")
    whitelisted_ig_user_ids: list[str] | None = Field(
        None, description="whitelisted_ig_user_ids parameter"
    )


class PageGetVideoReelsParams(BaseModel):
    """Parameters for Page.get_video_reels()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class PageCreateVideoReelParams(BaseModel):
    """Parameters for Page.create_video_reel()."""

    model_config = ConfigDict(extra="forbid")
    description: str | None = Field(None, description="description parameter")
    feed_targeting: dict[str, Any] | None = Field(None, description="feed_targeting parameter")
    place: str | None = Field(None, description="place parameter")
    scheduled_publish_time: datetime | None = Field(
        None, description="scheduled_publish_time parameter"
    )
    targeting: dict[str, Any] | None = Field(None, description="targeting parameter")
    title: str | None = Field(None, description="title parameter")
    upload_phase: pagevideo_reels_upload_phase_enum_param | None = Field(
        None, description="upload_phase parameter"
    )
    video_id: str | None = Field(None, description="video_id parameter")
    video_state: pagevideo_reels_video_state_enum_param | None = Field(
        None, description="video_state parameter"
    )


class PageCreateVideoStorieParams(BaseModel):
    """Parameters for Page.create_video_storie()."""

    model_config = ConfigDict(extra="forbid")
    description: str | None = Field(None, description="description parameter")
    feed_targeting: dict[str, Any] | None = Field(None, description="feed_targeting parameter")
    place: str | None = Field(None, description="place parameter")
    scheduled_publish_time: datetime | None = Field(
        None, description="scheduled_publish_time parameter"
    )
    targeting: dict[str, Any] | None = Field(None, description="targeting parameter")
    title: str | None = Field(None, description="title parameter")
    upload_phase: pagevideo_stories_upload_phase_enum_param | None = Field(
        None, description="upload_phase parameter"
    )
    video_id: str | None = Field(None, description="video_id parameter")
    video_state: pagevideo_stories_video_state_enum_param | None = Field(
        None, description="video_state parameter"
    )


class PageGetVideosParams(BaseModel):
    """Parameters for Page.get_videos()."""

    model_config = ConfigDict(extra="forbid")
    type: pagevideos_type_enum_param | None = Field(None, description="type parameter")


class PageCreateVideoParams(BaseModel):
    """Parameters for Page.create_video()."""

    model_config = ConfigDict(extra="forbid")
    ad_breaks: dict[str, Any] | None = Field(None, description="ad_breaks parameter")
    application_id: str | None = Field(None, description="application_id parameter")
    asked_fun_fact_prompt_id: int | None = Field(
        None, description="asked_fun_fact_prompt_id parameter"
    )
    audio_story_wave_animation_handle: str | None = Field(
        None, description="audio_story_wave_animation_handle parameter"
    )
    backdated_post: dict[str, Any] | None = Field(None, description="backdated_post parameter")
    call_to_action: dict[str, Any] | None = Field(None, description="call_to_action parameter")
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
    container_type: pagevideos_container_type_enum_param | None = Field(
        None, description="container_type parameter"
    )
    content_category: pagevideos_content_category_enum_param | None = Field(
        None, description="content_category parameter"
    )
    content_tags: list[str] | None = Field(None, description="content_tags parameter")
    creative_tools: str | None = Field(None, description="creative_tools parameter")
    crossposted_video_id: str | None = Field(None, description="crossposted_video_id parameter")
    custom_labels: list[str] | None = Field(None, description="custom_labels parameter")
    description: str | None = Field(None, description="description parameter")
    direct_share_status: int | None = Field(None, description="direct_share_status parameter")
    embeddable: bool | None = Field(None, description="embeddable parameter")
    end_offset: int | None = Field(None, description="end_offset parameter")
    expiration: dict[str, Any] | None = Field(None, description="expiration parameter")
    fbuploader_video_file_chunk: str | None = Field(
        None, description="fbuploader_video_file_chunk parameter"
    )
    feed_targeting: dict[str, Any] | None = Field(None, description="feed_targeting parameter")
    file_size: int | None = Field(None, description="file_size parameter")
    file_url: str | None = Field(None, description="file_url parameter")
    fisheye_video_cropped: bool | None = Field(None, description="fisheye_video_cropped parameter")
    formatting: pagevideos_formatting_enum_param | None = Field(
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
    multilingual_data: list[dict[str, Any]] | None = Field(
        None, description="multilingual_data parameter"
    )
    no_story: bool | None = Field(None, description="no_story parameter")
    og_action_type_id: str | None = Field(None, description="og_action_type_id parameter")
    og_icon_id: str | None = Field(None, description="og_icon_id parameter")
    og_object_id: str | None = Field(None, description="og_object_id parameter")
    og_phrase: str | None = Field(None, description="og_phrase parameter")
    og_suggestion_mechanism: str | None = Field(
        None, description="og_suggestion_mechanism parameter"
    )
    original_fov: int | None = Field(None, description="original_fov parameter")
    original_projection_type: pagevideos_original_projection_type_enum_param | None = Field(
        None, description="original_projection_type parameter"
    )
    partnership_ad_ad_code: str | None = Field(None, description="partnership_ad_ad_code parameter")
    publish_event_id: int | None = Field(None, description="publish_event_id parameter")
    published: bool | None = Field(None, description="published parameter")
    reference_only: bool | None = Field(None, description="reference_only parameter")
    referenced_sticker_id: str | None = Field(None, description="referenced_sticker_id parameter")
    replace_video_id: str | None = Field(None, description="replace_video_id parameter")
    scheduled_publish_time: int | None = Field(None, description="scheduled_publish_time parameter")
    secret: bool | None = Field(None, description="secret parameter")
    slideshow_spec: dict[str, Any] | None = Field(None, description="slideshow_spec parameter")
    social_actions: bool | None = Field(None, description="social_actions parameter")
    source: str | None = Field(None, description="source parameter")
    source_instagram_media_id: str | None = Field(
        None, description="source_instagram_media_id parameter"
    )
    specified_dialect: str | None = Field(None, description="specified_dialect parameter")
    spherical: bool | None = Field(None, description="spherical parameter")
    sponsor_id: str | None = Field(None, description="sponsor_id parameter")
    sponsor_relationship: int | None = Field(None, description="sponsor_relationship parameter")
    start_offset: int | None = Field(None, description="start_offset parameter")
    swap_mode: pagevideos_swap_mode_enum_param | None = Field(
        None, description="swap_mode parameter"
    )
    targeting: dict[str, Any] | None = Field(None, description="targeting parameter")
    text_format_metadata: str | None = Field(None, description="text_format_metadata parameter")
    thumb: dict[str, Any] | None = Field(None, description="thumb parameter")
    time_since_original_post: int | None = Field(
        None, description="time_since_original_post parameter"
    )
    title: str | None = Field(None, description="title parameter")
    transcode_setting_properties: str | None = Field(
        None, description="transcode_setting_properties parameter"
    )
    universal_video_id: str | None = Field(None, description="universal_video_id parameter")
    unpublished_content_type: pagevideos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    upload_phase: pagevideos_upload_phase_enum_param | None = Field(
        None, description="upload_phase parameter"
    )
    upload_session_id: str | None = Field(None, description="upload_session_id parameter")
    upload_setting_properties: str | None = Field(
        None, description="upload_setting_properties parameter"
    )
    video_asset_id: str | None = Field(None, description="video_asset_id parameter")
    video_file_chunk: str | None = Field(None, description="video_file_chunk parameter")
    video_id_original: str | None = Field(None, description="video_id_original parameter")
    video_start_time_ms: int | None = Field(None, description="video_start_time_ms parameter")
    waterfall_id: str | None = Field(None, description="waterfall_id parameter")


class PageGetVisitorPostsParams(BaseModel):
    """Parameters for Page.get_visitor_posts()."""

    model_config = ConfigDict(extra="forbid")
    include_hidden: bool | None = Field(None, description="include_hidden parameter")
    limit: int | None = Field(None, description="limit parameter")
    show_expired: bool | None = Field(None, description="show_expired parameter")
    with_: pagevisitor_posts_with_enum_param | None = Field(
        None, alias="with", description="with parameter"
    )


class PageDeleteWelcomeMessageFlowsParams(BaseModel):
    """Parameters for Page.delete_welcome_message_flows()."""

    model_config = ConfigDict(extra="forbid")
    flow_id: str | None = Field(None, description="flow_id parameter")


class PageGetWelcomeMessageFlowsParams(BaseModel):
    """Parameters for Page.get_welcome_message_flows()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")
    flow_id: str | None = Field(None, description="flow_id parameter")


class PageCreateWelcomeMessageFlowParams(BaseModel):
    """Parameters for Page.create_welcome_message_flow()."""

    model_config = ConfigDict(extra="forbid")
    eligible_platforms: list[pagewelcome_message_flows_eligible_platforms_enum_param] | None = (
        Field(None, description="eligible_platforms parameter")
    )
    flow_id: str | None = Field(None, description="flow_id parameter")
    name: str | None = Field(None, description="name parameter")
    welcome_message_flow: list[dict[str, Any]] | None = Field(
        None, description="welcome_message_flow parameter"
    )
