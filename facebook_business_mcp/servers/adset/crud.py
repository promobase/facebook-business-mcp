"""AdSet CRUD operations.

This module provides basic Create, Read, Update, and Delete operations for Facebook ad sets.
"""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet

from facebook_business_mcp.utils import wrapped_fn_tool


@wrapped_fn_tool
def adset_api_get(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get an ad set by ID."""
    adset = AdSet(adset_id)
    return adset.api_get(fields=fields, params=params)


@wrapped_fn_tool
def adset_api_create(
    account_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad set from an ad account."""
    # Ensure account_id has the correct prefix
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    account = AdAccount(account_id)
    return account.create_ad_set(fields=fields, params=params)


@wrapped_fn_tool
def adset_api_update(
    adset_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Update an ad set."""
    adset = AdSet(adset_id)
    return adset.api_update(fields=fields, params=params)


@wrapped_fn_tool
def adset_api_delete(adset_id: str, params: dict[str, Any] = {}) -> dict[str, Any]:
    """Delete an ad set by ID."""
    adset = AdSet(adset_id)
    return adset.api_delete(params=params)
