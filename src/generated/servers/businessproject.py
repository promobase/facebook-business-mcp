"""
Auto-generated MCP server for Facebook BusinessProject.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessproject import BusinessProject
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessproject")


# CRUD Operations


@mcp.tool()
async def get_businessproject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessProject.

    Args:
        object_id: The ID of the BusinessProject
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessProject(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessproject_server = mcp
