"""Consolidated Insights operations for all Facebook Business API levels.

This module provides insights operations for AdAccount, Campaign, AdSet, and Ad objects.
"""

from enum import Enum
from typing import Any

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


class CommonAdInsightsFields:
    """
    Organizes AdsInsights fields into groups based on their
    typical usage frequency for reporting and analysis.
    This version uses direct class attribute access for type safety.
    """

    # --- High Frequency Usage (Core Metrics) ---
    # These fields are fundamental for most performance reports, providing
    # a top-level overview of how your ads are doing.
    HIGH_FREQUENCY = [
        AdsInsights.Field.account_id,
        AdsInsights.Field.account_name,
        AdsInsights.Field.actions,
        AdsInsights.Field.action_values,
        AdsInsights.Field.ad_id,
        AdsInsights.Field.ad_name,
        AdsInsights.Field.adset_id,
        AdsInsights.Field.adset_name,
        AdsInsights.Field.campaign_id,
        AdsInsights.Field.campaign_name,
        AdsInsights.Field.clicks,
        AdsInsights.Field.cost_per_action_type,
        AdsInsights.Field.cost_per_result,
        AdsInsights.Field.cpc,
        AdsInsights.Field.cpm,
        AdsInsights.Field.cpp,
        AdsInsights.Field.ctr,
        AdsInsights.Field.date_start,
        AdsInsights.Field.date_stop,
        AdsInsights.Field.frequency,
        AdsInsights.Field.impressions,
        AdsInsights.Field.objective,
        AdsInsights.Field.purchase_roas,
        AdsInsights.Field.reach,
        AdsInsights.Field.results,
        AdsInsights.Field.spend,
    ]

    # --- Medium Frequency Usage (Deeper Analysis) ---
    # Use these fields when you need to dig deeper into engagement,
    # video performance, or specific conversion funnels.
    MEDIUM_FREQUENCY = [
        AdsInsights.Field.adset_end,
        AdsInsights.Field.adset_start,
        AdsInsights.Field.buying_type,
        AdsInsights.Field.conversion_rate_ranking,
        AdsInsights.Field.conversions,
        AdsInsights.Field.cost_per_conversion,
        AdsInsights.Field.cost_per_inline_link_click,
        AdsInsights.Field.cost_per_outbound_click,
        AdsInsights.Field.cost_per_thruplay,
        AdsInsights.Field.cost_per_unique_click,
        AdsInsights.Field.engagement_rate_ranking,
        AdsInsights.Field.inline_link_click_ctr,
        AdsInsights.Field.inline_link_clicks,
        AdsInsights.Field.inline_post_engagement,
        AdsInsights.Field.mobile_app_purchase_roas,
        AdsInsights.Field.optimization_goal,
        AdsInsights.Field.outbound_clicks,
        AdsInsights.Field.outbound_clicks_ctr,
        AdsInsights.Field.quality_ranking,
        AdsInsights.Field.unique_actions,
        AdsInsights.Field.unique_clicks,
        AdsInsights.Field.unique_ctr,
        AdsInsights.Field.unique_inline_link_clicks,
        AdsInsights.Field.video_p25_watched_actions,
        AdsInsights.Field.video_p50_watched_actions,
        AdsInsights.Field.video_p75_watched_actions,
        AdsInsights.Field.video_p100_watched_actions,
        AdsInsights.Field.video_play_actions,
        AdsInsights.Field.video_thruplay_watched_actions,
        AdsInsights.Field.website_ctr,
        AdsInsights.Field.website_purchase_roas,
    ]

    # --- Low Frequency Usage (Specialized & Granular Metrics) ---
    # These fields are for highly specific or advanced use cases, such as
    # analyzing catalog sales, attribution modeling, or detailed breakdowns.
    LOW_FREQUENCY = [
        AdsInsights.Field.account_currency,
        AdsInsights.Field.ad_click_actions,
        AdsInsights.Field.ad_impression_actions,
        AdsInsights.Field.age_targeting,
        AdsInsights.Field.attribution_setting,
        AdsInsights.Field.auction_bid,
        AdsInsights.Field.auction_competitiveness,
        AdsInsights.Field.auction_max_competitor_bid,
        AdsInsights.Field.average_purchases_conversion_value,
        AdsInsights.Field.canvas_avg_view_percent,
        AdsInsights.Field.canvas_avg_view_time,
        AdsInsights.Field.catalog_segment_actions,
        AdsInsights.Field.catalog_segment_value,
        AdsInsights.Field.catalog_segment_value_mobile_purchase_roas,
        AdsInsights.Field.catalog_segment_value_omni_purchase_roas,
        AdsInsights.Field.catalog_segment_value_website_purchase_roas,
        AdsInsights.Field.conversion_lead_rate,
        AdsInsights.Field.conversion_leads,
        AdsInsights.Field.conversion_values,
        AdsInsights.Field.cost_per_15_sec_video_view,
        AdsInsights.Field.cost_per_2_sec_continuous_video_view,
        AdsInsights.Field.created_time,
        AdsInsights.Field.creative_media_type,
        AdsInsights.Field.dda_countby_convs,
        AdsInsights.Field.dda_results,
        AdsInsights.Field.full_view_impressions,
        AdsInsights.Field.full_view_reach,
        AdsInsights.Field.gender_targeting,
        AdsInsights.Field.instagram_upcoming_event_reminders_set,
        AdsInsights.Field.labels,
        AdsInsights.Field.location,
        AdsInsights.Field.place_page_name,
        AdsInsights.Field.qualifying_question_qualify_answer_rate,
        AdsInsights.Field.social_spend,
        AdsInsights.Field.total_postbacks,
        AdsInsights.Field.total_postbacks_detailed,
        AdsInsights.Field.total_postbacks_detailed_v4,
        AdsInsights.Field.updated_time,
        AdsInsights.Field.wish_bid,
    ]

    basic = list(set(HIGH_FREQUENCY + MEDIUM_FREQUENCY))


class InsightsLevel(str, Enum):
    """Supported levels for insights operations."""

    ACCOUNT = "account"
    CAMPAIGN = "campaign"
    ADSET = "adset"
    AD = "ad"


def _get_object_by_level(level: str, object_id: str):
    """Get the appropriate Facebook object based on level."""
    if level == InsightsLevel.ACCOUNT:
        # Ensure account_id has the correct prefix
        if not object_id.startswith("act_"):
            object_id = f"act_{object_id}"
        return AdAccount(object_id)
    elif level == InsightsLevel.CAMPAIGN:
        return Campaign(object_id)
    elif level == InsightsLevel.ADSET:
        return AdSet(object_id)
    elif level == InsightsLevel.AD:
        return Ad(object_id)
    else:
        raise ValueError(
            f"Invalid level: {level}. Must be one of: {[e.value for e in InsightsLevel]}"
        )


@handle_facebook_errors
def get_insights(
    level: str, object_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for any Facebook Business object.

    This is a unified wrapper around get_insights() for all object types.
    If no fields are provided, it defaults to the basic fields.

    Args:
        level: The object level (account, campaign, adset, ad)
        object_id: The object ID
        fields: Fields to retrieve
        params: Additional parameters (e.g., date_preset, breakdowns)

    Returns:
        Insights data from the API
    """
    obj = _get_object_by_level(level, object_id)
    fields = fields or CommonAdInsightsFields.basic
    return obj.get_insights(fields=fields, params=params)


@handle_facebook_errors
def get_insights_async(
    level: str, object_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for any Facebook Business object.

    This is a unified wrapper around get_insights_async() for all object types.

    Args:
        level: The object level (account, campaign, adset, ad)
        object_id: The object ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    obj = _get_object_by_level(level, object_id)
    fields = fields or CommonAdInsightsFields.basic
    return obj.get_insights_async(fields=fields, params=params)


# Convenience functions for each level
@handle_facebook_errors
def account_get_insights(
    account_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for an ad account. use empty list for fields to use basic fields.

    This is a direct wrapper around AdAccount.get_insights().

    Args:
        account_id: The ad account ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.ACCOUNT, account_id, fields, params)


@handle_facebook_errors
def account_get_insights_async(
    account_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for an ad account. use empty list for fields to use basic fields.

    This is a direct wrapper around AdAccount.get_insights_async().

    Args:
        account_id: The ad account ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.ACCOUNT, account_id, fields, params)


@handle_facebook_errors
def campaign_get_insights(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for a campaign. use empty list for fields to use basic fields.

    This is a direct wrapper around Campaign.get_insights().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.CAMPAIGN, campaign_id, fields, params)


@handle_facebook_errors
def campaign_get_insights_async(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for a campaign. use empty list for fields to use basic fields.

    This is a direct wrapper around Campaign.get_insights_async().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.CAMPAIGN, campaign_id, fields, params)


@handle_facebook_errors
def adset_get_insights(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for an ad set. use empty list for fields to use basic fields.

    This is a direct wrapper around AdSet.get_insights().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.ADSET, adset_id, fields, params)


@handle_facebook_errors
def adset_get_insights_async(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for an ad set. use empty list for fields to use basic fields.

    This is a direct wrapper around AdSet.get_insights_async().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.ADSET, adset_id, fields, params)


@handle_facebook_errors
def ad_get_insights(
    ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for an ad. use empty list for fields to use basic fields.

    This is a direct wrapper around Ad.get_insights().

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.AD, ad_id, fields, params)


@handle_facebook_errors
def ad_get_insights_async(
    ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for an ad. use empty list for fields to use basic fields.

    This is a direct wrapper around Ad.get_insights_async().

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.AD, ad_id, fields, params)
