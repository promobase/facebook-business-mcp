"""
Auto-generated MCP server for Facebook Destination.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.destination import Destination
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-destination")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    destination_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Destination(fbid=destination_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    destination_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Destination(fbid=destination_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    destination_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Destination(fbid=destination_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    destination_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Destination(fbid=destination_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    destination_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Destination(fbid=destination_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    destination_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Destination(fbid=destination_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos_metadata(
    destination_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Destination(fbid=destination_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
destination_server = mcp
