"""MailingAddress MCP Server."""

from typing import Any

from facebook_business.adobjects.mailingaddress import MailingAddress
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMailingAddress"
instructions = """
MailingAddress MCP Server for Facebook Business API.

Provides typed access to all MailingAddress operations.
"""

mailingaddress_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@mailingaddress_server.tool
@wrapped_fn_tool
def get_mailingaddress(
    mailingaddress_id: str,
    fields: list[str] = [],
) -> str:
    obj = MailingAddress(mailingaddress_id)
    return obj.api_get(fields=fields)
