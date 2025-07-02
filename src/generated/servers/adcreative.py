"""AdCreative MCP Server."""

from typing import Any

from facebook_business.adobjects.adcreative import AdCreative
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdCreative"
instructions = """
AdCreative MCP Server for Facebook Business API.

Provides typed access to all AdCreative operations.
"""

adcreative_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adcreative_server.tool
@wrapped_fn_tool
def get_adcreative(
    adcreative_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdCreative(adcreative_id)
    return obj.api_get(fields=fields)


@adcreative_server.tool
@wrapped_fn_tool
def update_adcreative(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdCreative(adcreative_id).api_update(fields=fields, params=params)


@adcreative_server.tool
@wrapped_fn_tool
def delete_adcreative(
    adcreative_id: str,
) -> str:
    return AdCreative(adcreative_id).api_delete()


# ---- Edge Methods (2) ----
@adcreative_server.tool
@wrapped_fn_tool
def create_ad_label(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdCreative(adcreative_id).create_ad_label(fields=fields, params=params)


@adcreative_server.tool
@wrapped_fn_tool
def get_previews(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdCreative(adcreative_id).get_previews(fields=fields, params=params)
