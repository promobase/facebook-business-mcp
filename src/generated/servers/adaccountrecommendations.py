"""
Auto-generated MCP server for Facebook AdAccountRecommendations.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountrecommendations import AdAccountRecommendations
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountrecommendations")


# CRUD Operations


@mcp.tool()
async def create_adaccountrecommendations(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdAccountRecommendations.

    Args:
        object_id: The ID of the AdAccountRecommendations
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdAccountRecommendations(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountrecommendations_server = mcp
