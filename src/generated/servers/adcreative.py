"""
Auto-generated MCP server for Facebook AdCreative.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcreative import AdCreative
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcreative")


# CRUD Operations


@mcp.tool()
async def create_adcreative(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label_for_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=object_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_creative_insights_for_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=object_id).get_creative_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_previews_for_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=object_id).get_previews(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcreative_server = mcp
