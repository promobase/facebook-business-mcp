"""Campaign Insights operations.

This module provides thin wrappers around Campaign SDK methods for insights.
"""

from typing import Any

from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def campaign_get_insights(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for a campaign.

    This is a direct wrapper around Campaign.get_insights().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters (e.g., date_preset, breakdowns)

    Returns:
        List of insights data
    """
    campaign = Campaign(campaign_id)
    return campaign.get_insights(fields=fields, params=params)


@handle_facebook_errors
def campaign_get_insights_async(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for a campaign.

    This is a direct wrapper around Campaign.get_insights_async().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    campaign = Campaign(campaign_id)
    return campaign.get_insights_async(fields=fields, params=params)


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
