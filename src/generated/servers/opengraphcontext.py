"""
Auto-generated MCP server for Facebook OpenGraphContext.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.opengraphcontext import OpenGraphContext
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-opengraphcontext")


# CRUD Operations


@mcp.tool()
async def get_opengraphcontext(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OpenGraphContext.

    Args:
        object_id: The ID of the OpenGraphContext
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OpenGraphContext(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
opengraphcontext_server = mcp
