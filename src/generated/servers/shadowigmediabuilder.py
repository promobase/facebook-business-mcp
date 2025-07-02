"""
Auto-generated MCP server for Facebook ShadowIGMediaBuilder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowigmediabuilder import ShadowIGMediaBuilder
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowigmediabuilder")


# CRUD Operations


@mcp.tool()
async def get_shadowigmediabuilder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ShadowIGMediaBuilder.

    Args:
        object_id: The ID of the ShadowIGMediaBuilder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ShadowIGMediaBuilder(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowigmediabuilder_server = mcp
