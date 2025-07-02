"""Ad MCP Server."""

from typing import Any

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAd"
instructions = """
Ad MCP Server for Facebook Business API.

Provides typed access to all Ad operations.
"""

ad_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@ad_server.tool
@wrapped_fn_tool
def get_ad(
    ad_id: str,
    fields: list[str] = [],
) -> str:
    obj = Ad(ad_id)
    return obj.api_get(fields=fields)


@ad_server.tool
@wrapped_fn_tool
def update_ad(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).api_update(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def delete_ad(
    ad_id: str,
) -> str:
    return Ad(ad_id).api_delete()


# ---- Edge Methods (10) ----
@ad_server.tool
@wrapped_fn_tool
def get_adcreatives(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).get_adcreatives(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def create_adlabel(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).create_adlabel(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_adrules_governed(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).get_adrules_governed(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_copies(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).get_copies(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def create_copie(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).create_copie(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_insights(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).get_insights(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def create_insight(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).create_insight(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_leads(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).get_leads(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_previews(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).get_previews(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_targetingsentencelines(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Ad(ad_id).get_targetingsentencelines(fields=fields, params=params)
