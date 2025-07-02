"""BusinessUser MCP Server."""

from typing import Any

from facebook_business.adobjects.businessuser import BusinessUser
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessUser"
instructions = """
BusinessUser MCP Server for Facebook Business API.

Provides typed access to all BusinessUser operations.
"""

businessuser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@businessuser_server.tool
@wrapped_fn_tool
def get_businessuser(
    businessuser_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessUser(businessuser_id)
    return obj.api_get(fields=fields)


@businessuser_server.tool
@wrapped_fn_tool
def update_businessuser(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return BusinessUser(businessuser_id).api_update(fields=fields, params=params)


@businessuser_server.tool
@wrapped_fn_tool
def delete_businessuser(
    businessuser_id: str,
) -> str:
    return BusinessUser(businessuser_id).api_delete()


# ---- Edge Methods (4) ----
@businessuser_server.tool
@wrapped_fn_tool
def get_assigned_ad_accounts(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessUser(businessuser_id).get_assigned_ad_accounts(fields=fields, params=params)


@businessuser_server.tool
@wrapped_fn_tool
def get_assigned_business_asset_groups(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessUser(businessuser_id).get_assigned_business_asset_groups(
        fields=fields, params=params
    )


@businessuser_server.tool
@wrapped_fn_tool
def get_assigned_pages(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessUser(businessuser_id).get_assigned_pages(fields=fields, params=params)


@businessuser_server.tool
@wrapped_fn_tool
def get_assigned_product_catalogs(
    businessuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BusinessUser(businessuser_id).get_assigned_product_catalogs(fields=fields, params=params)
