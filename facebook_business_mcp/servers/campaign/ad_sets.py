"""Campaign Ad Sets operations.

This module provides thin wrappers around Campaign SDK methods for ad sets.
"""

from typing import Any

from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def campaign_get_ad_sets(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> Any:
    """Get ad sets for a campaign."""
    campaign = Campaign(campaign_id)
    return campaign.get_ad_sets(fields=fields, params=params)


@handle_facebook_errors
def campaign_create_budget_schedule(
    campaign_id: str, params: dict[str, Any], fields: list[str] = []
) -> Any:
    """Create a budget schedule for a campaign."""

    campaign = Campaign(campaign_id)
    return campaign.create_budget_schedule(fields=fields, params=params)
