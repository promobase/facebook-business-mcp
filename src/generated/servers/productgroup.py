"""
Auto-generated MCP server for Facebook ProductGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productgroup import ProductGroup
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-productgroup")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    productgroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductGroup(fbid=productgroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductGroup(fbid=productgroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductGroup(fbid=productgroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductGroup(fbid=productgroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_product(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductGroup(fbid=productgroup_id).create_product(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_products(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductGroup(fbid=productgroup_id).get_products(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productgroup_server = mcp
