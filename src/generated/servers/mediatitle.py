"""
Auto-generated MCP server for Facebook MediaTitle.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mediatitle import MediaTitle
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-mediatitle")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    mediatitle_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaTitle(fbid=mediatitle_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaTitle(fbid=mediatitle_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaTitle(fbid=mediatitle_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaTitle(fbid=mediatitle_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaTitle(fbid=mediatitle_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaTitle(fbid=mediatitle_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos_metadata(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaTitle(fbid=mediatitle_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mediatitle_server = mcp
