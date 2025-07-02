"""
Auto-generated MCP server for Facebook SlicedEventSourceGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.slicedeventsourcegroup import SlicedEventSourceGroup
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-slicedeventsourcegroup")


# CRUD Operations


@mcp.tool()
async def get_slicedeventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a SlicedEventSourceGroup.

    Args:
        object_id: The ID of the SlicedEventSourceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = SlicedEventSourceGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
slicedeventsourcegroup_server = mcp
