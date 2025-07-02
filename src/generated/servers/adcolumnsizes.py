"""
Auto-generated MCP server for Facebook AdColumnSizes.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcolumnsizes import AdColumnSizes
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcolumnsizes")


# CRUD Operations


@mcp.tool()
async def get_adcolumnsizes(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdColumnSizes.

    Args:
        object_id: The ID of the AdColumnSizes
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdColumnSizes(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcolumnsizes_server = mcp
