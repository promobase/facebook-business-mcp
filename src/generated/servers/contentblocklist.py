"""
Auto-generated MCP server for Facebook ContentBlockList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.contentblocklist import ContentBlockList
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-contentblocklist")


# CRUD Operations


@mcp.tool()
async def create_contentblocklist(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ContentBlockList(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ContentBlockList(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ContentBlockList(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ContentBlockList(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_applied_ad_accounts_for_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ContentBlockList(fbid=object_id).get_applied_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_facebook_content_for_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ContentBlockList(fbid=object_id).get_facebook_content(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_content_for_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ContentBlockList(fbid=object_id).get_instagram_content(
        fields=fields,
        params=params,
    )

    return result


# Export the server
contentblocklist_server = mcp
