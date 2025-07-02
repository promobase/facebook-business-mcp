"""
Auto-generated MCP server for Facebook Robot.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.robot import Robot
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-robot")


# CRUD Operations


@mcp.tool()
async def get_robot(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Robot.

    Args:
        object_id: The ID of the Robot
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Robot(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
robot_server = mcp
