"""
Auto-generated MCP server for Facebook AdAccountCreationRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountcreationrequest import AdAccountCreationRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountcreationrequest")


# CRUD Operations


@mcp.tool()
async def get_adaccountcreationrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdAccountCreationRequest.

    Args:
        object_id: The ID of the AdAccountCreationRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdAccountCreationRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_accounts_for_adaccountcreationrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Accounts for AdAccountCreationRequest.

    Args:
        object_id: The ID of the AdAccountCreationRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
    result = AdAccountCreationRequest(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountcreationrequest_server = mcp
