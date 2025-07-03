"""AdSet CRUD operations.

This module provides basic Create, Read, Update, and Delete operations for Facebook ad sets.
"""

from typing import Any

from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def adset_api_get(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get an ad set using the Facebook API.

    This is a direct wrapper around AdSet.api_get().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Ad set data from the API
    """
    adset = AdSet(adset_id)
    return adset.api_get(fields=fields, params=params)


@handle_facebook_errors
def adset_api_create(
    account_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad set using the Facebook API.

    This is a direct wrapper around AdAccount.create_ad_set().

    Args:
        account_id: The ad account ID (with or without 'act_' prefix)
        params: Ad set creation parameters
        fields: Fields to return in the response

    Returns:
        Created ad set data
    """
    # Ensure account_id has the correct prefix
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    account = AdAccount(account_id)
    return account.create_ad_set(fields=fields, params=params)


@handle_facebook_errors
def adset_api_update(
    adset_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Update an ad set using the Facebook API.

    This is a direct wrapper around AdSet.api_update().

    Args:
        adset_id: The ad set ID
        params: Update parameters
        fields: Fields to return in the response

    Returns:
        Updated ad set data
    """
    adset = AdSet(adset_id)
    return adset.api_update(fields=fields, params=params)


@handle_facebook_errors
def adset_api_delete(adset_id: str, params: dict[str, Any] = {}) -> dict[str, Any]:
    """Delete an ad set using the Facebook API.

    This is a direct wrapper around AdSet.api_delete().

    Args:
        adset_id: The ad set ID
        params: Additional parameters

    Returns:
        Deletion result
    """
    adset = AdSet(adset_id)
    return adset.api_delete(params=params)
