"""Campaign Copies operations.

This module provides thin wrappers around Campaign SDK methods for copying campaigns.
"""

from typing import Any

from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def campaign_get_copies(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get copies of a campaign.

    This is a direct wrapper around Campaign.get_copies().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of campaign copies
    """
    campaign = Campaign(campaign_id)
    return campaign.get_copies(fields=fields, params=params)


@handle_facebook_errors
def campaign_create_copy(
    campaign_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create a copy of a campaign.

    This is a direct wrapper around Campaign.create_copy().

    Args:
        campaign_id: The campaign ID to copy
        params: Copy parameters (e.g., deep_copy, rename_options)
        fields: Fields to return

    Returns:
        Created campaign copy data
    """
    campaign = Campaign(campaign_id)
    return campaign.create_copy(fields=fields, params=params)
