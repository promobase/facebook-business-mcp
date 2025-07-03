"""
Auto-generated MCP server for Facebook ProductItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productitem import ProductItem
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-productitem")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    productitem_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_product_sets(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).get_product_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos_metadata(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductItem(fbid=productitem_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productitem_server = mcp
