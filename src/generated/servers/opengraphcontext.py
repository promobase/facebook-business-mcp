"""
Auto-generated MCP server for Facebook OpenGraphContext.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.opengraphcontext import OpenGraphContext
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-opengraphcontext")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    opengraphcontext_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OpenGraphContext(fbid=opengraphcontext_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    opengraphcontext_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OpenGraphContext(fbid=opengraphcontext_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    opengraphcontext_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OpenGraphContext(fbid=opengraphcontext_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    opengraphcontext_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OpenGraphContext(fbid=opengraphcontext_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
opengraphcontext_server = mcp
