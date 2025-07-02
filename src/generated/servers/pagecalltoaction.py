"""
Auto-generated MCP server for Facebook PageCallToAction.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagecalltoaction import PageCallToAction
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagecalltoaction")


# CRUD Operations


@mcp.tool()
async def delete_pagecalltoaction(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a PageCallToAction.

    Args:
        object_id: The ID of the PageCallToAction
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = PageCallToAction(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pagecalltoaction(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PageCallToAction.

    Args:
        object_id: The ID of the PageCallToAction
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PageCallToAction(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_pagecalltoaction(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a PageCallToAction.

    Args:
        object_id: The ID of the PageCallToAction
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = PageCallToAction(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagecalltoaction_server = mcp
