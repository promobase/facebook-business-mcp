"""
Auto-generated MCP server for Facebook BusinessUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessuser import BusinessUser
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-businessuser")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    businessuser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_ad_accounts(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).get_assigned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_business_asset_groups(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).get_assigned_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_pages(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).get_assigned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_product_catalogs(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessUser(fbid=businessuser_id).get_assigned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessuser_server = mcp
