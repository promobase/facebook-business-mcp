"""Campaign Ads operations.

This module provides thin wrappers around Campaign SDK methods for ads.
"""

from typing import Any

from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def campaign_get_ads(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ads for a campaign.

    This is a direct wrapper around Campaign.get_ads().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters (e.g., filtering, pagination)

    Returns:
        List of ads
    """
    campaign = Campaign(campaign_id)
    return campaign.get_ads(fields=fields, params=params)


@handle_facebook_errors
def campaign_create_ad_label(
    campaign_id: str, params: dict[str, Any] = {}, fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad label for a campaign.

    This is a direct wrapper around Campaign.create_ad_label().

    Args:
        campaign_id: The campaign ID
        params: Ad label parameters
        fields: Fields to return

    Returns:
        Created ad label data
    """
    campaign = Campaign(campaign_id)
    return campaign.create_ad_label(fields=fields, params=params)


@handle_facebook_errors
def campaign_get_ad_rules_governed(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad rules that govern this campaign.

    This is a direct wrapper around Campaign.get_ad_rules_governed().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of ad rules
    """
    campaign = Campaign(campaign_id)
    return campaign.get_ad_rules_governed(fields=fields, params=params)
