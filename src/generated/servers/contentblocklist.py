"""
Auto-generated MCP server for Facebook ContentBlockList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.contentblocklist import ContentBlockList
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-contentblocklist")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    contentblocklist_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ContentBlockList(fbid=contentblocklist_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    contentblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ContentBlockList(fbid=contentblocklist_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    contentblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ContentBlockList(fbid=contentblocklist_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    contentblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ContentBlockList(fbid=contentblocklist_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_applied_ad_accounts(
    contentblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ContentBlockList(fbid=contentblocklist_id).get_applied_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_facebook_content(
    contentblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ContentBlockList(fbid=contentblocklist_id).get_facebook_content(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_instagram_content(
    contentblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ContentBlockList(fbid=contentblocklist_id).get_instagram_content(
        fields=fields,
        params=params,
    )

    return result


# Export the server
contentblocklist_server = mcp
