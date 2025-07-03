"""
Auto-generated MCP server for Facebook HomeListing.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.homelisting import HomeListing
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-homelisting")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    homelisting_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HomeListing(fbid=homelisting_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HomeListing(fbid=homelisting_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HomeListing(fbid=homelisting_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HomeListing(fbid=homelisting_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HomeListing(fbid=homelisting_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HomeListing(fbid=homelisting_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos_metadata(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HomeListing(fbid=homelisting_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
homelisting_server = mcp
