"""
Auto-generated MCP server for Facebook AppEventConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.appeventconfig import AppEventConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-appeventconfig")


# CRUD Operations


@mcp.tool()
async def get_appeventconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AppEventConfig.

    Args:
        object_id: The ID of the AppEventConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AppEventConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
appeventconfig_server = mcp
