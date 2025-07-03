"""
Auto-generated MCP server for Facebook CopyrightOwnershipTransfer.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.copyrightownershiptransfer import CopyrightOwnershipTransfer
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-copyrightownershiptransfer")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    copyrightownershiptransfer_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CopyrightOwnershipTransfer(fbid=copyrightownershiptransfer_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    copyrightownershiptransfer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CopyrightOwnershipTransfer(fbid=copyrightownershiptransfer_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    copyrightownershiptransfer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CopyrightOwnershipTransfer(fbid=copyrightownershiptransfer_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    copyrightownershiptransfer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CopyrightOwnershipTransfer(fbid=copyrightownershiptransfer_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
copyrightownershiptransfer_server = mcp
