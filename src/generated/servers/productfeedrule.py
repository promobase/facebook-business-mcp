"""
Auto-generated MCP server for Facebook ProductFeedRule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeedrule import ProductFeedRule
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeedrule")


# CRUD Operations


@mcp.tool()
async def delete_productfeedrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ProductFeedRule.

    Args:
        object_id: The ID of the ProductFeedRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ProductFeedRule(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productfeedrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductFeedRule.

    Args:
        object_id: The ID of the ProductFeedRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductFeedRule(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productfeedrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ProductFeedRule.

    Args:
        object_id: The ID of the ProductFeedRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ProductFeedRule(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeedrule_server = mcp
