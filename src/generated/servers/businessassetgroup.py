"""BusinessAssetGroup MCP Server."""

from typing import Any

from facebook_business.adobjects.businessassetgroup import BusinessAssetGroup
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessAssetGroup"
instructions = """
BusinessAssetGroup MCP Server for Facebook Business API.

Provides typed access to all BusinessAssetGroup operations.
"""

businessassetgroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@businessassetgroup_server.tool
@wrapped_fn_tool
def get_businessassetgroup(
    businessassetgroup_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessAssetGroup(businessassetgroup_id)
    return obj.api_get(fields=fields)


@businessassetgroup_server.tool
@wrapped_fn_tool
def update_businessassetgroup(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return BusinessAssetGroup(businessassetgroup_id).api_update(fields=fields, params=params)


# ---- Edge Methods (17) ----
@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_assigned_users(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def get_assigned_users(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).get_assigned_users(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_assigned_user(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_assigned_user(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_ad_accounts(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_ad_accounts(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_ad_account(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_contained_ad_account(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_applications(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_applications(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_application(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_contained_application(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_custom_conversions(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_custom_conversions(
        params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_custom_conversion(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_contained_custom_conversion(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_instagram_accounts(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_instagram_accounts(
        params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_instagram_account(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_contained_instagram_account(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_pages(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_pages(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_page(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_contained_page(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_pixels(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_pixels(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_pixel(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_contained_pixel(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_product_catalogs(
    businessassetgroup_id: str,
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_product_catalogs(
        params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_product_catalog(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessAssetGroup(businessassetgroup_id).create_contained_product_catalog(
        fields=fields, params=params
    )
