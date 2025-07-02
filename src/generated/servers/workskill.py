"""
Auto-generated MCP server for Facebook WorkSkill.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.workskill import WorkSkill
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-workskill")


# CRUD Operations


@mcp.tool()
async def api_create_workskill(
    workskill_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkSkill(fbid=workskill_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_workskill(
    workskill_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkSkill(fbid=workskill_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_workskill(
    workskill_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkSkill(fbid=workskill_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_workskill(
    workskill_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkSkill(fbid=workskill_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_users(
    workskill_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WorkSkill(fbid=workskill_id).get_users(
        fields=fields,
        params=params,
    )

    return result


# Export the server
workskill_server = mcp
