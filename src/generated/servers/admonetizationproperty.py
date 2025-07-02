"""AdMonetizationProperty MCP Server."""

from typing import Any

from facebook_business.adobjects.admonetizationproperty import AdMonetizationProperty
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdMonetizationProperty"
instructions = """
AdMonetizationProperty MCP Server for Facebook Business API.

Provides typed access to all AdMonetizationProperty operations.
"""

admonetizationproperty_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@admonetizationproperty_server.tool
@wrapped_fn_tool
def get_admonetizationproperty(
    admonetizationproperty_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdMonetizationProperty(admonetizationproperty_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (3) ----
@admonetizationproperty_server.tool
@wrapped_fn_tool
def get_adnetworkanalytics(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdMonetizationProperty(admonetizationproperty_id).get_adnetworkanalytics(
        fields=fields, params=params
    )


@admonetizationproperty_server.tool
@wrapped_fn_tool
def create_adnetworkanalytic(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdMonetizationProperty(admonetizationproperty_id).create_adnetworkanalytic(
        fields=fields, params=params
    )


@admonetizationproperty_server.tool
@wrapped_fn_tool
def get_adnetworkanalytics_results(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdMonetizationProperty(admonetizationproperty_id).get_adnetworkanalytics_results(
        fields=fields, params=params
    )
