"""
Auto-generated MCP server for Facebook BizInboxOffsiteEmailAccount.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.bizinboxoffsiteemailaccount import BizInboxOffsiteEmailAccount
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-bizinboxoffsiteemailaccount")


# CRUD Operations


@mcp.tool()
async def get_bizinboxoffsiteemailaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BizInboxOffsiteEmailAccount.

    Args:
        object_id: The ID of the BizInboxOffsiteEmailAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BizInboxOffsiteEmailAccount(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_assigned_users_for_bizinboxoffsiteemailaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Users for BizInboxOffsiteEmailAccount.

    Args:
        object_id: The ID of the BizInboxOffsiteEmailAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_users result
    """
    result = BizInboxOffsiteEmailAccount(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bizinboxoffsiteemailaccount_server = mcp
