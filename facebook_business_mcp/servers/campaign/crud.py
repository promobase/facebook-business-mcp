"""Campaign CRUD operations.

This module provides basic Create, Read, Update, and Delete operations for Facebook campaigns.
"""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def api_get(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get a campaign using the Facebook API.

    This is a direct wrapper around Campaign.api_get().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Campaign data from the API
    """

    campaign = Campaign(campaign_id)
    return campaign.api_get(fields=fields, params=params)


@handle_facebook_errors
def api_create(account_id: str, params: dict[str, Any], fields: list[str] = []) -> dict[str, Any]:
    """Create a campaign using the Facebook API.

    This is a direct wrapper around AdAccount.create_campaign().

    Args:
        account_id: The ad account ID (with or without 'act_' prefix)
        params: Campaign creation parameters
        fields: Fields to return in the response

    Returns:
        Created campaign data
    """
    # Ensure account_id has the correct prefix
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    account = AdAccount(account_id)
    return account.create_campaign(fields=fields, params=params)


@handle_facebook_errors
def campaign_api_update(
    campaign_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Update a campaign using the Facebook API.

    This is a direct wrapper around Campaign.api_update().

    Args:
        campaign_id: The campaign ID
        params: Update parameters
        fields: Fields to return in the response

    Returns:
        Updated campaign data
    """

    campaign = Campaign(campaign_id)
    return campaign.api_update(fields=fields, params=params)


@handle_facebook_errors
def campaign_api_delete(campaign_id: str, params: dict[str, Any] = {}) -> dict[str, Any]:
    """Delete a campaign using the Facebook API.

    This is a direct wrapper around Campaign.api_delete().

    Args:
        campaign_id: The campaign ID
        params: Additional parameters

    Returns:
        Deletion result
    """
    campaign = Campaign(campaign_id)
    return campaign.api_delete(params=params)
