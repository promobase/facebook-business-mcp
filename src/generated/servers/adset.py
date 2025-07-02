"""AdSet MCP Server."""

from typing import Any

from facebook_business.adobjects.adset import AdSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdSet"
instructions = """
AdSet MCP Server for Facebook Business API.

Provides typed access to all AdSet operations.
"""

adset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adset_server.tool
@wrapped_fn_tool
def get_adset(
    adset_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdSet(adset_id)
    return obj.api_get(fields=fields)


@adset_server.tool
@wrapped_fn_tool
def update_adset(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).api_update(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def delete_adset(
    adset_id: str,
) -> str:
    return AdSet(adset_id).api_delete()


# ---- Edge Methods (13) ----
@adset_server.tool
@wrapped_fn_tool
def get_activities(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_activities(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def delete_ad_labels(
    adset_id: str,
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).delete_ad_labels(params=params)


@adset_server.tool
@wrapped_fn_tool
def create_ad_label(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).create_ad_label(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_ad_rules_governed(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_ad_rules_governed(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_ads(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_ads(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_async_ad_requests(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_async_ad_requests(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def create_budget_schedule(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).create_budget_schedule(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_copies(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_copies(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def create_copy(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).create_copy(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_delivery_estimate(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_insights(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_insights(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_insights_async(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_insights_async(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_message_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_message_delivery_estimate(fields=fields, params=params)
