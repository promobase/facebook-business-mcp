"""
Auto-generated MCP server for Facebook PageUserMessageThreadLabel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pageusermessagethreadlabel")


# CRUD Operations


@mcp.tool()
async def create_pageusermessagethreadlabel(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUserMessageThreadLabel(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUserMessageThreadLabel(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUserMessageThreadLabel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUserMessageThreadLabel(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_label_for_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUserMessageThreadLabel(fbid=object_id).create_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_label_for_pageusermessagethreadlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUserMessageThreadLabel(fbid=object_id).delete_label(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pageusermessagethreadlabel_server = mcp
