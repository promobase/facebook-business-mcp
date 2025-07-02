"""AdsMcmeConversion MCP Server."""

from typing import Any

from facebook_business.adobjects.adsmcmeconversion import AdsMcmeConversion
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsMcmeConversion"
instructions = """
AdsMcmeConversion MCP Server for Facebook Business API.

Provides typed access to all AdsMcmeConversion operations.
"""

adsmcmeconversion_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsmcmeconversion_server.tool
@wrapped_fn_tool
def get_adsmcmeconversion(
    adsmcmeconversion_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsMcmeConversion(adsmcmeconversion_id)
    return obj.api_get(fields=fields)
