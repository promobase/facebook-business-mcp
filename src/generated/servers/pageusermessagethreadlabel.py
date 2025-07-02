"""
Auto-generated MCP server for Facebook PageUserMessageThreadLabel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pageusermessagethreadlabel")


# CRUD Operations


@mcp.tool()
async def delete_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a PageUserMessageThreadLabel.

    Args:
        object_id: The ID of the PageUserMessageThreadLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = PageUserMessageThreadLabel(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PageUserMessageThreadLabel.

    Args:
        object_id: The ID of the PageUserMessageThreadLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PageUserMessageThreadLabel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_label_for_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Label for PageUserMessageThreadLabel.

    Args:
        object_id: The ID of the PageUserMessageThreadLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_label result
    """
    result = PageUserMessageThreadLabel(fbid=object_id).create_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_label_for_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Label for PageUserMessageThreadLabel.

    Args:
        object_id: The ID of the PageUserMessageThreadLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_label result
    """
    result = PageUserMessageThreadLabel(fbid=object_id).delete_label(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pageusermessagethreadlabel_server = mcp
