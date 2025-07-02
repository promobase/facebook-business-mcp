"""IGMediaForIGOnlyAPI MCP Server."""

from typing import Any

from facebook_business.adobjects.igmediaforigonlyapi import IGMediaForIGOnlyAPI
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGMediaForIGOnlyAPI"
instructions = """
IGMediaForIGOnlyAPI MCP Server for Facebook Business API.

Provides typed access to all IGMediaForIGOnlyAPI operations.
"""

igmediaforigonlyapi_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def get_igmediaforigonlyapi(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGMediaForIGOnlyAPI(igmediaforigonlyapi_id)
    return obj.api_get(fields=fields)


@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def update_igmediaforigonlyapi(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).api_update(fields=fields, params=params)


# ---- Edge Methods (4) ----
@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def get_children(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).get_children(fields=fields, params=params)


@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def get_comments(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).get_comments(fields=fields, params=params)


@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def create_comment(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).create_comment(fields=fields, params=params)


@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def get_insights(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).get_insights(fields=fields, params=params)
