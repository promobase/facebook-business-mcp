"""AdRule MCP Server."""

from typing import Any

from facebook_business.adobjects.adrule import AdRule
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdRule"
instructions = """
AdRule MCP Server for Facebook Business API.

Provides typed access to all AdRule operations.
"""

adrule_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adrule_server.tool
@wrapped_fn_tool
def get_adrule(
    adrule_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdRule(adrule_id)
    return obj.api_get(fields=fields)


@adrule_server.tool
@wrapped_fn_tool
def update_adrule(
    adrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdRule(adrule_id).api_update(fields=fields, params=params)


@adrule_server.tool
@wrapped_fn_tool
def delete_adrule(
    adrule_id: str,
) -> str:
    return AdRule(adrule_id).api_delete()


# ---- Edge Methods (3) ----
@adrule_server.tool
@wrapped_fn_tool
def create_execute(
    adrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdRule(adrule_id).create_execute(fields=fields, params=params)


@adrule_server.tool
@wrapped_fn_tool
def get_history(
    adrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdRule(adrule_id).get_history(fields=fields, params=params)


@adrule_server.tool
@wrapped_fn_tool
def create_preview(
    adrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdRule(adrule_id).create_preview(fields=fields, params=params)
