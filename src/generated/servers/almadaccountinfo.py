"""
Auto-generated MCP server for Facebook ALMAdAccountInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.almadaccountinfo import ALMAdAccountInfo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-almadaccountinfo")


# CRUD Operations


@mcp.tool()
async def get_almadaccountinfo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ALMAdAccountInfo.

    Args:
        object_id: The ID of the ALMAdAccountInfo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ALMAdAccountInfo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
almadaccountinfo_server = mcp
