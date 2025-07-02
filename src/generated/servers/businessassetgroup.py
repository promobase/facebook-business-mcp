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
async def create_businessassetgroup(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_assigned_user_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_ad_account_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_contained_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_application_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_contained_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_custom_conversion_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_contained_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_instagram_account_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_contained_instagram_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_page_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_contained_page(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_pixel_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_contained_pixel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_product_catalog_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).create_contained_product_catalog(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_assigned_users_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_ad_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_contained_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_applications_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_contained_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_custom_conversions_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_contained_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_instagram_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_contained_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_pages_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_contained_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_pixels_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_contained_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_product_catalogs_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).delete_contained_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_ad_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_contained_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_applications_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_contained_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_custom_conversions_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_contained_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_instagram_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_contained_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_pages_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_contained_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_pixels_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_contained_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_product_catalogs_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAssetGroup(fbid=object_id).get_contained_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessassetgroup_server = mcp
