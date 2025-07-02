"""
Auto-generated MCP server for Facebook FAMEKumo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.famekumo import FAMEKumo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-famekumo")


# CRUD Operations


@mcp.tool()
async def get_famekumo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a FAMEKumo.

    Args:
        object_id: The ID of the FAMEKumo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = FAMEKumo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
famekumo_server = mcp
