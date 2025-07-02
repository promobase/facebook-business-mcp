"""
Auto-generated MCP server for Facebook AdPlacePageSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adplacepageset import AdPlacePageSet
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adplacepageset")


# CRUD Operations


@mcp.tool()
async def create_adplacepageset(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdPlacePageSet.

    Args:
        object_id: The ID of the AdPlacePageSet
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdPlacePageSet(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adplacepageset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdPlacePageSet.

    Args:
        object_id: The ID of the AdPlacePageSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdPlacePageSet(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adplacepageset_server = mcp
