"""
Auto-generated MCP server for Facebook ExtendedCreditAllocationConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcreditallocationconfig import (
    ExtendedCreditAllocationConfig,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcreditallocationconfig")


# CRUD Operations


@mcp.tool()
async def delete_extendedcreditallocationconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ExtendedCreditAllocationConfig.

    Args:
        object_id: The ID of the ExtendedCreditAllocationConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ExtendedCreditAllocationConfig(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_extendedcreditallocationconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ExtendedCreditAllocationConfig.

    Args:
        object_id: The ID of the ExtendedCreditAllocationConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ExtendedCreditAllocationConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_extendedcreditallocationconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ExtendedCreditAllocationConfig.

    Args:
        object_id: The ID of the ExtendedCreditAllocationConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ExtendedCreditAllocationConfig(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcreditallocationconfig_server = mcp
