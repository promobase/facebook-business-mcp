"""Specialized insights operations.

This module provides additional insights-related operations specific to certain object types.
"""

from typing import Any

from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import wrapped_fn_tool


@wrapped_fn_tool
def adset_get_delivery_estimate(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get delivery estimate for an ad set."""
    adset = AdSet(adset_id)
    return adset.get_delivery_estimate(fields=fields, params=params)


@wrapped_fn_tool
def adset_get_message_delivery_estimate(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get message delivery estimate for an ad set."""
    adset = AdSet(adset_id)
    return adset.get_message_delivery_estimate(fields=fields, params=params)


@wrapped_fn_tool
def campaign_get_ad_studies(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad studies for a campaign."""
    campaign = Campaign(campaign_id)
    return campaign.get_ad_studies(fields=fields, params=params)


@wrapped_fn_tool
def adset_get_ad_studies(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad studies for an ad set."""
    adset = AdSet(adset_id)
    return adset.get_ad_studies(fields=fields, params=params)
