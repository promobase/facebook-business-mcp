"""
Auto-generated MCP server for Facebook AdTopline.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adtopline import AdTopline
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adtopline")


# CRUD Operations


@mcp.tool()
async def get_adtopline(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdTopline.

    Args:
        object_id: The ID of the AdTopline
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdTopline(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adtopline_server = mcp
