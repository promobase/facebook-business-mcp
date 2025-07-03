"""
Auto-generated MCP server for Facebook PublisherWhiteList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.publisherwhitelist import PublisherWhiteList
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-publisherwhitelist")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    publisherwhitelist_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherWhiteList(fbid=publisherwhitelist_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    publisherwhitelist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherWhiteList(fbid=publisherwhitelist_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    publisherwhitelist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherWhiteList(fbid=publisherwhitelist_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    publisherwhitelist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherWhiteList(fbid=publisherwhitelist_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
publisherwhitelist_server = mcp
