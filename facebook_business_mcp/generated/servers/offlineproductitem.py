"""
Auto-generated MCP server for Facebook OfflineProductItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineproductitem import OfflineProductItem
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineproductitem")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    offlineproductitem_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineProductItem(fbid=offlineproductitem_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineProductItem(fbid=offlineproductitem_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineProductItem(fbid=offlineproductitem_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineproductitem_server = mcp
