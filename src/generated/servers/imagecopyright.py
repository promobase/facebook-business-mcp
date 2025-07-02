"""
Auto-generated MCP server for Facebook ImageCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.imagecopyright import ImageCopyright
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-imagecopyright")


# CRUD Operations


@mcp.tool()
async def get_imagecopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ImageCopyright.

    Args:
        object_id: The ID of the ImageCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ImageCopyright(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_imagecopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ImageCopyright.

    Args:
        object_id: The ID of the ImageCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ImageCopyright(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
imagecopyright_server = mcp
