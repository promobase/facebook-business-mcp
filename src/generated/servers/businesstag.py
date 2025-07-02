"""
Auto-generated MCP server for Facebook BusinessTag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businesstag import BusinessTag
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businesstag")


# CRUD Operations


@mcp.tool()
async def get_businesstag(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessTag.

    Args:
        object_id: The ID of the BusinessTag
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessTag(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businesstag_server = mcp
