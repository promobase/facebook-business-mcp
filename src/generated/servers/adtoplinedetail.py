"""
Auto-generated MCP server for Facebook AdToplineDetail.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adtoplinedetail import AdToplineDetail
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adtoplinedetail")


# CRUD Operations


@mcp.tool()
async def get_adtoplinedetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdToplineDetail.

    Args:
        object_id: The ID of the AdToplineDetail
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdToplineDetail(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adtoplinedetail_server = mcp
