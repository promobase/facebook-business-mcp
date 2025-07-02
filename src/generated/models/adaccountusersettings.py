"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .user import UserFields


class AdAccountUserSettings_syd_campaign_trends_objective(str, Enum):
    """AdAccountUserSettings_syd_campaign_trends_objective enum values."""

    APP_INSTALLS = "APP_INSTALLS"
    BRAND_AWARENESS = "BRAND_AWARENESS"
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
    WEBSITE_CONVERSIONS = "WEBSITE_CONVERSIONS"


# Field literal type
AdAccountUserSettingsField = Literal[
    "acf_should_opt_out_video_adjustments",
    "aco_sticky_settings",
    "actions_quick_view_created",
    "active_ads_quick_view_created",
    "ad_account",
    "ad_object_export_format",
    "ads_manager_footer_row_toast_impressions",
    "auto_review_video_caption",
    "campaign_overview_columns",
    "column_suggestion_status",
    "conditional_formatting_rules",
    "default_account_overview_agegender_metrics",
    "default_account_overview_location_metrics",
    "default_account_overview_metrics",
    "default_account_overview_time_metrics",
    "default_builtin_column_preset",
    "default_nam_time_range",
    "draft_mode_enabled",
    "export_deleted_items_with_delivery",
    "export_summary_row",
    "had_delivery_quick_view_created",
    "has_seen_groups_column_flexing_experience",
    "has_seen_instagram_column_flexing_experience",
    "has_seen_leads_column_flexing_experience",
    "has_seen_shops_ads_metrics_onboarding_tour",
    "has_seen_shops_column_flexing_experience",
    "hidden_optimization_tips",
    "high_performing_quick_view_created",
    "id",
    "is_3p_auth_setting_set",
    "is_ads_manager_footer_row_preference_set",
    "is_ads_manager_footer_row_shown",
    "is_text_variation_nux_close",
    "last_used_columns",
    "last_used_pe_filters",
    "last_used_website_urls",
    "outlier_preferences",
    "pinned_ad_object_ids",
    "rb_export_format",
    "rb_export_raw_data",
    "rb_export_summary_row",
    "saip_advertiser_setup_optimisation_guidance_overall_state",
    "saip_advertiser_setup_optimisation_guidance_state",
    "shops_ads_metrics_onboarding_tour_close_count",
    "shops_ads_metrics_onboarding_tour_last_action_time",
    "should_default_image_auto_crop",
    "should_default_image_auto_crop_for_tail",
    "should_default_image_auto_crop_optimization",
    "should_default_image_dof_toggle",
    "should_default_image_lpp_ads_to_square",
    "should_default_instagram_profile_card_optimization",
    "should_default_text_swapping_optimization",
    "should_logout_of_3p_sourcing",
    "should_show_shops_ads_metrics_onboarding_tour",
    "show_archived_data",
    "show_text_variation_nux_tooltip",
    "syd_campaign_trends_activemetric",
    "syd_campaign_trends_attribution",
    "syd_campaign_trends_metrics",
    "syd_campaign_trends_objective",
    "syd_campaign_trends_time_range",
    "syd_landing_page_opt_in_status",
    "text_gen_persona_opt_in_type",
    "text_variations_opt_in_out_ts",
    "text_variations_opt_in_type",
    "user",
]


class AdAccountUserSettingsFields(BaseModel):
    """Pydantic model for AdAccountUserSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    acf_should_opt_out_video_adjustments: bool = Field(
        None, alias="acf_should_opt_out_video_adjustments"
    )
    aco_sticky_settings: list[dict[str, str]] = Field(None, alias="aco_sticky_settings")
    actions_quick_view_created: bool = Field(None, alias="actions_quick_view_created")
    active_ads_quick_view_created: bool = Field(None, alias="active_ads_quick_view_created")
    ad_account: AdAccountFields = Field(None, alias="ad_account")
    ad_object_export_format: str = Field(None, alias="ad_object_export_format")
    ads_manager_footer_row_toast_impressions: int = Field(
        None, alias="ads_manager_footer_row_toast_impressions"
    )
    auto_review_video_caption: bool = Field(None, alias="auto_review_video_caption")
    campaign_overview_columns: list[str] = Field(None, alias="campaign_overview_columns")
    column_suggestion_status: str = Field(None, alias="column_suggestion_status")
    conditional_formatting_rules: list[str] = Field(None, alias="conditional_formatting_rules")
    default_account_overview_agegender_metrics: list[str] = Field(
        None, alias="default_account_overview_agegender_metrics"
    )
    default_account_overview_location_metrics: list[str] = Field(
        None, alias="default_account_overview_location_metrics"
    )
    default_account_overview_metrics: list[str] = Field(
        None, alias="default_account_overview_metrics"
    )
    default_account_overview_time_metrics: list[str] = Field(
        None, alias="default_account_overview_time_metrics"
    )
    default_builtin_column_preset: str = Field(None, alias="default_builtin_column_preset")
    default_nam_time_range: str = Field(None, alias="default_nam_time_range")
    draft_mode_enabled: bool = Field(None, alias="draft_mode_enabled")
    export_deleted_items_with_delivery: bool = Field(
        None, alias="export_deleted_items_with_delivery"
    )
    export_summary_row: bool = Field(None, alias="export_summary_row")
    had_delivery_quick_view_created: bool = Field(None, alias="had_delivery_quick_view_created")
    has_seen_groups_column_flexing_experience: bool = Field(
        None, alias="has_seen_groups_column_flexing_experience"
    )
    has_seen_instagram_column_flexing_experience: bool = Field(
        None, alias="has_seen_instagram_column_flexing_experience"
    )
    has_seen_leads_column_flexing_experience: bool = Field(
        None, alias="has_seen_leads_column_flexing_experience"
    )
    has_seen_shops_ads_metrics_onboarding_tour: bool = Field(
        None, alias="has_seen_shops_ads_metrics_onboarding_tour"
    )
    has_seen_shops_column_flexing_experience: bool = Field(
        None, alias="has_seen_shops_column_flexing_experience"
    )
    hidden_optimization_tips: list[dict[str, bool]] = Field(None, alias="hidden_optimization_tips")
    high_performing_quick_view_created: bool = Field(
        None, alias="high_performing_quick_view_created"
    )
    id: str = Field(None, alias="id")
    is_3p_auth_setting_set: bool = Field(None, alias="is_3p_auth_setting_set")
    is_ads_manager_footer_row_preference_set: bool = Field(
        None, alias="is_ads_manager_footer_row_preference_set"
    )
    is_ads_manager_footer_row_shown: bool = Field(None, alias="is_ads_manager_footer_row_shown")
    is_text_variation_nux_close: bool = Field(None, alias="is_text_variation_nux_close")
    last_used_columns: dict[str, Any] = Field(None, alias="last_used_columns")
    last_used_pe_filters: list[dict[str, Any]] = Field(None, alias="last_used_pe_filters")
    last_used_website_urls: list[str] = Field(None, alias="last_used_website_urls")
    outlier_preferences: dict[str, Any] = Field(None, alias="outlier_preferences")
    pinned_ad_object_ids: list[str] = Field(None, alias="pinned_ad_object_ids")
    rb_export_format: str = Field(None, alias="rb_export_format")
    rb_export_raw_data: bool = Field(None, alias="rb_export_raw_data")
    rb_export_summary_row: bool = Field(None, alias="rb_export_summary_row")
    saip_advertiser_setup_optimisation_guidance_overall_state: str = Field(
        None, alias="saip_advertiser_setup_optimisation_guidance_overall_state"
    )
    saip_advertiser_setup_optimisation_guidance_state: list[dict[str, str]] = Field(
        None, alias="saip_advertiser_setup_optimisation_guidance_state"
    )
    shops_ads_metrics_onboarding_tour_close_count: int = Field(
        None, alias="shops_ads_metrics_onboarding_tour_close_count"
    )
    shops_ads_metrics_onboarding_tour_last_action_time: datetime = Field(
        None, alias="shops_ads_metrics_onboarding_tour_last_action_time"
    )
    should_default_image_auto_crop: bool = Field(None, alias="should_default_image_auto_crop")
    should_default_image_auto_crop_for_tail: bool = Field(
        None, alias="should_default_image_auto_crop_for_tail"
    )
    should_default_image_auto_crop_optimization: bool = Field(
        None, alias="should_default_image_auto_crop_optimization"
    )
    should_default_image_dof_toggle: bool = Field(None, alias="should_default_image_dof_toggle")
    should_default_image_lpp_ads_to_square: bool = Field(
        None, alias="should_default_image_lpp_ads_to_square"
    )
    should_default_instagram_profile_card_optimization: bool = Field(
        None, alias="should_default_instagram_profile_card_optimization"
    )
    should_default_text_swapping_optimization: bool = Field(
        None, alias="should_default_text_swapping_optimization"
    )
    should_logout_of_3p_sourcing: bool = Field(None, alias="should_logout_of_3p_sourcing")
    should_show_shops_ads_metrics_onboarding_tour: bool = Field(
        None, alias="should_show_shops_ads_metrics_onboarding_tour"
    )
    show_archived_data: bool = Field(None, alias="show_archived_data")
    show_text_variation_nux_tooltip: bool = Field(None, alias="show_text_variation_nux_tooltip")
    syd_campaign_trends_activemetric: str = Field(None, alias="syd_campaign_trends_activemetric")
    syd_campaign_trends_attribution: str = Field(None, alias="syd_campaign_trends_attribution")
    syd_campaign_trends_metrics: list[str] = Field(None, alias="syd_campaign_trends_metrics")
    syd_campaign_trends_objective: dict[str, Any] = Field(
        None, alias="syd_campaign_trends_objective"
    )
    syd_campaign_trends_time_range: str = Field(None, alias="syd_campaign_trends_time_range")
    syd_landing_page_opt_in_status: str = Field(None, alias="syd_landing_page_opt_in_status")
    text_gen_persona_opt_in_type: str = Field(None, alias="text_gen_persona_opt_in_type")
    text_variations_opt_in_out_ts: datetime = Field(None, alias="text_variations_opt_in_out_ts")
    text_variations_opt_in_type: str = Field(None, alias="text_variations_opt_in_type")
    user: UserFields = Field(None, alias="user")
