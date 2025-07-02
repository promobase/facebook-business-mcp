"""
Auto-generated MCP server for Facebook WorkExperience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.workexperience import WorkExperience
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-workexperience")


# CRUD Operations


@mcp.tool()
async def get_workexperience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WorkExperience.

    Args:
        object_id: The ID of the WorkExperience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WorkExperience(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
workexperience_server = mcp
