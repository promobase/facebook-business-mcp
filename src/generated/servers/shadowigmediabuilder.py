"""
Auto-generated MCP server for Facebook ShadowIGMediaBuilder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowigmediabuilder import ShadowIGMediaBuilder
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowigmediabuilder")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    shadowigmediabuilder_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGMediaBuilder(fbid=shadowigmediabuilder_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    shadowigmediabuilder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGMediaBuilder(fbid=shadowigmediabuilder_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    shadowigmediabuilder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGMediaBuilder(fbid=shadowigmediabuilder_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    shadowigmediabuilder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGMediaBuilder(fbid=shadowigmediabuilder_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowigmediabuilder_server = mcp
