"""
Auto-generated MCP server for Facebook Experience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.experience import Experience
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-experience")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    experience_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Experience(fbid=experience_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    experience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Experience(fbid=experience_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    experience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Experience(fbid=experience_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    experience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Experience(fbid=experience_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
experience_server = mcp
