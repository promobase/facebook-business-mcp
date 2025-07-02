"""
Auto-generated MCP server for Facebook AdsCreationSavedState.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adscreationsavedstate import AdsCreationSavedState
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adscreationsavedstate")


# CRUD Operations


@mcp.tool()
async def get_adscreationsavedstate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsCreationSavedState.

    Args:
        object_id: The ID of the AdsCreationSavedState
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsCreationSavedState(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adscreationsavedstate_server = mcp
