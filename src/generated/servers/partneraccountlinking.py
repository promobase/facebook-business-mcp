"""PartnerAccountLinking MCP Server."""

from typing import Any

from facebook_business.adobjects.partneraccountlinking import PartnerAccountLinking
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPartnerAccountLinking"
instructions = """
PartnerAccountLinking MCP Server for Facebook Business API.

Provides typed access to all PartnerAccountLinking operations.
"""

partneraccountlinking_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@partneraccountlinking_server.tool
@wrapped_fn_tool
def get_partneraccountlinking(
    partneraccountlinking_id: str,
    fields: list[str] = [],
) -> str:
    obj = PartnerAccountLinking(partneraccountlinking_id)
    return obj.api_get(fields=fields)
