"""
Auto-generated MCP server for Facebook AdvAInstance.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.advainstance import AdvAInstance
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-advainstance")


# CRUD Operations


@mcp.tool()
async def get_advainstance(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdvAInstance.

    Args:
        object_id: The ID of the AdvAInstance
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdvAInstance(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
advainstance_server = mcp
