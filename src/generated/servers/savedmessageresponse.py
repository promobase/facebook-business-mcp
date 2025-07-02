"""
Auto-generated MCP server for Facebook SavedMessageResponse.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.savedmessageresponse import SavedMessageResponse
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-savedmessageresponse")


# CRUD Operations


@mcp.tool()
async def get_savedmessageresponse(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a SavedMessageResponse.

    Args:
        object_id: The ID of the SavedMessageResponse
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = SavedMessageResponse(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
savedmessageresponse_server = mcp
