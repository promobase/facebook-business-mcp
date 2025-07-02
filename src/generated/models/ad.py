"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreative import AdCreativeFields
    from .adcreativeassetgroupsspec import AdCreativeAssetGroupsSpecFields
    from .adgroupissuesinfo import AdgroupIssuesInfoFields
    from .adgroupreviewfeedback import AdgroupReviewFeedbackFields
    from .adlabel import AdLabelFields
    from .adrecommendation import AdRecommendationFields
    from .adset import AdSetFields
    from .campaign import CampaignFields
    from .conversionactionquery import ConversionActionQueryFields
    from .deliverycheck import DeliveryCheckFields
    from .placement import PlacementFields
    from .targeting import TargetingFields
    from .trackingandconversionwithdefaults import TrackingAndConversionWithDefaultsFields


class Ad_bid_type(str, Enum):
    """Ad_bid_type enum values."""

    ABSOLUTE_OCPM = "ABSOLUTE_OCPM"
    CPA = "CPA"
    CPC = "CPC"
    CPM = "CPM"
    MULTI_PREMIUM = "MULTI_PREMIUM"


class Ad_configured_status(str, Enum):
    """Ad_configured_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class Ad_effective_status(str, Enum):
    """Ad_effective_status enum values."""

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


class Ad_status(str, Enum):
    """Ad_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class adgroupinsights_action_breakdowns_enum_param(str, Enum):
    """adgroupinsights_action_breakdowns_enum_param enum values."""

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


class adgrouppreviews_render_type_enum_param(str, Enum):
    """adgrouppreviews_render_type_enum_param enum values."""

    FALLBACK = "FALLBACK"


class adgroupcopies_date_preset_enum_param(str, Enum):
    """adgroupcopies_date_preset_enum_param enum values."""

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


class adgrouppreviews_creative_feature_enum_param(str, Enum):
    """adgrouppreviews_creative_feature_enum_param enum values."""

    product_metadata_automation = "product_metadata_automation"
    profile_card = "profile_card"
    standard_enhancements_catalog = "standard_enhancements_catalog"
    video_to_image = "video_to_image"


class adgroupcopies_status_option_enum_param(str, Enum):
    """adgroupcopies_status_option_enum_param enum values."""

    ACTIVE = "ACTIVE"
    INHERITED_FROM_SOURCE = "INHERITED_FROM_SOURCE"
    PAUSED = "PAUSED"


class adgroupinsights_date_preset_enum_param(str, Enum):
    """adgroupinsights_date_preset_enum_param enum values."""

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


class adgroupinsights_level_enum_param(str, Enum):
    """adgroupinsights_level_enum_param enum values."""

    account = "account"
    ad = "ad"
    adset = "adset"
    campaign = "campaign"


class adgroupinsights_action_attribution_windows_enum_param(str, Enum):
    """adgroupinsights_action_attribution_windows_enum_param enum values."""

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


class adgroupinsights_action_report_time_enum_param(str, Enum):
    """adgroupinsights_action_report_time_enum_param enum values."""

    conversion = "conversion"
    impression = "impression"
    lifetime = "lifetime"
    mixed = "mixed"


class adgroupinsights_breakdowns_enum_param(str, Enum):
    """adgroupinsights_breakdowns_enum_param enum values."""

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


class adgrouppreviews_ad_format_enum_param(str, Enum):
    """adgrouppreviews_ad_format_enum_param enum values."""

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


class adgroupadlabels_execution_options_enum_param(str, Enum):
    """adgroupadlabels_execution_options_enum_param enum values."""

    validate_only = "validate_only"


class adgroupinsights_summary_action_breakdowns_enum_param(str, Enum):
    """adgroupinsights_summary_action_breakdowns_enum_param enum values."""

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


# Field literal type
AdField = Literal[
    "account_id",
    "ad_active_time",
    "ad_review_feedback",
    "ad_schedule_end_time",
    "ad_schedule_start_time",
    "adlabels",
    "adset",
    "adset_id",
    "bid_amount",
    "bid_info",
    "bid_type",
    "campaign",
    "campaign_id",
    "configured_status",
    "conversion_domain",
    "conversion_specs",
    "created_time",
    "creative",
    "creative_asset_groups_spec",
    "demolink_hash",
    "display_sequence",
    "effective_status",
    "engagement_audience",
    "failed_delivery_checks",
    "id",
    "issues_info",
    "last_updated_by_app_id",
    "name",
    "placement",
    "preview_shareable_link",
    "priority",
    "recommendations",
    "source_ad",
    "source_ad_id",
    "status",
    "targeting",
    "tracking_and_conversion_with_defaults",
    "tracking_specs",
    "updated_time",
]


class AdFields(BaseModel):
    """Pydantic model for Ad fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    ad_active_time: str = Field(None, alias="ad_active_time")
    ad_review_feedback: AdgroupReviewFeedbackFields = Field(None, alias="ad_review_feedback")
    ad_schedule_end_time: datetime = Field(None, alias="ad_schedule_end_time")
    ad_schedule_start_time: datetime = Field(None, alias="ad_schedule_start_time")
    adlabels: list[AdLabelFields] = Field(None, alias="adlabels")
    adset: AdSetFields = Field(None, alias="adset")
    adset_id: str = Field(None, alias="adset_id")
    bid_amount: int = Field(None, alias="bid_amount")
    bid_info: dict[str, int] = Field(None, alias="bid_info")
    bid_type: dict[str, Any] = Field(None, alias="bid_type")
    campaign: CampaignFields = Field(None, alias="campaign")
    campaign_id: str = Field(None, alias="campaign_id")
    configured_status: dict[str, Any] = Field(None, alias="configured_status")
    conversion_domain: str = Field(None, alias="conversion_domain")
    conversion_specs: list[ConversionActionQueryFields] = Field(None, alias="conversion_specs")
    created_time: datetime = Field(None, alias="created_time")
    creative: AdCreativeFields = Field(None, alias="creative")
    creative_asset_groups_spec: AdCreativeAssetGroupsSpecFields = Field(
        None, alias="creative_asset_groups_spec"
    )
    demolink_hash: str = Field(None, alias="demolink_hash")
    display_sequence: int = Field(None, alias="display_sequence")
    effective_status: dict[str, Any] = Field(None, alias="effective_status")
    engagement_audience: bool = Field(None, alias="engagement_audience")
    failed_delivery_checks: list[DeliveryCheckFields] = Field(None, alias="failed_delivery_checks")
    id: str = Field(None, alias="id")
    issues_info: list[AdgroupIssuesInfoFields] = Field(None, alias="issues_info")
    last_updated_by_app_id: str = Field(None, alias="last_updated_by_app_id")
    name: str = Field(None, alias="name")
    placement: PlacementFields = Field(None, alias="placement")
    preview_shareable_link: str = Field(None, alias="preview_shareable_link")
    priority: int = Field(None, alias="priority")
    recommendations: list[AdRecommendationFields] = Field(None, alias="recommendations")
    source_ad: AdFields = Field(None, alias="source_ad")
    source_ad_id: str = Field(None, alias="source_ad_id")
    status: dict[str, Any] = Field(None, alias="status")
    targeting: TargetingFields = Field(None, alias="targeting")
    tracking_and_conversion_with_defaults: TrackingAndConversionWithDefaultsFields = Field(
        None, alias="tracking_and_conversion_with_defaults"
    )
    tracking_specs: list[ConversionActionQueryFields] = Field(None, alias="tracking_specs")
    updated_time: datetime = Field(None, alias="updated_time")


class AdCreateAdLabelParams(BaseModel):
    """Parameters for Ad.create_ad_label()."""

    model_config = ConfigDict(extra="forbid")
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    execution_options: list[adgroupadlabels_execution_options_enum_param] | None = Field(
        None, description="execution_options parameter"
    )


class AdGetAdrulesGovernedParams(BaseModel):
    """Parameters for Ad.get_adrules_governed()."""

    model_config = ConfigDict(extra="forbid")
    pass_evaluation: bool | None = Field(None, description="pass_evaluation parameter")


class AdGetCopiesParams(BaseModel):
    """Parameters for Ad.get_copies()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adgroupcopies_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[str] | None = Field(None, description="effective_status parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    updated_since: int | None = Field(None, description="updated_since parameter")


class AdCreateCopieParams(BaseModel):
    """Parameters for Ad.create_copie()."""

    model_config = ConfigDict(extra="forbid")
    adset_id: str | None = Field(None, description="adset_id parameter")
    creative_parameters: dict[str, Any] | None = Field(
        None, description="creative_parameters parameter"
    )
    rename_options: dict[str, Any] | None = Field(None, description="rename_options parameter")
    status_option: adgroupcopies_status_option_enum_param | None = Field(
        None, description="status_option parameter"
    )


class AdGetInsightsParams(BaseModel):
    """Parameters for Ad.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adgroupinsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adgroupinsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adgroupinsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adgroupinsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adgroupinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adgroupinsights_level_enum_param | None = Field(None, description="level parameter")
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: list[adgroupinsights_summary_action_breakdowns_enum_param] | None = (
        Field(None, description="summary_action_breakdowns parameter")
    )
    time_increment: str | None = Field(None, description="time_increment parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    time_ranges: list[dict[str, Any]] | None = Field(None, description="time_ranges parameter")
    use_account_attribution_setting: bool | None = Field(
        None, description="use_account_attribution_setting parameter"
    )
    use_unified_attribution_setting: bool | None = Field(
        None, description="use_unified_attribution_setting parameter"
    )


class AdCreateInsightParams(BaseModel):
    """Parameters for Ad.create_insight()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adgroupinsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adgroupinsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adgroupinsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adgroupinsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adgroupinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adgroupinsights_level_enum_param | None = Field(None, description="level parameter")
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: list[adgroupinsights_summary_action_breakdowns_enum_param] | None = (
        Field(None, description="summary_action_breakdowns parameter")
    )
    time_increment: str | None = Field(None, description="time_increment parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    time_ranges: list[dict[str, Any]] | None = Field(None, description="time_ranges parameter")
    use_account_attribution_setting: bool | None = Field(
        None, description="use_account_attribution_setting parameter"
    )
    use_unified_attribution_setting: bool | None = Field(
        None, description="use_unified_attribution_setting parameter"
    )


class AdGetPreviewsParams(BaseModel):
    """Parameters for Ad.get_previews()."""

    model_config = ConfigDict(extra="forbid")
    ad_format: adgrouppreviews_ad_format_enum_param | None = Field(
        None, description="ad_format parameter"
    )
    creative_feature: adgrouppreviews_creative_feature_enum_param | None = Field(
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
    render_type: adgrouppreviews_render_type_enum_param | None = Field(
        None, description="render_type parameter"
    )
    start_date: datetime | None = Field(None, description="start_date parameter")
    width: int | None = Field(None, description="width parameter")
