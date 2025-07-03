"""Campaign Ad Sets operations.

This module provides thin wrappers around Campaign SDK methods for ad sets.
"""

from typing import Any

from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def campaign_get_ad_sets(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad sets for a campaign.

    This is a direct wrapper around Campaign.get_ad_sets().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters (e.g., filtering, pagination)

    Returns:
        List of ad sets
    """
    campaign = Campaign(campaign_id)
    return campaign.get_ad_sets(fields=fields, params=params)


@handle_facebook_errors
def campaign_create_budget_schedule(
    campaign_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create a budget schedule for a campaign.

    This is a direct wrapper around Campaign.create_budget_schedule().

    Args:
        campaign_id: The campaign ID
        params: Budget schedule parameters
        fields: Fields to return

    Returns:
        Created budget schedule data
    """

    campaign = Campaign(campaign_id)
    return campaign.create_budget_schedule(fields=fields, params=params)
