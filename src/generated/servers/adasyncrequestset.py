"""AdAsyncRequestSet MCP Server."""

from typing import Any

from facebook_business.adobjects.adasyncrequestset import AdAsyncRequestSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAsyncRequestSet"
instructions = """
AdAsyncRequestSet MCP Server for Facebook Business API.

Provides typed access to all AdAsyncRequestSet operations.
"""

adasyncrequestset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adasyncrequestset_server.tool
@wrapped_fn_tool
def get_adasyncrequestset(
    adasyncrequestset_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdAsyncRequestSet(adasyncrequestset_id)
    return obj.api_get(fields=fields)


@adasyncrequestset_server.tool
@wrapped_fn_tool
def update_adasyncrequestset(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAsyncRequestSet(adasyncrequestset_id).api_update(fields=fields, params=params)


@adasyncrequestset_server.tool
@wrapped_fn_tool
def delete_adasyncrequestset(
    adasyncrequestset_id: str,
) -> str:
    return AdAsyncRequestSet(adasyncrequestset_id).api_delete()


# ---- Edge Methods (1) ----
@adasyncrequestset_server.tool
@wrapped_fn_tool
def get_requests(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAsyncRequestSet(adasyncrequestset_id).get_requests(fields=fields, params=params)
