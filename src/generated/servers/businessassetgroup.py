"""
Auto-generated MCP server for Facebook BusinessAssetGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessassetgroup import BusinessAssetGroup
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessassetgroup")


# CRUD Operations


@mcp.tool()
async def api_create_businessassetgroup(
    businessassetgroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessassetgroup(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessassetgroup(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessassetgroup(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_assigned_user(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_ad_account(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_contained_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_application(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_contained_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_custom_conversion(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_contained_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_instagram_account(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_contained_instagram_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_page(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_contained_page(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_pixel(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_contained_pixel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_product_catalog(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).create_contained_product_catalog(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_assigned_users(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_ad_accounts(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_contained_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_applications(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_contained_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_custom_conversions(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_contained_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_instagram_accounts(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_contained_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_pages(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_contained_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_pixels(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_contained_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_product_catalogs(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).delete_contained_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_ad_accounts(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_contained_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_applications(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_contained_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_custom_conversions(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_contained_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_instagram_accounts(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_contained_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_pages(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_contained_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_pixels(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_contained_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_product_catalogs(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=businessassetgroup_id).get_contained_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessassetgroup_server = mcp
