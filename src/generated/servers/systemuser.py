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
async def create_systemuser(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_systemuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_systemuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_systemuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_assigned_ad_accounts_for_systemuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).get_assigned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_business_asset_groups_for_systemuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).get_assigned_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_pages_for_systemuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).get_assigned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_product_catalogs_for_systemuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SystemUser(fbid=object_id).get_assigned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
systemuser_server = mcp
