"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adbidadjustments import AdBidAdjustmentsFields
    from .adcampaignbidconstraint import AdCampaignBidConstraintFields
    from .adcampaignfrequencycontrolspecs import AdCampaignFrequencyControlSpecsFields
    from .adcampaignissuesinfo import AdCampaignIssuesInfoFields
    from .adcampaignlearningstageinfo import AdCampaignLearningStageInfoFields
    from .adlabel import AdLabelFields
    from .adpromotedobject import AdPromotedObjectFields
    from .adrecommendation import AdRecommendationFields
    from .attributionspec import AttributionSpecFields
    from .brandsafetycampaignconfig import BrandSafetyCampaignConfigFields
    from .campaign import CampaignFields
    from .daypart import DayPartFields
    from .regionalregulationidentities import RegionalRegulationIdentitiesFields
    from .targeting import TargetingFields


class AdSet_bid_strategy(str, Enum):
    """AdSet_bid_strategy enum values."""

    COST_CAP = "COST_CAP"
    LOWEST_COST_WITHOUT_CAP = "LOWEST_COST_WITHOUT_CAP"
    LOWEST_COST_WITH_BID_CAP = "LOWEST_COST_WITH_BID_CAP"
    LOWEST_COST_WITH_MIN_ROAS = "LOWEST_COST_WITH_MIN_ROAS"


class AdSet_billing_event(str, Enum):
    """AdSet_billing_event enum values."""

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


class AdSet_configured_status(str, Enum):
    """AdSet_configured_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class AdSet_effective_status(str, Enum):
    """AdSet_effective_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    DELETED = "DELETED"
    IN_PROCESS = "IN_PROCESS"
    PAUSED = "PAUSED"
    WITH_ISSUES = "WITH_ISSUES"


class AdSet_optimization_goal(str, Enum):
    """AdSet_optimization_goal enum values."""

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


class AdSet_status(str, Enum):
    """AdSet_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class adcampaigninsights_action_report_time_enum_param(str, Enum):
    """adcampaigninsights_action_report_time_enum_param enum values."""

    conversion = "conversion"
    impression = "impression"
    lifetime = "lifetime"
    mixed = "mixed"


class adcampaigncopies_effective_status_enum_param(str, Enum):
    """adcampaigncopies_effective_status_enum_param enum values."""

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


class adcampaignads_date_preset_enum_param(str, Enum):
    """adcampaignads_date_preset_enum_param enum values."""

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


class adcampaigninsights_action_breakdowns_enum_param(str, Enum):
    """adcampaigninsights_action_breakdowns_enum_param enum values."""

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


class adcampaigncopies_date_preset_enum_param(str, Enum):
    """adcampaigncopies_date_preset_enum_param enum values."""

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


class adcampaigninsights_summary_action_breakdowns_enum_param(str, Enum):
    """adcampaigninsights_summary_action_breakdowns_enum_param enum values."""

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


class adcampaignmessage_delivery_estimate_optimization_goal_enum_param(str, Enum):
    """adcampaignmessage_delivery_estimate_optimization_goal_enum_param enum values."""

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


class adcampaignmessage_delivery_estimate_pacing_type_enum_param(str, Enum):
    """adcampaignmessage_delivery_estimate_pacing_type_enum_param enum values."""

    DAY_PARTING = "DAY_PARTING"
    DISABLED = "DISABLED"
    NO_PACING = "NO_PACING"
    PROBABILISTIC_PACING = "PROBABILISTIC_PACING"
    PROBABILISTIC_PACING_V2 = "PROBABILISTIC_PACING_V2"
    STANDARD = "STANDARD"


class adcampaigninsights_level_enum_param(str, Enum):
    """adcampaigninsights_level_enum_param enum values."""

    account = "account"
    ad = "ad"
    adset = "adset"
    campaign = "campaign"


class adcampaignactivities_category_enum_param(str, Enum):
    """adcampaignactivities_category_enum_param enum values."""

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


class adcampaigndelivery_estimate_optimization_goal_enum_param(str, Enum):
    """adcampaigndelivery_estimate_optimization_goal_enum_param enum values."""

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


class adcampaigninsights_date_preset_enum_param(str, Enum):
    """adcampaigninsights_date_preset_enum_param enum values."""

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


class adcampaigninsights_action_attribution_windows_enum_param(str, Enum):
    """adcampaigninsights_action_attribution_windows_enum_param enum values."""

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


class adcampaigninsights_breakdowns_enum_param(str, Enum):
    """adcampaigninsights_breakdowns_enum_param enum values."""

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


class adcampaignadlabels_execution_options_enum_param(str, Enum):
    """adcampaignadlabels_execution_options_enum_param enum values."""

    validate_only = "validate_only"


class adcampaigncopies_status_option_enum_param(str, Enum):
    """adcampaigncopies_status_option_enum_param enum values."""

    ACTIVE = "ACTIVE"
    INHERITED_FROM_SOURCE = "INHERITED_FROM_SOURCE"
    PAUSED = "PAUSED"


class adcampaignbudget_schedules_budget_value_type_enum_param(str, Enum):
    """adcampaignbudget_schedules_budget_value_type_enum_param enum values."""

    ABSOLUTE = "ABSOLUTE"
    MULTIPLIER = "MULTIPLIER"


class adcampaignasyncadrequests_statuses_enum_param(str, Enum):
    """adcampaignasyncadrequests_statuses_enum_param enum values."""

    CANCELED = "CANCELED"
    CANCELED_DEPENDENCY = "CANCELED_DEPENDENCY"
    ERROR = "ERROR"
    ERROR_CONFLICTS = "ERROR_CONFLICTS"
    ERROR_DEPENDENCY = "ERROR_DEPENDENCY"
    INITIAL = "INITIAL"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING_DEPENDENCY = "PENDING_DEPENDENCY"
    PROCESS_BY_AD_ASYNC_ENGINE = "PROCESS_BY_AD_ASYNC_ENGINE"
    PROCESS_BY_EVENT_PROCESSOR = "PROCESS_BY_EVENT_PROCESSOR"
    SUCCESS = "SUCCESS"
    USER_CANCELED = "USER_CANCELED"
    USER_CANCELED_DEPENDENCY = "USER_CANCELED_DEPENDENCY"


# Field literal type
AdSetField = Literal[
    "account_id",
    "adlabels",
    "adset_schedule",
    "asset_feed_id",
    "attribution_spec",
    "bid_adjustments",
    "bid_amount",
    "bid_constraints",
    "bid_info",
    "bid_strategy",
    "billing_event",
    "brand_safety_config",
    "budget_remaining",
    "campaign",
    "campaign_active_time",
    "campaign_attribution",
    "campaign_id",
    "configured_status",
    "created_time",
    "creative_sequence",
    "creative_sequence_repetition_pattern",
    "daily_budget",
    "daily_min_spend_target",
    "daily_spend_cap",
    "destination_type",
    "dsa_beneficiary",
    "dsa_payor",
    "effective_status",
    "end_time",
    "existing_customer_budget_percentage",
    "frequency_control_specs",
    "full_funnel_exploration_mode",
    "id",
    "instagram_user_id",
    "is_ba_skip_delayed_eligible",
    "is_budget_schedule_enabled",
    "is_dynamic_creative",
    "is_incremental_attribution_enabled",
    "issues_info",
    "learning_stage_info",
    "lifetime_budget",
    "lifetime_imps",
    "lifetime_min_spend_target",
    "lifetime_spend_cap",
    "max_budget_spend_percentage",
    "min_budget_spend_percentage",
    "multi_optimization_goal_weight",
    "name",
    "optimization_goal",
    "optimization_sub_event",
    "pacing_type",
    "promoted_object",
    "recommendations",
    "recurring_budget_semantics",
    "regional_regulated_categories",
    "regional_regulation_identities",
    "review_feedback",
    "rf_prediction_id",
    "source_adset",
    "source_adset_id",
    "start_time",
    "status",
    "targeting",
    "targeting_optimization_types",
    "time_based_ad_rotation_id_blocks",
    "time_based_ad_rotation_intervals",
    "updated_time",
    "use_new_app_click",
]


class AdSetFields(BaseModel):
    """Pydantic model for AdSet fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    adlabels: list[AdLabelFields] = Field(None, alias="adlabels")
    adset_schedule: list[DayPartFields] = Field(None, alias="adset_schedule")
    asset_feed_id: str = Field(None, alias="asset_feed_id")
    attribution_spec: list[AttributionSpecFields] = Field(None, alias="attribution_spec")
    bid_adjustments: AdBidAdjustmentsFields = Field(None, alias="bid_adjustments")
    bid_amount: int = Field(None, alias="bid_amount")
    bid_constraints: AdCampaignBidConstraintFields = Field(None, alias="bid_constraints")
    bid_info: dict[str, int] = Field(None, alias="bid_info")
    bid_strategy: dict[str, Any] = Field(None, alias="bid_strategy")
    billing_event: dict[str, Any] = Field(None, alias="billing_event")
    brand_safety_config: BrandSafetyCampaignConfigFields = Field(None, alias="brand_safety_config")
    budget_remaining: str = Field(None, alias="budget_remaining")
    campaign: CampaignFields = Field(None, alias="campaign")
    campaign_active_time: str = Field(None, alias="campaign_active_time")
    campaign_attribution: str = Field(None, alias="campaign_attribution")
    campaign_id: str = Field(None, alias="campaign_id")
    configured_status: dict[str, Any] = Field(None, alias="configured_status")
    created_time: datetime = Field(None, alias="created_time")
    creative_sequence: list[str] = Field(None, alias="creative_sequence")
    creative_sequence_repetition_pattern: str = Field(
        None, alias="creative_sequence_repetition_pattern"
    )
    daily_budget: str = Field(None, alias="daily_budget")
    daily_min_spend_target: str = Field(None, alias="daily_min_spend_target")
    daily_spend_cap: str = Field(None, alias="daily_spend_cap")
    destination_type: str = Field(None, alias="destination_type")
    dsa_beneficiary: str = Field(None, alias="dsa_beneficiary")
    dsa_payor: str = Field(None, alias="dsa_payor")
    effective_status: dict[str, Any] = Field(None, alias="effective_status")
    end_time: datetime = Field(None, alias="end_time")
    existing_customer_budget_percentage: int = Field(
        None, alias="existing_customer_budget_percentage"
    )
    frequency_control_specs: list[AdCampaignFrequencyControlSpecsFields] = Field(
        None, alias="frequency_control_specs"
    )
    full_funnel_exploration_mode: str = Field(None, alias="full_funnel_exploration_mode")
    id: str = Field(None, alias="id")
    instagram_user_id: str = Field(None, alias="instagram_user_id")
    is_ba_skip_delayed_eligible: bool = Field(None, alias="is_ba_skip_delayed_eligible")
    is_budget_schedule_enabled: bool = Field(None, alias="is_budget_schedule_enabled")
    is_dynamic_creative: bool = Field(None, alias="is_dynamic_creative")
    is_incremental_attribution_enabled: bool = Field(
        None, alias="is_incremental_attribution_enabled"
    )
    issues_info: list[AdCampaignIssuesInfoFields] = Field(None, alias="issues_info")
    learning_stage_info: AdCampaignLearningStageInfoFields = Field(
        None, alias="learning_stage_info"
    )
    lifetime_budget: str = Field(None, alias="lifetime_budget")
    lifetime_imps: int = Field(None, alias="lifetime_imps")
    lifetime_min_spend_target: str = Field(None, alias="lifetime_min_spend_target")
    lifetime_spend_cap: str = Field(None, alias="lifetime_spend_cap")
    max_budget_spend_percentage: str = Field(None, alias="max_budget_spend_percentage")
    min_budget_spend_percentage: str = Field(None, alias="min_budget_spend_percentage")
    multi_optimization_goal_weight: str = Field(None, alias="multi_optimization_goal_weight")
    name: str = Field(None, alias="name")
    optimization_goal: dict[str, Any] = Field(None, alias="optimization_goal")
    optimization_sub_event: str = Field(None, alias="optimization_sub_event")
    pacing_type: list[str] = Field(None, alias="pacing_type")
    promoted_object: AdPromotedObjectFields = Field(None, alias="promoted_object")
    recommendations: list[AdRecommendationFields] = Field(None, alias="recommendations")
    recurring_budget_semantics: bool = Field(None, alias="recurring_budget_semantics")
    regional_regulated_categories: list[str] = Field(None, alias="regional_regulated_categories")
    regional_regulation_identities: RegionalRegulationIdentitiesFields = Field(
        None, alias="regional_regulation_identities"
    )
    review_feedback: str = Field(None, alias="review_feedback")
    rf_prediction_id: str = Field(None, alias="rf_prediction_id")
    source_adset: AdSetFields = Field(None, alias="source_adset")
    source_adset_id: str = Field(None, alias="source_adset_id")
    start_time: datetime = Field(None, alias="start_time")
    status: dict[str, Any] = Field(None, alias="status")
    targeting: TargetingFields = Field(None, alias="targeting")
    targeting_optimization_types: list[dict[str, int]] = Field(
        None, alias="targeting_optimization_types"
    )
    time_based_ad_rotation_id_blocks: list[list[int]] = Field(
        None, alias="time_based_ad_rotation_id_blocks"
    )
    time_based_ad_rotation_intervals: list[int] = Field(
        None, alias="time_based_ad_rotation_intervals"
    )
    updated_time: datetime = Field(None, alias="updated_time")
    use_new_app_click: bool = Field(None, alias="use_new_app_click")


class AdSetGetActivitiesParams(BaseModel):
    """Parameters for AdSet.get_activities()."""

    model_config = ConfigDict(extra="forbid")
    after: str | None = Field(None, description="after parameter")
    business_id: str | None = Field(None, description="business_id parameter")
    category: adcampaignactivities_category_enum_param | None = Field(
        None, description="category parameter"
    )
    limit: int | None = Field(None, description="limit parameter")
    since: datetime | None = Field(None, description="since parameter")
    uid: int | None = Field(None, description="uid parameter")
    until: datetime | None = Field(None, description="until parameter")


class AdSetDeleteAdLabelsParams(BaseModel):
    """Parameters for AdSet.delete_ad_labels()."""

    model_config = ConfigDict(extra="forbid")
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    execution_options: list[adcampaignadlabels_execution_options_enum_param] | None = Field(
        None, description="execution_options parameter"
    )


class AdSetCreateAdLabelParams(BaseModel):
    """Parameters for AdSet.create_ad_label()."""

    model_config = ConfigDict(extra="forbid")
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")
    execution_options: list[adcampaignadlabels_execution_options_enum_param] | None = Field(
        None, description="execution_options parameter"
    )


class AdSetGetAdrulesGovernedParams(BaseModel):
    """Parameters for AdSet.get_adrules_governed()."""

    model_config = ConfigDict(extra="forbid")
    pass_evaluation: bool | None = Field(None, description="pass_evaluation parameter")


class AdSetGetAdSParams(BaseModel):
    """Parameters for AdSet.get_ad_s()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adcampaignads_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[str] | None = Field(None, description="effective_status parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")
    updated_since: int | None = Field(None, description="updated_since parameter")


class AdSetGetAsyncAdRequestsParams(BaseModel):
    """Parameters for AdSet.get_async_ad_requests()."""

    model_config = ConfigDict(extra="forbid")
    statuses: list[adcampaignasyncadrequests_statuses_enum_param] | None = Field(
        None, description="statuses parameter"
    )


class AdSetCreateBudgetScheduleParams(BaseModel):
    """Parameters for AdSet.create_budget_schedule()."""

    model_config = ConfigDict(extra="forbid")
    budget_value: int | None = Field(None, description="budget_value parameter")
    budget_value_type: adcampaignbudget_schedules_budget_value_type_enum_param | None = Field(
        None, description="budget_value_type parameter"
    )
    time_end: int | None = Field(None, description="time_end parameter")
    time_start: int | None = Field(None, description="time_start parameter")


class AdSetGetCopiesParams(BaseModel):
    """Parameters for AdSet.get_copies()."""

    model_config = ConfigDict(extra="forbid")
    date_preset: adcampaigncopies_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    effective_status: list[adcampaigncopies_effective_status_enum_param] | None = Field(
        None, description="effective_status parameter"
    )
    is_completed: bool | None = Field(None, description="is_completed parameter")
    time_range: dict[str, Any] | None = Field(None, description="time_range parameter")


class AdSetCreateCopieParams(BaseModel):
    """Parameters for AdSet.create_copie()."""

    model_config = ConfigDict(extra="forbid")
    campaign_id: str | None = Field(None, description="campaign_id parameter")
    create_dco_adset: bool | None = Field(None, description="create_dco_adset parameter")
    deep_copy: bool | None = Field(None, description="deep_copy parameter")
    end_time: datetime | None = Field(None, description="end_time parameter")
    rename_options: dict[str, Any] | None = Field(None, description="rename_options parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")
    status_option: adcampaigncopies_status_option_enum_param | None = Field(
        None, description="status_option parameter"
    )


class AdSetGetDeliveryEstimateParams(BaseModel):
    """Parameters for AdSet.get_delivery_estimate()."""

    model_config = ConfigDict(extra="forbid")
    optimization_goal: adcampaigndelivery_estimate_optimization_goal_enum_param | None = Field(
        None, description="optimization_goal parameter"
    )
    promoted_object: dict[str, Any] | None = Field(None, description="promoted_object parameter")
    targeting_spec: dict[str, Any] | None = Field(None, description="targeting_spec parameter")


class AdSetGetInsightsParams(BaseModel):
    """Parameters for AdSet.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adcampaigninsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adcampaigninsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adcampaigninsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adcampaigninsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adcampaigninsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adcampaigninsights_level_enum_param | None = Field(None, description="level parameter")
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: (
        list[adcampaigninsights_summary_action_breakdowns_enum_param] | None
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


class AdSetCreateInsightParams(BaseModel):
    """Parameters for AdSet.create_insight()."""

    model_config = ConfigDict(extra="forbid")
    action_attribution_windows: (
        list[adcampaigninsights_action_attribution_windows_enum_param] | None
    ) = Field(None, description="action_attribution_windows parameter")
    action_breakdowns: list[adcampaigninsights_action_breakdowns_enum_param] | None = Field(
        None, description="action_breakdowns parameter"
    )
    action_report_time: adcampaigninsights_action_report_time_enum_param | None = Field(
        None, description="action_report_time parameter"
    )
    breakdowns: list[adcampaigninsights_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    date_preset: adcampaigninsights_date_preset_enum_param | None = Field(
        None, description="date_preset parameter"
    )
    default_summary: bool | None = Field(None, description="default_summary parameter")
    export_columns: list[str] | None = Field(None, description="export_columns parameter")
    export_format: str | None = Field(None, description="export_format parameter")
    export_name: str | None = Field(None, description="export_name parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    filtering: list[dict[str, Any]] | None = Field(None, description="filtering parameter")
    level: adcampaigninsights_level_enum_param | None = Field(None, description="level parameter")
    limit: int | None = Field(None, description="limit parameter")
    product_id_limit: int | None = Field(None, description="product_id_limit parameter")
    sort: list[str] | None = Field(None, description="sort parameter")
    summary: list[str] | None = Field(None, description="summary parameter")
    summary_action_breakdowns: (
        list[adcampaigninsights_summary_action_breakdowns_enum_param] | None
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


class AdSetGetMessageDeliveryEstimateParams(BaseModel):
    """Parameters for AdSet.get_message_delivery_estimate()."""

    model_config = ConfigDict(extra="forbid")
    bid_amount: int | None = Field(None, description="bid_amount parameter")
    daily_budget: int | None = Field(None, description="daily_budget parameter")
    is_direct_send_campaign: bool | None = Field(
        None, description="is_direct_send_campaign parameter"
    )
    lifetime_budget: int | None = Field(None, description="lifetime_budget parameter")
    lifetime_in_days: int | None = Field(None, description="lifetime_in_days parameter")
    optimization_goal: adcampaignmessage_delivery_estimate_optimization_goal_enum_param | None = (
        Field(None, description="optimization_goal parameter")
    )
    pacing_type: adcampaignmessage_delivery_estimate_pacing_type_enum_param | None = Field(
        None, description="pacing_type parameter"
    )
    promoted_object: dict[str, Any] | None = Field(None, description="promoted_object parameter")
    targeting_spec: dict[str, Any] | None = Field(None, description="targeting_spec parameter")
