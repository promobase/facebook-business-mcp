"""
Auto-generated MCP server for Facebook IGMedia.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmedia import IGMedia
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-igmedia")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    igmedia_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_branded_content_partner_promote(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).create_branded_content_partner_promote(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_comment(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_partnership_ad_code(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).create_partnership_ad_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_product_tag(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).create_product_tag(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_partnership_ad_code(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).delete_partnership_ad_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_boost_ads_list(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).get_boost_ads_list(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_branded_content_partner_promote(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).get_branded_content_partner_promote(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_children(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).get_children(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_collaborators(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).get_collaborators(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_insights(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_product_tags(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMedia(fbid=igmedia_id).get_product_tags(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmedia_server = mcp
