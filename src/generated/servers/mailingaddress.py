"""MailingAddress MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.mailingaddress import MailingAddress
from fastmcp import FastMCP

from src.generated.models.mailingaddress import MailingAddressField
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
    fields: list[MailingAddressField] = [],
) -> str:
    """Get a MailingAddress object by ID.

    Args:
        mailingaddress_id: The ID of the MailingAddress.
        fields: Fields to retrieve. Available fields: See MailingAddressField type.
    """
    obj = MailingAddress(mailingaddress_id)
    return obj.api_get(fields=fields)
