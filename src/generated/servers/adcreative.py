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
async def api_create_adcreative(
    adcreative_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=adcreative_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adcreative(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=adcreative_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adcreative(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=adcreative_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adcreative(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=adcreative_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=adcreative_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_creative_insights(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=adcreative_id).get_creative_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_previews(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreative(fbid=adcreative_id).get_previews(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcreative_server = mcp
