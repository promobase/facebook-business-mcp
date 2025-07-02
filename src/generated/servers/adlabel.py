"""AdLabel MCP Server."""

from typing import Any

from facebook_business.adobjects.adlabel import AdLabel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdLabel"
instructions = """
AdLabel MCP Server for Facebook Business API.

Provides typed access to all AdLabel operations.
"""

adlabel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adlabel_server.tool
@wrapped_fn_tool
def get_adlabel(
    adlabel_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdLabel(adlabel_id)
    return obj.api_get(fields=fields)


@adlabel_server.tool
@wrapped_fn_tool
def update_adlabel(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdLabel(adlabel_id).api_update(fields=fields, params=params)


@adlabel_server.tool
@wrapped_fn_tool
def delete_adlabel(
    adlabel_id: str,
) -> str:
    return AdLabel(adlabel_id).api_delete()


# ---- Edge Methods (4) ----
@adlabel_server.tool
@wrapped_fn_tool
def get_adcreatives(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdLabel(adlabel_id).get_adcreatives(fields=fields, params=params)


@adlabel_server.tool
@wrapped_fn_tool
def get_ads(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdLabel(adlabel_id).get_ads(fields=fields, params=params)


@adlabel_server.tool
@wrapped_fn_tool
def get_adsets(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdLabel(adlabel_id).get_adsets(fields=fields, params=params)


@adlabel_server.tool
@wrapped_fn_tool
def get_campaigns(
    adlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdLabel(adlabel_id).get_campaigns(fields=fields, params=params)
