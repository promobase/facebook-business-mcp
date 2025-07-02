"""
Auto-generated MCP server for Facebook WorkExperience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.workexperience import WorkExperience
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-workexperience")


# CRUD Operations


@mcp.tool()
async def api_create_workexperience(
    workexperience_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkExperience(fbid=workexperience_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_workexperience(
    workexperience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkExperience(fbid=workexperience_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_workexperience(
    workexperience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkExperience(fbid=workexperience_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_workexperience(
    workexperience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkExperience(fbid=workexperience_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
workexperience_server = mcp
