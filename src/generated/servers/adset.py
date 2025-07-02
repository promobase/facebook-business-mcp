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


# ---- Edge Methods (16) ----
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
def get_ad_studies(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_ad_studies(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_adcreatives(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_adcreatives(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def delete_adlabels(
    adset_id: str,
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).delete_adlabels(params=params)


@adset_server.tool
@wrapped_fn_tool
def create_adlabel(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).create_adlabel(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_adrules_governed(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_adrules_governed(fields=fields, params=params)


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
def get_asyncadrequests(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_asyncadrequests(fields=fields, params=params)


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
def create_copie(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).create_copie(fields=fields, params=params)


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
def create_insight(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).create_insight(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_message_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_message_delivery_estimate(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_targetingsentencelines(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdSet(adset_id).get_targetingsentencelines(fields=fields, params=params)
