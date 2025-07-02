"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccountpromotableobjects import AdAccountPromotableObjectsFields
    from .agencyclientdeclaration import AgencyClientDeclarationFields
    from .attributionspec import AttributionSpecFields
    from .business import BusinessFields
    from .crmaddress import CRMAddressFields
    from .customaudiencegroup import CustomAudienceGroupFields
    from .deliverycheck import DeliveryCheckFields
    from .extendedcreditinvoicegroup import ExtendedCreditInvoiceGroupFields
    from .fundingsourcedetails import FundingSourceDetailsFields
    from .reachfrequencyspec import ReachFrequencySpecFields


class adaccountads_date_preset_enum_param(str, Enum):
    """adaccountads_date_preset_enum_param enum values."""

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


class adaccountadsets_tune_for_category_enum_param(str, Enum):
    """adaccountadsets_tune_for_category_enum_param enum values."""

    CREDIT = "CREDIT"
    EMPLOYMENT = "EMPLOYMENT"
    FINANCIAL_PRODUCTS_SERVICES = "FINANCIAL_PRODUCTS_SERVICES"
    HOUSING = "HOUSING"
    ISSUES_ELECTIONS_POLITICS = "ISSUES_ELECTIONS_POLITICS"
    NONE = "NONE"
    ONLINE_GAMBLING_AND_GAMING = "ONLINE_GAMBLING_AND_GAMING"


class adaccountadsets_full_funnel_exploration_mode_enum_param(str, Enum):
    """adaccountadsets_full_funnel_exploration_mode_enum_param enum values."""

    EXTENDED_EXPLORATION = "EXTENDED_EXPLORATION"
    LIMITED_EXPLORATION = "LIMITED_EXPLORATION"
    NONE_EXPLORATION = "NONE_EXPLORATION"


class adaccountcampaigns_date_preset_enum_param(str, Enum):
    """adaccountcampaigns_date_preset_enum_param enum values."""

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


class adaccountproduct_audiences_subtype_enum_param(str, Enum):
    """adaccountproduct_audiences_subtype_enum_param enum values."""

    APP = "APP"
    BAG_OF_ACCOUNTS = "BAG_OF_ACCOUNTS"
    BIDDING = "BIDDING"
    CLAIM = "CLAIM"
    CUSTOM = "CUSTOM"
    ENGAGEMENT = "ENGAGEMENT"
    EXCLUSION = "EXCLUSION"
    FOX = "FOX"
    LOOKALIKE = "LOOKALIKE"
    MANAGED = "MANAGED"
    MEASUREMENT = "MEASUREMENT"
    MESSENGER_SUBSCRIBER_LIST = "MESSENGER_SUBSCRIBER_LIST"
    OFFLINE_CONVERSION = "OFFLINE_CONVERSION"
    PARTNER = "PARTNER"
    PRIMARY = "PRIMARY"
    REGULATED_CATEGORIES_AUDIENCE = "REGULATED_CATEGORIES_AUDIENCE"
    STUDY_RULE_AUDIENCE = "STUDY_RULE_AUDIENCE"
    VIDEO = "VIDEO"
    WEBSITE = "WEBSITE"


class adaccountadsets_bid_strategy_enum_param(str, Enum):
    """adaccountadsets_bid_strategy_enum_param enum values."""

    COST_CAP = "COST_CAP"
    LOWEST_COST_WITHOUT_CAP = "LOWEST_COST_WITHOUT_CAP"
    LOWEST_COST_WITH_BID_CAP = "LOWEST_COST_WITH_BID_CAP"
    LOWEST_COST_WITH_MIN_ROAS = "LOWEST_COST_WITH_MIN_ROAS"


class adaccountvideo_ads_video_state_enum_param(str, Enum):
    """adaccountvideo_ads_video_state_enum_param enum values."""

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    SCHEDULED = "SCHEDULED"


class adaccountadvideos_container_type_enum_param(str, Enum):
    """adaccountadvideos_container_type_enum_param enum values."""

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


class adaccountads_execution_options_enum_param(str, Enum):
    """adaccountads_execution_options_enum_param enum values."""

    include_recommendations = "include_recommendations"
    synchronous_ad_review = "synchronous_ad_review"
    validate_only = "validate_only"


class adaccountad_place_page_sets_async_location_types_enum_param(str, Enum):
    """adaccountad_place_page_sets_async_location_types_enum_param enum values."""

    home = "home"
    recent = "recent"


class adaccounttargetingbrowse_whitelisted_types_enum_param(str, Enum):
    """adaccounttargetingbrowse_whitelisted_types_enum_param enum values."""

    adgroup_id = "adgroup_id"
    age_max = "age_max"
    age_min = "age_min"
    age_range = "age_range"
    alternate_auto_targeting_option = "alternate_auto_targeting_option"
    app_install_state = "app_install_state"
    audience_network_positions = "audience_network_positions"
    behaviors = "behaviors"
    brand_safety_content_filter_levels = "brand_safety_content_filter_levels"
    brand_safety_content_severity_levels = "brand_safety_content_severity_levels"
    cafe_ca_contraction_targeting_signal = "cafe_ca_contraction_targeting_signal"
    cafe_ca_expansion_targeting_signal = "cafe_ca_expansion_targeting_signal"
    catalog_based_targeting = "catalog_based_targeting"
    cities = "cities"
    city_keys = "city_keys"
    college_years = "college_years"
    conjunctive_user_adclusters = "conjunctive_user_adclusters"
    connections = "connections"
    contextual_targeting_categories = "contextual_targeting_categories"
    countries = "countries"
    country = "country"
    country_groups = "country_groups"
    custom_audiences = "custom_audiences"
    device_platforms = "device_platforms"
    direct_install_devices = "direct_install_devices"
    dynamic_audience_ids = "dynamic_audience_ids"
    education_majors = "education_majors"
    education_schools = "education_schools"
    education_statuses = "education_statuses"
    effective_audience_network_positions = "effective_audience_network_positions"
    effective_device_platforms = "effective_device_platforms"
    effective_facebook_positions = "effective_facebook_positions"
    effective_instagram_positions = "effective_instagram_positions"
    effective_messenger_positions = "effective_messenger_positions"
    effective_oculus_positions = "effective_oculus_positions"
    effective_publisher_platforms = "effective_publisher_platforms"
    effective_threads_positions = "effective_threads_positions"
    effective_whatsapp_positions = "effective_whatsapp_positions"
    engagement_specs = "engagement_specs"
    ethnic_affinity = "ethnic_affinity"
    exclude_previous_days = "exclude_previous_days"
    exclude_reached_since = "exclude_reached_since"
    excluded_brand_safety_content_types = "excluded_brand_safety_content_types"
    excluded_connections = "excluded_connections"
    excluded_custom_audiences = "excluded_custom_audiences"
    excluded_dynamic_audience_ids = "excluded_dynamic_audience_ids"
    excluded_engagement_specs = "excluded_engagement_specs"
    excluded_geo_locations = "excluded_geo_locations"
    excluded_mobile_device_model = "excluded_mobile_device_model"
    excluded_product_audience_specs = "excluded_product_audience_specs"
    excluded_publisher_categories = "excluded_publisher_categories"
    excluded_publisher_list_ids = "excluded_publisher_list_ids"
    excluded_user_adclusters = "excluded_user_adclusters"
    excluded_user_device = "excluded_user_device"
    exclusions = "exclusions"
    expanded_implicit_custom_audiences = "expanded_implicit_custom_audiences"
    facebook_positions = "facebook_positions"
    family_statuses = "family_statuses"
    fb_deal_id = "fb_deal_id"
    flexible_spec = "flexible_spec"
    follow_profiles = "follow_profiles"
    follow_profiles_negative = "follow_profiles_negative"
    format = "format"
    friends_of_connections = "friends_of_connections"
    gatekeepers = "gatekeepers"
    genders = "genders"
    generation = "generation"
    geo_locations = "geo_locations"
    home_ownership = "home_ownership"
    home_type = "home_type"
    home_value = "home_value"
    household_composition = "household_composition"
    household_income = "household_income"
    id = "id"
    income = "income"
    industries = "industries"
    instagram_hashtags = "instagram_hashtags"
    instagram_positions = "instagram_positions"
    install_state_application = "install_state_application"
    instream_video_skippable_excluded = "instream_video_skippable_excluded"
    instream_video_sponsorship_placements = "instream_video_sponsorship_placements"
    interest_defaults_source = "interest_defaults_source"
    interested_in = "interested_in"
    interests = "interests"
    is_instagram_destination_ad = "is_instagram_destination_ad"
    is_whatsapp_destination_ad = "is_whatsapp_destination_ad"
    keywords = "keywords"
    life_events = "life_events"
    locales = "locales"
    location_categories = "location_categories"
    location_cluster_ids = "location_cluster_ids"
    location_expansion = "location_expansion"
    marketing_message_channels = "marketing_message_channels"
    marketplace_product_categories = "marketplace_product_categories"
    messenger_positions = "messenger_positions"
    mobile_device_model = "mobile_device_model"
    moms = "moms"
    net_worth = "net_worth"
    oculus_positions = "oculus_positions"
    office_type = "office_type"
    page_types = "page_types"
    place_page_set_ids = "place_page_set_ids"
    political_views = "political_views"
    politics = "politics"
    product_audience_specs = "product_audience_specs"
    prospecting_audience = "prospecting_audience"
    publisher_platforms = "publisher_platforms"
    radius = "radius"
    region_keys = "region_keys"
    regions = "regions"
    relationship_statuses = "relationship_statuses"
    rtb_flag = "rtb_flag"
    site_category = "site_category"
    subscriber_universe = "subscriber_universe"
    tafe_ca_mitigation_strategy = "tafe_ca_mitigation_strategy"
    targeting_automation = "targeting_automation"
    targeting_optimization = "targeting_optimization"
    targeting_relaxation_types = "targeting_relaxation_types"
    threads_positions = "threads_positions"
    timezones = "timezones"
    topic = "topic"
    trending = "trending"
    user_adclusters = "user_adclusters"
    user_age_unknown = "user_age_unknown"
    user_device = "user_device"
    user_event = "user_event"
    user_os = "user_os"
    user_page_threads = "user_page_threads"
    user_page_threads_excluded = "user_page_threads_excluded"
    whatsapp_positions = "whatsapp_positions"
    wireless_carrier = "wireless_carrier"
    work_employers = "work_employers"
    work_positions = "work_positions"
    zips = "zips"


class adaccountcustomaudiences_customer_file_source_enum_param(str, Enum):
    """adaccountcustomaudiences_customer_file_source_enum_param enum values."""

    BOTH_USER_AND_PARTNER_PROVIDED = "BOTH_USER_AND_PARTNER_PROVIDED"
    PARTNER_PROVIDED_ONLY = "PARTNER_PROVIDED_ONLY"
    USER_PROVIDED_ONLY = "USER_PROVIDED_ONLY"


class adaccountgeneratepreviews_render_type_enum_param(str, Enum):
    """adaccountgeneratepreviews_render_type_enum_param enum values."""

    FALLBACK = "FALLBACK"


class adaccounttargetingsuggestions_mode_enum_param(str, Enum):
    """adaccounttargetingsuggestions_mode_enum_param enum values."""

    best_performing = "best_performing"
    recently_used = "recently_used"
    related = "related"
    suggestions = "suggestions"


class adaccounttargetingsuggestions_limit_type_enum_param(str, Enum):
    """adaccounttargetingsuggestions_limit_type_enum_param enum values."""

    behaviors = "behaviors"
    college_years = "college_years"
    education_majors = "education_majors"
    education_schools = "education_schools"
    education_statuses = "education_statuses"
    family_statuses = "family_statuses"
    home_value = "home_value"
    income = "income"
    industries = "industries"
    interested_in = "interested_in"
    interests = "interests"
    life_events = "life_events"
    location_categories = "location_categories"
    relationship_statuses = "relationship_statuses"
    user_adclusters = "user_adclusters"
    work_employers = "work_employers"
    work_positions = "work_positions"


class adaccounttargetingbrowse_regulated_categories_enum_param(str, Enum):
    """adaccounttargetingbrowse_regulated_categories_enum_param enum values."""

    CREDIT = "CREDIT"
    EMPLOYMENT = "EMPLOYMENT"
    FINANCIAL_PRODUCTS_SERVICES = "FINANCIAL_PRODUCTS_SERVICES"
    HOUSING = "HOUSING"
    ISSUES_ELECTIONS_POLITICS = "ISSUES_ELECTIONS_POLITICS"
    NONE = "NONE"
    ONLINE_GAMBLING_AND_GAMING = "ONLINE_GAMBLING_AND_GAMING"


class adaccountadvideos_original_projection_type_enum_param(str, Enum):
    """adaccountadvideos_original_projection_type_enum_param enum values."""

    cubemap = "cubemap"
    equirectangular = "equirectangular"
    half_equirectangular = "half_equirectangular"


class adaccountcampaignsbylabels_operator_enum_param(str, Enum):
    """adaccountcampaignsbylabels_operator_enum_param enum values."""

    ALL = "ALL"
    ANY = "ANY"


class adaccountasync_requests_status_enum_param(str, Enum):
    """adaccountasync_requests_status_enum_param enum values."""

    ERROR = "ERROR"
    EXECUTING = "EXECUTING"
    FINISHED = "FINISHED"
    INITIALIZED = "INITIALIZED"


class adaccountcampaigns_effective_status_enum_param(str, Enum):
    """adaccountcampaigns_effective_status_enum_param enum values."""

    ACTIVE = "ACTIVE"
    ADSET_PAUSED = "ADSET_PAUSED"
    ARCHIVED = "ARCHIVED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    DELETED = "DELETED"
    DISAPPROVED = "DISAPPROVED"
    IN_PROCESS = "IN_PROCESS"
    PAUSED = "PAUSED"
    PENDING_BILLING_INFO = "PENDING_BILLING_INFO"
    PENDING_REVIEW = "PENDING_REVIEW"
    PREAPPROVED = "PREAPPROVED"
    WITH_ISSUES = "WITH_ISSUES"


class adaccountcustomaudiences_content_type_enum_param(str, Enum):
    """adaccountcustomaudiences_content_type_enum_param enum values."""

    AUTOMOTIVE_MODEL = "AUTOMOTIVE_MODEL"
    DESTINATION = "DESTINATION"
    FLIGHT = "FLIGHT"
    GENERIC = "GENERIC"
    HOME_LISTING = "HOME_LISTING"
    HOTEL = "HOTEL"
    LOCAL_SERVICE_BUSINESS = "LOCAL_SERVICE_BUSINESS"
    MEDIA_TITLE = "MEDIA_TITLE"
    OFFLINE_PRODUCT = "OFFLINE_PRODUCT"
    PRODUCT = "PRODUCT"
    VEHICLE = "VEHICLE"
    VEHICLE_OFFER = "VEHICLE_OFFER"


class adaccountinsights_action_attribution_windows_enum_param(str, Enum):
    """adaccountinsights_action_attribution_windows_enum_param enum values."""

    VALUE_1D_CLICK = "1d_click"
    VALUE_1D_EV = "1d_ev"
    VALUE_1D_VIEW = "1d_view"
    VALUE_28D_CLICK = "28d_click"
    VALUE_28D_VIEW = "28d_view"
    VALUE_28D_VIEW_ALL_CONVERSIONS = "28d_view_all_conversions"
    VALUE_28D_VIEW_FIRST_CONVERSION = "28d_view_first_conversion"
    VALUE_7D_CLICK = "7d_click"
    VALUE_7D_VIEW = "7d_view"
    VALUE_7D_VIEW_ALL_CONVERSIONS = "7d_view_all_conversions"
    VALUE_7D_VIEW_FIRST_CONVERSION = "7d_view_first_conversion"
    dda = "dda"
    default = "default"
    skan_click = "skan_click"
    skan_click_second_postback = "skan_click_second_postback"
    skan_click_third_postback = "skan_click_third_postback"
    skan_view = "skan_view"
    skan_view_second_postback = "skan_view_second_postback"
    skan_view_third_postback = "skan_view_third_postback"


class adaccountcampaigns_objective_enum_param(str, Enum):
    """adaccountcampaigns_objective_enum_param enum values."""

    APP_INSTALLS = "APP_INSTALLS"
    BRAND_AWARENESS = "BRAND_AWARENESS"
    CONVERSIONS = "CONVERSIONS"
    EVENT_RESPONSES = "EVENT_RESPONSES"
    LEAD_GENERATION = "LEAD_GENERATION"
    LINK_CLICKS = "LINK_CLICKS"
    LOCAL_AWARENESS = "LOCAL_AWARENESS"
    MESSAGES = "MESSAGES"
    OFFER_CLAIMS = "OFFER_CLAIMS"
    OUTCOME_APP_PROMOTION = "OUTCOME_APP_PROMOTION"
    OUTCOME_AWARENESS = "OUTCOME_AWARENESS"
    OUTCOME_ENGAGEMENT = "OUTCOME_ENGAGEMENT"
    OUTCOME_LEADS = "OUTCOME_LEADS"
    OUTCOME_SALES = "OUTCOME_SALES"
    OUTCOME_TRAFFIC = "OUTCOME_TRAFFIC"
    PAGE_LIKES = "PAGE_LIKES"
    POST_ENGAGEMENT = "POST_ENGAGEMENT"
    PRODUCT_CATALOG_SALES = "PRODUCT_CATALOG_SALES"
    REACH = "REACH"
    STORE_VISITS = "STORE_VISITS"
    VIDEO_VIEWS = "VIDEO_VIEWS"


class adaccountcampaigns_delete_strategy_enum_param(str, Enum):
    """adaccountcampaigns_delete_strategy_enum_param enum values."""

    DELETE_ANY = "DELETE_ANY"
    DELETE_ARCHIVED_BEFORE = "DELETE_ARCHIVED_BEFORE"
    DELETE_OLDEST = "DELETE_OLDEST"


class adaccounttargetingbrowse_regulated_countries_enum_param(str, Enum):
    """adaccounttargetingbrowse_regulated_countries_enum_param enum values."""

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


class adaccountvalue_rule_set_product_type_enum_param(str, Enum):
    """adaccountvalue_rule_set_product_type_enum_param enum values."""

    AUDIENCE = "AUDIENCE"
    LEADGEN_ADS = "LEADGEN_ADS"
    OMNI_CHANNEL = "OMNI_CHANNEL"


class adaccountadrules_library_ui_creation_source_enum_param(str, Enum):
    """adaccountadrules_library_ui_creation_source_enum_param enum values."""

    AM_ACCOUNT_OVERVIEW_RECOMMENDATIONS = "AM_ACCOUNT_OVERVIEW_RECOMMENDATIONS"
    AM_ACTIVITY_HISTORY_TABLE = "AM_ACTIVITY_HISTORY_TABLE"
    AM_AD_OBJECT_NAME_CARD = "AM_AD_OBJECT_NAME_CARD"
    AM_AMFE_L3_RECOMMENDATION = "AM_AMFE_L3_RECOMMENDATION"
    AM_AUTOFLOW_GUIDANCE_CARD = "AM_AUTOFLOW_GUIDANCE_CARD"
    AM_AUTO_APPLY_WIDGET = "AM_AUTO_APPLY_WIDGET"
    AM_EDITOR_CARD = "AM_EDITOR_CARD"
    AM_INFO_CARD = "AM_INFO_CARD"
    AM_NAME_CELL_DROPDOWN = "AM_NAME_CELL_DROPDOWN"
    AM_OPTIMIZATION_TIP_GUIDANCE_CARD = "AM_OPTIMIZATION_TIP_GUIDANCE_CARD"
    AM_PERFORMANCE_SUMMARY = "AM_PERFORMANCE_SUMMARY"
    AM_RULE_LANDING_PAGE_BANNER = "AM_RULE_LANDING_PAGE_BANNER"
    AM_SYD_RESOLUTION_FLOW = "AM_SYD_RESOLUTION_FLOW"
    AM_SYD_RESOLUTION_FLOW_MODAL = "AM_SYD_RESOLUTION_FLOW_MODAL"
    AM_TABLE_DELIVERY_COLUMN_POPOVER = "AM_TABLE_DELIVERY_COLUMN_POPOVER"
    AM_TABLE_MORE_RULES_DROPDOWN = "AM_TABLE_MORE_RULES_DROPDOWN"
    AM_TABLE_TOGGLE_POPOVER = "AM_TABLE_TOGGLE_POPOVER"
    AM_TOOLBAR_CREATE_RULE_DROPDOWN = "AM_TOOLBAR_CREATE_RULE_DROPDOWN"
    PE_CAMPAIGN_STRUCTURE_MENU = "PE_CAMPAIGN_STRUCTURE_MENU"
    PE_EDITOR_CARD = "PE_EDITOR_CARD"
    PE_INFO_CARD = "PE_INFO_CARD"
    PE_TOOLBAR_CREATE_RULE_DROPDOWN = "PE_TOOLBAR_CREATE_RULE_DROPDOWN"
    RULES_MANAGEMENT_PAGE_ACTION_DROPDOWN = "RULES_MANAGEMENT_PAGE_ACTION_DROPDOWN"
    RULES_MANAGEMENT_PAGE_RULE_GROUP = "RULES_MANAGEMENT_PAGE_RULE_GROUP"
    RULES_MANAGEMENT_PAGE_RULE_NAME = "RULES_MANAGEMENT_PAGE_RULE_NAME"
    RULES_MANAGEMENT_PAGE_TOP_NAV = "RULES_MANAGEMENT_PAGE_TOP_NAV"
    RULES_VIEW_ACTIVE_RULES_DIALOG = "RULES_VIEW_ACTIVE_RULES_DIALOG"
    RULE_CREATION_SUCCESS_DIALOG = "RULE_CREATION_SUCCESS_DIALOG"
    RULE_SYD_REDIRECT = "RULE_SYD_REDIRECT"
    RULE_TEMPLATES_DIALOG = "RULE_TEMPLATES_DIALOG"


class adaccountvalue_rule_set_status_enum_param(str, Enum):
    """adaccountvalue_rule_set_status_enum_param enum values."""

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


class adaccountinsights_breakdowns_enum_param(str, Enum):
    """adaccountinsights_breakdowns_enum_param enum values."""

    ad_extension_domain = "ad_extension_domain"
    ad_extension_url = "ad_extension_url"
    ad_format_asset = "ad_format_asset"
    age = "age"
    app_id = "app_id"
    body_asset = "body_asset"
    breakdown_ad_objective = "breakdown_ad_objective"
    breakdown_reporting_ad_id = "breakdown_reporting_ad_id"
    call_to_action_asset = "call_to_action_asset"
    coarse_conversion_value = "coarse_conversion_value"
    comscore_market = "comscore_market"
    comscore_market_code = "comscore_market_code"
    conversion_destination = "conversion_destination"
    country = "country"
    creative_relaxation_asset_type = "creative_relaxation_asset_type"
    description_asset = "description_asset"
    device_platform = "device_platform"
    dma = "dma"
    fidelity_type = "fidelity_type"
    flexible_format_asset_type = "flexible_format_asset_type"
    frequency_value = "frequency_value"
    gen_ai_asset_type = "gen_ai_asset_type"
    gender = "gender"
    hourly_stats_aggregated_by_advertiser_time_zone = (
        "hourly_stats_aggregated_by_advertiser_time_zone"
    )
    hourly_stats_aggregated_by_audience_time_zone = "hourly_stats_aggregated_by_audience_time_zone"
    hsid = "hsid"
    image_asset = "image_asset"
    impression_device = "impression_device"
    impression_view_time_advertiser_hour_v2 = "impression_view_time_advertiser_hour_v2"
    is_auto_advance = "is_auto_advance"
    is_conversion_id_modeled = "is_conversion_id_modeled"
    is_rendered_as_delayed_skip_ad = "is_rendered_as_delayed_skip_ad"
    landing_destination = "landing_destination"
    link_url_asset = "link_url_asset"
    marketing_messages_btn_name = "marketing_messages_btn_name"
    mdsa_landing_destination = "mdsa_landing_destination"
    media_asset_url = "media_asset_url"
    media_creator = "media_creator"
    media_destination_url = "media_destination_url"
    media_format = "media_format"
    media_origin_url = "media_origin_url"
    media_text_content = "media_text_content"
    media_type = "media_type"
    mmm = "mmm"
    place_page_id = "place_page_id"
    platform_position = "platform_position"
    postback_sequence_index = "postback_sequence_index"
    product_id = "product_id"
    publisher_platform = "publisher_platform"
    redownload = "redownload"
    region = "region"
    signal_source_bucket = "signal_source_bucket"
    skan_campaign_id = "skan_campaign_id"
    skan_conversion_id = "skan_conversion_id"
    skan_version = "skan_version"
    sot_attribution_model_type = "sot_attribution_model_type"
    sot_attribution_window = "sot_attribution_window"
    sot_channel = "sot_channel"
    sot_event_type = "sot_event_type"
    sot_source = "sot_source"
    standard_event_content_type = "standard_event_content_type"
    title_asset = "title_asset"
    user_persona_id = "user_persona_id"
    user_persona_name = "user_persona_name"
    video_asset = "video_asset"


class adaccounttargetingsearch_regulated_countries_enum_param(str, Enum):
    """adaccounttargetingsearch_regulated_countries_enum_param enum values."""

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


class adaccountadsets_regional_regulated_categories_enum_param(str, Enum):
    """adaccountadsets_regional_regulated_categories_enum_param enum values."""

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class adaccountasyncadrequestsets_notification_mode_enum_param(str, Enum):
    """adaccountasyncadrequestsets_notification_mode_enum_param enum values."""

    OFF = "OFF"
    ON_COMPLETE = "ON_COMPLETE"


class adaccountactivities_category_enum_param(str, Enum):
    """adaccountactivities_category_enum_param enum values."""

    ACCOUNT = "ACCOUNT"
    AD = "AD"
    AD_KEYWORDS = "AD_KEYWORDS"
    AD_SET = "AD_SET"
    AUDIENCE = "AUDIENCE"
    BID = "BID"
    BUDGET = "BUDGET"
    CAMPAIGN = "CAMPAIGN"
    DATE = "DATE"
    STATUS = "STATUS"
    TARGETING = "TARGETING"


class adaccountcampaigns_special_ad_categories_enum_param(str, Enum):
    """adaccountcampaigns_special_ad_categories_enum_param enum values."""

    CREDIT = "CREDIT"
    EMPLOYMENT = "EMPLOYMENT"
    FINANCIAL_PRODUCTS_SERVICES = "FINANCIAL_PRODUCTS_SERVICES"
    HOUSING = "HOUSING"
    ISSUES_ELECTIONS_POLITICS = "ISSUES_ELECTIONS_POLITICS"
    NONE = "NONE"
    ONLINE_GAMBLING_AND_GAMING = "ONLINE_GAMBLING_AND_GAMING"


class adaccountadrules_history_evaluation_type_enum_param(str, Enum):
    """adaccountadrules_history_evaluation_type_enum_param enum values."""

    SCHEDULE = "SCHEDULE"
    TRIGGER = "TRIGGER"


class adaccountadvideos_unpublished_content_type_enum_param(str, Enum):
    """adaccountadvideos_unpublished_content_type_enum_param enum values."""

    ADS_POST = "ADS_POST"
    DRAFT = "DRAFT"
    INLINE_CREATED = "INLINE_CREATED"
    PUBLISHED = "PUBLISHED"
    REVIEWABLE_BRANDED_CONTENT = "REVIEWABLE_BRANDED_CONTENT"
    SCHEDULED = "SCHEDULED"
    SCHEDULED_RECURRING = "SCHEDULED_RECURRING"


class adaccounttargetingsuggestions_whitelisted_types_enum_param(str, Enum):
    """adaccounttargetingsuggestions_whitelisted_types_enum_param enum values."""

    behaviors = "behaviors"
    college_years = "college_years"
    education_majors = "education_majors"
    education_schools = "education_schools"
    education_statuses = "education_statuses"
    family_statuses = "family_statuses"
    home_value = "home_value"
    income = "income"
    industries = "industries"
    interested_in = "interested_in"
    interests = "interests"
    life_events = "life_events"
    location_categories = "location_categories"
    relationship_statuses = "relationship_statuses"
    user_adclusters = "user_adclusters"
    work_employers = "work_employers"
    work_positions = "work_positions"


class adaccountadcreatives_dynamic_ad_voice_enum_param(str, Enum):
    """adaccountadcreatives_dynamic_ad_voice_enum_param enum values."""

    DYNAMIC = "DYNAMIC"
    STORY_OWNER = "STORY_OWNER"


class adaccountadcreatives_applink_treatment_enum_param(str, Enum):
    """adaccountadcreatives_applink_treatment_enum_param enum values."""

    automatic = "automatic"
    deeplink_with_appstore_fallback = "deeplink_with_appstore_fallback"
    deeplink_with_web_fallback = "deeplink_with_web_fallback"
    web_only = "web_only"


class adaccounttargetingbrowse_limit_type_enum_param(str, Enum):
    """adaccounttargetingbrowse_limit_type_enum_param enum values."""

    behaviors = "behaviors"
    college_years = "college_years"
    education_majors = "education_majors"
    education_schools = "education_schools"
    education_statuses = "education_statuses"
    ethnic_affinity = "ethnic_affinity"
    family_statuses = "family_statuses"
    generation = "generation"
    home_ownership = "home_ownership"
    home_type = "home_type"
    home_value = "home_value"
    household_composition = "household_composition"
    income = "income"
    industries = "industries"
    interested_in = "interested_in"
    interests = "interests"
    life_events = "life_events"
    location_categories = "location_categories"
    moms = "moms"
    net_worth = "net_worth"
    office_type = "office_type"
    politics = "politics"
    relationship_statuses = "relationship_statuses"
    user_adclusters = "user_adclusters"
    work_employers = "work_employers"
    work_positions = "work_positions"


class adaccountadsets_budget_source_enum_param(str, Enum):
    """adaccountadsets_budget_source_enum_param enum values."""

    NONE = "NONE"
    RMN = "RMN"


class adaccountmatched_search_applications_app_store_enum_param(str, Enum):
    """adaccountmatched_search_applications_app_store_enum_param enum values."""

    AMAZON_APP_STORE = "AMAZON_APP_STORE"
    APK_MIRROR = "APK_MIRROR"
    APK_MONK = "APK_MONK"
    APK_PURE = "APK_PURE"
    APTOIDE_A1_STORE = "APTOIDE_A1_STORE"
    BEMOBI_MOBILE_STORE = "BEMOBI_MOBILE_STORE"
    DIGITAL_TURBINE_STORE = "DIGITAL_TURBINE_STORE"
    DOES_NOT_EXIST = "DOES_NOT_EXIST"
    FB_ANDROID_STORE = "FB_ANDROID_STORE"
    FB_CANVAS = "FB_CANVAS"
    FB_GAMEROOM = "FB_GAMEROOM"
    GALAXY_STORE = "GALAXY_STORE"
    GOOGLE_PLAY = "GOOGLE_PLAY"
    INSTANT_GAME = "INSTANT_GAME"
    ITUNES = "ITUNES"
    ITUNES_IPAD = "ITUNES_IPAD"
    NEON_ANDROID_STORE = "NEON_ANDROID_STORE"
    NONE = "NONE"
    OCULUS_APP_STORE = "OCULUS_APP_STORE"
    OPPO = "OPPO"
    ROKU_STORE = "ROKU_STORE"
    UPTODOWN = "UPTODOWN"
    VIVO = "VIVO"
    WINDOWS_10_STORE = "WINDOWS_10_STORE"
    WINDOWS_STORE = "WINDOWS_STORE"
    XIAOMI = "XIAOMI"


class adaccountcampaigns_special_ad_category_country_enum_param(str, Enum):
    """adaccountcampaigns_special_ad_category_country_enum_param enum values."""

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


class adaccountadsets_execution_options_enum_param(str, Enum):
    """adaccountadsets_execution_options_enum_param enum values."""

    include_recommendations = "include_recommendations"
    validate_only = "validate_only"


class adaccountadsets_date_preset_enum_param(str, Enum):
    """adaccountadsets_date_preset_enum_param enum values."""

    DATA_MAXIMUM = "DATA_MAXIMUM"
    LAST_14D = "LAST_14D"
    LAST_28D = "LAST_28D"
    LAST_30D = "LAST_30D"
    LAST_3D = "LAST_3D"
    LAST_7D = "LAST_7D"
    LAST_90D = "LAST_90D"
    LAST_MONTH = "LAST_MONTH"
    LAST_QUARTER = "LAST_QUARTER"
    LAST_WEEK_MON_SUN = "LAST_WEEK_MON_SUN"
    LAST_WEEK_SUN_SAT = "LAST_WEEK_SUN_SAT"
    LAST_YEAR = "LAST_YEAR"
    MAXIMUM = "MAXIMUM"
    THIS_MONTH = "THIS_MONTH"
    THIS_QUARTER = "THIS_QUARTER"
    THIS_WEEK_MON_TODAY = "THIS_WEEK_MON_TODAY"
    THIS_WEEK_SUN_TODAY = "THIS_WEEK_SUN_TODAY"
    THIS_YEAR = "THIS_YEAR"
    TODAY = "TODAY"
    YESTERDAY = "YESTERDAY"


class adaccountadsbylabels_operator_enum_param(str, Enum):
    """adaccountadsbylabels_operator_enum_param enum values."""

    ALL = "ALL"
    ANY = "ANY"


class adaccountadsets_status_enum_param(str, Enum):
    """adaccountadsets_status_enum_param enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class adaccountcampaigns_status_enum_param(str, Enum):
    """adaccountcampaigns_status_enum_param enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class adaccountproduct_audiences_content_type_enum_param(str, Enum):
    """adaccountproduct_audiences_content_type_enum_param enum values."""

    AUTOMOTIVE_MODEL = "AUTOMOTIVE_MODEL"
    DESTINATION = "DESTINATION"
    FLIGHT = "FLIGHT"
    GENERIC = "GENERIC"
    HOME_LISTING = "HOME_LISTING"
    HOTEL = "HOTEL"
    LOCAL_SERVICE_BUSINESS = "LOCAL_SERVICE_BUSINESS"
    MEDIA_TITLE = "MEDIA_TITLE"
    OFFLINE_PRODUCT = "OFFLINE_PRODUCT"
    PRODUCT = "PRODUCT"
    VEHICLE = "VEHICLE"
    VEHICLE_OFFER = "VEHICLE_OFFER"


class adaccountadsets_billing_event_enum_param(str, Enum):
    """adaccountadsets_billing_event_enum_param enum values."""

    APP_INSTALLS = "APP_INSTALLS"
    CLICKS = "CLICKS"
    IMPRESSIONS = "IMPRESSIONS"
    LINK_CLICKS = "LINK_CLICKS"
    LISTING_INTERACTION = "LISTING_INTERACTION"
    NONE = "NONE"
    OFFER_CLAIMS = "OFFER_CLAIMS"
    PAGE_LIKES = "PAGE_LIKES"
    POST_ENGAGEMENT = "POST_ENGAGEMENT"
    PURCHASE = "PURCHASE"
    THRUPLAY = "THRUPLAY"


class adaccountadsets_creative_sequence_repetition_pattern_enum_param(str, Enum):
    """adaccountadsets_creative_sequence_repetition_pattern_enum_param enum values."""

    FULL_SEQUENCE = "FULL_SEQUENCE"
    LAST_AD = "LAST_AD"


class adaccountonbehalf_requests_status_enum_param(str, Enum):
    """adaccountonbehalf_requests_status_enum_param enum values."""

    APPROVE = "APPROVE"
    CANCELED = "CANCELED"
    DECLINE = "DECLINE"
    EXPIRED = "EXPIRED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    PENDING_EMAIL_VERIFICATION = "PENDING_EMAIL_VERIFICATION"
    PENDING_INTEGRITY_REVIEW = "PENDING_INTEGRITY_REVIEW"


class adaccountadsets_multi_optimization_goal_weight_enum_param(str, Enum):
    """adaccountadsets_multi_optimization_goal_weight_enum_param enum values."""

    BALANCED = "BALANCED"
    PREFER_EVENT = "PREFER_EVENT"
    PREFER_INSTALL = "PREFER_INSTALL"
    UNDEFINED = "UNDEFINED"


class adaccountadrules_history_action_enum_param(str, Enum):
    """adaccountadrules_history_action_enum_param enum values."""

    BUDGET_NOT_REDISTRIBUTED = "BUDGET_NOT_REDISTRIBUTED"
    CHANGED_BID = "CHANGED_BID"
    CHANGED_BUDGET = "CHANGED_BUDGET"
    CONSOLIDATE_ASC_FRAGMENTATION = "CONSOLIDATE_ASC_FRAGMENTATION"
    CONSOLIDATE_FRAGMENTATION = "CONSOLIDATE_FRAGMENTATION"
    CONVERT_ASC_CP_SINGLE_INSTANCE = "CONVERT_ASC_CP_SINGLE_INSTANCE"
    EMAIL = "EMAIL"
    ENABLE_ADVANTAGE_CAMPAIGN_BUDGET = "ENABLE_ADVANTAGE_CAMPAIGN_BUDGET"
    ENABLE_ADVANTAGE_PLUS_AUDIENCE = "ENABLE_ADVANTAGE_PLUS_AUDIENCE"
    ENABLE_ADVANTAGE_PLUS_CREATIVE = "ENABLE_ADVANTAGE_PLUS_CREATIVE"
    ENABLE_ADVANTAGE_PLUS_PLACEMENTS = "ENABLE_ADVANTAGE_PLUS_PLACEMENTS"
    ENABLE_AUTOFLOW = "ENABLE_AUTOFLOW"
    ENABLE_GEN_UNCROP = "ENABLE_GEN_UNCROP"
    ENABLE_LANDING_PAGE_VIEWS = "ENABLE_LANDING_PAGE_VIEWS"
    ENABLE_MUSIC = "ENABLE_MUSIC"
    ENABLE_REELS_PLACEMENTS = "ENABLE_REELS_PLACEMENTS"
    ENABLE_SEMANTIC_BASED_AUDIENCE_EXPANSION = "ENABLE_SEMANTIC_BASED_AUDIENCE_EXPANSION"
    ENABLE_SHOPS_ADS = "ENABLE_SHOPS_ADS"
    ENDPOINT_PINGED = "ENDPOINT_PINGED"
    ERROR = "ERROR"
    FACEBOOK_NOTIFICATION_SENT = "FACEBOOK_NOTIFICATION_SENT"
    MESSAGE_SENT = "MESSAGE_SENT"
    NOT_CHANGED = "NOT_CHANGED"
    PAUSED = "PAUSED"
    UNPAUSED = "UNPAUSED"


class adaccountad_place_page_sets_async_targeted_area_type_enum_param(str, Enum):
    """adaccountad_place_page_sets_async_targeted_area_type_enum_param enum values."""

    CUSTOM_RADIUS = "CUSTOM_RADIUS"
    MARKETING_AREA = "MARKETING_AREA"
    NONE = "NONE"


class adaccountadsets_optimization_sub_event_enum_param(str, Enum):
    """adaccountadsets_optimization_sub_event_enum_param enum values."""

    NONE = "NONE"
    TRAVEL_INTENT = "TRAVEL_INTENT"
    TRAVEL_INTENT_BUCKET_01 = "TRAVEL_INTENT_BUCKET_01"
    TRAVEL_INTENT_BUCKET_02 = "TRAVEL_INTENT_BUCKET_02"
    TRAVEL_INTENT_BUCKET_03 = "TRAVEL_INTENT_BUCKET_03"
    TRAVEL_INTENT_BUCKET_04 = "TRAVEL_INTENT_BUCKET_04"
    TRAVEL_INTENT_BUCKET_05 = "TRAVEL_INTENT_BUCKET_05"
    TRAVEL_INTENT_NO_DESTINATION_INTENT = "TRAVEL_INTENT_NO_DESTINATION_INTENT"
    TRIP_CONSIDERATION = "TRIP_CONSIDERATION"
    VIDEO_SOUND_ON = "VIDEO_SOUND_ON"


class adaccounttargetingsuggestions_app_store_enum_param(str, Enum):
    """adaccounttargetingsuggestions_app_store_enum_param enum values."""

    amazon_app_store = "amazon_app_store"
    apk_mirror = "apk_mirror"
    apk_monk = "apk_monk"
    apk_pure = "apk_pure"
    aptoide_a1_store = "aptoide_a1_store"
    bemobi_mobile_store = "bemobi_mobile_store"
    digital_turbine_store = "digital_turbine_store"
    does_not_exist = "does_not_exist"
    fb_android_store = "fb_android_store"
    fb_canvas = "fb_canvas"
    fb_gameroom = "fb_gameroom"
    galaxy_store = "galaxy_store"
    google_play = "google_play"
    instant_game = "instant_game"
    itunes = "itunes"
    itunes_ipad = "itunes_ipad"
    neon_android_store = "neon_android_store"
    none = "none"
    oculus_app_store = "oculus_app_store"
    oppo = "oppo"
    roku_channel_store = "roku_channel_store"
    uptodown = "uptodown"
    vivo = "vivo"
    windows_10_store = "windows_10_store"
    windows_store = "windows_store"
    xiaomi = "xiaomi"


class adaccountads_status_enum_param(str, Enum):
    """adaccountads_status_enum_param enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class adaccountadsets_optimization_goal_enum_param(str, Enum):
    """adaccountadsets_optimization_goal_enum_param enum values."""

    ADVERTISER_SILOED_VALUE = "ADVERTISER_SILOED_VALUE"
    AD_RECALL_LIFT = "AD_RECALL_LIFT"
    APP_INSTALLS = "APP_INSTALLS"
    APP_INSTALLS_AND_OFFSITE_CONVERSIONS = "APP_INSTALLS_AND_OFFSITE_CONVERSIONS"
    CONVERSATIONS = "CONVERSATIONS"
    DERIVED_EVENTS = "DERIVED_EVENTS"
    ENGAGED_USERS = "ENGAGED_USERS"
    EVENT_RESPONSES = "EVENT_RESPONSES"
    IMPRESSIONS = "IMPRESSIONS"
    IN_APP_VALUE = "IN_APP_VALUE"
    LANDING_PAGE_VIEWS = "LANDING_PAGE_VIEWS"
    LEAD_GENERATION = "LEAD_GENERATION"
    LINK_CLICKS = "LINK_CLICKS"
    MEANINGFUL_CALL_ATTEMPT = "MEANINGFUL_CALL_ATTEMPT"
    MESSAGING_APPOINTMENT_CONVERSION = "MESSAGING_APPOINTMENT_CONVERSION"
    MESSAGING_PURCHASE_CONVERSION = "MESSAGING_PURCHASE_CONVERSION"
    NONE = "NONE"
    OFFSITE_CONVERSIONS = "OFFSITE_CONVERSIONS"
    PAGE_LIKES = "PAGE_LIKES"
    POST_ENGAGEMENT = "POST_ENGAGEMENT"
    PROFILE_AND_PAGE_ENGAGEMENT = "PROFILE_AND_PAGE_ENGAGEMENT"
    PROFILE_VISIT = "PROFILE_VISIT"
    QUALITY_CALL = "QUALITY_CALL"
    QUALITY_LEAD = "QUALITY_LEAD"
    REACH = "REACH"
    REMINDERS_SET = "REMINDERS_SET"
    SUBSCRIBERS = "SUBSCRIBERS"
    THRUPLAY = "THRUPLAY"
    VALUE = "VALUE"
    VISIT_INSTAGRAM_PROFILE = "VISIT_INSTAGRAM_PROFILE"


class adaccountproduct_audiences_claim_objective_enum_param(str, Enum):
    """adaccountproduct_audiences_claim_objective_enum_param enum values."""

    AUTOMOTIVE_MODEL = "AUTOMOTIVE_MODEL"
    COLLABORATIVE_ADS = "COLLABORATIVE_ADS"
    HOME_LISTING = "HOME_LISTING"
    MEDIA_TITLE = "MEDIA_TITLE"
    PRODUCT = "PRODUCT"
    TRAVEL = "TRAVEL"
    VEHICLE = "VEHICLE"
    VEHICLE_OFFER = "VEHICLE_OFFER"


class adaccounttargetingsearch_app_store_enum_param(str, Enum):
    """adaccounttargetingsearch_app_store_enum_param enum values."""

    amazon_app_store = "amazon_app_store"
    apk_mirror = "apk_mirror"
    apk_monk = "apk_monk"
    apk_pure = "apk_pure"
    aptoide_a1_store = "aptoide_a1_store"
    bemobi_mobile_store = "bemobi_mobile_store"
    digital_turbine_store = "digital_turbine_store"
    does_not_exist = "does_not_exist"
    fb_android_store = "fb_android_store"
    fb_canvas = "fb_canvas"
    fb_gameroom = "fb_gameroom"
    galaxy_store = "galaxy_store"
    google_play = "google_play"
    instant_game = "instant_game"
    itunes = "itunes"
    itunes_ipad = "itunes_ipad"
    neon_android_store = "neon_android_store"
    none = "none"
    oculus_app_store = "oculus_app_store"
    oppo = "oppo"
    roku_channel_store = "roku_channel_store"
    uptodown = "uptodown"
    vivo = "vivo"
    windows_10_store = "windows_10_store"
    windows_store = "windows_store"
    xiaomi = "xiaomi"


class adaccounttargetingsuggestions_regulated_categories_enum_param(str, Enum):
    """adaccounttargetingsuggestions_regulated_categories_enum_param enum values."""

    CREDIT = "CREDIT"
    EMPLOYMENT = "EMPLOYMENT"
    FINANCIAL_PRODUCTS_SERVICES = "FINANCIAL_PRODUCTS_SERVICES"
    HOUSING = "HOUSING"
    ISSUES_ELECTIONS_POLITICS = "ISSUES_ELECTIONS_POLITICS"
    NONE = "NONE"
    ONLINE_GAMBLING_AND_GAMING = "ONLINE_GAMBLING_AND_GAMING"


class adaccountadsets_destination_type_enum_param(str, Enum):
    """adaccountadsets_destination_type_enum_param enum values."""

    APP = "APP"
    APPLINKS_AUTOMATIC = "APPLINKS_AUTOMATIC"
    FACEBOOK = "FACEBOOK"
    FACEBOOK_LIVE = "FACEBOOK_LIVE"
    FACEBOOK_PAGE = "FACEBOOK_PAGE"
    IMAGINE = "IMAGINE"
    INSTAGRAM_DIRECT = "INSTAGRAM_DIRECT"
    INSTAGRAM_LIVE = "INSTAGRAM_LIVE"
    INSTAGRAM_PROFILE = "INSTAGRAM_PROFILE"
    INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE = "INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE"
    MESSAGING_INSTAGRAM_DIRECT_MESSENGER = "MESSAGING_INSTAGRAM_DIRECT_MESSENGER"
    MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP = "MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP"
    MESSAGING_INSTAGRAM_DIRECT_WHATSAPP = "MESSAGING_INSTAGRAM_DIRECT_WHATSAPP"
    MESSAGING_MESSENGER_WHATSAPP = "MESSAGING_MESSENGER_WHATSAPP"
    MESSENGER = "MESSENGER"
    ON_AD = "ON_AD"
    ON_EVENT = "ON_EVENT"
    ON_PAGE = "ON_PAGE"
    ON_POST = "ON_POST"
    ON_VIDEO = "ON_VIDEO"
    SHOP_AUTOMATIC = "SHOP_AUTOMATIC"
    WEBSITE = "WEBSITE"
    WHATSAPP = "WHATSAPP"


class adaccountadspixels_sort_by_enum_param(str, Enum):
    """adaccountadspixels_sort_by_enum_param enum values."""

    LAST_FIRED_TIME = "LAST_FIRED_TIME"
    NAME = "NAME"


class adaccountad_place_page_sets_targeted_area_type_enum_param(str, Enum):
    """adaccountad_place_page_sets_targeted_area_type_enum_param enum values."""

    CUSTOM_RADIUS = "CUSTOM_RADIUS"
    MARKETING_AREA = "MARKETING_AREA"
    NONE = "NONE"


class adaccountagencies_permitted_tasks_enum_param(str, Enum):
    """adaccountagencies_permitted_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    DRAFT = "DRAFT"
    MANAGE = "MANAGE"


class adaccountinsights_action_breakdowns_enum_param(str, Enum):
    """adaccountinsights_action_breakdowns_enum_param enum values."""

    action_canvas_component_name = "action_canvas_component_name"
    action_carousel_card_id = "action_carousel_card_id"
    action_carousel_card_name = "action_carousel_card_name"
    action_destination = "action_destination"
    action_device = "action_device"
    action_reaction = "action_reaction"
    action_target_id = "action_target_id"
    action_type = "action_type"
    action_video_sound = "action_video_sound"
    action_video_type = "action_video_type"
    conversion_destination = "conversion_destination"
    matched_persona_id = "matched_persona_id"
    matched_persona_name = "matched_persona_name"
    signal_source_bucket = "signal_source_bucket"
    standard_event_content_type = "standard_event_content_type"


class adaccountcustomconversions_action_source_type_enum_param(str, Enum):
    """adaccountcustomconversions_action_source_type_enum_param enum values."""

    app = "app"
    business_messaging = "business_messaging"
    chat = "chat"
    email = "email"
    other = "other"
    phone_call = "phone_call"
    physical_store = "physical_store"
    system_generated = "system_generated"
    website = "website"


class adaccountasync_requests_type_enum_param(str, Enum):
    """adaccountasync_requests_type_enum_param enum values."""

    ASYNC_ADGROUP_CREATION = "ASYNC_ADGROUP_CREATION"
    BATCH_API = "BATCH_API"
    DRAFTS = "DRAFTS"


class adaccountadcreatives_categorization_criteria_enum_param(str, Enum):
    """adaccountadcreatives_categorization_criteria_enum_param enum values."""

    brand = "brand"
    category = "category"
    product_type = "product_type"


class adaccountreachfrequencypredictions_instream_packages_enum_param(str, Enum):
    """adaccountreachfrequencypredictions_instream_packages_enum_param enum values."""

    BEAUTY = "BEAUTY"
    ENTERTAINMENT = "ENTERTAINMENT"
    FOOD = "FOOD"
    NORMAL = "NORMAL"
    PREMIUM = "PREMIUM"
    REGULAR_ANIMALS_PETS = "REGULAR_ANIMALS_PETS"
    REGULAR_FOOD = "REGULAR_FOOD"
    REGULAR_GAMES = "REGULAR_GAMES"
    REGULAR_POLITICS = "REGULAR_POLITICS"
    REGULAR_SPORTS = "REGULAR_SPORTS"
    REGULAR_STYLE = "REGULAR_STYLE"
    REGULAR_TV_MOVIES = "REGULAR_TV_MOVIES"
    SPANISH = "SPANISH"
    SPORTS = "SPORTS"


class adaccountasyncadcreatives_notification_mode_enum_param(str, Enum):
    """adaccountasyncadcreatives_notification_mode_enum_param enum values."""

    OFF = "OFF"
    ON_COMPLETE = "ON_COMPLETE"


class adaccountcampaigns_bid_strategy_enum_param(str, Enum):
    """adaccountcampaigns_bid_strategy_enum_param enum values."""

    COST_CAP = "COST_CAP"
    LOWEST_COST_WITHOUT_CAP = "LOWEST_COST_WITHOUT_CAP"
    LOWEST_COST_WITH_BID_CAP = "LOWEST_COST_WITH_BID_CAP"
    LOWEST_COST_WITH_MIN_ROAS = "LOWEST_COST_WITH_MIN_ROAS"


class adaccounttargetingsearch_regulated_categories_enum_param(str, Enum):
    """adaccounttargetingsearch_regulated_categories_enum_param enum values."""

    CREDIT = "CREDIT"
    EMPLOYMENT = "EMPLOYMENT"
    FINANCIAL_PRODUCTS_SERVICES = "FINANCIAL_PRODUCTS_SERVICES"
    HOUSING = "HOUSING"
    ISSUES_ELECTIONS_POLITICS = "ISSUES_ELECTIONS_POLITICS"
    NONE = "NONE"
    ONLINE_GAMBLING_AND_GAMING = "ONLINE_GAMBLING_AND_GAMING"


class adaccountadrules_library_status_enum_param(str, Enum):
    """adaccountadrules_library_status_enum_param enum values."""

    DELETED = "DELETED"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    HAS_ISSUES = "HAS_ISSUES"


class adaccountdelivery_estimate_optimization_goal_enum_param(str, Enum):
    """adaccountdelivery_estimate_optimization_goal_enum_param enum values."""

    ADVERTISER_SILOED_VALUE = "ADVERTISER_SILOED_VALUE"
    AD_RECALL_LIFT = "AD_RECALL_LIFT"
    APP_INSTALLS = "APP_INSTALLS"
    APP_INSTALLS_AND_OFFSITE_CONVERSIONS = "APP_INSTALLS_AND_OFFSITE_CONVERSIONS"
    CONVERSATIONS = "CONVERSATIONS"
    DERIVED_EVENTS = "DERIVED_EVENTS"
    ENGAGED_USERS = "ENGAGED_USERS"
    EVENT_RESPONSES = "EVENT_RESPONSES"
    IMPRESSIONS = "IMPRESSIONS"
    IN_APP_VALUE = "IN_APP_VALUE"
    LANDING_PAGE_VIEWS = "LANDING_PAGE_VIEWS"
    LEAD_GENERATION = "LEAD_GENERATION"
    LINK_CLICKS = "LINK_CLICKS"
    MEANINGFUL_CALL_ATTEMPT = "MEANINGFUL_CALL_ATTEMPT"
    MESSAGING_APPOINTMENT_CONVERSION = "MESSAGING_APPOINTMENT_CONVERSION"
    MESSAGING_PURCHASE_CONVERSION = "MESSAGING_PURCHASE_CONVERSION"
    NONE = "NONE"
    OFFSITE_CONVERSIONS = "OFFSITE_CONVERSIONS"
    PAGE_LIKES = "PAGE_LIKES"
    POST_ENGAGEMENT = "POST_ENGAGEMENT"
    PROFILE_AND_PAGE_ENGAGEMENT = "PROFILE_AND_PAGE_ENGAGEMENT"
    PROFILE_VISIT = "PROFILE_VISIT"
    QUALITY_CALL = "QUALITY_CALL"
    QUALITY_LEAD = "QUALITY_LEAD"
    REACH = "REACH"
    REMINDERS_SET = "REMINDERS_SET"
    SUBSCRIBERS = "SUBSCRIBERS"
    THRUPLAY = "THRUPLAY"
    VALUE = "VALUE"
    VISIT_INSTAGRAM_PROFILE = "VISIT_INSTAGRAM_PROFILE"


class adaccountcampaigns_execution_options_enum_param(str, Enum):
    """adaccountcampaigns_execution_options_enum_param enum values."""

    include_recommendations = "include_recommendations"
    validate_only = "validate_only"


class adaccountadvideos_formatting_enum_param(str, Enum):
    """adaccountadvideos_formatting_enum_param enum values."""

    MARKDOWN = "MARKDOWN"
    PLAINTEXT = "PLAINTEXT"


class adaccountinsights_date_preset_enum_param(str, Enum):
    """adaccountinsights_date_preset_enum_param enum values."""

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


class adaccountadvideos_swap_mode_enum_param(str, Enum):
    """adaccountadvideos_swap_mode_enum_param enum values."""

    replace = "replace"


class adaccountinsights_action_report_time_enum_param(str, Enum):
    """adaccountinsights_action_report_time_enum_param enum values."""

    conversion = "conversion"
    impression = "impression"
    lifetime = "lifetime"
    mixed = "mixed"


class adaccountgeneratepreviews_creative_feature_enum_param(str, Enum):
    """adaccountgeneratepreviews_creative_feature_enum_param enum values."""

    product_metadata_automation = "product_metadata_automation"
    profile_card = "profile_card"
    standard_enhancements_catalog = "standard_enhancements_catalog"
    video_to_image = "video_to_image"


class adaccountcustomaudiences_subtype_enum_param(str, Enum):
    """adaccountcustomaudiences_subtype_enum_param enum values."""

    APP = "APP"
    BAG_OF_ACCOUNTS = "BAG_OF_ACCOUNTS"
    BIDDING = "BIDDING"
    CLAIM = "CLAIM"
    CUSTOM = "CUSTOM"
    ENGAGEMENT = "ENGAGEMENT"
    EXCLUSION = "EXCLUSION"
    FOX = "FOX"
    LOOKALIKE = "LOOKALIKE"
    MANAGED = "MANAGED"
    MEASUREMENT = "MEASUREMENT"
    MESSENGER_SUBSCRIBER_LIST = "MESSENGER_SUBSCRIBER_LIST"
    OFFLINE_CONVERSION = "OFFLINE_CONVERSION"
    PARTNER = "PARTNER"
    PRIMARY = "PRIMARY"
    REGULATED_CATEGORIES_AUDIENCE = "REGULATED_CATEGORIES_AUDIENCE"
    STUDY_RULE_AUDIENCE = "STUDY_RULE_AUDIENCE"
    VIDEO = "VIDEO"
    WEBSITE = "WEBSITE"


class adaccounttargetingsearch_whitelisted_types_enum_param(str, Enum):
    """adaccounttargetingsearch_whitelisted_types_enum_param enum values."""

    adgroup_id = "adgroup_id"
    age_max = "age_max"
    age_min = "age_min"
    age_range = "age_range"
    alternate_auto_targeting_option = "alternate_auto_targeting_option"
    app_install_state = "app_install_state"
    audience_network_positions = "audience_network_positions"
    behaviors = "behaviors"
    brand_safety_content_filter_levels = "brand_safety_content_filter_levels"
    brand_safety_content_severity_levels = "brand_safety_content_severity_levels"
    cafe_ca_contraction_targeting_signal = "cafe_ca_contraction_targeting_signal"
    cafe_ca_expansion_targeting_signal = "cafe_ca_expansion_targeting_signal"
    catalog_based_targeting = "catalog_based_targeting"
    cities = "cities"
    city_keys = "city_keys"
    college_years = "college_years"
    conjunctive_user_adclusters = "conjunctive_user_adclusters"
    connections = "connections"
    contextual_targeting_categories = "contextual_targeting_categories"
    countries = "countries"
    country = "country"
    country_groups = "country_groups"
    custom_audiences = "custom_audiences"
    device_platforms = "device_platforms"
    direct_install_devices = "direct_install_devices"
    dynamic_audience_ids = "dynamic_audience_ids"
    education_majors = "education_majors"
    education_schools = "education_schools"
    education_statuses = "education_statuses"
    effective_audience_network_positions = "effective_audience_network_positions"
    effective_device_platforms = "effective_device_platforms"
    effective_facebook_positions = "effective_facebook_positions"
    effective_instagram_positions = "effective_instagram_positions"
    effective_messenger_positions = "effective_messenger_positions"
    effective_oculus_positions = "effective_oculus_positions"
    effective_publisher_platforms = "effective_publisher_platforms"
    effective_threads_positions = "effective_threads_positions"
    effective_whatsapp_positions = "effective_whatsapp_positions"
    engagement_specs = "engagement_specs"
    ethnic_affinity = "ethnic_affinity"
    exclude_previous_days = "exclude_previous_days"
    exclude_reached_since = "exclude_reached_since"
    excluded_brand_safety_content_types = "excluded_brand_safety_content_types"
    excluded_connections = "excluded_connections"
    excluded_custom_audiences = "excluded_custom_audiences"
    excluded_dynamic_audience_ids = "excluded_dynamic_audience_ids"
    excluded_engagement_specs = "excluded_engagement_specs"
    excluded_geo_locations = "excluded_geo_locations"
    excluded_mobile_device_model = "excluded_mobile_device_model"
    excluded_product_audience_specs = "excluded_product_audience_specs"
    excluded_publisher_categories = "excluded_publisher_categories"
    excluded_publisher_list_ids = "excluded_publisher_list_ids"
    excluded_user_adclusters = "excluded_user_adclusters"
    excluded_user_device = "excluded_user_device"
    exclusions = "exclusions"
    expanded_implicit_custom_audiences = "expanded_implicit_custom_audiences"
    facebook_positions = "facebook_positions"
    family_statuses = "family_statuses"
    fb_deal_id = "fb_deal_id"
    flexible_spec = "flexible_spec"
    follow_profiles = "follow_profiles"
    follow_profiles_negative = "follow_profiles_negative"
    format = "format"
    friends_of_connections = "friends_of_connections"
    gatekeepers = "gatekeepers"
    genders = "genders"
    generation = "generation"
    geo_locations = "geo_locations"
    home_ownership = "home_ownership"
    home_type = "home_type"
    home_value = "home_value"
    household_composition = "household_composition"
    household_income = "household_income"
    id = "id"
    income = "income"
    industries = "industries"
    instagram_hashtags = "instagram_hashtags"
    instagram_positions = "instagram_positions"
    install_state_application = "install_state_application"
    instream_video_skippable_excluded = "instream_video_skippable_excluded"
    instream_video_sponsorship_placements = "instream_video_sponsorship_placements"
    interest_defaults_source = "interest_defaults_source"
    interested_in = "interested_in"
    interests = "interests"
    is_instagram_destination_ad = "is_instagram_destination_ad"
    is_whatsapp_destination_ad = "is_whatsapp_destination_ad"
    keywords = "keywords"
    life_events = "life_events"
    locales = "locales"
    location_categories = "location_categories"
    location_cluster_ids = "location_cluster_ids"
    location_expansion = "location_expansion"
    marketing_message_channels = "marketing_message_channels"
    marketplace_product_categories = "marketplace_product_categories"
    messenger_positions = "messenger_positions"
    mobile_device_model = "mobile_device_model"
    moms = "moms"
    net_worth = "net_worth"
    oculus_positions = "oculus_positions"
    office_type = "office_type"
    page_types = "page_types"
    place_page_set_ids = "place_page_set_ids"
    political_views = "political_views"
    politics = "politics"
    product_audience_specs = "product_audience_specs"
    prospecting_audience = "prospecting_audience"
    publisher_platforms = "publisher_platforms"
    radius = "radius"
    region_keys = "region_keys"
    regions = "regions"
    relationship_statuses = "relationship_statuses"
    rtb_flag = "rtb_flag"
    site_category = "site_category"
    subscriber_universe = "subscriber_universe"
    tafe_ca_mitigation_strategy = "tafe_ca_mitigation_strategy"
    targeting_automation = "targeting_automation"
    targeting_optimization = "targeting_optimization"
    targeting_relaxation_types = "targeting_relaxation_types"
    threads_positions = "threads_positions"
    timezones = "timezones"
    topic = "topic"
    trending = "trending"
    user_adclusters = "user_adclusters"
    user_age_unknown = "user_age_unknown"
    user_device = "user_device"
    user_event = "user_event"
    user_os = "user_os"
    user_page_threads = "user_page_threads"
    user_page_threads_excluded = "user_page_threads_excluded"
    whatsapp_positions = "whatsapp_positions"
    wireless_carrier = "wireless_carrier"
    work_employers = "work_employers"
    work_positions = "work_positions"
    zips = "zips"


class adaccountvideo_ads_upload_phase_enum_param(str, Enum):
    """adaccountvideo_ads_upload_phase_enum_param enum values."""

    FINISH = "FINISH"
    START = "START"


class adaccountcustomaudiences_subscription_info_enum_param(str, Enum):
    """adaccountcustomaudiences_subscription_info_enum_param enum values."""

    MESSENGER = "MESSENGER"
    WHATSAPP = "WHATSAPP"


class adaccountcustomaudiences_claim_objective_enum_param(str, Enum):
    """adaccountcustomaudiences_claim_objective_enum_param enum values."""

    AUTOMOTIVE_MODEL = "AUTOMOTIVE_MODEL"
    COLLABORATIVE_ADS = "COLLABORATIVE_ADS"
    HOME_LISTING = "HOME_LISTING"
    MEDIA_TITLE = "MEDIA_TITLE"
    PRODUCT = "PRODUCT"
    TRAVEL = "TRAVEL"
    VEHICLE = "VEHICLE"
    VEHICLE_OFFER = "VEHICLE_OFFER"


class adaccountinsights_level_enum_param(str, Enum):
    """adaccountinsights_level_enum_param enum values."""

    account = "account"
    ad = "ad"
    adset = "adset"
    campaign = "campaign"


class adaccountadvideos_content_category_enum_param(str, Enum):
    """adaccountadvideos_content_category_enum_param enum values."""

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


class adaccountreachfrequencypredictions_action_enum_param(str, Enum):
    """adaccountreachfrequencypredictions_action_enum_param enum values."""

    cancel = "cancel"
    quote = "quote"
    reserve = "reserve"


class adaccountadcreativesbylabels_operator_enum_param(str, Enum):
    """adaccountadcreativesbylabels_operator_enum_param enum values."""

    ALL = "ALL"
    ANY = "ANY"


class adaccountadsetsbylabels_operator_enum_param(str, Enum):
    """adaccountadsetsbylabels_operator_enum_param enum values."""

    ALL = "ALL"
    ANY = "ANY"


class adaccountadsets_effective_status_enum_param(str, Enum):
    """adaccountadsets_effective_status_enum_param enum values."""

    ACTIVE = "ACTIVE"
    ADSET_PAUSED = "ADSET_PAUSED"
    ARCHIVED = "ARCHIVED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    DELETED = "DELETED"
    DISAPPROVED = "DISAPPROVED"
    IN_PROCESS = "IN_PROCESS"
    PAUSED = "PAUSED"
    PENDING_BILLING_INFO = "PENDING_BILLING_INFO"
    PENDING_REVIEW = "PENDING_REVIEW"
    PREAPPROVED = "PREAPPROVED"
    WITH_ISSUES = "WITH_ISSUES"


class adaccountadcreatives_category_media_source_enum_param(str, Enum):
    """adaccountadcreatives_category_media_source_enum_param enum values."""

    CATEGORY = "CATEGORY"
    MIXED = "MIXED"
    PRODUCTS_COLLAGE = "PRODUCTS_COLLAGE"
    PRODUCTS_SLIDESHOW = "PRODUCTS_SLIDESHOW"


class adaccounttargetingsuggestions_objective_enum_param(str, Enum):
    """adaccounttargetingsuggestions_objective_enum_param enum values."""

    APP_INSTALLS = "APP_INSTALLS"
    BRAND_AWARENESS = "BRAND_AWARENESS"
    CONVERSIONS = "CONVERSIONS"
    EVENT_RESPONSES = "EVENT_RESPONSES"
    LEAD_GENERATION = "LEAD_GENERATION"
    LINK_CLICKS = "LINK_CLICKS"
    LOCAL_AWARENESS = "LOCAL_AWARENESS"
    MESSAGES = "MESSAGES"
    OFFER_CLAIMS = "OFFER_CLAIMS"
    OUTCOME_APP_PROMOTION = "OUTCOME_APP_PROMOTION"
    OUTCOME_AWARENESS = "OUTCOME_AWARENESS"
    OUTCOME_ENGAGEMENT = "OUTCOME_ENGAGEMENT"
    OUTCOME_LEADS = "OUTCOME_LEADS"
    OUTCOME_SALES = "OUTCOME_SALES"
    OUTCOME_TRAFFIC = "OUTCOME_TRAFFIC"
    PAGE_LIKES = "PAGE_LIKES"
    POST_ENGAGEMENT = "POST_ENGAGEMENT"
    PRODUCT_CATALOG_SALES = "PRODUCT_CATALOG_SALES"
    REACH = "REACH"
    STORE_VISITS = "STORE_VISITS"
    VIDEO_VIEWS = "VIDEO_VIEWS"


class adaccountactivities_data_source_enum_param(str, Enum):
    """adaccountactivities_data_source_enum_param enum values."""

    CALYPSO = "CALYPSO"
    TAO = "TAO"
    TAO_AD_ACCOUNT = "TAO_AD_ACCOUNT"
    TAO_AD_STATUS = "TAO_AD_STATUS"


class adaccounttargetingsuggestions_regulated_countries_enum_param(str, Enum):
    """adaccounttargetingsuggestions_regulated_countries_enum_param enum values."""

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


class adaccountreachfrequencypredictions_buying_type_enum_param(str, Enum):
    """adaccountreachfrequencypredictions_buying_type_enum_param enum values."""

    AUCTION = "AUCTION"
    DEPRECATED_REACH_BLOCK = "DEPRECATED_REACH_BLOCK"
    FIXED_CPM = "FIXED_CPM"
    MIXED = "MIXED"
    REACHBLOCK = "REACHBLOCK"
    RESEARCH_POLL = "RESEARCH_POLL"
    RESERVED = "RESERVED"


class adaccountcampaigns_smart_promotion_type_enum_param(str, Enum):
    """adaccountcampaigns_smart_promotion_type_enum_param enum values."""

    GUIDED_CREATION = "GUIDED_CREATION"
    SMART_APP_PROMOTION = "SMART_APP_PROMOTION"


class adaccountads_volume_recommendation_type_enum_param(str, Enum):
    """adaccountads_volume_recommendation_type_enum_param enum values."""

    AAC_CREATION_PACKAGE = "AAC_CREATION_PACKAGE"
    AB_TEST = "AB_TEST"
    ACCOUNT_ERROR = "ACCOUNT_ERROR"
    ACCOUNT_NEEDS_CREDIT = "ACCOUNT_NEEDS_CREDIT"
    ACCOUNT_SPEND_LIMIT = "ACCOUNT_SPEND_LIMIT"
    ACCOUNT_SPEND_LIMIT_DUPLICATION = "ACCOUNT_SPEND_LIMIT_DUPLICATION"
    ACO_TOGGLE = "ACO_TOGGLE"
    ADSET_BUDGET_SHARING = "ADSET_BUDGET_SHARING"
    ADS_REPORTING = "ADS_REPORTING"
    ADS_STATUS = "ADS_STATUS"
    ADVANCED_CAMPAIGN_BUDGET = "ADVANCED_CAMPAIGN_BUDGET"
    ADVANTAGE_APP_CAMPAIGN = "ADVANTAGE_APP_CAMPAIGN"
    ADVANTAGE_CAMPAIGN_BUDGET_DUPLICATION = "ADVANTAGE_CAMPAIGN_BUDGET_DUPLICATION"
    ADVANTAGE_CUSTOM_AUDIENCE = "ADVANTAGE_CUSTOM_AUDIENCE"
    ADVANTAGE_CUSTOM_AUDIENCE_DUPLICATION = "ADVANTAGE_CUSTOM_AUDIENCE_DUPLICATION"
    ADVANTAGE_CUSTOM_AUDIENCE_UPSELL = "ADVANTAGE_CUSTOM_AUDIENCE_UPSELL"
    ADVANTAGE_DETAILED_TARGETING = "ADVANTAGE_DETAILED_TARGETING"
    ADVANTAGE_LOOKALIKE_AUDIENCE = "ADVANTAGE_LOOKALIKE_AUDIENCE"
    ADVANTAGE_LOOKALIKE_DUPLICATION = "ADVANTAGE_LOOKALIKE_DUPLICATION"
    ADVANTAGE_PLUS_APP_CAMPAIGN = "ADVANTAGE_PLUS_APP_CAMPAIGN"
    ADVANTAGE_PLUS_APP_CAMPAIGN_PRECREATE = "ADVANTAGE_PLUS_APP_CAMPAIGN_PRECREATE"
    ADVANTAGE_PLUS_AUDIENCE = "ADVANTAGE_PLUS_AUDIENCE"
    ADVANTAGE_PLUS_AUDIENCE_DUPLICATION = "ADVANTAGE_PLUS_AUDIENCE_DUPLICATION"
    ADVANTAGE_PLUS_AUDIENCE_FRICTION = "ADVANTAGE_PLUS_AUDIENCE_FRICTION"
    ADVANTAGE_PLUS_AUDIENCE_TOGGLE = "ADVANTAGE_PLUS_AUDIENCE_TOGGLE"
    ADVANTAGE_PLUS_CAMPAIGN_BUDGET = "ADVANTAGE_PLUS_CAMPAIGN_BUDGET"
    ADVANTAGE_PLUS_CATALOG_ADS = "ADVANTAGE_PLUS_CATALOG_ADS"
    ADVANTAGE_PLUS_CREATIVE = "ADVANTAGE_PLUS_CREATIVE"
    ADVANTAGE_PLUS_CREATIVE_CATALOG = "ADVANTAGE_PLUS_CREATIVE_CATALOG"
    ADVANTAGE_PLUS_CREATIVE_SE = "ADVANTAGE_PLUS_CREATIVE_SE"
    ADVANTAGE_PLUS_LEAD_CAMPAIGN = "ADVANTAGE_PLUS_LEAD_CAMPAIGN"
    ADVANTAGE_PLUS_PLACEMENTS_DUPLICATION = "ADVANTAGE_PLUS_PLACEMENTS_DUPLICATION"
    ADVANTAGE_PLUS_PLACEMENTS_FRICTION = "ADVANTAGE_PLUS_PLACEMENTS_FRICTION"
    ADVANTAGE_PLUS_PLACEMENTS_V2_DUPLICATION = "ADVANTAGE_PLUS_PLACEMENTS_V2_DUPLICATION"
    ADVANTAGE_SHOPPING_CAMPAIGN = "ADVANTAGE_SHOPPING_CAMPAIGN"
    ADVANTAGE_SHOPPING_CAMPAIGN_FRAGMENTATION = "ADVANTAGE_SHOPPING_CAMPAIGN_FRAGMENTATION"
    AD_ACCOUNT_PLACEMENT_CONTROLS_UPSELL = "AD_ACCOUNT_PLACEMENT_CONTROLS_UPSELL"
    AD_LIFT_RECALL_GOAL = "AD_LIFT_RECALL_GOAL"
    AD_LIFT_RECALL_GOAL_PRECREATE = "AD_LIFT_RECALL_GOAL_PRECREATE"
    AD_LIFT_RECALL_OPTIMIZATION_GOAL = "AD_LIFT_RECALL_OPTIMIZATION_GOAL"
    AD_OBJECTIVE = "AD_OBJECTIVE"
    AD_SET_BUDGET_SHARING_GUIDANCE = "AD_SET_BUDGET_SHARING_GUIDANCE"
    AEM_V2_INELIGIBLE = "AEM_V2_INELIGIBLE"
    AGGREGATED_BID_LIMITED = "AGGREGATED_BID_LIMITED"
    AGGREGATED_BUDGET_LIMITED = "AGGREGATED_BUDGET_LIMITED"
    AGGREGATED_COST_LIMITED = "AGGREGATED_COST_LIMITED"
    APLUSC_ADD_OVERLAYS = "APLUSC_ADD_OVERLAYS"
    APLUSC_DYNAMIC_DESCRIPTION = "APLUSC_DYNAMIC_DESCRIPTION"
    APLUSC_IMAGE_BACKGROUND_GENERATION = "APLUSC_IMAGE_BACKGROUND_GENERATION"
    APLUSC_MUSIC = "APLUSC_MUSIC"
    APLUSC_RELEVANT_COMMENTS = "APLUSC_RELEVANT_COMMENTS"
    APLUSC_STANDARD_ENHANCEMENTS_BUNDLE = "APLUSC_STANDARD_ENHANCEMENTS_BUNDLE"
    APLUSC_TEXT_IMPROVEMENTS = "APLUSC_TEXT_IMPROVEMENTS"
    APLUSC_VISUAL_TOUCHUPS = "APLUSC_VISUAL_TOUCHUPS"
    APLUS_C_CATALOG_DUPLICATION = "APLUS_C_CATALOG_DUPLICATION"
    APP_AEM_V2_INSTALLATION_PROMOTION = "APP_AEM_V2_INSTALLATION_PROMOTION"
    APP_ENGAGED_VIEW_CONVERSIONS_DUPLICATION = "APP_ENGAGED_VIEW_CONVERSIONS_DUPLICATION"
    ASC_AUTOMATION = "ASC_AUTOMATION"
    ASC_BUDGET_OPTIMIZATION = "ASC_BUDGET_OPTIMIZATION"
    ASC_CREATION_PACKAGE = "ASC_CREATION_PACKAGE"
    ASC_FRAGMENTATION_V2 = "ASC_FRAGMENTATION_V2"
    ASC_PRECREATE = "ASC_PRECREATE"
    ASPECT_RATIO = "ASPECT_RATIO"
    ATLEAST_6_PLACEMENTS = "ATLEAST_6_PLACEMENTS"
    AUCTION_OVERLAP = "AUCTION_OVERLAP"
    AUCTION_OVERLAP_CONSOLIDATION = "AUCTION_OVERLAP_CONSOLIDATION"
    AUDIENCE_EXPANSION = "AUDIENCE_EXPANSION"
    AUDIENCE_EXPANSION_GEORADIUS = "AUDIENCE_EXPANSION_GEORADIUS"
    AUDIENCE_EXPANSION_LOOKALIKE = "AUDIENCE_EXPANSION_LOOKALIKE"
    AUDIENCE_EXPANSION_RETARGETING = "AUDIENCE_EXPANSION_RETARGETING"
    AUDIENCE_LEARNING_LIMITED = "AUDIENCE_LEARNING_LIMITED"
    AUTOBID_TO_MANUAL_BID = "AUTOBID_TO_MANUAL_BID"
    AUTOFLOW_OPT_IN = "AUTOFLOW_OPT_IN"
    AUTOFLOW_OPT_IN_FALLBACK_DUPLICATION_FLOW = "AUTOFLOW_OPT_IN_FALLBACK_DUPLICATION_FLOW"
    AUTOFLOW_OPT_IN_V2 = "AUTOFLOW_OPT_IN_V2"
    AUTOMATIC_PLACEMENTS = "AUTOMATIC_PLACEMENTS"
    AUTOMATIC_PLACEMENTS_V2 = "AUTOMATIC_PLACEMENTS_V2"
    AUTO_BID = "AUTO_BID"
    AUTO_CAT_SELECTION_ENHANCEMENT = "AUTO_CAT_SELECTION_ENHANCEMENT"
    BACKGROUND_GENERATION = "BACKGROUND_GENERATION"
    BID_LIMITED_SENSITIVE = "BID_LIMITED_SENSITIVE"
    BID_LIMITED_STARVING = "BID_LIMITED_STARVING"
    BLENDED_ADS = "BLENDED_ADS"
    BLENDED_ADS_DUPLICATION = "BLENDED_ADS_DUPLICATION"
    BLENDED_ADS_FOR_SHOPS_ADS_DUPLICATION = "BLENDED_ADS_FOR_SHOPS_ADS_DUPLICATION"
    BPBAA_WITH_CAPI_UPSELL = "BPBAA_WITH_CAPI_UPSELL"
    BROADGEO_AM_UPSELL_GUIDANCE = "BROADGEO_AM_UPSELL_GUIDANCE"
    BROAD_TARGETING = "BROAD_TARGETING"
    BUDGET_AMORTIZATION = "BUDGET_AMORTIZATION"
    BUDGET_LIMITED = "BUDGET_LIMITED"
    BUDGET_REALLOCATION = "BUDGET_REALLOCATION"
    CALL_ADS_DAYPARTING_L3_RECOMMENDATION = "CALL_ADS_DAYPARTING_L3_RECOMMENDATION"
    CAMPAIGN_GUIDANCE_NAVIGATOR_REELS_TIPS = "CAMPAIGN_GUIDANCE_NAVIGATOR_REELS_TIPS"
    CAPI = "CAPI"
    CAPI_CRM_FUNNEL = "CAPI_CRM_FUNNEL"
    CAPI_CRM_GUIDANCE = "CAPI_CRM_GUIDANCE"
    CAPI_CRM_SETUP = "CAPI_CRM_SETUP"
    CAPI_EVENT_COVERAGE = "CAPI_EVENT_COVERAGE"
    CAPI_PENETRATION = "CAPI_PENETRATION"
    CAPI_PERFORMANCE_MATCH_KEY = "CAPI_PERFORMANCE_MATCH_KEY"
    CAPI_PERFORMANCE_MATCH_KEY_V2 = "CAPI_PERFORMANCE_MATCH_KEY_V2"
    CASH_REWARDS_OPT_IN = "CASH_REWARDS_OPT_IN"
    CATALOG_DYNAMIC_MEDIA = "CATALOG_DYNAMIC_MEDIA"
    CATALOG_MATCH_RATE = "CATALOG_MATCH_RATE"
    COMMERCE_SHOPS_ADS_DUPLICATION = "COMMERCE_SHOPS_ADS_DUPLICATION"
    CONNECTED_SOURCES = "CONNECTED_SOURCES"
    CONNECTED_SOURCES_DUPLICATION = "CONNECTED_SOURCES_DUPLICATION"
    CONNECT_FACEBOOK_PAGE_TO_INSTAGRAM = "CONNECT_FACEBOOK_PAGE_TO_INSTAGRAM"
    CONNECT_FACEBOOK_PAGE_TO_WHATSAPP = "CONNECT_FACEBOOK_PAGE_TO_WHATSAPP"
    CONVERSION_LEADS_OPTIMIZATION = "CONVERSION_LEADS_OPTIMIZATION"
    CONVERSION_LEADS_OPTIMIZATION_DUPLICATION = "CONVERSION_LEADS_OPTIMIZATION_DUPLICATION"
    CONVERSION_LEAD_ADS = "CONVERSION_LEAD_ADS"
    COST_GOAL = "COST_GOAL"
    COST_GOAL_BUDGET_LIMITED = "COST_GOAL_BUDGET_LIMITED"
    COST_GOAL_CPA_LIMITED = "COST_GOAL_CPA_LIMITED"
    COST_PER_RESULT = "COST_PER_RESULT"
    CREATION_PACKAGE_UPGRADE_TO_ASC = "CREATION_PACKAGE_UPGRADE_TO_ASC"
    CREATION_PACKAGE_UPGRADE_TO_CTX = "CREATION_PACKAGE_UPGRADE_TO_CTX"
    CREATION_PACKAGE_UPGRADE_TO_TLA = "CREATION_PACKAGE_UPGRADE_TO_TLA"
    CREATION_PACKAGE_UPGRADE_TO_TMC = "CREATION_PACKAGE_UPGRADE_TO_TMC"
    CREATIVE_BADGE = "CREATIVE_BADGE"
    CREATIVE_DIVERSITY = "CREATIVE_DIVERSITY"
    CREATIVE_FATIGUE = "CREATIVE_FATIGUE"
    CREATIVE_FATIGUE_DUPLICATION = "CREATIVE_FATIGUE_DUPLICATION"
    CREATIVE_FATIGUE_HOURLY = "CREATIVE_FATIGUE_HOURLY"
    CREATIVE_LIMITED = "CREATIVE_LIMITED"
    CREATIVE_LIMITED_DUPLICATION = "CREATIVE_LIMITED_DUPLICATION"
    CREATIVE_LIMITED_HOURLY = "CREATIVE_LIMITED_HOURLY"
    CREATOR_ADS_PA_CONVERSION = "CREATOR_ADS_PA_CONVERSION"
    CTA = "CTA"
    CTM_AD_OBJECTIVE_GROWTH = "CTM_AD_OBJECTIVE_GROWTH"
    CTM_LEADS_OPTIMIZATION_UPSELL = "CTM_LEADS_OPTIMIZATION_UPSELL"
    CTX_BUDGET_OPTIMIZATION = "CTX_BUDGET_OPTIMIZATION"
    CTX_CREATION_PACKAGE = "CTX_CREATION_PACKAGE"
    CTX_CTA_UPGRADE_IN_DUPLICATION = "CTX_CTA_UPGRADE_IN_DUPLICATION"
    CTX_CTMPO_UPGRADE = "CTX_CTMPO_UPGRADE"
    CTX_CTWAPO_UPGRADE = "CTX_CTWAPO_UPGRADE"
    CTX_GUIDANCE = "CTX_GUIDANCE"
    CTX_HVS = "CTX_HVS"
    CTX_MULTI_MESSAGE_DESTINATION = "CTX_MULTI_MESSAGE_DESTINATION"
    CTX_PRECREATE = "CTX_PRECREATE"
    CTX_PRODUCT_EXTENSION_DUPLICATION = "CTX_PRODUCT_EXTENSION_DUPLICATION"
    CTX_SABR_CBO = "CTX_SABR_CBO"
    CTX_SABR_NON_CBO = "CTX_SABR_NON_CBO"
    CTX_SMART_DEFAULTING = "CTX_SMART_DEFAULTING"
    CTX_ZO_CBO = "CTX_ZO_CBO"
    CTX_ZO_NON_CBO = "CTX_ZO_NON_CBO"
    CUSTOM_AUDIENCE_RELAXATION = "CUSTOM_AUDIENCE_RELAXATION"
    DA_ADVANTAGE_PLUS_CREATIVE_INFO_LABELS = "DA_ADVANTAGE_PLUS_CREATIVE_INFO_LABELS"
    DA_DUPLICATION_PRODUCT_TAGS = "DA_DUPLICATION_PRODUCT_TAGS"
    DEAD_LINK = "DEAD_LINK"
    DEFRAGMENTATION_ACB = "DEFRAGMENTATION_ACB"
    DEFRAGMENTATION_ACB_DUPLICATION = "DEFRAGMENTATION_ACB_DUPLICATION"
    DEFRAGMENTATION_USING_VALUE_RULES_TEST_V2 = "DEFRAGMENTATION_USING_VALUE_RULES_TEST_V2"
    DELIVERY_ERROR = "DELIVERY_ERROR"
    DELIVERY_WARNING = "DELIVERY_WARNING"
    DYNAMIC_ADVANTAGE_CAMPAIGN_BUDGET = "DYNAMIC_ADVANTAGE_CAMPAIGN_BUDGET"
    ECOSYSTEM_BID_REDUCE_L1_CARDINALITY = "ECOSYSTEM_BID_REDUCE_L1_CARDINALITY"
    ENABLE_WHATS_APP_ADS_DATA_SHARING = "ENABLE_WHATS_APP_ADS_DATA_SHARING"
    ENGAGED_VIEW_CONVERSIONS_CREATION = "ENGAGED_VIEW_CONVERSIONS_CREATION"
    EVC_APP_DUPLICATION_UPGRADE = "EVC_APP_DUPLICATION_UPGRADE"
    EVC_WEB_DUPLICATION_UPGRADE = "EVC_WEB_DUPLICATION_UPGRADE"
    FRAGMENTATION = "FRAGMENTATION"
    FRAGMENTATION_RESOLUTION_UPDATE = "FRAGMENTATION_RESOLUTION_UPDATE"
    FRAGMENTATION_V2 = "FRAGMENTATION_V2"
    GENERATIVE_UNCROP_DUPLICATION = "GENERATIVE_UNCROP_DUPLICATION"
    GEN_AI_MVP = "GEN_AI_MVP"
    GES_TEST = "GES_TEST"
    GUIDANCE_CENTER_CODE_GEN = "GUIDANCE_CENTER_CODE_GEN"
    HEURISTIC_DEFAULT_DURATION = "HEURISTIC_DEFAULT_DURATION"
    HIGH_COST = "HIGH_COST"
    HISTORICAL_BENCHMARK = "HISTORICAL_BENCHMARK"
    IAA_ROAS_OPTIMIZATION = "IAA_ROAS_OPTIMIZATION"
    IG_MULTI_ADS = "IG_MULTI_ADS"
    IG_SURFACES_MANUAL_PLACEMENTS = "IG_SURFACES_MANUAL_PLACEMENTS"
    INCREMENTAL_ATTRIBUTION = "INCREMENTAL_ATTRIBUTION"
    INSTANT_FORMS_LEADS = "INSTANT_FORMS_LEADS"
    LANDING_PAGE_VIEW = "LANDING_PAGE_VIEW"
    LANDING_PAGE_VIEW_OPTIMIZATION_GOAL = "LANDING_PAGE_VIEW_OPTIMIZATION_GOAL"
    LANDING_PAGE_VIEW_PRECREATE = "LANDING_PAGE_VIEW_PRECREATE"
    LEAD_ADS_GUIDANCE = "LEAD_ADS_GUIDANCE"
    LEARNING_LIMITED = "LEARNING_LIMITED"
    LEARNING_PAUSE_FRICTION = "LEARNING_PAUSE_FRICTION"
    LEARNING_PHASE_BUDGET_EDITS = "LEARNING_PHASE_BUDGET_EDITS"
    LOW_BUDGET_UTILIZATION = "LOW_BUDGET_UTILIZATION"
    LOW_OUTCOME = "LOW_OUTCOME"
    MERLIN_GUIDANCE = "MERLIN_GUIDANCE"
    MESSAGING_EVENTS = "MESSAGING_EVENTS"
    MESSAGING_EVENTS_PRECREATE = "MESSAGING_EVENTS_PRECREATE"
    MESSAGING_PARTNERS = "MESSAGING_PARTNERS"
    MESSAGING_PARTNERS_PRECREATE = "MESSAGING_PARTNERS_PRECREATE"
    META_VERIFIED_ADS_PERFORMANCE_GUIDANCE = "META_VERIFIED_ADS_PERFORMANCE_GUIDANCE"
    MISSING_OR_INVALID_PARAMETERS = "MISSING_OR_INVALID_PARAMETERS"
    MIXED_FORMATS = "MIXED_FORMATS"
    MIXED_PA_COMBINE_ADSETS = "MIXED_PA_COMBINE_ADSETS"
    MMT_CAROUSEL_TO_VIDEO = "MMT_CAROUSEL_TO_VIDEO"
    MOBILE_FIRST_CREATIVE = "MOBILE_FIRST_CREATIVE"
    MOBILE_FIRST_VIDEO = "MOBILE_FIRST_VIDEO"
    MR_AEMV2SUB_KCONSOLIDATION = "MR_AEMV2SUB_KCONSOLIDATION"
    MULTI_ADVERTISER_ADS = "MULTI_ADVERTISER_ADS"
    MULTI_TEXT = "MULTI_TEXT"
    MUSIC = "MUSIC"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NO_DELIVERY_STATUS = "NO_DELIVERY_STATUS"
    OFFSITE_CONVERSION = "OFFSITE_CONVERSION"
    OFFSITE_CONVERSION_BASED_ON_SIGNALS = "OFFSITE_CONVERSION_BASED_ON_SIGNALS"
    OPTIMAL_BAU = "OPTIMAL_BAU"
    OUTCOME_FORECASTER_BUDGET_RECOMMENDATION = "OUTCOME_FORECASTER_BUDGET_RECOMMENDATION"
    OUTCOME_FORECASTER_SHADOW_LOGGING = "OUTCOME_FORECASTER_SHADOW_LOGGING"
    PAYMENT_METHOD = "PAYMENT_METHOD"
    PERFORMANT_CREATIVE_REELS_OPT_IN = "PERFORMANT_CREATIVE_REELS_OPT_IN"
    PFR_L1_INLINE_MMT = "PFR_L1_INLINE_MMT"
    PIXELLESS_LPV_OPTIMIZATION_GOAL = "PIXELLESS_LPV_OPTIMIZATION_GOAL"
    PIXEL_OPTIMIZATION_AAM = "PIXEL_OPTIMIZATION_AAM"
    PIXEL_OPTIMIZATION_AAM_PRECREATE = "PIXEL_OPTIMIZATION_AAM_PRECREATE"
    PIXEL_OPTIMIZATION_HIE = "PIXEL_OPTIMIZATION_HIE"
    PIXEL_OPTIMIZATION_HIE_PRECREATE = "PIXEL_OPTIMIZATION_HIE_PRECREATE"
    PIXEL_SETUP = "PIXEL_SETUP"
    PIXEL_SETUP_PRECREATE = "PIXEL_SETUP_PRECREATE"
    PIXEL_UPSELL = "PIXEL_UPSELL"
    PLACEMENTS_LIQUIDITY_AUTOMATIC_GUIDANCE = "PLACEMENTS_LIQUIDITY_AUTOMATIC_GUIDANCE"
    PREDICTIVE_CREATIVE_LIMITED = "PREDICTIVE_CREATIVE_LIMITED"
    PREDICTIVE_CREATIVE_LIMITED_HOURLY = "PREDICTIVE_CREATIVE_LIMITED_HOURLY"
    PREPARING_STATUS = "PREPARING_STATUS"
    PRODUCT_SET_BOOSTING = "PRODUCT_SET_BOOSTING"
    PROMO_ADS_UPSELL_GUIDANCE = "PROMO_ADS_UPSELL_GUIDANCE"
    PURCHASE_OPTIMIZATION = "PURCHASE_OPTIMIZATION"
    RAPID_LEARNING_LIMITED = "RAPID_LEARNING_LIMITED"
    RAPID_LEARNING_PHASE = "RAPID_LEARNING_PHASE"
    REACH_OPTIMIZATION_GOAL = "REACH_OPTIMIZATION_GOAL"
    REACH_OPTIMIZATION_GOAL_PRECREATE = "REACH_OPTIMIZATION_GOAL_PRECREATE"
    REELS_DUPLICATION_UPSELL = "REELS_DUPLICATION_UPSELL"
    REELS_MUSIC_DUPLICATION = "REELS_MUSIC_DUPLICATION"
    REELS_PC_AND_MOBILE_FIRST_CREATIVE = "REELS_PC_AND_MOBILE_FIRST_CREATIVE"
    REELS_PC_RECOMMENDATION = "REELS_PC_RECOMMENDATION"
    REELS_PERFORMANT_CREATIVE = "REELS_PERFORMANT_CREATIVE"
    REELS_PLACEMENT = "REELS_PLACEMENT"
    REVERT = "REVERT"
    REVIEW_CREATIVE_DUPLICATED_REJECTED_ADS = "REVIEW_CREATIVE_DUPLICATED_REJECTED_ADS"
    SABR_DEFAULT_DURATION = "SABR_DEFAULT_DURATION"
    SALES_CONVERSION = "SALES_CONVERSION"
    SAVED_AUDIENCE = "SAVED_AUDIENCE"
    SCALE_GOOD_CAMPAIGN = "SCALE_GOOD_CAMPAIGN"
    SCALE_GOOD_CAMPAIGN_DUPLICATION = "SCALE_GOOD_CAMPAIGN_DUPLICATION"
    SCALE_GOOD_CAMPAIGN_SMB = "SCALE_GOOD_CAMPAIGN_SMB"
    SCALE_GOOD_CTX_CAMPAIGN = "SCALE_GOOD_CTX_CAMPAIGN"
    SEASONAL_CAMPAIGNS = "SEASONAL_CAMPAIGNS"
    SEMANTIC_BASED_AUDIENCE_DUPLICATION = "SEMANTIC_BASED_AUDIENCE_DUPLICATION"
    SEMANTIC_BASED_AUDIENCE_EXPANSION = "SEMANTIC_BASED_AUDIENCE_EXPANSION"
    SETUP_PIXEL = "SETUP_PIXEL"
    SHOPS_ADS = "SHOPS_ADS"
    SHOPS_ADS_DUPLICATION = "SHOPS_ADS_DUPLICATION"
    SHOPS_ADS_SAOFF = "SHOPS_ADS_SAOFF"
    SHOPS_ADS_TRAFFIC_CAP_SETTINGS = "SHOPS_ADS_TRAFFIC_CAP_SETTINGS"
    SHOP_ADS_V2 = "SHOP_ADS_V2"
    SIGNALS_DOWN_FUNNEL_EVENT_OPTIMIZATION = "SIGNALS_DOWN_FUNNEL_EVENT_OPTIMIZATION"
    SIGNALS_GROWTH_CAPI = "SIGNALS_GROWTH_CAPI"
    SIGNALS_GROWTH_CAPI_PRECREATE = "SIGNALS_GROWTH_CAPI_PRECREATE"
    SIGNALS_GROWTH_CAPI_TABLE = "SIGNALS_GROWTH_CAPI_TABLE"
    SIGNALS_GROWTH_CAPI_V2 = "SIGNALS_GROWTH_CAPI_V2"
    SIMILAR_ADVERTISER_BUDGET_RECOMMENDATION = "SIMILAR_ADVERTISER_BUDGET_RECOMMENDATION"
    SITE_EXTENSIONS_DUPLICATION = "SITE_EXTENSIONS_DUPLICATION"
    SIX_PLUS_MANUAL_PLACEMENTS = "SIX_PLUS_MANUAL_PLACEMENTS"
    SIX_PLUS_PLACEMENTS_DUPLICATION = "SIX_PLUS_PLACEMENTS_DUPLICATION"
    SPEND_LIMIT = "SPEND_LIMIT"
    SYD_TEST_MODE = "SYD_TEST_MODE"
    TAILORED_LEAD_AD_CAMPAIGN = "TAILORED_LEAD_AD_CAMPAIGN"
    TAILORED_MESSAGES_CAMPAIGN = "TAILORED_MESSAGES_CAMPAIGN"
    TARGETING_CREATIVE_FRAGMENTATION = "TARGETING_CREATIVE_FRAGMENTATION"
    TLA_CREATION_PACKAGE = "TLA_CREATION_PACKAGE"
    TOP_ADSETS_WITH_ADS_UNDER_CAP = "TOP_ADSETS_WITH_ADS_UNDER_CAP"
    TOP_CAMPAIGNS_WITH_ADS_UNDER_CAP = "TOP_CAMPAIGNS_WITH_ADS_UNDER_CAP"
    TWO_P_GUIDANCE_CARD_AAA = "TWO_P_GUIDANCE_CARD_AAA"
    TWO_P_GUIDANCE_CARD_AUTO_PLACEMENT = "TWO_P_GUIDANCE_CARD_AUTO_PLACEMENT"
    TWO_P_GUIDANCE_CARD_CBO_OFF = "TWO_P_GUIDANCE_CARD_CBO_OFF"
    TWO_P_GUIDANCE_CARD_CTM_PREFLIGHT = "TWO_P_GUIDANCE_CARD_CTM_PREFLIGHT"
    UNCROP_IMAGE = "UNCROP_IMAGE"
    UNECONOMICAL_ADS_THROTTLING = "UNECONOMICAL_ADS_THROTTLING"
    UNIFIED_INBOX = "UNIFIED_INBOX"
    UNUSED_BUDGET = "UNUSED_BUDGET"
    VALUE_DIAGNOSTICS_GUIDANCE = "VALUE_DIAGNOSTICS_GUIDANCE"
    VALUE_OPTIMIZATION_GOAL = "VALUE_OPTIMIZATION_GOAL"
    VALUE_RULES_GUIDANCE = "VALUE_RULES_GUIDANCE"
    VIDEO_LENGTH = "VIDEO_LENGTH"
    VIDEO_VIEWS_UPSELL = "VIDEO_VIEWS_UPSELL"
    VIDEO_VIEWS_UPSELL_PRECREATE = "VIDEO_VIEWS_UPSELL_PRECREATE"
    VO_VT_1D_DEFAULTING = "VO_VT_1D_DEFAULTING"
    WA_MESSAGING_PARTNERS = "WA_MESSAGING_PARTNERS"
    WA_MESSAGING_PARTNERS_PRECREATE = "WA_MESSAGING_PARTNERS_PRECREATE"
    WEB_ENGAGED_VIEW_CONVERSIONS = "WEB_ENGAGED_VIEW_CONVERSIONS"
    WTWA_UPSELL_IN_DUPLICATION = "WTWA_UPSELL_IN_DUPLICATION"
    ZERO_CONVERSION = "ZERO_CONVERSION"
    ZERO_IMPRESSION = "ZERO_IMPRESSION"
    ZERO_OUTCOME_BUDGET = "ZERO_OUTCOME_BUDGET"


class adaccountadcreatives_authorization_category_enum_param(str, Enum):
    """adaccountadcreatives_authorization_category_enum_param enum values."""

    NONE = "NONE"
    POLITICAL = "POLITICAL"
    POLITICAL_WITH_DIGITALLY_CREATED_MEDIA = "POLITICAL_WITH_DIGITALLY_CREATED_MEDIA"


class adaccountcustomaudiences_use_for_products_enum_param(str, Enum):
    """adaccountcustomaudiences_use_for_products_enum_param enum values."""

    ADS = "ADS"
    MARKETING_MESSAGES = "MARKETING_MESSAGES"


class adaccounttargetingsearch_limit_type_enum_param(str, Enum):
    """adaccounttargetingsearch_limit_type_enum_param enum values."""

    adgroup_id = "adgroup_id"
    age_max = "age_max"
    age_min = "age_min"
    age_range = "age_range"
    alternate_auto_targeting_option = "alternate_auto_targeting_option"
    app_install_state = "app_install_state"
    audience_network_positions = "audience_network_positions"
    behaviors = "behaviors"
    brand_safety_content_filter_levels = "brand_safety_content_filter_levels"
    brand_safety_content_severity_levels = "brand_safety_content_severity_levels"
    cafe_ca_contraction_targeting_signal = "cafe_ca_contraction_targeting_signal"
    cafe_ca_expansion_targeting_signal = "cafe_ca_expansion_targeting_signal"
    catalog_based_targeting = "catalog_based_targeting"
    cities = "cities"
    city_keys = "city_keys"
    college_years = "college_years"
    conjunctive_user_adclusters = "conjunctive_user_adclusters"
    connections = "connections"
    contextual_targeting_categories = "contextual_targeting_categories"
    countries = "countries"
    country = "country"
    country_groups = "country_groups"
    custom_audiences = "custom_audiences"
    device_platforms = "device_platforms"
    direct_install_devices = "direct_install_devices"
    dynamic_audience_ids = "dynamic_audience_ids"
    education_majors = "education_majors"
    education_schools = "education_schools"
    education_statuses = "education_statuses"
    effective_audience_network_positions = "effective_audience_network_positions"
    effective_device_platforms = "effective_device_platforms"
    effective_facebook_positions = "effective_facebook_positions"
    effective_instagram_positions = "effective_instagram_positions"
    effective_messenger_positions = "effective_messenger_positions"
    effective_oculus_positions = "effective_oculus_positions"
    effective_publisher_platforms = "effective_publisher_platforms"
    effective_threads_positions = "effective_threads_positions"
    effective_whatsapp_positions = "effective_whatsapp_positions"
    engagement_specs = "engagement_specs"
    ethnic_affinity = "ethnic_affinity"
    exclude_previous_days = "exclude_previous_days"
    exclude_reached_since = "exclude_reached_since"
    excluded_brand_safety_content_types = "excluded_brand_safety_content_types"
    excluded_connections = "excluded_connections"
    excluded_custom_audiences = "excluded_custom_audiences"
    excluded_dynamic_audience_ids = "excluded_dynamic_audience_ids"
    excluded_engagement_specs = "excluded_engagement_specs"
    excluded_geo_locations = "excluded_geo_locations"
    excluded_mobile_device_model = "excluded_mobile_device_model"
    excluded_product_audience_specs = "excluded_product_audience_specs"
    excluded_publisher_categories = "excluded_publisher_categories"
    excluded_publisher_list_ids = "excluded_publisher_list_ids"
    excluded_user_adclusters = "excluded_user_adclusters"
    excluded_user_device = "excluded_user_device"
    exclusions = "exclusions"
    expanded_implicit_custom_audiences = "expanded_implicit_custom_audiences"
    facebook_positions = "facebook_positions"
    family_statuses = "family_statuses"
    fb_deal_id = "fb_deal_id"
    flexible_spec = "flexible_spec"
    follow_profiles = "follow_profiles"
    follow_profiles_negative = "follow_profiles_negative"
    format = "format"
    friends_of_connections = "friends_of_connections"
    gatekeepers = "gatekeepers"
    genders = "genders"
    generation = "generation"
    geo_locations = "geo_locations"
    home_ownership = "home_ownership"
    home_type = "home_type"
    home_value = "home_value"
    household_composition = "household_composition"
    household_income = "household_income"
    id = "id"
    income = "income"
    industries = "industries"
    instagram_hashtags = "instagram_hashtags"
    instagram_positions = "instagram_positions"
    install_state_application = "install_state_application"
    instream_video_skippable_excluded = "instream_video_skippable_excluded"
    instream_video_sponsorship_placements = "instream_video_sponsorship_placements"
    interest_defaults_source = "interest_defaults_source"
    interested_in = "interested_in"
    interests = "interests"
    is_instagram_destination_ad = "is_instagram_destination_ad"
    is_whatsapp_destination_ad = "is_whatsapp_destination_ad"
    keywords = "keywords"
    life_events = "life_events"
    locales = "locales"
    location_categories = "location_categories"
    location_cluster_ids = "location_cluster_ids"
    location_expansion = "location_expansion"
    marketing_message_channels = "marketing_message_channels"
    marketplace_product_categories = "marketplace_product_categories"
    messenger_positions = "messenger_positions"
    mobile_device_model = "mobile_device_model"
    moms = "moms"
    net_worth = "net_worth"
    oculus_positions = "oculus_positions"
    office_type = "office_type"
    page_types = "page_types"
    place_page_set_ids = "place_page_set_ids"
    political_views = "political_views"
    politics = "politics"
    product_audience_specs = "product_audience_specs"
    prospecting_audience = "prospecting_audience"
    publisher_platforms = "publisher_platforms"
    radius = "radius"
    region_keys = "region_keys"
    regions = "regions"
    relationship_statuses = "relationship_statuses"
    rtb_flag = "rtb_flag"
    site_category = "site_category"
    subscriber_universe = "subscriber_universe"
    tafe_ca_mitigation_strategy = "tafe_ca_mitigation_strategy"
    targeting_automation = "targeting_automation"
    targeting_optimization = "targeting_optimization"
    targeting_relaxation_types = "targeting_relaxation_types"
    threads_positions = "threads_positions"
    timezones = "timezones"
    topic = "topic"
    trending = "trending"
    user_adclusters = "user_adclusters"
    user_age_unknown = "user_age_unknown"
    user_device = "user_device"
    user_event = "user_event"
    user_os = "user_os"
    user_page_threads = "user_page_threads"
    user_page_threads_excluded = "user_page_threads_excluded"
    whatsapp_positions = "whatsapp_positions"
    wireless_carrier = "wireless_carrier"
    work_employers = "work_employers"
    work_positions = "work_positions"
    zips = "zips"


class adaccountadvideos_upload_phase_enum_param(str, Enum):
    """adaccountadvideos_upload_phase_enum_param enum values."""

    cancel = "cancel"
    finish = "finish"
    start = "start"
    transfer = "transfer"


class adaccountad_place_page_sets_location_types_enum_param(str, Enum):
    """adaccountad_place_page_sets_location_types_enum_param enum values."""

    home = "home"
    recent = "recent"


class adaccountinsights_summary_action_breakdowns_enum_param(str, Enum):
    """adaccountinsights_summary_action_breakdowns_enum_param enum values."""

    action_canvas_component_name = "action_canvas_component_name"
    action_carousel_card_id = "action_carousel_card_id"
    action_carousel_card_name = "action_carousel_card_name"
    action_destination = "action_destination"
    action_device = "action_device"
    action_reaction = "action_reaction"
    action_target_id = "action_target_id"
    action_type = "action_type"
    action_video_sound = "action_video_sound"
    action_video_type = "action_video_type"
    conversion_destination = "conversion_destination"
    matched_persona_id = "matched_persona_id"
    matched_persona_name = "matched_persona_name"
    signal_source_bucket = "signal_source_bucket"
    standard_event_content_type = "standard_event_content_type"


class adaccountassigned_users_tasks_enum_param(str, Enum):
    """adaccountassigned_users_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    DRAFT = "DRAFT"
    MANAGE = "MANAGE"


class adaccountbrand_safety_content_filter_levels_brand_safety_content_filter_levels_enum_param(
    str, Enum
):
    """adaccountbrand_safety_content_filter_levels_brand_safety_content_filter_levels_enum_param enum values."""

    AN_RELAXED = "AN_RELAXED"
    AN_STANDARD = "AN_STANDARD"
    AN_STRICT = "AN_STRICT"
    FACEBOOK_RELAXED = "FACEBOOK_RELAXED"
    FACEBOOK_STANDARD = "FACEBOOK_STANDARD"
    FACEBOOK_STRICT = "FACEBOOK_STRICT"
    FEED_DNM = "FEED_DNM"
    FEED_RELAXED = "FEED_RELAXED"
    FEED_STANDARD = "FEED_STANDARD"
    FEED_STRICT = "FEED_STRICT"
    UNINITIALIZED = "UNINITIALIZED"
    UNKNOWN = "UNKNOWN"


class adaccountgeneratepreviews_ad_format_enum_param(str, Enum):
    """adaccountgeneratepreviews_ad_format_enum_param enum values."""

    AUDIENCE_NETWORK_INSTREAM_VIDEO = "AUDIENCE_NETWORK_INSTREAM_VIDEO"
    AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE = "AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE"
    AUDIENCE_NETWORK_OUTSTREAM_VIDEO = "AUDIENCE_NETWORK_OUTSTREAM_VIDEO"
    AUDIENCE_NETWORK_REWARDED_VIDEO = "AUDIENCE_NETWORK_REWARDED_VIDEO"
    BIZ_DISCO_FEED_MOBILE = "BIZ_DISCO_FEED_MOBILE"
    DESKTOP_FEED_STANDARD = "DESKTOP_FEED_STANDARD"
    FACEBOOK_PROFILE_FEED_DESKTOP = "FACEBOOK_PROFILE_FEED_DESKTOP"
    FACEBOOK_PROFILE_FEED_MOBILE = "FACEBOOK_PROFILE_FEED_MOBILE"
    FACEBOOK_PROFILE_REELS_MOBILE = "FACEBOOK_PROFILE_REELS_MOBILE"
    FACEBOOK_REELS_BANNER = "FACEBOOK_REELS_BANNER"
    FACEBOOK_REELS_BANNER_DESKTOP = "FACEBOOK_REELS_BANNER_DESKTOP"
    FACEBOOK_REELS_BANNER_FULLSCREEN_IOS = "FACEBOOK_REELS_BANNER_FULLSCREEN_IOS"
    FACEBOOK_REELS_BANNER_FULLSCREEN_MOBILE = "FACEBOOK_REELS_BANNER_FULLSCREEN_MOBILE"
    FACEBOOK_REELS_MOBILE = "FACEBOOK_REELS_MOBILE"
    FACEBOOK_REELS_POSTLOOP = "FACEBOOK_REELS_POSTLOOP"
    FACEBOOK_REELS_STICKER = "FACEBOOK_REELS_STICKER"
    FACEBOOK_STORY_MOBILE = "FACEBOOK_STORY_MOBILE"
    FACEBOOK_STORY_STICKER_MOBILE = "FACEBOOK_STORY_STICKER_MOBILE"
    INSTAGRAM_EXPLORE_CONTEXTUAL = "INSTAGRAM_EXPLORE_CONTEXTUAL"
    INSTAGRAM_EXPLORE_GRID_HOME = "INSTAGRAM_EXPLORE_GRID_HOME"
    INSTAGRAM_EXPLORE_IMMERSIVE = "INSTAGRAM_EXPLORE_IMMERSIVE"
    INSTAGRAM_FEED_WEB = "INSTAGRAM_FEED_WEB"
    INSTAGRAM_FEED_WEB_M_SITE = "INSTAGRAM_FEED_WEB_M_SITE"
    INSTAGRAM_LEAD_GEN_MULTI_SUBMIT_ADS = "INSTAGRAM_LEAD_GEN_MULTI_SUBMIT_ADS"
    INSTAGRAM_PROFILE_FEED = "INSTAGRAM_PROFILE_FEED"
    INSTAGRAM_PROFILE_REELS = "INSTAGRAM_PROFILE_REELS"
    INSTAGRAM_REELS = "INSTAGRAM_REELS"
    INSTAGRAM_REELS_OVERLAY = "INSTAGRAM_REELS_OVERLAY"
    INSTAGRAM_SEARCH_CHAIN = "INSTAGRAM_SEARCH_CHAIN"
    INSTAGRAM_SEARCH_GRID = "INSTAGRAM_SEARCH_GRID"
    INSTAGRAM_STANDARD = "INSTAGRAM_STANDARD"
    INSTAGRAM_STORY = "INSTAGRAM_STORY"
    INSTAGRAM_STORY_EFFECT_TRAY = "INSTAGRAM_STORY_EFFECT_TRAY"
    INSTAGRAM_STORY_WEB = "INSTAGRAM_STORY_WEB"
    INSTAGRAM_STORY_WEB_M_SITE = "INSTAGRAM_STORY_WEB_M_SITE"
    INSTANT_ARTICLE_RECIRCULATION_AD = "INSTANT_ARTICLE_RECIRCULATION_AD"
    INSTANT_ARTICLE_STANDARD = "INSTANT_ARTICLE_STANDARD"
    INSTREAM_BANNER_DESKTOP = "INSTREAM_BANNER_DESKTOP"
    INSTREAM_BANNER_FULLSCREEN_IOS = "INSTREAM_BANNER_FULLSCREEN_IOS"
    INSTREAM_BANNER_FULLSCREEN_MOBILE = "INSTREAM_BANNER_FULLSCREEN_MOBILE"
    INSTREAM_BANNER_IMMERSIVE_MOBILE = "INSTREAM_BANNER_IMMERSIVE_MOBILE"
    INSTREAM_BANNER_MOBILE = "INSTREAM_BANNER_MOBILE"
    INSTREAM_VIDEO_DESKTOP = "INSTREAM_VIDEO_DESKTOP"
    INSTREAM_VIDEO_FULLSCREEN_IOS = "INSTREAM_VIDEO_FULLSCREEN_IOS"
    INSTREAM_VIDEO_FULLSCREEN_MOBILE = "INSTREAM_VIDEO_FULLSCREEN_MOBILE"
    INSTREAM_VIDEO_IMAGE = "INSTREAM_VIDEO_IMAGE"
    INSTREAM_VIDEO_IMMERSIVE_MOBILE = "INSTREAM_VIDEO_IMMERSIVE_MOBILE"
    INSTREAM_VIDEO_MOBILE = "INSTREAM_VIDEO_MOBILE"
    JOB_BROWSER_DESKTOP = "JOB_BROWSER_DESKTOP"
    JOB_BROWSER_MOBILE = "JOB_BROWSER_MOBILE"
    MARKETPLACE_MOBILE = "MARKETPLACE_MOBILE"
    MESSENGER_MOBILE_INBOX_MEDIA = "MESSENGER_MOBILE_INBOX_MEDIA"
    MESSENGER_MOBILE_STORY_MEDIA = "MESSENGER_MOBILE_STORY_MEDIA"
    MOBILE_BANNER = "MOBILE_BANNER"
    MOBILE_FEED_BASIC = "MOBILE_FEED_BASIC"
    MOBILE_FEED_STANDARD = "MOBILE_FEED_STANDARD"
    MOBILE_FULLWIDTH = "MOBILE_FULLWIDTH"
    MOBILE_INTERSTITIAL = "MOBILE_INTERSTITIAL"
    MOBILE_MEDIUM_RECTANGLE = "MOBILE_MEDIUM_RECTANGLE"
    MOBILE_NATIVE = "MOBILE_NATIVE"
    RIGHT_COLUMN_STANDARD = "RIGHT_COLUMN_STANDARD"
    SUGGESTED_VIDEO_DESKTOP = "SUGGESTED_VIDEO_DESKTOP"
    SUGGESTED_VIDEO_FULLSCREEN_MOBILE = "SUGGESTED_VIDEO_FULLSCREEN_MOBILE"
    SUGGESTED_VIDEO_IMMERSIVE_MOBILE = "SUGGESTED_VIDEO_IMMERSIVE_MOBILE"
    SUGGESTED_VIDEO_MOBILE = "SUGGESTED_VIDEO_MOBILE"
    WATCH_FEED_HOME = "WATCH_FEED_HOME"
    WATCH_FEED_MOBILE = "WATCH_FEED_MOBILE"


class adaccounttargetingsearch_objective_enum_param(str, Enum):
    """adaccounttargetingsearch_objective_enum_param enum values."""

    APP_INSTALLS = "APP_INSTALLS"
    BRAND_AWARENESS = "BRAND_AWARENESS"
    CONVERSIONS = "CONVERSIONS"
    EVENT_RESPONSES = "EVENT_RESPONSES"
    LEAD_GENERATION = "LEAD_GENERATION"
    LINK_CLICKS = "LINK_CLICKS"
    LOCAL_AWARENESS = "LOCAL_AWARENESS"
    MESSAGES = "MESSAGES"
    OFFER_CLAIMS = "OFFER_CLAIMS"
    OUTCOME_APP_PROMOTION = "OUTCOME_APP_PROMOTION"
    OUTCOME_AWARENESS = "OUTCOME_AWARENESS"
    OUTCOME_ENGAGEMENT = "OUTCOME_ENGAGEMENT"
    OUTCOME_LEADS = "OUTCOME_LEADS"
    OUTCOME_SALES = "OUTCOME_SALES"
    OUTCOME_TRAFFIC = "OUTCOME_TRAFFIC"
    PAGE_LIKES = "PAGE_LIKES"
    POST_ENGAGEMENT = "POST_ENGAGEMENT"
    PRODUCT_CATALOG_SALES = "PRODUCT_CATALOG_SALES"
    REACH = "REACH"
    STORE_VISITS = "STORE_VISITS"
    VIDEO_VIEWS = "VIDEO_VIEWS"


class adaccountcustomconversions_custom_event_type_enum_param(str, Enum):
    """adaccountcustomconversions_custom_event_type_enum_param enum values."""

    ADD_PAYMENT_INFO = "ADD_PAYMENT_INFO"
    ADD_TO_CART = "ADD_TO_CART"
    ADD_TO_WISHLIST = "ADD_TO_WISHLIST"
    COMPLETE_REGISTRATION = "COMPLETE_REGISTRATION"
    CONTACT = "CONTACT"
    CONTENT_VIEW = "CONTENT_VIEW"
    CUSTOMIZE_PRODUCT = "CUSTOMIZE_PRODUCT"
    DONATE = "DONATE"
    FACEBOOK_SELECTED = "FACEBOOK_SELECTED"
    FIND_LOCATION = "FIND_LOCATION"
    INITIATED_CHECKOUT = "INITIATED_CHECKOUT"
    LEAD = "LEAD"
    LISTING_INTERACTION = "LISTING_INTERACTION"
    OTHER = "OTHER"
    PURCHASE = "PURCHASE"
    SCHEDULE = "SCHEDULE"
    SEARCH = "SEARCH"
    START_TRIAL = "START_TRIAL"
    SUBMIT_APPLICATION = "SUBMIT_APPLICATION"
    SUBSCRIBE = "SUBSCRIBE"


# Field literal type
AdAccountField = Literal[
    "account_id",
    "account_status",
    "ad_account_promotable_objects",
    "age",
    "agency_client_declaration",
    "all_capabilities",
    "amount_spent",
    "attribution_spec",
    "balance",
    "brand_safety_content_filter_levels",
    "business",
    "business_city",
    "business_country_code",
    "business_name",
    "business_state",
    "business_street",
    "business_street2",
    "business_zip",
    "can_create_brand_lift_study",
    "capabilities",
    "created_time",
    "currency",
    "custom_audience_info",
    "default_dsa_beneficiary",
    "default_dsa_payor",
    "disable_reason",
    "end_advertiser",
    "end_advertiser_name",
    "existing_customers",
    "expired_funding_source_details",
    "extended_credit_invoice_group",
    "failed_delivery_checks",
    "fb_entity",
    "funding_source",
    "funding_source_details",
    "has_migrated_permissions",
    "has_page_authorized_adaccount",
    "id",
    "io_number",
    "is_attribution_spec_system_default",
    "is_ba_skip_delayed_eligible",
    "is_direct_deals_enabled",
    "is_in_3ds_authorization_enabled_market",
    "is_notifications_enabled",
    "is_personal",
    "is_prepay_account",
    "is_tax_id_required",
    "liable_address",
    "line_numbers",
    "media_agency",
    "min_campaign_group_spend_cap",
    "min_daily_budget",
    "name",
    "offsite_pixels_tos_accepted",
    "owner",
    "owner_business",
    "partner",
    "rf_spec",
    "send_bill_to_address",
    "show_checkout_experience",
    "sold_to_address",
    "spend_cap",
    "tax_id",
    "tax_id_status",
    "tax_id_type",
    "timezone_id",
    "timezone_name",
    "timezone_offset_hours_utc",
    "tos_accepted",
    "user_access_expire_time",
    "user_tasks",
    "user_tos_accepted",
    "viewable_business",
]


class AdAccountFields(BaseModel):
    """Pydantic model for AdAccount fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    account_status: int = Field(None, alias="account_status")
    ad_account_promotable_objects: AdAccountPromotableObjectsFields = Field(
        None, alias="ad_account_promotable_objects"
    )
    age: float = Field(None, alias="age")
    agency_client_declaration: AgencyClientDeclarationFields = Field(
        None, alias="agency_client_declaration"
    )
    all_capabilities: list[str] = Field(None, alias="all_capabilities")
    amount_spent: str = Field(None, alias="amount_spent")
    attribution_spec: list[AttributionSpecFields] = Field(None, alias="attribution_spec")
    balance: str = Field(None, alias="balance")
    brand_safety_content_filter_levels: list[str] = Field(
        None, alias="brand_safety_content_filter_levels"
    )
    business: BusinessFields = Field(None, alias="business")
    business_city: str = Field(None, alias="business_city")
    business_country_code: str = Field(None, alias="business_country_code")
    business_name: str = Field(None, alias="business_name")
    business_state: str = Field(None, alias="business_state")
    business_street: str = Field(None, alias="business_street")
    business_street2: str = Field(None, alias="business_street2")
    business_zip: str = Field(None, alias="business_zip")
    can_create_brand_lift_study: bool = Field(None, alias="can_create_brand_lift_study")
    capabilities: list[str] = Field(None, alias="capabilities")
    created_time: datetime = Field(None, alias="created_time")
    currency: str = Field(None, alias="currency")
    custom_audience_info: CustomAudienceGroupFields = Field(None, alias="custom_audience_info")
    default_dsa_beneficiary: str = Field(None, alias="default_dsa_beneficiary")
    default_dsa_payor: str = Field(None, alias="default_dsa_payor")
    disable_reason: int = Field(None, alias="disable_reason")
    end_advertiser: str = Field(None, alias="end_advertiser")
    end_advertiser_name: str = Field(None, alias="end_advertiser_name")
    existing_customers: list[str] = Field(None, alias="existing_customers")
    expired_funding_source_details: FundingSourceDetailsFields = Field(
        None, alias="expired_funding_source_details"
    )
    extended_credit_invoice_group: ExtendedCreditInvoiceGroupFields = Field(
        None, alias="extended_credit_invoice_group"
    )
    failed_delivery_checks: list[DeliveryCheckFields] = Field(None, alias="failed_delivery_checks")
    fb_entity: int = Field(None, alias="fb_entity")
    funding_source: str = Field(None, alias="funding_source")
    funding_source_details: FundingSourceDetailsFields = Field(None, alias="funding_source_details")
    has_migrated_permissions: bool = Field(None, alias="has_migrated_permissions")
    has_page_authorized_adaccount: bool = Field(None, alias="has_page_authorized_adaccount")
    id: str = Field(None, alias="id")
    io_number: str = Field(None, alias="io_number")
    is_attribution_spec_system_default: bool = Field(
        None, alias="is_attribution_spec_system_default"
    )
    is_ba_skip_delayed_eligible: bool = Field(None, alias="is_ba_skip_delayed_eligible")
    is_direct_deals_enabled: bool = Field(None, alias="is_direct_deals_enabled")
    is_in_3ds_authorization_enabled_market: bool = Field(
        None, alias="is_in_3ds_authorization_enabled_market"
    )
    is_notifications_enabled: bool = Field(None, alias="is_notifications_enabled")
    is_personal: int = Field(None, alias="is_personal")
    is_prepay_account: bool = Field(None, alias="is_prepay_account")
    is_tax_id_required: bool = Field(None, alias="is_tax_id_required")
    liable_address: CRMAddressFields = Field(None, alias="liable_address")
    line_numbers: list[int] = Field(None, alias="line_numbers")
    media_agency: str = Field(None, alias="media_agency")
    min_campaign_group_spend_cap: str = Field(None, alias="min_campaign_group_spend_cap")
    min_daily_budget: int = Field(None, alias="min_daily_budget")
    name: str = Field(None, alias="name")
    offsite_pixels_tos_accepted: bool = Field(None, alias="offsite_pixels_tos_accepted")
    owner: str = Field(None, alias="owner")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    partner: str = Field(None, alias="partner")
    rf_spec: ReachFrequencySpecFields = Field(None, alias="rf_spec")
    send_bill_to_address: CRMAddressFields = Field(None, alias="send_bill_to_address")
    show_checkout_experience: bool = Field(None, alias="show_checkout_experience")
    sold_to_address: CRMAddressFields = Field(None, alias="sold_to_address")
    spend_cap: str = Field(None, alias="spend_cap")
    tax_id: str = Field(None, alias="tax_id")
    tax_id_status: int = Field(None, alias="tax_id_status")
    tax_id_type: str = Field(None, alias="tax_id_type")
    timezone_id: int = Field(None, alias="timezone_id")
    timezone_name: str = Field(None, alias="timezone_name")
    timezone_offset_hours_utc: float = Field(None, alias="timezone_offset_hours_utc")
    tos_accepted: dict[str, int] = Field(None, alias="tos_accepted")
    user_access_expire_time: datetime = Field(None, alias="user_access_expire_time")
    user_tasks: list[str] = Field(None, alias="user_tasks")
    user_tos_accepted: dict[str, int] = Field(None, alias="user_tos_accepted")
    viewable_business: BusinessFields = Field(None, alias="viewable_business")


class AdAccountCreateAccountControlParams(BaseModel):
    """Parameters for AdAccount.create_account_control()."""

    model_config = ConfigDict(extra="forbid")
    audience_controls: dict[str, Any] | None = Field(
        None, description="audience_controls parameter"
    )
    placement_controls: dict[str, Any] | None = Field(
        None, description="placement_controls parameter"
    )


class AdAccountGetActivitiesParams(BaseModel):
    """Parameters for AdAccount.get_activities()."""

    model_config = ConfigDict(extra="forbid")
    add_children: bool | None = Field(None, description="add_children parameter")
    after: str | None = Field(None, description="after parameter")
    business_id: str | None = Field(None, description="business_id parameter")
    category: adaccountactivities_category_enum_param | None = Field(
        None, description="category parameter"
    )
    data_source: adaccountactivities_data_source_enum_param | None = Field(
        None, description="data_source parameter"
    )
    extra_oids: list[str] | None = Field(None, description="extra_oids parameter")
    limit: int | None = Field(None, description="limit parameter")
    oid: str | None = Field(None, description="oid parameter")
    since: datetime | None = Field(None, description="since parameter")
    uid: int | None = Field(None, description="uid parameter")
    until: datetime | None = Field(None, description="until parameter")


class AdAccountCreateAdPlacePageSetParams(BaseModel):
    """Parameters for AdAccount.create_ad_place_page_set()."""

    model_config = ConfigDict(extra="forbid")
    location_types: list[adaccountad_place_page_sets_location_types_enum_param] | None = Field(
        None, description="location_types parameter"
    )
    name: str | None = Field(None, description="name parameter")
    parent_page: str | None = Field(None, description="parent_page parameter")
    targeted_area_type: adaccountad_place_page_sets_targeted_area_type_enum_param | None = Field(
        None, description="targeted_area_type parameter"
    )


class AdAccountCreateAdPlacePageSetsAsyncParams(BaseModel):
    """Parameters for AdAccount.create_ad_place_page_sets_async()."""

    model_config = ConfigDict(extra="forbid")
    location_types: list[adaccountad_place_page_sets_async_location_types_enum_param] | None = (
        Field(None, description="location_types parameter")
    )
    name: str | None = Field(None, description="name parameter")
    parent_page: str | None = Field(None, description="parent_page parameter")
    targeted_area_type: adaccountad_place_page_sets_async_targeted_area_type_enum_param | None = (
        Field(None, description="targeted_area_type parameter")
    )


class AdAccountGetAdSavedKeywordsParams(BaseModel):
    """Parameters for AdAccount.get_ad_saved_keywords()."""

    model_config = ConfigDict(extra="forbid")
    fields: list[str] | None = Field(None, description="fields parameter")


class AdAccountCreateAdCreativeParams(BaseModel):
    """Parameters for AdAccount.create_ad_creative()."""

    model_config = ConfigDict(extra="forbid")
    actor_id: int | None = Field(None, description="actor_id parameter")
    ad_disclaimer_spec: dict[str, Any] | None = Field(
        None, description="ad_disclaimer_spec parameter"
    )
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    applink_treatment: adaccountadcreatives_applink_treatment_enum_param | None = Field(
        None, description="applink_treatment parameter"
    )
    asset_feed_spec: dict[str, Any] | None = Field(None, description="asset_feed_spec parameter")
    authorization_category: adaccountadcreatives_authorization_category_enum_param | None = Field(
        None, description="authorization_category parameter"
    )
    body: str | None = Field(None, description="body parameter")
    branded_content: dict[str, Any] | None = Field(None, description="branded_content parameter")
    branded_content_sponsor_page_id: str | None = Field(
        None, description="branded_content_sponsor_page_id parameter"
    )
    bundle_folder_id: str | None = Field(None, description="bundle_folder_id parameter")
    call_to_action: dict[str, Any] | None = Field(None, description="call_to_action parameter")
    categorization_criteria: adaccountadcreatives_categorization_criteria_enum_param | None = Field(
        None, description="categorization_criteria parameter"
    )
    category_media_source: adaccountadcreatives_category_media_source_enum_param | None = Field(
        None, description="category_media_source parameter"
    )
    contextual_multi_ads: dict[str, Any] | None = Field(
        None, description="contextual_multi_ads parameter"
    )
    creative_sourcing_spec: dict[str, Any] | None = Field(
        None, description="creative_sourcing_spec parameter"
    )
    degrees_of_freedom_spec: dict[str, Any] | None = Field(
        None, description="degrees_of_freedom_spec parameter"
    )
    destination_set_id: str | None = Field(None, description="destination_set_id parameter")
    dynamic_ad_voice: adaccountadcreatives_dynamic_ad_voice_enum_param | None = Field(
        None, description="dynamic_ad_voice parameter"
    )
    enable_launch_instant_app: bool | None = Field(
        None, description="enable_launch_instant_app parameter"
    )
    facebook_branded_content: dict[str, Any] | None = Field(
        None, description="facebook_branded_content parameter"
    )
    image_crops: dict[str, Any] | None = Field(None, description="image_crops parameter")
    image_file: str | None = Field(None, description="image_file parameter")
    image_hash: str | None = Field(None, description="image_hash parameter")
    image_url: str | None = Field(None, description="image_url parameter")
    instagram_branded_content: dict[str, Any] | None = Field(
        None, description="instagram_branded_content parameter"
    )
    instagram_permalink_url: str | None = Field(
        None, description="instagram_permalink_url parameter"
    )
    instagram_user_id: str | None = Field(None, description="instagram_user_id parameter")
    interactive_components_spec: dict[str, Any] | None = Field(
        None, description="interactive_components_spec parameter"
    )
    is_dco_internal: bool | None = Field(None, description="is_dco_internal parameter")
    link_og_id: str | None = Field(None, description="link_og_id parameter")
    link_url: str | None = Field(None, description="link_url parameter")
    name: str | None = Field(None, description="name parameter")
    object_id: int | None = Field(None, description="object_id parameter")
    object_story_id: str | None = Field(None, description="object_story_id parameter")
    object_story_spec: dict[str, Any] | None = Field(
        None, description="object_story_spec parameter"
    )
    object_type: str | None = Field(None, description="object_type parameter")
    object_url: str | None = Field(None, description="object_url parameter")
    omnichannel_link_spec: dict[str, Any] | None = Field(
        None, description="omnichannel_link_spec parameter"
    )
    page_welcome_message: str | None = Field(None, description="page_welcome_message parameter")
    place_page_set_id: str | None = Field(None, description="place_page_set_id parameter")
    platform_customizations: dict[str, Any] | None = Field(
        None, description="platform_customizations parameter"
    )
    playable_asset_id: str | None = Field(None, description="playable_asset_id parameter")
    portrait_customizations: dict[str, Any] | None = Field(
        None, description="portrait_customizations parameter"
    )
    product_set_id: str | None = Field(None, description="product_set_id parameter")
    recommender_settings: dict[str, Any] | None = Field(
        None, description="recommender_settings parameter"
    )
    regional_regulation_disclaimer_spec: dict[str, Any] | None = Field(
        None, description="regional_regulation_disclaimer_spec parameter"
    )
    source_instagram_media_id: str | None = Field(
        None, description="source_instagram_media_id parameter"
    )
    template_url: str | None = Field(None, description="template_url parameter")
    template_url_spec: str | None = Field(None, description="template_url_spec parameter")
    thumbnail_url: str | None = Field(None, description="thumbnail_url parameter")
    title: str | None = Field(None, description="title parameter")
    url_tags: str | None = Field(None, description="url_tags parameter")
    use_page_actor_override: bool | None = Field(
        None, description="use_page_actor_override parameter"
    )


class AdAccountGetAdCreativesByLabelsParams(BaseModel):
    """Parameters for AdAccount.get_ad_creatives_by_labels()."""

    model_config = ConfigDict(extra="forbid")
    ad_label_ids: list[str] | None = Field(None, description="ad_label_ids parameter")
    operator: adaccountadcreativesbylabels_operator_enum_param | None = Field(
        None, description="operator parameter"
    )


class AdAccountDeleteAdImagesParams(BaseModel):
    """Parameters for AdAccount.delete_ad_images()."""

    model_config = ConfigDict(extra="forbid")
    hash: str | None = Field(None, description="hash parameter")


class AdAccountGetAdImagesParams(BaseModel):
    """Parameters for AdAccount.get_ad_images()."""

    model_config = ConfigDict(extra="forbid")
    biz_tag_id: int | None = Field(None, description="biz_tag_id parameter")
    business_id: str | None = Field(None, description="business_id parameter")
    hashes: list[str] | None = Field(None, description="hashes parameter")
    minheight: int | None = Field(None, description="minheight parameter")
    minwidth: int | None = Field(None, description="minwidth parameter")
    name: str | None = Field(None, description="name parameter")
    selected_hashes: list[str] | None = Field(None, description="selected_hashes parameter")


class AdAccountCreateAdImageParams(BaseModel):
    """Parameters for AdAccount.create_ad_image()."""

    model_config = ConfigDict(extra="forbid")
    bytes: str | None = Field(None, description="bytes parameter")
    copy_from: dict[str, Any] | None = Field(None, description="copy_from parameter")


class AdAccountCreateAdLabelParams(BaseModel):
    """Parameters for AdAccount.create_ad_label()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")


class AdAccountCreateAdPlayableParams(BaseModel):
    """Parameters for AdAccount.create_ad_playable()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")
    name: str | None = Field(None, description="name parameter")
    session_id: str | None = Field(None, description="session_id parameter")
    source: dict[str, Any] | None = Field(None, description="source parameter")
    source_url: str | None = Field(None, description="source_url parameter")
    source_zip: dict[str, Any] | None = Field(None, description="source_zip parameter")


class AdAccountGetAdrulesHistoryParams(BaseModel):
    """Parameters for AdAccount.get_adrules_history()."""

    model_config = ConfigDict(extra="forbid")
    action: adaccountadrules_history_action_enum_param | None = Field(
        None, description="action parameter"
    )
    evaluation_type: adaccountadrules_history_evaluation_type_enum_param | None = Field(
        None, description="evaluation_type parameter"
    )
    hide_no_changes: bool | None = Field(None, description="hide_no_changes parameter")
    object_id: str | None = Field(None, description="object_id parameter")


class AdAccountCreateAdrulesLibraryParams(BaseModel):
    """Parameters for AdAccount.create_adrules_library()."""

    model_config = ConfigDict(extra="forbid")
    account_id: str | None = Field(None, description="account_id parameter")
    evaluation_spec: dict[str, Any] | None = Field(None, description="evaluation_spec parameter")
    execution_spec: dict[str, Any] | None = Field(None, description="execution_spec parameter")
    name: str | None = Field(None, description="name parameter")
    schedule_spec: dict[str, Any] | None = Field(None, description="schedule_spec parameter")
    status: adaccountadrules_library_status_enum_param | None = Field(
        None, description="status parameter"
    )
    ui_creation_source: adaccountadrules_library_ui_creation_source_enum_param | None = Field(
        None, description="ui_creation_source parameter"
    )


class AdAccountGetAdSParams(BaseModel):
    """Parameters for AdAccount.get_ad_s()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adaccountads_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[str] | None = Field(None, description="effective_status parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    updated_since: int | None = Field(None, description="updated_since parameter")


class AdAccountCreateAdParams(BaseModel):
    """Parameters for AdAccount.create_ad_()."""

    model_config = ConfigDict(extra="forbid")
    ad_schedule_end_time: datetime | None = Field(
        None, description="ad_schedule_end_time parameter"
    )
    ad_schedule_start_time: datetime | None = Field(
        None, description="ad_schedule_start_time parameter"
    )
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    adset_id: int | None = Field(None, description="adset_id parameter")
    adset_spec: dict[str, Any] | None = Field(None, description="adset_spec parameter")
    audience_id: str | None = Field(None, description="audience_id parameter")
    bid_amount: int | None = Field(None, description="bid_amount parameter")
    conversion_domain: str | None = Field(None, description="conversion_domain parameter")
    creative: dict[str, Any] | None = Field(None, description="creative parameter")
    creative_asset_groups_spec: dict[str, Any] | None = Field(
        None, description="creative_asset_groups_spec parameter"
    )
    date_format: str | None = Field(None, description="date_format parameter")
    display_sequence: int | None = Field(None, description="display_sequence parameter")
    draft_adgroup_id: str | None = Field(None, description="draft_adgroup_id parameter")
    engagement_audience: bool | None = Field(None, description="engagement_audience parameter")
    execution_options: list[adaccountads_execution_options_enum_param] | None = Field(
        None, description="execution_options parameter"
    )
    include_demolink_hashes: bool | None = Field(
        None, description="include_demolink_hashes parameter"
    )
    name: str | None = Field(None, description="name parameter")
    priority: int | None = Field(None, description="priority parameter")
    source_ad_id: str | None = Field(None, description="source_ad_id parameter")
    status: adaccountads_status_enum_param | None = Field(None, description="status parameter")
    tracking_specs: dict[str, Any] | None = Field(None, description="tracking_specs parameter")


class AdAccountGetAdsReportingMmmReportsParams(BaseModel):
    """Parameters for AdAccount.get_ads_reporting_mmm_reports()."""

    model_config = ConfigDict(extra="forbid")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")


class AdAccountGetAdsVolumeParams(BaseModel):
    """Parameters for AdAccount.get_ads_volume()."""

    model_config = ConfigDict(extra="forbid")
    page_id: str | None = Field(None, description="page_id parameter")
    recommendation_type: adaccountads_volume_recommendation_type_enum_param | None = Field(
        None, description="recommendation_type parameter"
    )
    show_breakdown_by_actor: bool | None = Field(
        None, description="show_breakdown_by_actor parameter"
    )


class AdAccountGetAdSByLabelsParams(BaseModel):
    """Parameters for AdAccount.get_ad_s_by_labels()."""

    model_config = ConfigDict(extra="forbid")
    ad_label_ids: list[str] | None = Field(None, description="ad_label_ids parameter")
    operator: adaccountadsbylabels_operator_enum_param | None = Field(
        None, description="operator parameter"
    )


class AdAccountGetAdSetsParams(BaseModel):
    """Parameters for AdAccount.get_ad_sets()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adaccountadsets_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[adaccountadsets_effective_status_enum_param] | None = Field(
        None, description="effective_status parameter"
    )
    is_completed: bool | None = Field(None, description="is_completed parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    updated_since: int | None = Field(None, description="updated_since parameter")


class AdAccountCreateAdSetParams(BaseModel):
    """Parameters for AdAccount.create_ad_set()."""

    model_config = ConfigDict(extra="forbid")
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    adset_schedule: list[dict[str, Any]] | None = Field(
        None, description="adset_schedule parameter"
    )
    attribution_spec: list[dict[str, Any]] | None = Field(
        None, description="attribution_spec parameter"
    )
    bid_adjustments: dict[str, Any] | None = Field(None, description="bid_adjustments parameter")
    bid_amount: int | None = Field(None, description="bid_amount parameter")
    bid_constraints: dict[str, dict[str, Any]] | None = Field(
        None, description="bid_constraints parameter"
    )
    bid_strategy: adaccountadsets_bid_strategy_enum_param | None = Field(
        None, description="bid_strategy parameter"
    )
    billing_event: adaccountadsets_billing_event_enum_param | None = Field(
        None, description="billing_event parameter"
    )
    budget_source: adaccountadsets_budget_source_enum_param | None = Field(
        None, description="budget_source parameter"
    )
    budget_split_set_id: str | None = Field(None, description="budget_split_set_id parameter")
    campaign_attribution: dict[str, Any] | None = Field(
        None, description="campaign_attribution parameter"
    )
    campaign_id: str | None = Field(None, description="campaign_id parameter")
    campaign_spec: dict[str, Any] | None = Field(None, description="campaign_spec parameter")
    creative_sequence: list[str] | None = Field(None, description="creative_sequence parameter")
    creative_sequence_repetition_pattern: (
        adaccountadsets_creative_sequence_repetition_pattern_enum_param | None
    ) = Field(None, description="creative_sequence_repetition_pattern parameter")
    daily_budget: int | None = Field(None, description="daily_budget parameter")
    daily_imps: int | None = Field(None, description="daily_imps parameter")
    daily_min_spend_target: int | None = Field(None, description="daily_min_spend_target parameter")
    daily_spend_cap: int | None = Field(None, description="daily_spend_cap parameter")
    date_format: str | None = Field(None, description="date_format parameter")
    destination_type: adaccountadsets_destination_type_enum_param | None = Field(
        None, description="destination_type parameter"
    )
    dsa_beneficiary: str | None = Field(None, description="dsa_beneficiary parameter")
    dsa_payor: str | None = Field(None, description="dsa_payor parameter")
    end_time: datetime | None = Field(None, description="end_time parameter")
    execution_options: list[adaccountadsets_execution_options_enum_param] | None = Field(
        None, description="execution_options parameter"
    )
    existing_customer_budget_percentage: int | None = Field(
        None, description="existing_customer_budget_percentage parameter"
    )
    frequency_control_specs: list[dict[str, Any]] | None = Field(
        None, description="frequency_control_specs parameter"
    )
    full_funnel_exploration_mode: adaccountadsets_full_funnel_exploration_mode_enum_param | None = (
        Field(None, description="full_funnel_exploration_mode parameter")
    )
    is_ba_skip_delayed_eligible: bool | None = Field(
        None, description="is_ba_skip_delayed_eligible parameter"
    )
    is_dynamic_creative: bool | None = Field(None, description="is_dynamic_creative parameter")
    is_incremental_attribution_enabled: bool | None = Field(
        None, description="is_incremental_attribution_enabled parameter"
    )
    is_sac_cfca_terms_certified: bool | None = Field(
        None, description="is_sac_cfca_terms_certified parameter"
    )
    lifetime_budget: int | None = Field(None, description="lifetime_budget parameter")
    lifetime_imps: int | None = Field(None, description="lifetime_imps parameter")
    lifetime_min_spend_target: int | None = Field(
        None, description="lifetime_min_spend_target parameter"
    )
    lifetime_spend_cap: int | None = Field(None, description="lifetime_spend_cap parameter")
    line_number: int | None = Field(None, description="line_number parameter")
    max_budget_spend_percentage: int | None = Field(
        None, description="max_budget_spend_percentage parameter"
    )
    min_budget_spend_percentage: int | None = Field(
        None, description="min_budget_spend_percentage parameter"
    )
    multi_optimization_goal_weight: (
        adaccountadsets_multi_optimization_goal_weight_enum_param | None
    ) = Field(None, description="multi_optimization_goal_weight parameter")
    name: str | None = Field(None, description="name parameter")
    optimization_goal: adaccountadsets_optimization_goal_enum_param | None = Field(
        None, description="optimization_goal parameter"
    )
    optimization_sub_event: adaccountadsets_optimization_sub_event_enum_param | None = Field(
        None, description="optimization_sub_event parameter"
    )
    pacing_type: list[str] | None = Field(None, description="pacing_type parameter")
    promoted_object: dict[str, Any] | None = Field(None, description="promoted_object parameter")
    rb_prediction_id: str | None = Field(None, description="rb_prediction_id parameter")
    regional_regulated_categories: (
        list[adaccountadsets_regional_regulated_categories_enum_param] | None
    ) = Field(None, description="regional_regulated_categories parameter")
    regional_regulation_identities: dict[str, Any] | None = Field(
        None, description="regional_regulation_identities parameter"
    )
    rf_prediction_id: str | None = Field(None, description="rf_prediction_id parameter")
    source_adset_id: str | None = Field(None, description="source_adset_id parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")
    status: adaccountadsets_status_enum_param | None = Field(None, description="status parameter")
    targeting: dict[str, Any] | None = Field(None, description="targeting parameter")
    time_based_ad_rotation_id_blocks: list[list[int]] | None = Field(
        None, description="time_based_ad_rotation_id_blocks parameter"
    )
    time_based_ad_rotation_intervals: list[int] | None = Field(
        None, description="time_based_ad_rotation_intervals parameter"
    )
    time_start: datetime | None = Field(None, description="time_start parameter")
    time_stop: datetime | None = Field(None, description="time_stop parameter")
    topline_id: str | None = Field(None, description="topline_id parameter")
    tune_for_category: adaccountadsets_tune_for_category_enum_param | None = Field(
        None, description="tune_for_category parameter"
    )


class AdAccountGetAdSetsByLabelsParams(BaseModel):
    """Parameters for AdAccount.get_ad_sets_by_labels()."""

    model_config = ConfigDict(extra="forbid")
    ad_label_ids: list[str] | None = Field(None, description="ad_label_ids parameter")
    operator: adaccountadsetsbylabels_operator_enum_param | None = Field(
        None, description="operator parameter"
    )


class AdAccountGetAdSpixelsParams(BaseModel):
    """Parameters for AdAccount.get_ad_spixels()."""

    model_config = ConfigDict(extra="forbid")
    sort_by: adaccountadspixels_sort_by_enum_param | None = Field(
        None, description="sort_by parameter"
    )


class AdAccountCreateAdSpixelParams(BaseModel):
    """Parameters for AdAccount.create_ad_spixel()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")


class AdAccountGetAdvertisableApplicationsParams(BaseModel):
    """Parameters for AdAccount.get_advertisable_applications()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")
    business_id: str | None = Field(None, description="business_id parameter")


class AdAccountDeleteAdVideosParams(BaseModel):
    """Parameters for AdAccount.delete_ad_videos()."""

    model_config = ConfigDict(extra="forbid")
    video_id: str | None = Field(None, description="video_id parameter")


class AdAccountGetAdVideosParams(BaseModel):
    """Parameters for AdAccount.get_ad_videos()."""

    model_config = ConfigDict(extra="forbid")
    max_aspect_ratio: float | None = Field(None, description="max_aspect_ratio parameter")
    maxheight: int | None = Field(None, description="maxheight parameter")
    maxlength: int | None = Field(None, description="maxlength parameter")
    maxwidth: int | None = Field(None, description="maxwidth parameter")
    min_aspect_ratio: float | None = Field(None, description="min_aspect_ratio parameter")
    minheight: int | None = Field(None, description="minheight parameter")
    minlength: int | None = Field(None, description="minlength parameter")
    minwidth: int | None = Field(None, description="minwidth parameter")
    title: str | None = Field(None, description="title parameter")


class AdAccountCreateAdVideoParams(BaseModel):
    """Parameters for AdAccount.create_ad_video()."""

    model_config = ConfigDict(extra="forbid")
    application_id: str | None = Field(None, description="application_id parameter")
    asked_fun_fact_prompt_id: int | None = Field(
        None, description="asked_fun_fact_prompt_id parameter"
    )
    audio_story_wave_animation_handle: str | None = Field(
        None, description="audio_story_wave_animation_handle parameter"
    )
    chunk_session_id: str | None = Field(None, description="chunk_session_id parameter")
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
    container_type: adaccountadvideos_container_type_enum_param | None = Field(
        None, description="container_type parameter"
    )
    content_category: adaccountadvideos_content_category_enum_param | None = Field(
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
    formatting: adaccountadvideos_formatting_enum_param | None = Field(
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
    is_group_linking_post: bool | None = Field(None, description="is_group_linking_post parameter")
    is_partnership_ad: bool | None = Field(None, description="is_partnership_ad parameter")
    is_voice_clip: bool | None = Field(None, description="is_voice_clip parameter")
    location_source_id: str | None = Field(None, description="location_source_id parameter")
    name: str | None = Field(None, description="name parameter")
    og_action_type_id: str | None = Field(None, description="og_action_type_id parameter")
    og_icon_id: str | None = Field(None, description="og_icon_id parameter")
    og_object_id: str | None = Field(None, description="og_object_id parameter")
    og_phrase: str | None = Field(None, description="og_phrase parameter")
    og_suggestion_mechanism: str | None = Field(
        None, description="og_suggestion_mechanism parameter"
    )
    original_fov: int | None = Field(None, description="original_fov parameter")
    original_projection_type: adaccountadvideos_original_projection_type_enum_param | None = Field(
        None, description="original_projection_type parameter"
    )
    partnership_ad_ad_code: str | None = Field(None, description="partnership_ad_ad_code parameter")
    publish_event_id: int | None = Field(None, description="publish_event_id parameter")
    referenced_sticker_id: str | None = Field(None, description="referenced_sticker_id parameter")
    replace_video_id: str | None = Field(None, description="replace_video_id parameter")
    slideshow_spec: dict[str, Any] | None = Field(None, description="slideshow_spec parameter")
    source: str | None = Field(None, description="source parameter")
    source_instagram_media_id: str | None = Field(
        None, description="source_instagram_media_id parameter"
    )
    spherical: bool | None = Field(None, description="spherical parameter")
    start_offset: int | None = Field(None, description="start_offset parameter")
    swap_mode: adaccountadvideos_swap_mode_enum_param | None = Field(
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
    unpublished_content_type: adaccountadvideos_unpublished_content_type_enum_param | None = Field(
        None, description="unpublished_content_type parameter"
    )
    upload_phase: adaccountadvideos_upload_phase_enum_param | None = Field(
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


class AdAccountDeleteAgenciesParams(BaseModel):
    """Parameters for AdAccount.delete_agencies()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class AdAccountCreateAgencieParams(BaseModel):
    """Parameters for AdAccount.create_agencie()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")
    permitted_tasks: list[adaccountagencies_permitted_tasks_enum_param] | None = Field(
        None, description="permitted_tasks parameter"
    )


class AdAccountDeleteAssignedUsersParams(BaseModel):
    """Parameters for AdAccount.delete_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    user: int | None = Field(None, description="user parameter")


class AdAccountGetAssignedUsersParams(BaseModel):
    """Parameters for AdAccount.get_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class AdAccountCreateAssignedUserParams(BaseModel):
    """Parameters for AdAccount.create_assigned_user()."""

    model_config = ConfigDict(extra="forbid")
    tasks: list[adaccountassigned_users_tasks_enum_param] | None = Field(
        None, description="tasks parameter"
    )
    user: int | None = Field(None, description="user parameter")


class AdAccountCreateAsyncBatchRequestParams(BaseModel):
    """Parameters for AdAccount.create_async_batch_request()."""

    model_config = ConfigDict(extra="forbid")
    adbatch: list[dict[str, Any]] | None = Field(None, description="adbatch parameter")
    name: str | None = Field(None, description="name parameter")


class AdAccountGetAsyncRequestsParams(BaseModel):
    """Parameters for AdAccount.get_async_requests()."""

    model_config = ConfigDict(extra="forbid")
    status: adaccountasync_requests_status_enum_param | None = Field(
        None, description="status parameter"
    )
    type: adaccountasync_requests_type_enum_param | None = Field(None, description="type parameter")


class AdAccountGetAsyncAdCreativesParams(BaseModel):
    """Parameters for AdAccount.get_async_ad_creatives()."""

    model_config = ConfigDict(extra="forbid")
    is_completed: bool | None = Field(None, description="is_completed parameter")


class AdAccountCreateAsyncAdCreativeParams(BaseModel):
    """Parameters for AdAccount.create_async_ad_creative()."""

    model_config = ConfigDict(extra="forbid")
    creative_spec: dict[str, Any] | None = Field(None, description="creative_spec parameter")
    name: str | None = Field(None, description="name parameter")
    notification_mode: adaccountasyncadcreatives_notification_mode_enum_param | None = Field(
        None, description="notification_mode parameter"
    )
    notification_uri: str | None = Field(None, description="notification_uri parameter")


class AdAccountGetAsyncAdrequestsetsParams(BaseModel):
    """Parameters for AdAccount.get_async_adrequestsets()."""

    model_config = ConfigDict(extra="forbid")
    is_completed: bool | None = Field(None, description="is_completed parameter")


class AdAccountCreateAsyncAdrequestsetParams(BaseModel):
    """Parameters for AdAccount.create_async_adrequestset()."""

    model_config = ConfigDict(extra="forbid")
    ad_specs: list[dict[str, Any]] | None = Field(None, description="ad_specs parameter")
    name: str | None = Field(None, description="name parameter")
    notification_mode: adaccountasyncadrequestsets_notification_mode_enum_param | None = Field(
        None, description="notification_mode parameter"
    )
    notification_uri: str | None = Field(None, description="notification_uri parameter")


class AdAccountCreateBlockListDraftParams(BaseModel):
    """Parameters for AdAccount.create_block_list_draft()."""

    model_config = ConfigDict(extra="forbid")
    publisher_urls_file: dict[str, Any] | None = Field(
        None, description="publisher_urls_file parameter"
    )


class AdAccountCreateBrandSafetyContentFilterLevelParams(BaseModel):
    """Parameters for AdAccount.create_brand_safety_content_filter_level()."""

    model_config = ConfigDict(extra="forbid")
    brand_safety_content_filter_levels: (
        list[
            adaccountbrand_safety_content_filter_levels_brand_safety_content_filter_levels_enum_param
        ]
        | None
    ) = Field(None, description="brand_safety_content_filter_levels parameter")
    business_id: str | None = Field(None, description="business_id parameter")


class AdAccountGetBroadtargetingcategoriesParams(BaseModel):
    """Parameters for AdAccount.get_broadtargetingcategories()."""

    model_config = ConfigDict(extra="forbid")
    custom_categories_only: bool | None = Field(
        None, description="custom_categories_only parameter"
    )


class AdAccountGetBusinessprojectsParams(BaseModel):
    """Parameters for AdAccount.get_businessprojects()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class AdAccountDeleteCampaignsParams(BaseModel):
    """Parameters for AdAccount.delete_campaigns()."""

    model_config = ConfigDict(extra="forbid")
    before_date: datetime | None = Field(None, description="before_date parameter")
    delete_offset: int | None = Field(None, description="delete_offset parameter")
    delete_strategy: adaccountcampaigns_delete_strategy_enum_param | None = Field(
        None, description="delete_strategy parameter"
    )
    object_count: int | None = Field(None, description="object_count parameter")


class AdAccountGetCampaignsParams(BaseModel):
    """Parameters for AdAccount.get_campaigns()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adaccountcampaigns_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[adaccountcampaigns_effective_status_enum_param] | None = Field(
        None, description="effective_status parameter"
    )
    is_completed: bool | None = Field(None, description="is_completed parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")


class AdAccountCreateCampaignParams(BaseModel):
    """Parameters for AdAccount.create_campaign()."""

    model_config = ConfigDict(extra="forbid")
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    bid_strategy: adaccountcampaigns_bid_strategy_enum_param | None = Field(
        None, description="bid_strategy parameter"
    )
    buying_type: str | None = Field(None, description="buying_type parameter")
    daily_budget: int | None = Field(None, description="daily_budget parameter")
    execution_options: list[adaccountcampaigns_execution_options_enum_param] | None = Field(
        None, description="execution_options parameter"
    )
    is_skadnetwork_attribution: bool | None = Field(
        None, description="is_skadnetwork_attribution parameter"
    )
    iterative_split_test_configs: list[dict[str, Any]] | None = Field(
        None, description="iterative_split_test_configs parameter"
    )
    lifetime_budget: int | None = Field(None, description="lifetime_budget parameter")
    name: str | None = Field(None, description="name parameter")
    objective: adaccountcampaigns_objective_enum_param | None = Field(
        None, description="objective parameter"
    )
    pacing_type: list[str] | None = Field(None, description="pacing_type parameter")
    promoted_object: dict[str, Any] | None = Field(None, description="promoted_object parameter")
    smart_promotion_type: adaccountcampaigns_smart_promotion_type_enum_param | None = Field(
        None, description="smart_promotion_type parameter"
    )
    source_campaign_id: str | None = Field(None, description="source_campaign_id parameter")
    special_ad_categories: list[adaccountcampaigns_special_ad_categories_enum_param] | None = Field(
        None, description="special_ad_categories parameter"
    )
    special_ad_category_country: (
        list[adaccountcampaigns_special_ad_category_country_enum_param] | None
    ) = Field(None, description="special_ad_category_country parameter")
    spend_cap: int | None = Field(None, description="spend_cap parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")
    status: adaccountcampaigns_status_enum_param | None = Field(
        None, description="status parameter"
    )
    stop_time: datetime | None = Field(None, description="stop_time parameter")
    topline_id: str | None = Field(None, description="topline_id parameter")


class AdAccountGetCampaignsByLabelsParams(BaseModel):
    """Parameters for AdAccount.get_campaigns_by_labels()."""

    model_config = ConfigDict(extra="forbid")
    ad_label_ids: list[str] | None = Field(None, description="ad_label_ids parameter")
    operator: adaccountcampaignsbylabels_operator_enum_param | None = Field(
        None, description="operator parameter"
    )


class AdAccountGetConnectedInstagramAccountsWithIabpParams(BaseModel):
    """Parameters for AdAccount.get_connected_instagram_accounts_with_iabp()."""

    model_config = ConfigDict(extra="forbid")
    business_id: str | None = Field(None, description="business_id parameter")


class AdAccountGetCustomAudiencesParams(BaseModel):
    """Parameters for AdAccount.get_custom_audiences()."""

    model_config = ConfigDict(extra="forbid")
    business_id: str | None = Field(None, description="business_id parameter")
    fetch_primary_audience: bool | None = Field(
        None, description="fetch_primary_audience parameter"
    )
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    pixel_id: str | None = Field(None, description="pixel_id parameter")


class AdAccountCreateCustomAudienceParams(BaseModel):
    """Parameters for AdAccount.create_custom_audience()."""

    model_config = ConfigDict(extra="forbid")
    allowed_domains: list[str] | None = Field(None, description="allowed_domains parameter")
    associated_audience_id: int | None = Field(None, description="associated_audience_id parameter")
    claim_objective: adaccountcustomaudiences_claim_objective_enum_param | None = Field(
        None, description="claim_objective parameter"
    )
    content_type: adaccountcustomaudiences_content_type_enum_param | None = Field(
        None, description="content_type parameter"
    )
    countries: str | None = Field(None, description="countries parameter")
    creation_params: dict[str, Any] | None = Field(None, description="creation_params parameter")
    customer_file_source: adaccountcustomaudiences_customer_file_source_enum_param | None = Field(
        None, description="customer_file_source parameter"
    )
    dataset_id: str | None = Field(None, description="dataset_id parameter")
    description: str | None = Field(None, description="description parameter")
    enable_fetch_or_create: bool | None = Field(
        None, description="enable_fetch_or_create parameter"
    )
    event_source_group: str | None = Field(None, description="event_source_group parameter")
    event_sources: list[dict[str, Any]] | None = Field(None, description="event_sources parameter")
    exclusions: list[dict[str, Any]] | None = Field(None, description="exclusions parameter")
    facebook_page_id: str | None = Field(None, description="facebook_page_id parameter")
    inclusions: list[dict[str, Any]] | None = Field(None, description="inclusions parameter")
    is_snapshot: bool | None = Field(None, description="is_snapshot parameter")
    is_value_based: bool | None = Field(None, description="is_value_based parameter")
    list_of_accounts: list[int] | None = Field(None, description="list_of_accounts parameter")
    lookalike_spec: str | None = Field(None, description="lookalike_spec parameter")
    marketing_message_channels: dict[str, Any] | None = Field(
        None, description="marketing_message_channels parameter"
    )
    name: str | None = Field(None, description="name parameter")
    opt_out_link: str | None = Field(None, description="opt_out_link parameter")
    origin_audience_id: str | None = Field(None, description="origin_audience_id parameter")
    parent_audience_id: int | None = Field(None, description="parent_audience_id parameter")
    partner_reference_key: str | None = Field(None, description="partner_reference_key parameter")
    pixel_id: str | None = Field(None, description="pixel_id parameter")
    prefill: bool | None = Field(None, description="prefill parameter")
    product_set_id: str | None = Field(None, description="product_set_id parameter")
    regulated_audience_spec: str | None = Field(
        None, description="regulated_audience_spec parameter"
    )
    retention_days: int | None = Field(None, description="retention_days parameter")
    rev_share_policy_id: int | None = Field(None, description="rev_share_policy_id parameter")
    rule: str | None = Field(None, description="rule parameter")
    rule_aggregation: str | None = Field(None, description="rule_aggregation parameter")
    subscription_info: list[adaccountcustomaudiences_subscription_info_enum_param] | None = Field(
        None, description="subscription_info parameter"
    )
    subtype: adaccountcustomaudiences_subtype_enum_param | None = Field(
        None, description="subtype parameter"
    )
    use_for_products: list[adaccountcustomaudiences_use_for_products_enum_param] | None = Field(
        None, description="use_for_products parameter"
    )
    use_in_campaigns: bool | None = Field(None, description="use_in_campaigns parameter")
    video_group_ids: list[str] | None = Field(None, description="video_group_ids parameter")
    whats_app_business_phone_number_id: str | None = Field(
        None, description="whats_app_business_phone_number_id parameter"
    )


class AdAccountCreateCustomAudiencestoParams(BaseModel):
    """Parameters for AdAccount.create_custom_audiencesto()."""

    model_config = ConfigDict(extra="forbid")
    business_id: str | None = Field(None, description="business_id parameter")
    tos_id: str | None = Field(None, description="tos_id parameter")


class AdAccountCreateCustomConversionParams(BaseModel):
    """Parameters for AdAccount.create_custom_conversion()."""

    model_config = ConfigDict(extra="forbid")
    action_source_type: adaccountcustomconversions_action_source_type_enum_param | None = Field(
        None, description="action_source_type parameter"
    )
    advanced_rule: str | None = Field(None, description="advanced_rule parameter")
    custom_event_type: adaccountcustomconversions_custom_event_type_enum_param | None = Field(
        None, description="custom_event_type parameter"
    )
    default_conversion_value: float | None = Field(
        None, description="default_conversion_value parameter"
    )
    description: str | None = Field(None, description="description parameter")
    event_source_id: str | None = Field(None, description="event_source_id parameter")
    name: str | None = Field(None, description="name parameter")
    rule: str | None = Field(None, description="rule parameter")


class AdAccountGetDeliveryEstimateParams(BaseModel):
    """Parameters for AdAccount.get_delivery_estimate()."""

    model_config = ConfigDict(extra="forbid")
    optimization_goal: adaccountdelivery_estimate_optimization_goal_enum_param | None = Field(
        None, description="optimization_goal parameter"
    )
    promoted_object: dict[str, Any] | None = Field(None, description="promoted_object parameter")
    targeting_spec: dict[str, Any] | None = Field(None, description="targeting_spec parameter")


class AdAccountGetDeprecatedtargetingadsetsParams(BaseModel):
    """Parameters for AdAccount.get_deprecatedtargetingadsets()."""

    model_config = ConfigDict(extra="forbid")
    type: str | None = Field(None, description="type parameter")


class AdAccountGetGeneratepreviewsParams(BaseModel):
    """Parameters for AdAccount.get_generatepreviews()."""

    model_config = ConfigDict(extra="forbid")
    ad_format: adaccountgeneratepreviews_ad_format_enum_param | None = Field(
        None, description="ad_format parameter"
    )
    creative: dict[str, Any] | None = Field(None, description="creative parameter")
    creative_feature: adaccountgeneratepreviews_creative_feature_enum_param | None = Field(
        None, description="creative_feature parameter"
    )
    dynamic_asset_label: str | None = Field(None, description="dynamic_asset_label parameter")
    dynamic_creative_spec: dict[str, Any] | None = Field(
        None, description="dynamic_creative_spec parameter"
    )
    dynamic_customization: dict[str, Any] | None = Field(
        None, description="dynamic_customization parameter"
    )
    end_date: datetime | None = Field(None, description="end_date parameter")
    height: int | None = Field(None, description="height parameter")
    locale: str | None = Field(None, description="locale parameter")
    place_page_id: int | None = Field(None, description="place_page_id parameter")
    post: dict[str, Any] | None = Field(None, description="post parameter")
    product_item_ids: list[str] | None = Field(None, description="product_item_ids parameter")
    render_type: adaccountgeneratepreviews_render_type_enum_param | None = Field(
        None, description="render_type parameter"
    )
    start_date: datetime | None = Field(None, description="start_date parameter")
    width: int | None = Field(None, description="width parameter")


class AdAccountGetInsightsParams(BaseModel):
    """Parameters for AdAccount.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adaccountinsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adaccountinsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adaccountinsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adaccountinsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adaccountinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adaccountinsights_level_enum_param | None = Field(None, description="level parameter")
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: (
        list[adaccountinsights_summary_action_breakdowns_enum_param] | None
    ) = Field(None, description="summary_action_breakdowns parameter")
    time_increment: str | None = Field(None, description="time_increment parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    time_ranges: list[dict[str, Any]] | None = Field(None, description="time_ranges parameter")
    use_account_attribution_setting: bool | None = Field(
        None, description="use_account_attribution_setting parameter"
    )
    use_unified_attribution_setting: bool | None = Field(
        None, description="use_unified_attribution_setting parameter"
    )


class AdAccountCreateInsightParams(BaseModel):
    """Parameters for AdAccount.create_insight()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adaccountinsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adaccountinsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adaccountinsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adaccountinsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adaccountinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adaccountinsights_level_enum_param | None = Field(None, description="level parameter")
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: (
        list[adaccountinsights_summary_action_breakdowns_enum_param] | None
    ) = Field(None, description="summary_action_breakdowns parameter")
    time_increment: str | None = Field(None, description="time_increment parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    time_ranges: list[dict[str, Any]] | None = Field(None, description="time_ranges parameter")
    use_account_attribution_setting: bool | None = Field(
        None, description="use_account_attribution_setting parameter"
    )
    use_unified_attribution_setting: bool | None = Field(
        None, description="use_unified_attribution_setting parameter"
    )


class AdAccountGetIosFourteenCampaignLimitsParams(BaseModel):
    """Parameters for AdAccount.get_ios_fourteen_campaign_limits()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")


class AdAccountGetMatchedSearchApplicationsParams(BaseModel):
    """Parameters for AdAccount.get_matched_search_applications()."""

    model_config = ConfigDict(extra="forbid")
    allow_incomplete_app: bool | None = Field(None, description="allow_incomplete_app parameter")
    app_store: adaccountmatched_search_applications_app_store_enum_param | None = Field(
        None, description="app_store parameter"
    )
    app_store_country: str | None = Field(None, description="app_store_country parameter")
    business_id: str | None = Field(None, description="business_id parameter")
    is_skadnetwork_search: bool | None = Field(None, description="is_skadnetwork_search parameter")
    only_apps_with_permission: bool | None = Field(
        None, description="only_apps_with_permission parameter"
    )
    query_term: str | None = Field(None, description="query_term parameter")


class AdAccountGetMinimumBudgetsParams(BaseModel):
    """Parameters for AdAccount.get_minimum_budgets()."""

    model_config = ConfigDict(extra="forbid")
    bid_amount: int | None = Field(None, description="bid_amount parameter")


class AdAccountGetOnbehalfRequestsParams(BaseModel):
    """Parameters for AdAccount.get_onbehalf_requests()."""

    model_config = ConfigDict(extra="forbid")
    status: adaccountonbehalf_requests_status_enum_param | None = Field(
        None, description="status parameter"
    )


class AdAccountCreateProductAudienceParams(BaseModel):
    """Parameters for AdAccount.create_product_audience()."""

    model_config = ConfigDict(extra="forbid")
    allowed_domains: list[str] | None = Field(None, description="allowed_domains parameter")
    associated_audience_id: int | None = Field(None, description="associated_audience_id parameter")
    claim_objective: adaccountproduct_audiences_claim_objective_enum_param | None = Field(
        None, description="claim_objective parameter"
    )
    content_type: adaccountproduct_audiences_content_type_enum_param | None = Field(
        None, description="content_type parameter"
    )
    creation_params: dict[str, Any] | None = Field(None, description="creation_params parameter")
    description: str | None = Field(None, description="description parameter")
    enable_fetch_or_create: bool | None = Field(
        None, description="enable_fetch_or_create parameter"
    )
    event_source_group: str | None = Field(None, description="event_source_group parameter")
    event_sources: list[dict[str, Any]] | None = Field(None, description="event_sources parameter")
    exclusions: list[dict[str, Any]] | None = Field(None, description="exclusions parameter")
    inclusions: list[dict[str, Any]] | None = Field(None, description="inclusions parameter")
    is_snapshot: bool | None = Field(None, description="is_snapshot parameter")
    is_value_based: bool | None = Field(None, description="is_value_based parameter")
    name: str | None = Field(None, description="name parameter")
    opt_out_link: str | None = Field(None, description="opt_out_link parameter")
    parent_audience_id: int | None = Field(None, description="parent_audience_id parameter")
    product_set_id: str | None = Field(None, description="product_set_id parameter")
    rev_share_policy_id: int | None = Field(None, description="rev_share_policy_id parameter")
    subtype: adaccountproduct_audiences_subtype_enum_param | None = Field(
        None, description="subtype parameter"
    )


class AdAccountCreatePublisherBlockListParams(BaseModel):
    """Parameters for AdAccount.create_publisher_block_list()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")


class AdAccountGetReachestimateParams(BaseModel):
    """Parameters for AdAccount.get_reachestimate()."""

    model_config = ConfigDict(extra="forbid")
    adgroup_ids: list[str] | None = Field(None, description="adgroup_ids parameter")
    caller_id: str | None = Field(None, description="caller_id parameter")
    concepts: str | None = Field(None, description="concepts parameter")
    creative_action_spec: str | None = Field(None, description="creative_action_spec parameter")
    is_debug: bool | None = Field(None, description="is_debug parameter")
    object_store_url: str | None = Field(None, description="object_store_url parameter")
    targeting_spec: dict[str, Any] | None = Field(None, description="targeting_spec parameter")


class AdAccountCreateReachfrequencypredictionParams(BaseModel):
    """Parameters for AdAccount.create_reachfrequencyprediction()."""

    model_config = ConfigDict(extra="forbid")
    action: adaccountreachfrequencypredictions_action_enum_param | None = Field(
        None, description="action parameter"
    )
    ad_formats: list[dict[str, Any]] | None = Field(None, description="ad_formats parameter")
    auction_entry_option_index: int | None = Field(
        None, description="auction_entry_option_index parameter"
    )
    budget: int | None = Field(None, description="budget parameter")
    buying_type: adaccountreachfrequencypredictions_buying_type_enum_param | None = Field(
        None, description="buying_type parameter"
    )
    campaign_group_id: str | None = Field(None, description="campaign_group_id parameter")
    day_parting_schedule: list[dict[str, Any]] | None = Field(
        None, description="day_parting_schedule parameter"
    )
    deal_id: str | None = Field(None, description="deal_id parameter")
    destination_id: int | None = Field(None, description="destination_id parameter")
    destination_ids: list[str] | None = Field(None, description="destination_ids parameter")
    end_time: int | None = Field(None, description="end_time parameter")
    exceptions: bool | None = Field(None, description="exceptions parameter")
    existing_campaign_id: str | None = Field(None, description="existing_campaign_id parameter")
    expiration_time: int | None = Field(None, description="expiration_time parameter")
    frequency_cap: int | None = Field(None, description="frequency_cap parameter")
    grp_buying: bool | None = Field(None, description="grp_buying parameter")
    impression: int | None = Field(None, description="impression parameter")
    instream_packages: (
        list[adaccountreachfrequencypredictions_instream_packages_enum_param] | None
    ) = Field(None, description="instream_packages parameter")
    interval_frequency_cap_reset_period: int | None = Field(
        None, description="interval_frequency_cap_reset_period parameter"
    )
    is_balanced_frequency: bool | None = Field(None, description="is_balanced_frequency parameter")
    is_bonus_media: bool | None = Field(None, description="is_bonus_media parameter")
    is_conversion_goal: bool | None = Field(None, description="is_conversion_goal parameter")
    is_full_view: bool | None = Field(None, description="is_full_view parameter")
    is_higher_average_frequency: bool | None = Field(
        None, description="is_higher_average_frequency parameter"
    )
    is_reach_and_frequency_io_buying: bool | None = Field(
        None, description="is_reach_and_frequency_io_buying parameter"
    )
    is_reserved_buying: bool | None = Field(None, description="is_reserved_buying parameter")
    num_curve_points: int | None = Field(None, description="num_curve_points parameter")
    objective: str | None = Field(None, description="objective parameter")
    optimization_goal: str | None = Field(None, description="optimization_goal parameter")
    prediction_mode: int | None = Field(None, description="prediction_mode parameter")
    reach: int | None = Field(None, description="reach parameter")
    rf_prediction_id: str | None = Field(None, description="rf_prediction_id parameter")
    rf_prediction_id_to_release: str | None = Field(
        None, description="rf_prediction_id_to_release parameter"
    )
    rf_prediction_id_to_share: str | None = Field(
        None, description="rf_prediction_id_to_share parameter"
    )
    start_time: int | None = Field(None, description="start_time parameter")
    stop_time: int | None = Field(None, description="stop_time parameter")
    story_event_type: int | None = Field(None, description="story_event_type parameter")
    target_cpm: int | None = Field(None, description="target_cpm parameter")
    target_frequency: int | None = Field(None, description="target_frequency parameter")
    target_frequency_reset_period: int | None = Field(
        None, description="target_frequency_reset_period parameter"
    )
    target_spec: dict[str, Any] | None = Field(None, description="target_spec parameter")
    video_view_length_constraint: int | None = Field(
        None, description="video_view_length_constraint parameter"
    )


class AdAccountCreateRecommendationParams(BaseModel):
    """Parameters for AdAccount.create_recommendation()."""

    model_config = ConfigDict(extra="forbid")
    asc_fragmentation_parameters: dict[str, Any] | None = Field(
        None, description="asc_fragmentation_parameters parameter"
    )
    autoflow_parameters: dict[str, Any] | None = Field(
        None, description="autoflow_parameters parameter"
    )
    fragmentation_parameters: dict[str, Any] | None = Field(
        None, description="fragmentation_parameters parameter"
    )
    music_parameters: dict[str, Any] | None = Field(None, description="music_parameters parameter")
    recommendation_signature: str | None = Field(
        None, description="recommendation_signature parameter"
    )
    scale_good_campaign_parameters: dict[str, Any] | None = Field(
        None, description="scale_good_campaign_parameters parameter"
    )


class AdAccountGetSavedAudiencesParams(BaseModel):
    """Parameters for AdAccount.get_saved_audiences()."""

    model_config = ConfigDict(extra="forbid")
    business_id: str | None = Field(None, description="business_id parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")


class AdAccountDeleteSubscribedAppsParams(BaseModel):
    """Parameters for AdAccount.delete_subscribed_apps()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")


class AdAccountCreateSubscribedAppParams(BaseModel):
    """Parameters for AdAccount.create_subscribed_app()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")


class AdAccountGetTargetingbrowseParams(BaseModel):
    """Parameters for AdAccount.get_targetingbrowse()."""

    model_config = ConfigDict(extra="forbid")
    excluded_category: str | None = Field(None, description="excluded_category parameter")
    include_nodes: bool | None = Field(None, description="include_nodes parameter")
    is_exclusion: bool | None = Field(None, description="is_exclusion parameter")
    limit_type: adaccounttargetingbrowse_limit_type_enum_param | None = Field(
        None, description="limit_type parameter"
    )
    regulated_categories: list[adaccounttargetingbrowse_regulated_categories_enum_param] | None = (
        Field(None, description="regulated_categories parameter")
    )
    regulated_countries: list[adaccounttargetingbrowse_regulated_countries_enum_param] | None = (
        Field(None, description="regulated_countries parameter")
    )
    whitelisted_types: list[adaccounttargetingbrowse_whitelisted_types_enum_param] | None = Field(
        None, description="whitelisted_types parameter"
    )


class AdAccountGetTargetingsearchParams(BaseModel):
    """Parameters for AdAccount.get_targetingsearch()."""

    model_config = ConfigDict(extra="forbid")
    allow_only_fat_head_interests: bool | None = Field(
        None, description="allow_only_fat_head_interests parameter"
    )
    app_store: adaccounttargetingsearch_app_store_enum_param | None = Field(
        None, description="app_store parameter"
    )
    countries: list[str] | None = Field(None, description="countries parameter")
    is_account_level_brand_safety_exclusion: bool | None = Field(
        None, description="is_account_level_brand_safety_exclusion parameter"
    )
    is_account_level_employer_exclusion: bool | None = Field(
        None, description="is_account_level_employer_exclusion parameter"
    )
    is_exclusion: bool | None = Field(None, description="is_exclusion parameter")
    limit_type: adaccounttargetingsearch_limit_type_enum_param | None = Field(
        None, description="limit_type parameter"
    )
    objective: adaccounttargetingsearch_objective_enum_param | None = Field(
        None, description="objective parameter"
    )
    promoted_object: dict[str, Any] | None = Field(None, description="promoted_object parameter")
    q: str | None = Field(None, description="q parameter")
    regulated_categories: list[adaccounttargetingsearch_regulated_categories_enum_param] | None = (
        Field(None, description="regulated_categories parameter")
    )
    regulated_countries: list[adaccounttargetingsearch_regulated_countries_enum_param] | None = (
        Field(None, description="regulated_countries parameter")
    )
    session_id: int | None = Field(None, description="session_id parameter")
    targeting_list: list[dict[str, Any]] | None = Field(
        None, description="targeting_list parameter"
    )
    whitelisted_types: list[adaccounttargetingsearch_whitelisted_types_enum_param] | None = Field(
        None, description="whitelisted_types parameter"
    )


class AdAccountGetTargetingSentenceLinesParams(BaseModel):
    """Parameters for AdAccount.get_targeting_sentence_lines()."""

    model_config = ConfigDict(extra="forbid")
    discard_ages: bool | None = Field(None, description="discard_ages parameter")
    discard_placements: bool | None = Field(None, description="discard_placements parameter")
    hide_targeting_spec_from_return: bool | None = Field(
        None, description="hide_targeting_spec_from_return parameter"
    )
    targeting_spec: dict[str, Any] | None = Field(None, description="targeting_spec parameter")


class AdAccountGetTargetingsuggestionsParams(BaseModel):
    """Parameters for AdAccount.get_targetingsuggestions()."""

    model_config = ConfigDict(extra="forbid")
    app_store: adaccounttargetingsuggestions_app_store_enum_param | None = Field(
        None, description="app_store parameter"
    )
    countries: list[str] | None = Field(None, description="countries parameter")
    limit_type: adaccounttargetingsuggestions_limit_type_enum_param | None = Field(
        None, description="limit_type parameter"
    )
    mode: adaccounttargetingsuggestions_mode_enum_param | None = Field(
        None, description="mode parameter"
    )
    objective: adaccounttargetingsuggestions_objective_enum_param | None = Field(
        None, description="objective parameter"
    )
    objects: dict[str, Any] | None = Field(None, description="objects parameter")
    regulated_categories: (
        list[adaccounttargetingsuggestions_regulated_categories_enum_param] | None
    ) = Field(None, description="regulated_categories parameter")
    regulated_countries: (
        list[adaccounttargetingsuggestions_regulated_countries_enum_param] | None
    ) = Field(None, description="regulated_countries parameter")
    session_id: int | None = Field(None, description="session_id parameter")
    targeting_list: list[dict[str, Any]] | None = Field(
        None, description="targeting_list parameter"
    )
    whitelisted_types: list[adaccounttargetingsuggestions_whitelisted_types_enum_param] | None = (
        Field(None, description="whitelisted_types parameter")
    )


class AdAccountGetTargetingvalidationParams(BaseModel):
    """Parameters for AdAccount.get_targetingvalidation()."""

    model_config = ConfigDict(extra="forbid")
    id_list: list[int] | None = Field(None, description="id_list parameter")
    is_exclusion: bool | None = Field(None, description="is_exclusion parameter")
    name_list: list[str] | None = Field(None, description="name_list parameter")
    targeting_list: list[dict[str, Any]] | None = Field(
        None, description="targeting_list parameter"
    )


class AdAccountCreateTrackingParams(BaseModel):
    """Parameters for AdAccount.create_tracking()."""

    model_config = ConfigDict(extra="forbid")
    tracking_specs: dict[str, Any] | None = Field(None, description="tracking_specs parameter")


class AdAccountDeleteUsersofanyaudienceParams(BaseModel):
    """Parameters for AdAccount.delete_usersofanyaudience()."""

    model_config = ConfigDict(extra="forbid")
    namespace: str | None = Field(None, description="namespace parameter")
    payload: dict[str, Any] | None = Field(None, description="payload parameter")
    session: dict[str, Any] | None = Field(None, description="session parameter")


class AdAccountGetValueRuleSetParams(BaseModel):
    """Parameters for AdAccount.get_value_rule_set()."""

    model_config = ConfigDict(extra="forbid")
    product_type: adaccountvalue_rule_set_product_type_enum_param | None = Field(
        None, description="product_type parameter"
    )
    status: adaccountvalue_rule_set_status_enum_param | None = Field(
        None, description="status parameter"
    )


class AdAccountCreateValueRuleSetParams(BaseModel):
    """Parameters for AdAccount.create_value_rule_set()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")
    product_type: adaccountvalue_rule_set_product_type_enum_param | None = Field(
        None, description="product_type parameter"
    )
    rules: list[dict[str, Any]] | None = Field(None, description="rules parameter")


class AdAccountGetVideoAdsParams(BaseModel):
    """Parameters for AdAccount.get_video_ads()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class AdAccountCreateVideoAdParams(BaseModel):
    """Parameters for AdAccount.create_video_ad()."""

    model_config = ConfigDict(extra="forbid")
    description: str | None = Field(None, description="description parameter")
    privacy: str | None = Field(None, description="privacy parameter")
    title: str | None = Field(None, description="title parameter")
    upload_phase: adaccountvideo_ads_upload_phase_enum_param | None = Field(
        None, description="upload_phase parameter"
    )
    video_id: str | None = Field(None, description="video_id parameter")
    video_state: adaccountvideo_ads_video_state_enum_param | None = Field(
        None, description="video_state parameter"
    )
