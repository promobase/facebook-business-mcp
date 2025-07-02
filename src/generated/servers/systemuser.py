"""SystemUser MCP Server."""

from typing import Any

from facebook_business.adobjects.systemuser import SystemUser
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSystemUser"
instructions = """
SystemUser MCP Server for Facebook Business API.

Provides typed access to all SystemUser operations.
"""

systemuser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@systemuser_server.tool
@wrapped_fn_tool
def get_systemuser(
    systemuser_id: str,
    fields: list[str] = [],
) -> str:
    obj = SystemUser(systemuser_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (4) ----
@systemuser_server.tool
@wrapped_fn_tool
def get_assigned_ad_accounts(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return SystemUser(systemuser_id).get_assigned_ad_accounts(fields=fields, params=params)


@systemuser_server.tool
@wrapped_fn_tool
def get_assigned_business_asset_groups(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return SystemUser(systemuser_id).get_assigned_business_asset_groups(
        fields=fields, params=params
    )


@systemuser_server.tool
@wrapped_fn_tool
def get_assigned_pages(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return SystemUser(systemuser_id).get_assigned_pages(fields=fields, params=params)


@systemuser_server.tool
@wrapped_fn_tool
def get_assigned_product_catalogs(
    systemuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return SystemUser(systemuser_id).get_assigned_product_catalogs(fields=fields, params=params)
