"""
Auto-generated MCP server for Facebook CanvasTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.canvastemplate import CanvasTemplate
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-canvastemplate")


# CRUD Operations


@mcp.tool()
async def get_canvastemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CanvasTemplate.

    Args:
        object_id: The ID of the CanvasTemplate
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CanvasTemplate(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
canvastemplate_server = mcp
