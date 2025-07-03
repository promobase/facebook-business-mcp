"""Specialized insights operations.

This module provides additional insights-related operations specific to certain object types.
"""

from typing import Any

from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def adset_get_delivery_estimate(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get delivery estimate for an ad set.

    This is a direct wrapper around AdSet.get_delivery_estimate().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Delivery estimate data
    """
    adset = AdSet(adset_id)
    return adset.get_delivery_estimate(fields=fields, params=params)


@handle_facebook_errors
def adset_get_message_delivery_estimate(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get message delivery estimate for an ad set.

    This is a direct wrapper around AdSet.get_message_delivery_estimate().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Message delivery estimate data
    """
    adset = AdSet(adset_id)
    return adset.get_message_delivery_estimate(fields=fields, params=params)


@handle_facebook_errors
def campaign_get_ad_studies(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad studies for a campaign.

    This is a direct wrapper around Campaign.get_ad_studies().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of ad studies
    """
    campaign = Campaign(campaign_id)
    return campaign.get_ad_studies(fields=fields, params=params)


@handle_facebook_errors
def adset_get_ad_studies(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad studies for an ad set.

    This is a direct wrapper around AdSet.get_ad_studies().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of ad studies
    """
    adset = AdSet(adset_id)
    return adset.get_ad_studies(fields=fields, params=params)
