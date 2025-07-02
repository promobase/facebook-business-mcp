"""
Auto-generated MCP server for Facebook OfflineProductItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineproductitem import OfflineProductItem
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineproductitem")


# CRUD Operations


@mcp.tool()
async def api_create_offlineproductitem(
    offlineproductitem_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_offlineproductitem(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_offlineproductitem(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_offlineproductitem(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineProductItem(fbid=offlineproductitem_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineProductItem(fbid=offlineproductitem_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineproductitem_server = mcp
