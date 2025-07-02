"""CustomAudience MCP Server."""

from typing import Any

from facebook_business.adobjects.customaudience import CustomAudience
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCustomAudience"
instructions = """
CustomAudience MCP Server for Facebook Business API.

Provides typed access to all CustomAudience operations.
"""

customaudience_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@customaudience_server.tool
@wrapped_fn_tool
def get_customaudience(
    customaudience_id: str,
    fields: list[str] = [],
) -> str:
    obj = CustomAudience(customaudience_id)
    return obj.api_get(fields=fields)


@customaudience_server.tool
@wrapped_fn_tool
def update_customaudience(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return CustomAudience(customaudience_id).api_update(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def delete_customaudience(
    customaudience_id: str,
) -> str:
    return CustomAudience(customaudience_id).api_delete()


# ---- Edge Methods (11) ----
@customaudience_server.tool
@wrapped_fn_tool
def delete_ad_accounts(
    customaudience_id: str,
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).delete_ad_accounts(params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_ad_accounts(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).get_ad_accounts(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_ad_account(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).create_ad_account(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_ads(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).get_ads(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_health(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).get_health(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_salts(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).get_salts(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_salt(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).create_salt(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_sessions(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).get_sessions(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def delete_users(
    customaudience_id: str,
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).delete_users(params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_user(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).create_user(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_users_replace(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomAudience(customaudience_id).create_users_replace(fields=fields, params=params)
