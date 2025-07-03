"""
Auto-generated MCP server for Facebook UserIDForPage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.useridforpage import UserIDForPage
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-useridforpage")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    useridforpage_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserIDForPage(fbid=useridforpage_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    useridforpage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserIDForPage(fbid=useridforpage_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    useridforpage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserIDForPage(fbid=useridforpage_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    useridforpage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserIDForPage(fbid=useridforpage_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
useridforpage_server = mcp
