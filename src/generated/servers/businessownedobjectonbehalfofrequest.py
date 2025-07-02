"""
Auto-generated MCP server for Facebook BusinessOwnedObjectOnBehalfOfRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessownedobjectonbehalfofrequest import (
    BusinessOwnedObjectOnBehalfOfRequest,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessownedobjectonbehalfofrequest")


# CRUD Operations


@mcp.tool()
async def get_businessownedobjectonbehalfofrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessOwnedObjectOnBehalfOfRequest.

    Args:
        object_id: The ID of the BusinessOwnedObjectOnBehalfOfRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessOwnedObjectOnBehalfOfRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessownedobjectonbehalfofrequest_server = mcp
