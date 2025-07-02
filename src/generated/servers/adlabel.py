"""
Auto-generated MCP server for Facebook AdLabel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adlabel import AdLabel
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adlabel")


# CRUD Operations


@mcp.tool()
async def api_create_adlabel(
    adlabel_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adlabel(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adlabel(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adlabel(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_creatives(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).get_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaigns(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLabel(fbid=adlabel_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adlabel_server = mcp
