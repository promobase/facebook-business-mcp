"""
Auto-generated MCP server for Facebook AssignedUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.assigneduser import AssignedUser
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-assigneduser")


# CRUD Operations


@mcp.tool()
async def api_create_assigneduser(
    assigneduser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AssignedUser(fbid=assigneduser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_assigneduser(
    assigneduser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AssignedUser(fbid=assigneduser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_assigneduser(
    assigneduser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AssignedUser(fbid=assigneduser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_assigneduser(
    assigneduser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AssignedUser(fbid=assigneduser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
assigneduser_server = mcp
