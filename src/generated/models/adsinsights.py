"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adsactionstats import AdsActionStatsFields
    from .adshistogramstats import AdsHistogramStatsFields


# Field literal type
AdsInsightsField = Literal[
    "account_currency",
    "account_id",
    "account_name",
    "action_values",
    "actions",
    "ad_click_actions",
    "ad_id",
    "ad_impression_actions",
    "ad_name",
    "adset_end",
    "adset_id",
    "adset_name",
    "adset_start",
    "age_targeting",
    "attribution_setting",
    "auction_bid",
    "auction_competitiveness",
    "auction_max_competitor_bid",
    "average_purchases_conversion_value",
    "buying_type",
    "campaign_id",
    "campaign_name",
    "canvas_avg_view_percent",
    "canvas_avg_view_time",
    "catalog_segment_actions",
    "catalog_segment_value",
    "catalog_segment_value_mobile_purchase_roas",
    "catalog_segment_value_omni_purchase_roas",
    "catalog_segment_value_website_purchase_roas",
    "clicks",
    "conversion_lead_rate",
    "conversion_leads",
    "conversion_rate_ranking",
    "conversion_values",
    "conversions",
    "converted_product_app_custom_event_fb_mobile_purchase",
    "converted_product_app_custom_event_fb_mobile_purchase_value",
    "converted_product_offline_purchase",
    "converted_product_offline_purchase_value",
    "converted_product_omni_purchase",
    "converted_product_omni_purchase_values",
    "converted_product_quantity",
    "converted_product_value",
    "converted_product_website_pixel_purchase",
    "converted_product_website_pixel_purchase_value",
    "converted_promoted_product_app_custom_event_fb_mobile_purchase",
    "converted_promoted_product_app_custom_event_fb_mobile_purchase_value",
    "converted_promoted_product_offline_purchase",
    "converted_promoted_product_offline_purchase_value",
    "converted_promoted_product_omni_purchase",
    "converted_promoted_product_omni_purchase_values",
    "converted_promoted_product_quantity",
    "converted_promoted_product_value",
    "converted_promoted_product_website_pixel_purchase",
    "converted_promoted_product_website_pixel_purchase_value",
    "cost_per_15_sec_video_view",
    "cost_per_2_sec_continuous_video_view",
    "cost_per_action_type",
    "cost_per_ad_click",
    "cost_per_conversion",
    "cost_per_conversion_lead",
    "cost_per_dda_countby_convs",
    "cost_per_estimated_ad_recallers",
    "cost_per_inline_link_click",
    "cost_per_inline_post_engagement",
    "cost_per_objective_result",
    "cost_per_one_thousand_ad_impression",
    "cost_per_outbound_click",
    "cost_per_result",
    "cost_per_thruplay",
    "cost_per_unique_action_type",
    "cost_per_unique_click",
    "cost_per_unique_conversion",
    "cost_per_unique_inline_link_click",
    "cost_per_unique_outbound_click",
    "cpc",
    "cpm",
    "cpp",
    "created_time",
    "creative_media_type",
    "ctr",
    "date_start",
    "date_stop",
    "dda_countby_convs",
    "dda_results",
    "engagement_rate_ranking",
    "estimated_ad_recall_rate",
    "estimated_ad_recall_rate_lower_bound",
    "estimated_ad_recall_rate_upper_bound",
    "estimated_ad_recallers",
    "estimated_ad_recallers_lower_bound",
    "estimated_ad_recallers_upper_bound",
    "frequency",
    "full_view_impressions",
    "full_view_reach",
    "gender_targeting",
    "impressions",
    "inline_link_click_ctr",
    "inline_link_clicks",
    "inline_post_engagement",
    "instagram_upcoming_event_reminders_set",
    "instant_experience_clicks_to_open",
    "instant_experience_clicks_to_start",
    "instant_experience_outbound_clicks",
    "interactive_component_tap",
    "labels",
    "landing_page_view_actions_per_link_click",
    "landing_page_view_per_link_click",
    "landing_page_view_per_purchase_rate",
    "location",
    "marketing_messages_click_rate_benchmark",
    "marketing_messages_cost_per_delivered",
    "marketing_messages_cost_per_link_btn_click",
    "marketing_messages_delivered",
    "marketing_messages_delivery_rate",
    "marketing_messages_link_btn_click",
    "marketing_messages_link_btn_click_rate",
    "marketing_messages_media_view_rate",
    "marketing_messages_phone_call_btn_click_rate",
    "marketing_messages_quick_reply_btn_click",
    "marketing_messages_quick_reply_btn_click_rate",
    "marketing_messages_read",
    "marketing_messages_read_rate",
    "marketing_messages_read_rate_benchmark",
    "marketing_messages_sent",
    "marketing_messages_spend",
    "marketing_messages_spend_currency",
    "marketing_messages_website_add_to_cart",
    "marketing_messages_website_initiate_checkout",
    "marketing_messages_website_purchase",
    "marketing_messages_website_purchase_values",
    "mobile_app_purchase_roas",
    "objective",
    "objective_result_rate",
    "objective_results",
    "onsite_conversion_messaging_detected_purchase_deduped",
    "optimization_goal",
    "outbound_clicks",
    "outbound_clicks_ctr",
    "place_page_name",
    "product_brand",
    "product_category",
    "product_content_id",
    "product_custom_label_0",
    "product_custom_label_1",
    "product_custom_label_2",
    "product_custom_label_3",
    "product_custom_label_4",
    "product_group_content_id",
    "product_group_retailer_id",
    "product_name",
    "product_retailer_id",
    "purchase_per_landing_page_view",
    "purchase_roas",
    "purchases_per_link_click",
    "qualifying_question_qualify_answer_rate",
    "quality_ranking",
    "reach",
    "result_rate",
    "result_values_performance_indicator",
    "results",
    "shops_assisted_purchases",
    "social_spend",
    "spend",
    "total_postbacks",
    "total_postbacks_detailed",
    "total_postbacks_detailed_v4",
    "unique_actions",
    "unique_clicks",
    "unique_conversions",
    "unique_ctr",
    "unique_inline_link_click_ctr",
    "unique_inline_link_clicks",
    "unique_link_clicks_ctr",
    "unique_outbound_clicks",
    "unique_outbound_clicks_ctr",
    "unique_video_continuous_2_sec_watched_actions",
    "unique_video_view_15_sec",
    "updated_time",
    "video_15_sec_watched_actions",
    "video_30_sec_watched_actions",
    "video_avg_time_watched_actions",
    "video_continuous_2_sec_watched_actions",
    "video_p100_watched_actions",
    "video_p25_watched_actions",
    "video_p50_watched_actions",
    "video_p75_watched_actions",
    "video_p95_watched_actions",
    "video_play_actions",
    "video_play_curve_actions",
    "video_play_retention_0_to_15s_actions",
    "video_play_retention_20_to_60s_actions",
    "video_play_retention_graph_actions",
    "video_thruplay_watched_actions",
    "video_time_watched_actions",
    "video_view_per_impression",
    "website_ctr",
    "website_purchase_roas",
    "wish_bid",
]


class AdsInsightsFields(BaseModel):
    """Pydantic model for AdsInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_currency: str = Field(None, alias="account_currency")
    account_id: str = Field(None, alias="account_id")
    account_name: str = Field(None, alias="account_name")
    action_values: list[AdsActionStatsFields] = Field(None, alias="action_values")
    actions: list[AdsActionStatsFields] = Field(None, alias="actions")
    ad_click_actions: list[AdsActionStatsFields] = Field(None, alias="ad_click_actions")
    ad_id: str = Field(None, alias="ad_id")
    ad_impression_actions: list[AdsActionStatsFields] = Field(None, alias="ad_impression_actions")
    ad_name: str = Field(None, alias="ad_name")
    adset_end: str = Field(None, alias="adset_end")
    adset_id: str = Field(None, alias="adset_id")
    adset_name: str = Field(None, alias="adset_name")
    adset_start: str = Field(None, alias="adset_start")
    age_targeting: str = Field(None, alias="age_targeting")
    attribution_setting: str = Field(None, alias="attribution_setting")
    auction_bid: str = Field(None, alias="auction_bid")
    auction_competitiveness: str = Field(None, alias="auction_competitiveness")
    auction_max_competitor_bid: str = Field(None, alias="auction_max_competitor_bid")
    average_purchases_conversion_value: list[AdsActionStatsFields] = Field(
        None, alias="average_purchases_conversion_value"
    )
    buying_type: str = Field(None, alias="buying_type")
    campaign_id: str = Field(None, alias="campaign_id")
    campaign_name: str = Field(None, alias="campaign_name")
    canvas_avg_view_percent: str = Field(None, alias="canvas_avg_view_percent")
    canvas_avg_view_time: str = Field(None, alias="canvas_avg_view_time")
    catalog_segment_actions: list[AdsActionStatsFields] = Field(
        None, alias="catalog_segment_actions"
    )
    catalog_segment_value: list[AdsActionStatsFields] = Field(None, alias="catalog_segment_value")
    catalog_segment_value_mobile_purchase_roas: list[AdsActionStatsFields] = Field(
        None, alias="catalog_segment_value_mobile_purchase_roas"
    )
    catalog_segment_value_omni_purchase_roas: list[AdsActionStatsFields] = Field(
        None, alias="catalog_segment_value_omni_purchase_roas"
    )
    catalog_segment_value_website_purchase_roas: list[AdsActionStatsFields] = Field(
        None, alias="catalog_segment_value_website_purchase_roas"
    )
    clicks: str = Field(None, alias="clicks")
    conversion_lead_rate: list[AdsActionStatsFields] = Field(None, alias="conversion_lead_rate")
    conversion_leads: list[AdsActionStatsFields] = Field(None, alias="conversion_leads")
    conversion_rate_ranking: str = Field(None, alias="conversion_rate_ranking")
    conversion_values: list[AdsActionStatsFields] = Field(None, alias="conversion_values")
    conversions: list[AdsActionStatsFields] = Field(None, alias="conversions")
    converted_product_app_custom_event_fb_mobile_purchase: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_app_custom_event_fb_mobile_purchase"
    )
    converted_product_app_custom_event_fb_mobile_purchase_value: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_app_custom_event_fb_mobile_purchase_value"
    )
    converted_product_offline_purchase: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_offline_purchase"
    )
    converted_product_offline_purchase_value: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_offline_purchase_value"
    )
    converted_product_omni_purchase: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_omni_purchase"
    )
    converted_product_omni_purchase_values: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_omni_purchase_values"
    )
    converted_product_quantity: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_quantity"
    )
    converted_product_value: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_value"
    )
    converted_product_website_pixel_purchase: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_website_pixel_purchase"
    )
    converted_product_website_pixel_purchase_value: list[AdsActionStatsFields] = Field(
        None, alias="converted_product_website_pixel_purchase_value"
    )
    converted_promoted_product_app_custom_event_fb_mobile_purchase: list[AdsActionStatsFields] = (
        Field(None, alias="converted_promoted_product_app_custom_event_fb_mobile_purchase")
    )
    converted_promoted_product_app_custom_event_fb_mobile_purchase_value: list[
        AdsActionStatsFields
    ] = Field(None, alias="converted_promoted_product_app_custom_event_fb_mobile_purchase_value")
    converted_promoted_product_offline_purchase: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_offline_purchase"
    )
    converted_promoted_product_offline_purchase_value: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_offline_purchase_value"
    )
    converted_promoted_product_omni_purchase: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_omni_purchase"
    )
    converted_promoted_product_omni_purchase_values: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_omni_purchase_values"
    )
    converted_promoted_product_quantity: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_quantity"
    )
    converted_promoted_product_value: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_value"
    )
    converted_promoted_product_website_pixel_purchase: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_website_pixel_purchase"
    )
    converted_promoted_product_website_pixel_purchase_value: list[AdsActionStatsFields] = Field(
        None, alias="converted_promoted_product_website_pixel_purchase_value"
    )
    cost_per_15_sec_video_view: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_15_sec_video_view"
    )
    cost_per_2_sec_continuous_video_view: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_2_sec_continuous_video_view"
    )
    cost_per_action_type: list[AdsActionStatsFields] = Field(None, alias="cost_per_action_type")
    cost_per_ad_click: list[AdsActionStatsFields] = Field(None, alias="cost_per_ad_click")
    cost_per_conversion: list[AdsActionStatsFields] = Field(None, alias="cost_per_conversion")
    cost_per_conversion_lead: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_conversion_lead"
    )
    cost_per_dda_countby_convs: str = Field(None, alias="cost_per_dda_countby_convs")
    cost_per_estimated_ad_recallers: str = Field(None, alias="cost_per_estimated_ad_recallers")
    cost_per_inline_link_click: str = Field(None, alias="cost_per_inline_link_click")
    cost_per_inline_post_engagement: str = Field(None, alias="cost_per_inline_post_engagement")
    cost_per_objective_result: list[dict[str, Any]] = Field(None, alias="cost_per_objective_result")
    cost_per_one_thousand_ad_impression: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_one_thousand_ad_impression"
    )
    cost_per_outbound_click: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_outbound_click"
    )
    cost_per_result: list[dict[str, Any]] = Field(None, alias="cost_per_result")
    cost_per_thruplay: list[AdsActionStatsFields] = Field(None, alias="cost_per_thruplay")
    cost_per_unique_action_type: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_unique_action_type"
    )
    cost_per_unique_click: str = Field(None, alias="cost_per_unique_click")
    cost_per_unique_conversion: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_unique_conversion"
    )
    cost_per_unique_inline_link_click: str = Field(None, alias="cost_per_unique_inline_link_click")
    cost_per_unique_outbound_click: list[AdsActionStatsFields] = Field(
        None, alias="cost_per_unique_outbound_click"
    )
    cpc: str = Field(None, alias="cpc")
    cpm: str = Field(None, alias="cpm")
    cpp: str = Field(None, alias="cpp")
    created_time: str = Field(None, alias="created_time")
    creative_media_type: str = Field(None, alias="creative_media_type")
    ctr: str = Field(None, alias="ctr")
    date_start: str = Field(None, alias="date_start")
    date_stop: str = Field(None, alias="date_stop")
    dda_countby_convs: str = Field(None, alias="dda_countby_convs")
    dda_results: list[dict[str, Any]] = Field(None, alias="dda_results")
    engagement_rate_ranking: str = Field(None, alias="engagement_rate_ranking")
    estimated_ad_recall_rate: str = Field(None, alias="estimated_ad_recall_rate")
    estimated_ad_recall_rate_lower_bound: str = Field(
        None, alias="estimated_ad_recall_rate_lower_bound"
    )
    estimated_ad_recall_rate_upper_bound: str = Field(
        None, alias="estimated_ad_recall_rate_upper_bound"
    )
    estimated_ad_recallers: str = Field(None, alias="estimated_ad_recallers")
    estimated_ad_recallers_lower_bound: str = Field(
        None, alias="estimated_ad_recallers_lower_bound"
    )
    estimated_ad_recallers_upper_bound: str = Field(
        None, alias="estimated_ad_recallers_upper_bound"
    )
    frequency: str = Field(None, alias="frequency")
    full_view_impressions: str = Field(None, alias="full_view_impressions")
    full_view_reach: str = Field(None, alias="full_view_reach")
    gender_targeting: str = Field(None, alias="gender_targeting")
    impressions: str = Field(None, alias="impressions")
    inline_link_click_ctr: str = Field(None, alias="inline_link_click_ctr")
    inline_link_clicks: str = Field(None, alias="inline_link_clicks")
    inline_post_engagement: str = Field(None, alias="inline_post_engagement")
    instagram_upcoming_event_reminders_set: str = Field(
        None, alias="instagram_upcoming_event_reminders_set"
    )
    instant_experience_clicks_to_open: str = Field(None, alias="instant_experience_clicks_to_open")
    instant_experience_clicks_to_start: str = Field(
        None, alias="instant_experience_clicks_to_start"
    )
    instant_experience_outbound_clicks: list[AdsActionStatsFields] = Field(
        None, alias="instant_experience_outbound_clicks"
    )
    interactive_component_tap: list[AdsActionStatsFields] = Field(
        None, alias="interactive_component_tap"
    )
    labels: str = Field(None, alias="labels")
    landing_page_view_actions_per_link_click: str = Field(
        None, alias="landing_page_view_actions_per_link_click"
    )
    landing_page_view_per_link_click: str = Field(None, alias="landing_page_view_per_link_click")
    landing_page_view_per_purchase_rate: str = Field(
        None, alias="landing_page_view_per_purchase_rate"
    )
    location: str = Field(None, alias="location")
    marketing_messages_click_rate_benchmark: str = Field(
        None, alias="marketing_messages_click_rate_benchmark"
    )
    marketing_messages_cost_per_delivered: str = Field(
        None, alias="marketing_messages_cost_per_delivered"
    )
    marketing_messages_cost_per_link_btn_click: str = Field(
        None, alias="marketing_messages_cost_per_link_btn_click"
    )
    marketing_messages_delivered: str = Field(None, alias="marketing_messages_delivered")
    marketing_messages_delivery_rate: str = Field(None, alias="marketing_messages_delivery_rate")
    marketing_messages_link_btn_click: str = Field(None, alias="marketing_messages_link_btn_click")
    marketing_messages_link_btn_click_rate: str = Field(
        None, alias="marketing_messages_link_btn_click_rate"
    )
    marketing_messages_media_view_rate: str = Field(
        None, alias="marketing_messages_media_view_rate"
    )
    marketing_messages_phone_call_btn_click_rate: str = Field(
        None, alias="marketing_messages_phone_call_btn_click_rate"
    )
    marketing_messages_quick_reply_btn_click: str = Field(
        None, alias="marketing_messages_quick_reply_btn_click"
    )
    marketing_messages_quick_reply_btn_click_rate: str = Field(
        None, alias="marketing_messages_quick_reply_btn_click_rate"
    )
    marketing_messages_read: str = Field(None, alias="marketing_messages_read")
    marketing_messages_read_rate: str = Field(None, alias="marketing_messages_read_rate")
    marketing_messages_read_rate_benchmark: str = Field(
        None, alias="marketing_messages_read_rate_benchmark"
    )
    marketing_messages_sent: str = Field(None, alias="marketing_messages_sent")
    marketing_messages_spend: str = Field(None, alias="marketing_messages_spend")
    marketing_messages_spend_currency: str = Field(None, alias="marketing_messages_spend_currency")
    marketing_messages_website_add_to_cart: str = Field(
        None, alias="marketing_messages_website_add_to_cart"
    )
    marketing_messages_website_initiate_checkout: str = Field(
        None, alias="marketing_messages_website_initiate_checkout"
    )
    marketing_messages_website_purchase: str = Field(
        None, alias="marketing_messages_website_purchase"
    )
    marketing_messages_website_purchase_values: str = Field(
        None, alias="marketing_messages_website_purchase_values"
    )
    mobile_app_purchase_roas: list[AdsActionStatsFields] = Field(
        None, alias="mobile_app_purchase_roas"
    )
    objective: str = Field(None, alias="objective")
    objective_result_rate: list[dict[str, Any]] = Field(None, alias="objective_result_rate")
    objective_results: list[dict[str, Any]] = Field(None, alias="objective_results")
    onsite_conversion_messaging_detected_purchase_deduped: list[AdsActionStatsFields] = Field(
        None, alias="onsite_conversion_messaging_detected_purchase_deduped"
    )
    optimization_goal: str = Field(None, alias="optimization_goal")
    outbound_clicks: list[AdsActionStatsFields] = Field(None, alias="outbound_clicks")
    outbound_clicks_ctr: list[AdsActionStatsFields] = Field(None, alias="outbound_clicks_ctr")
    place_page_name: str = Field(None, alias="place_page_name")
    product_brand: str = Field(None, alias="product_brand")
    product_category: str = Field(None, alias="product_category")
    product_content_id: str = Field(None, alias="product_content_id")
    product_custom_label_0: str = Field(None, alias="product_custom_label_0")
    product_custom_label_1: str = Field(None, alias="product_custom_label_1")
    product_custom_label_2: str = Field(None, alias="product_custom_label_2")
    product_custom_label_3: str = Field(None, alias="product_custom_label_3")
    product_custom_label_4: str = Field(None, alias="product_custom_label_4")
    product_group_content_id: str = Field(None, alias="product_group_content_id")
    product_group_retailer_id: str = Field(None, alias="product_group_retailer_id")
    product_name: str = Field(None, alias="product_name")
    product_retailer_id: str = Field(None, alias="product_retailer_id")
    purchase_per_landing_page_view: str = Field(None, alias="purchase_per_landing_page_view")
    purchase_roas: list[AdsActionStatsFields] = Field(None, alias="purchase_roas")
    purchases_per_link_click: str = Field(None, alias="purchases_per_link_click")
    qualifying_question_qualify_answer_rate: str = Field(
        None, alias="qualifying_question_qualify_answer_rate"
    )
    quality_ranking: str = Field(None, alias="quality_ranking")
    reach: str = Field(None, alias="reach")
    result_rate: list[dict[str, Any]] = Field(None, alias="result_rate")
    result_values_performance_indicator: str = Field(
        None, alias="result_values_performance_indicator"
    )
    results: list[dict[str, Any]] = Field(None, alias="results")
    shops_assisted_purchases: str = Field(None, alias="shops_assisted_purchases")
    social_spend: str = Field(None, alias="social_spend")
    spend: str = Field(None, alias="spend")
    total_postbacks: str = Field(None, alias="total_postbacks")
    total_postbacks_detailed: list[AdsActionStatsFields] = Field(
        None, alias="total_postbacks_detailed"
    )
    total_postbacks_detailed_v4: list[AdsActionStatsFields] = Field(
        None, alias="total_postbacks_detailed_v4"
    )
    unique_actions: list[AdsActionStatsFields] = Field(None, alias="unique_actions")
    unique_clicks: str = Field(None, alias="unique_clicks")
    unique_conversions: list[AdsActionStatsFields] = Field(None, alias="unique_conversions")
    unique_ctr: str = Field(None, alias="unique_ctr")
    unique_inline_link_click_ctr: str = Field(None, alias="unique_inline_link_click_ctr")
    unique_inline_link_clicks: str = Field(None, alias="unique_inline_link_clicks")
    unique_link_clicks_ctr: str = Field(None, alias="unique_link_clicks_ctr")
    unique_outbound_clicks: list[AdsActionStatsFields] = Field(None, alias="unique_outbound_clicks")
    unique_outbound_clicks_ctr: list[AdsActionStatsFields] = Field(
        None, alias="unique_outbound_clicks_ctr"
    )
    unique_video_continuous_2_sec_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="unique_video_continuous_2_sec_watched_actions"
    )
    unique_video_view_15_sec: list[AdsActionStatsFields] = Field(
        None, alias="unique_video_view_15_sec"
    )
    updated_time: str = Field(None, alias="updated_time")
    video_15_sec_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_15_sec_watched_actions"
    )
    video_30_sec_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_30_sec_watched_actions"
    )
    video_avg_time_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_avg_time_watched_actions"
    )
    video_continuous_2_sec_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_continuous_2_sec_watched_actions"
    )
    video_p100_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_p100_watched_actions"
    )
    video_p25_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_p25_watched_actions"
    )
    video_p50_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_p50_watched_actions"
    )
    video_p75_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_p75_watched_actions"
    )
    video_p95_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_p95_watched_actions"
    )
    video_play_actions: list[AdsActionStatsFields] = Field(None, alias="video_play_actions")
    video_play_curve_actions: list[AdsHistogramStatsFields] = Field(
        None, alias="video_play_curve_actions"
    )
    video_play_retention_0_to_15s_actions: list[AdsHistogramStatsFields] = Field(
        None, alias="video_play_retention_0_to_15s_actions"
    )
    video_play_retention_20_to_60s_actions: list[AdsHistogramStatsFields] = Field(
        None, alias="video_play_retention_20_to_60s_actions"
    )
    video_play_retention_graph_actions: list[AdsHistogramStatsFields] = Field(
        None, alias="video_play_retention_graph_actions"
    )
    video_thruplay_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_thruplay_watched_actions"
    )
    video_time_watched_actions: list[AdsActionStatsFields] = Field(
        None, alias="video_time_watched_actions"
    )
    video_view_per_impression: list[AdsActionStatsFields] = Field(
        None, alias="video_view_per_impression"
    )
    website_ctr: list[AdsActionStatsFields] = Field(None, alias="website_ctr")
    website_purchase_roas: list[AdsActionStatsFields] = Field(None, alias="website_purchase_roas")
    wish_bid: str = Field(None, alias="wish_bid")
