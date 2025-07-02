"""OmegaCustomerTrx MCP Server."""

from typing import Any

from facebook_business.adobjects.omegacustomertrx import OmegaCustomerTrx
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOmegaCustomerTrx"
instructions = """
OmegaCustomerTrx MCP Server for Facebook Business API.

Provides typed access to all OmegaCustomerTrx operations.
"""

omegacustomertrx_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@omegacustomertrx_server.tool
@wrapped_fn_tool
def get_omegacustomertrx(
    omegacustomertrx_id: str,
    fields: list[str] = [],
) -> str:
    obj = OmegaCustomerTrx(omegacustomertrx_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@omegacustomertrx_server.tool
@wrapped_fn_tool
def get_campaigns(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OmegaCustomerTrx(omegacustomertrx_id).get_campaigns(fields=fields, params=params)
