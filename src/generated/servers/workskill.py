"""
Auto-generated MCP server for Facebook WorkSkill.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.workskill import WorkSkill
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-workskill")


# CRUD Operations


@mcp.tool()
async def get_workskill(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WorkSkill.

    Args:
        object_id: The ID of the WorkSkill
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WorkSkill(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_users_for_workskill(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Users for WorkSkill.

    Args:
        object_id: The ID of the WorkSkill
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_users result
    """
    result = WorkSkill(fbid=object_id).get_users(
        fields=fields,
        params=params,
    )

    return result


# Export the server
workskill_server = mcp
