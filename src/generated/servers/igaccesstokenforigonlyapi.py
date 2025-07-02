"""IGAccessTokenForIGOnlyAPI MCP Server."""

from typing import Any

from facebook_business.adobjects.igaccesstokenforigonlyapi import IGAccessTokenForIGOnlyAPI
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGAccessTokenForIGOnlyAPI"
instructions = """
IGAccessTokenForIGOnlyAPI MCP Server for Facebook Business API.

Provides typed access to all IGAccessTokenForIGOnlyAPI operations.
"""

igaccesstokenforigonlyapi_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@igaccesstokenforigonlyapi_server.tool
@wrapped_fn_tool
def get_igaccesstokenforigonlyapi(
    igaccesstokenforigonlyapi_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGAccessTokenForIGOnlyAPI(igaccesstokenforigonlyapi_id)
    return obj.api_get(fields=fields)
