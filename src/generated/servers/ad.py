"""
Auto-generated MCP server for Facebook Ad.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-ad")


# CRUD Operations


@mcp.tool()
async def create_ad(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_copy_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).create_copy(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_creatives_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_rules_governed_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_ad_rules_governed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_copies_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_copies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_async_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_leads_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_leads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_previews_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_previews(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_sentence_lines_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Ad(fbid=object_id).get_targeting_sentence_lines(
        fields=fields,
        params=params,
    )

    return result


# Export the server
ad_server = mcp
