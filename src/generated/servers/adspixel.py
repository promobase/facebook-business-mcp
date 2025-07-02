"""AdsPixel MCP Server."""

from typing import Any

from facebook_business.adobjects.adspixel import AdsPixel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsPixel"
instructions = """
AdsPixel MCP Server for Facebook Business API.

Provides typed access to all AdsPixel operations.
"""

adspixel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adspixel_server.tool
@wrapped_fn_tool
def get_adspixel(
    adspixel_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsPixel(adspixel_id)
    return obj.api_get(fields=fields)


@adspixel_server.tool
@wrapped_fn_tool
def update_adspixel(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdsPixel(adspixel_id).api_update(fields=fields, params=params)


# ---- Edge Methods (17) ----
@adspixel_server.tool
@wrapped_fn_tool
def get_adaccounts(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_adaccounts(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def delete_agencies(
    adspixel_id: str,
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).delete_agencies(params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_agencies(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_agencies(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_agencie(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).create_agencie(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_ahp_config(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).create_ahp_config(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_assigned_users(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_assigned_users(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_assigned_user(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).create_assigned_user(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_da_checks(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_da_checks(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_event(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).create_event(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_offline_event_uploads(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_offline_event_uploads(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_openbridge_configurations(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_openbridge_configurations(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_shadowtraffichelper(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).create_shadowtraffichelper(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def delete_shared_accounts(
    adspixel_id: str,
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).delete_shared_accounts(params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_shared_accounts(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_shared_accounts(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_shared_account(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).create_shared_account(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_shared_agencies(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_shared_agencies(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_stats(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixel(adspixel_id).get_stats(fields=fields, params=params)
