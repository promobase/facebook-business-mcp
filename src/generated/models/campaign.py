"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcampaigngroupadvantagestate import AdCampaignGroupAdvantageStateFields
    from .adcampaignissuesinfo import AdCampaignIssuesInfoFields
    from .adlabel import AdLabelFields
    from .adpromotedobject import AdPromotedObjectFields
    from .adrecommendation import AdRecommendationFields
    from .adstudy import AdStudyFields


class Campaign_bid_strategy(str, Enum):
    """Campaign_bid_strategy enum values."""

    COST_CAP = "COST_CAP"
    LOWEST_COST_WITHOUT_CAP = "LOWEST_COST_WITHOUT_CAP"
    LOWEST_COST_WITH_BID_CAP = "LOWEST_COST_WITH_BID_CAP"
    LOWEST_COST_WITH_MIN_ROAS = "LOWEST_COST_WITH_MIN_ROAS"


class Campaign_configured_status(str, Enum):
    """Campaign_configured_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class Campaign_effective_status(str, Enum):
    """Campaign_effective_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    IN_PROCESS = "IN_PROCESS"
    PAUSED = "PAUSED"
    WITH_ISSUES = "WITH_ISSUES"


class Campaign_status(str, Enum):
    """Campaign_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class adcampaigngroupinsights_action_breakdowns_enum_param(str, Enum):
    """adcampaigngroupinsights_action_breakdowns_enum_param enum values."""

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


class adcampaigngroupcopies_date_preset_enum_param(str, Enum):
    """adcampaigngroupcopies_date_preset_enum_param enum values."""

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


class adcampaigngroupinsights_breakdowns_enum_param(str, Enum):
    """adcampaigngroupinsights_breakdowns_enum_param enum values."""

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


class adcampaigngroupinsights_date_preset_enum_param(str, Enum):
    """adcampaigngroupinsights_date_preset_enum_param enum values."""

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


class adcampaigngroupinsights_summary_action_breakdowns_enum_param(str, Enum):
    """adcampaigngroupinsights_summary_action_breakdowns_enum_param enum values."""

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


class adcampaigngroupbudget_schedules_budget_value_type_enum_param(str, Enum):
    """adcampaigngroupbudget_schedules_budget_value_type_enum_param enum values."""

    ABSOLUTE = "ABSOLUTE"
    MULTIPLIER = "MULTIPLIER"


class adcampaigngroupcopies_effective_status_enum_param(str, Enum):
    """adcampaigngroupcopies_effective_status_enum_param enum values."""

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


class adcampaigngroupcopies_status_option_enum_param(str, Enum):
    """adcampaigngroupcopies_status_option_enum_param enum values."""

    ACTIVE = "ACTIVE"
    INHERITED_FROM_SOURCE = "INHERITED_FROM_SOURCE"
    PAUSED = "PAUSED"


class adcampaigngroupinsights_action_attribution_windows_enum_param(str, Enum):
    """adcampaigngroupinsights_action_attribution_windows_enum_param enum values."""

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


class adcampaigngroupadlabels_execution_options_enum_param(str, Enum):
    """adcampaigngroupadlabels_execution_options_enum_param enum values."""

    validate_only = "validate_only"


class adcampaigngroupinsights_level_enum_param(str, Enum):
    """adcampaigngroupinsights_level_enum_param enum values."""

    account = "account"
    ad = "ad"
    adset = "adset"
    campaign = "campaign"


class adcampaigngroupadsets_date_preset_enum_param(str, Enum):
    """adcampaigngroupadsets_date_preset_enum_param enum values."""

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


class adcampaigngroupads_date_preset_enum_param(str, Enum):
    """adcampaigngroupads_date_preset_enum_param enum values."""

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


class adcampaigngroupinsights_action_report_time_enum_param(str, Enum):
    """adcampaigngroupinsights_action_report_time_enum_param enum values."""

    conversion = "conversion"
    impression = "impression"
    lifetime = "lifetime"
    mixed = "mixed"


class adcampaigngroupadsets_effective_status_enum_param(str, Enum):
    """adcampaigngroupadsets_effective_status_enum_param enum values."""

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


# Field literal type
CampaignField = Literal[
    "account_id",
    "adlabels",
    "advantage_state_info",
    "bid_strategy",
    "boosted_object_id",
    "brand_lift_studies",
    "budget_rebalance_flag",
    "budget_remaining",
    "buying_type",
    "campaign_group_active_time",
    "can_create_brand_lift_study",
    "can_use_spend_cap",
    "configured_status",
    "created_time",
    "daily_budget",
    "effective_status",
    "has_secondary_skadnetwork_reporting",
    "id",
    "is_budget_schedule_enabled",
    "is_skadnetwork_attribution",
    "issues_info",
    "last_budget_toggling_time",
    "lifetime_budget",
    "name",
    "objective",
    "pacing_type",
    "primary_attribution",
    "promoted_object",
    "recommendations",
    "smart_promotion_type",
    "source_campaign",
    "source_campaign_id",
    "source_recommendation_type",
    "special_ad_categories",
    "special_ad_category",
    "special_ad_category_country",
    "spend_cap",
    "start_time",
    "status",
    "stop_time",
    "topline_id",
    "updated_time",
]


class CampaignFields(BaseModel):
    """Pydantic model for Campaign fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    adlabels: list[AdLabelFields] = Field(None, alias="adlabels")
    advantage_state_info: AdCampaignGroupAdvantageStateFields = Field(
        None, alias="advantage_state_info"
    )
    bid_strategy: dict[str, Any] = Field(None, alias="bid_strategy")
    boosted_object_id: str = Field(None, alias="boosted_object_id")
    brand_lift_studies: list[AdStudyFields] = Field(None, alias="brand_lift_studies")
    budget_rebalance_flag: bool = Field(None, alias="budget_rebalance_flag")
    budget_remaining: str = Field(None, alias="budget_remaining")
    buying_type: str = Field(None, alias="buying_type")
    campaign_group_active_time: str = Field(None, alias="campaign_group_active_time")
    can_create_brand_lift_study: bool = Field(None, alias="can_create_brand_lift_study")
    can_use_spend_cap: bool = Field(None, alias="can_use_spend_cap")
    configured_status: dict[str, Any] = Field(None, alias="configured_status")
    created_time: datetime = Field(None, alias="created_time")
    daily_budget: str = Field(None, alias="daily_budget")
    effective_status: dict[str, Any] = Field(None, alias="effective_status")
    has_secondary_skadnetwork_reporting: bool = Field(
        None, alias="has_secondary_skadnetwork_reporting"
    )
    id: str = Field(None, alias="id")
    is_budget_schedule_enabled: bool = Field(None, alias="is_budget_schedule_enabled")
    is_skadnetwork_attribution: bool = Field(None, alias="is_skadnetwork_attribution")
    issues_info: list[AdCampaignIssuesInfoFields] = Field(None, alias="issues_info")
    last_budget_toggling_time: datetime = Field(None, alias="last_budget_toggling_time")
    lifetime_budget: str = Field(None, alias="lifetime_budget")
    name: str = Field(None, alias="name")
    objective: str = Field(None, alias="objective")
    pacing_type: list[str] = Field(None, alias="pacing_type")
    primary_attribution: str = Field(None, alias="primary_attribution")
    promoted_object: AdPromotedObjectFields = Field(None, alias="promoted_object")
    recommendations: list[AdRecommendationFields] = Field(None, alias="recommendations")
    smart_promotion_type: str = Field(None, alias="smart_promotion_type")
    source_campaign: CampaignFields = Field(None, alias="source_campaign")
    source_campaign_id: str = Field(None, alias="source_campaign_id")
    source_recommendation_type: str = Field(None, alias="source_recommendation_type")
    special_ad_categories: list[str] = Field(None, alias="special_ad_categories")
    special_ad_category: str = Field(None, alias="special_ad_category")
    special_ad_category_country: list[str] = Field(None, alias="special_ad_category_country")
    spend_cap: str = Field(None, alias="spend_cap")
    start_time: datetime = Field(None, alias="start_time")
    status: dict[str, Any] = Field(None, alias="status")
    stop_time: datetime = Field(None, alias="stop_time")
    topline_id: str = Field(None, alias="topline_id")
    updated_time: datetime = Field(None, alias="updated_time")


class CampaignCreateAdLabelParams(BaseModel):
    """Parameters for Campaign.create_ad_label()."""

    model_config = ConfigDict(extra="forbid")
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    execution_options: list[adcampaigngroupadlabels_execution_options_enum_param] | None = Field(
        None, description="execution_options parameter"
    )


class CampaignGetAdrulesGovernedParams(BaseModel):
    """Parameters for Campaign.get_adrules_governed()."""

    model_config = ConfigDict(extra="forbid")
    pass_evaluation: bool | None = Field(None, description="pass_evaluation parameter")


class CampaignGetAdSParams(BaseModel):
    """Parameters for Campaign.get_ad_s()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adcampaigngroupads_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[str] | None = Field(None, description="effective_status parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    updated_since: int | None = Field(None, description="updated_since parameter")


class CampaignGetAdSetsParams(BaseModel):
    """Parameters for Campaign.get_ad_sets()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adcampaigngroupadsets_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[adcampaigngroupadsets_effective_status_enum_param] | None = Field(
        None, description="effective_status parameter"
    )
    is_completed: bool | None = Field(None, description="is_completed parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")


class CampaignCreateBudgetScheduleParams(BaseModel):
    """Parameters for Campaign.create_budget_schedule()."""

    model_config = ConfigDict(extra="forbid")
    budget_value: int | None = Field(None, description="budget_value parameter")
    budget_value_type: adcampaigngroupbudget_schedules_budget_value_type_enum_param | None = Field(
        None, description="budget_value_type parameter"
    )
    time_end: int | None = Field(None, description="time_end parameter")
    time_start: int | None = Field(None, description="time_start parameter")


class CampaignGetCopiesParams(BaseModel):
    """Parameters for Campaign.get_copies()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adcampaigngroupcopies_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[adcampaigngroupcopies_effective_status_enum_param] | None = Field(
        None, description="effective_status parameter"
    )
    is_completed: bool | None = Field(None, description="is_completed parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")


class CampaignCreateCopieParams(BaseModel):
    """Parameters for Campaign.create_copie()."""

    model_config = ConfigDict(extra="forbid")
    deep_copy: bool | None = Field(None, description="deep_copy parameter")
    end_time: datetime | None = Field(None, description="end_time parameter")
    rename_options: dict[str, Any] | None = Field(None, description="rename_options parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")
    status_option: adcampaigngroupcopies_status_option_enum_param | None = Field(
        None, description="status_option parameter"
    )


class CampaignGetInsightsParams(BaseModel):
    """Parameters for Campaign.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adcampaigngroupinsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adcampaigngroupinsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adcampaigngroupinsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adcampaigngroupinsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adcampaigngroupinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adcampaigngroupinsights_level_enum_param | None = Field(
        None, description="level parameter"
    )
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: (
        list[adcampaigngroupinsights_summary_action_breakdowns_enum_param] | None
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


class CampaignCreateInsightParams(BaseModel):
    """Parameters for Campaign.create_insight()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adcampaigngroupinsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adcampaigngroupinsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adcampaigngroupinsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adcampaigngroupinsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adcampaigngroupinsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adcampaigngroupinsights_level_enum_param | None = Field(
        None, description="level parameter"
    )
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: (
        list[adcampaigngroupinsights_summary_action_breakdowns_enum_param] | None
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
