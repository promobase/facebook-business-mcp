"""
Auto-generated MCP server for Facebook BlindPig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.blindpig import BlindPig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-blindpig")


# CRUD Operations


@mcp.tool()
async def get_blindpig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BlindPig.

    Args:
        object_id: The ID of the BlindPig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BlindPig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
blindpig_server = mcp
