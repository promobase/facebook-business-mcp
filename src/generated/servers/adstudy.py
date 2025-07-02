"""AdStudy MCP Server."""

from typing import Any

from facebook_business.adobjects.adstudy import AdStudy
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdStudy"
instructions = """
AdStudy MCP Server for Facebook Business API.

Provides typed access to all AdStudy operations.
"""

adstudy_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adstudy_server.tool
@wrapped_fn_tool
def get_adstudy(
    adstudy_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdStudy(adstudy_id)
    return obj.api_get(fields=fields)


@adstudy_server.tool
@wrapped_fn_tool
def update_adstudy(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdStudy(adstudy_id).api_update(fields=fields, params=params)


@adstudy_server.tool
@wrapped_fn_tool
def delete_adstudy(
    adstudy_id: str,
) -> str:
    return AdStudy(adstudy_id).api_delete()


# ---- Edge Methods (2) ----
@adstudy_server.tool
@wrapped_fn_tool
def create_check_point(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudy(adstudy_id).create_check_point(fields=fields, params=params)


@adstudy_server.tool
@wrapped_fn_tool
def create_instance(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudy(adstudy_id).create_instance(fields=fields, params=params)
