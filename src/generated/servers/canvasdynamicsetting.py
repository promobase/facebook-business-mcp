"""
Auto-generated MCP server for Facebook CanvasDynamicSetting.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.canvasdynamicsetting import CanvasDynamicSetting
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-canvasdynamicsetting")


# CRUD Operations


@mcp.tool()
async def get_canvasdynamicsetting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CanvasDynamicSetting.

    Args:
        object_id: The ID of the CanvasDynamicSetting
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CanvasDynamicSetting(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
canvasdynamicsetting_server = mcp
