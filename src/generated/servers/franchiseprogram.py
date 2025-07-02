"""
Auto-generated MCP server for Facebook FranchiseProgram.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.franchiseprogram import FranchiseProgram
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-franchiseprogram")


# CRUD Operations


@mcp.tool()
async def get_franchiseprogram(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a FranchiseProgram.

    Args:
        object_id: The ID of the FranchiseProgram
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = FranchiseProgram(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
franchiseprogram_server = mcp
