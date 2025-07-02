"""
Auto-generated MCP server for Facebook SystemUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.systemuser import SystemUser
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-systemuser")


# CRUD Operations


@mcp.tool()
async def api_create_systemuser(
    systemuser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_systemuser(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_systemuser(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_systemuser(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_assigned_ad_accounts(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).get_assigned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_business_asset_groups(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).get_assigned_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_pages(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).get_assigned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_product_catalogs(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=systemuser_id).get_assigned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
systemuser_server = mcp
