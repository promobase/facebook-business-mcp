"""PartnerAccountLinking MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.partneraccountlinking import PartnerAccountLinking
from fastmcp import FastMCP

from src.generated.models.partneraccountlinking import PartnerAccountLinkingField
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
    fields: list[PartnerAccountLinkingField] = [],
) -> str:
    """Get a PartnerAccountLinking object by ID.

    Args:
        partneraccountlinking_id: The ID of the PartnerAccountLinking.
        fields: Fields to retrieve. Available fields: See PartnerAccountLinkingField type.
    """
    obj = PartnerAccountLinking(partneraccountlinking_id)
    return obj.api_get(fields=fields)
