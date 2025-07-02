"""
Auto-generated MCP server for Facebook PersonalAdsPersona.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.personaladspersona import PersonalAdsPersona
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-personaladspersona")


# CRUD Operations


@mcp.tool()
async def get_personaladspersona(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PersonalAdsPersona.

    Args:
        object_id: The ID of the PersonalAdsPersona
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PersonalAdsPersona(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
personaladspersona_server = mcp
