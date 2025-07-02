"""
Auto-generated MCP server for Facebook ExtendedCreditInvoiceGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcreditinvoicegroup import ExtendedCreditInvoiceGroup
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcreditinvoicegroup")


# CRUD Operations


@mcp.tool()
async def delete_extendedcreditinvoicegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ExtendedCreditInvoiceGroup.

    Args:
        object_id: The ID of the ExtendedCreditInvoiceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ExtendedCreditInvoiceGroup(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_extendedcreditinvoicegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ExtendedCreditInvoiceGroup.

    Args:
        object_id: The ID of the ExtendedCreditInvoiceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ExtendedCreditInvoiceGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_extendedcreditinvoicegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ExtendedCreditInvoiceGroup.

    Args:
        object_id: The ID of the ExtendedCreditInvoiceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ExtendedCreditInvoiceGroup(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_account_for_extendedcreditinvoicegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Account for ExtendedCreditInvoiceGroup.

    Args:
        object_id: The ID of the ExtendedCreditInvoiceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_account result
    """
    result = ExtendedCreditInvoiceGroup(fbid=object_id).create_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad_accounts_for_extendedcreditinvoicegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Ad Accounts for ExtendedCreditInvoiceGroup.

    Args:
        object_id: The ID of the ExtendedCreditInvoiceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_ad_accounts result
    """
    result = ExtendedCreditInvoiceGroup(fbid=object_id).delete_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_accounts_for_extendedcreditinvoicegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Accounts for ExtendedCreditInvoiceGroup.

    Args:
        object_id: The ID of the ExtendedCreditInvoiceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
    result = ExtendedCreditInvoiceGroup(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcreditinvoicegroup_server = mcp
