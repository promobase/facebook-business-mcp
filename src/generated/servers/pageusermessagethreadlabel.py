"""
Auto-generated MCP server for Facebook PageUserMessageThreadLabel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-pageusermessagethreadlabel")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    pageusermessagethreadlabel_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PageUserMessageThreadLabel(fbid=pageusermessagethreadlabel_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PageUserMessageThreadLabel(fbid=pageusermessagethreadlabel_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PageUserMessageThreadLabel(fbid=pageusermessagethreadlabel_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PageUserMessageThreadLabel(fbid=pageusermessagethreadlabel_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_label(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PageUserMessageThreadLabel(fbid=pageusermessagethreadlabel_id).create_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_label(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PageUserMessageThreadLabel(fbid=pageusermessagethreadlabel_id).delete_label(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pageusermessagethreadlabel_server = mcp
