"""AdAccountCreationRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.adaccountcreationrequest import AdAccountCreationRequest
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountCreationRequest"
instructions = """
AdAccountCreationRequest MCP Server for Facebook Business API.

Provides typed access to all AdAccountCreationRequest operations.
"""

adaccountcreationrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adaccountcreationrequest_server.tool
@wrapped_fn_tool
def get_adaccountcreationrequest(
    adaccountcreationrequest_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdAccountCreationRequest(adaccountcreationrequest_id)
    return obj.api_get(fields=fields)
