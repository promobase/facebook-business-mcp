"""
Auto-generated MCP server for Facebook AudioSubLabel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audiosublabel import AudioSubLabel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-audiosublabel")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    audiosublabel_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioSubLabel(fbid=audiosublabel_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    audiosublabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioSubLabel(fbid=audiosublabel_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    audiosublabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioSubLabel(fbid=audiosublabel_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    audiosublabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioSubLabel(fbid=audiosublabel_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audiosublabel_server = mcp
