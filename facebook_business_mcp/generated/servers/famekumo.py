"""
Auto-generated MCP server for Facebook FAMEKumo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.famekumo import FAMEKumo
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-famekumo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    famekumo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FAMEKumo(fbid=famekumo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    famekumo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FAMEKumo(fbid=famekumo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    famekumo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FAMEKumo(fbid=famekumo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    famekumo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FAMEKumo(fbid=famekumo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
famekumo_server = mcp
