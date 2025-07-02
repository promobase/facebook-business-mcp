"""
Auto-generated MCP server for Facebook ReachFrequencyPrediction.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-reachfrequencyprediction")


# CRUD Operations


@mcp.tool()
async def create_reachfrequencyprediction(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ReachFrequencyPrediction.

    Args:
        object_id: The ID of the ReachFrequencyPrediction
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ReachFrequencyPrediction(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reachfrequencyprediction(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ReachFrequencyPrediction.

    Args:
        object_id: The ID of the ReachFrequencyPrediction
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ReachFrequencyPrediction(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
reachfrequencyprediction_server = mcp
