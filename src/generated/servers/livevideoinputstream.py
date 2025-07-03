"""
Auto-generated MCP server for Facebook LiveVideoInputStream.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.livevideoinputstream import LiveVideoInputStream
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-livevideoinputstream")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    livevideoinputstream_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoInputStream(fbid=livevideoinputstream_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    livevideoinputstream_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoInputStream(fbid=livevideoinputstream_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    livevideoinputstream_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoInputStream(fbid=livevideoinputstream_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    livevideoinputstream_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoInputStream(fbid=livevideoinputstream_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
livevideoinputstream_server = mcp
