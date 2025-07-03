"""AdCreative CRUD operations.

This module provides basic Create, Read, Update, and Delete operations for Facebook ad creatives.
"""

from typing import Any

from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def adcreative_api_get(
    creative_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get an ad creative using the Facebook API.

    This is a direct wrapper around AdCreative.api_get().

    Args:
        creative_id: The ad creative ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Ad creative data from the API
    """
    creative = AdCreative(creative_id)
    return creative.api_get(fields=fields, params=params)


@handle_facebook_errors
def adcreative_api_create(
    account_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad creative using the Facebook API.

    This is a direct wrapper around AdAccount.create_ad_creative().

    Args:
        account_id: The ad account ID (with or without 'act_' prefix)
        params: Ad creative creation parameters
        fields: Fields to return in the response

    Returns:
        Created ad creative data
    """
    # Ensure account_id has the correct prefix
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    account = AdAccount(account_id)
    return account.create_ad_creative(fields=fields, params=params)


@handle_facebook_errors
def adcreative_api_update(
    creative_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Update an ad creative using the Facebook API.

    This is a direct wrapper around AdCreative.api_update().

    Args:
        creative_id: The ad creative ID
        params: Update parameters
        fields: Fields to return in the response

    Returns:
        Updated ad creative data
    """
    creative = AdCreative(creative_id)
    return creative.api_update(fields=fields, params=params)


@handle_facebook_errors
def adcreative_api_delete(creative_id: str, params: dict[str, Any] = {}) -> dict[str, Any]:
    """Delete an ad creative using the Facebook API.

    This is a direct wrapper around AdCreative.api_delete().

    Args:
        creative_id: The ad creative ID
        params: Additional parameters

    Returns:
        Deletion result
    """
    creative = AdCreative(creative_id)
    return creative.api_delete(params=params)
