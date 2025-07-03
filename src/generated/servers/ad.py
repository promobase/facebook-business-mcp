"""
Auto-generated MCP server for Facebook Ad.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-ad")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    ad_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_ad_label(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_copy(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).create_copy(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_creatives(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_rules_governed(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_ad_rules_governed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_copies(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_copies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_insights(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_insights_async(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_leads(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_leads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_previews(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_previews(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_targeting_sentence_lines(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Ad(fbid=ad_id).get_targeting_sentence_lines(
        fields=fields,
        params=params,
    )

    return result


# Export the server
ad_server = mcp
