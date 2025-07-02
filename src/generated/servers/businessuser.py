"""
Auto-generated MCP server for Facebook BusinessUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessuser import BusinessUser
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessuser")


# CRUD Operations


@mcp.tool()
async def api_create_businessuser(
    businessuser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessuser(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessuser(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessuser(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_assigned_ad_accounts(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).get_assigned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_business_asset_groups(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).get_assigned_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_pages(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).get_assigned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_product_catalogs(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessUser(fbid=businessuser_id).get_assigned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessuser_server = mcp
