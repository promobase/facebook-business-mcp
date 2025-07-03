"""
Auto-generated MCP server for Facebook PublisherBlockList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.publisherblocklist import PublisherBlockList
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-publisherblocklist")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    publisherblocklist_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherBlockList(fbid=publisherblocklist_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherBlockList(fbid=publisherblocklist_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherBlockList(fbid=publisherblocklist_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherBlockList(fbid=publisherblocklist_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_append_publisher_url(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherBlockList(fbid=publisherblocklist_id).create_append_publisher_url(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_paged_web_publishers(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PublisherBlockList(fbid=publisherblocklist_id).get_paged_web_publishers(
        fields=fields,
        params=params,
    )

    return result


# Export the server
publisherblocklist_server = mcp
