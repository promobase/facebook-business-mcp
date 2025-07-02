"""
Auto-generated MCP server for Facebook AdDraft.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.addraft import AdDraft
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-addraft")


# CRUD Operations


@mcp.tool()
async def get_addraft(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdDraft.

    Args:
        object_id: The ID of the AdDraft
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdDraft(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
addraft_server = mcp
