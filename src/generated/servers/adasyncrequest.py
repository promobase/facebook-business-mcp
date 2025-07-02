"""AdAsyncRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.adasyncrequest import AdAsyncRequest
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAsyncRequest"
instructions = """
AdAsyncRequest MCP Server for Facebook Business API.

Provides typed access to all AdAsyncRequest operations.
"""

adasyncrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adasyncrequest_server.tool
@wrapped_fn_tool
def get_adasyncrequest(
    adasyncrequest_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdAsyncRequest(adasyncrequest_id)
    return obj.api_get(fields=fields)


@adasyncrequest_server.tool
@wrapped_fn_tool
def delete_adasyncrequest(
    adasyncrequest_id: str,
) -> str:
    return AdAsyncRequest(adasyncrequest_id).api_delete()
