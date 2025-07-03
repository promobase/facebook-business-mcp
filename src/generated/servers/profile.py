"""
Auto-generated MCP server for Facebook Profile.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.profile import Profile
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-profile")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    profile_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Profile(fbid=profile_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    profile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Profile(fbid=profile_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    profile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Profile(fbid=profile_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    profile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Profile(fbid=profile_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_picture(
    profile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Profile(fbid=profile_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


# Export the server
profile_server = mcp
