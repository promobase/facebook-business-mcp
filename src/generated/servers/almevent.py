"""
Auto-generated MCP server for Facebook ALMEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.almevent import ALMEvent
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-almevent")


# CRUD Operations


@mcp.tool()
async def get_almevent(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ALMEvent.

    Args:
        object_id: The ID of the ALMEvent
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ALMEvent(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
almevent_server = mcp
