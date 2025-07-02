"""
Auto-generated MCP server for Facebook CPASBusinessSetupConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasbusinesssetupconfig import CPASBusinessSetupConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasbusinesssetupconfig")


# CRUD Operations


@mcp.tool()
async def create_cpasbusinesssetupconfig(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a CPASBusinessSetupConfig.

    Args:
        object_id: The ID of the CPASBusinessSetupConfig
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = CPASBusinessSetupConfig(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cpasbusinesssetupconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CPASBusinessSetupConfig.

    Args:
        object_id: The ID of the CPASBusinessSetupConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CPASBusinessSetupConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_accounts_for_cpasbusinesssetupconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Accounts for CPASBusinessSetupConfig.

    Args:
        object_id: The ID of the CPASBusinessSetupConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
    result = CPASBusinessSetupConfig(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasbusinesssetupconfig_server = mcp
