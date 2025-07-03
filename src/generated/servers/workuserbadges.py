"""
Auto-generated MCP server for Facebook WorkUserBadges.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.workuserbadges import WorkUserBadges
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-workuserbadges")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    workuserbadges_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WorkUserBadges(fbid=workuserbadges_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    workuserbadges_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WorkUserBadges(fbid=workuserbadges_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    workuserbadges_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WorkUserBadges(fbid=workuserbadges_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    workuserbadges_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WorkUserBadges(fbid=workuserbadges_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
workuserbadges_server = mcp
