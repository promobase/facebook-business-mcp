"""PartnerIntegrationLinked MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.partnerintegrationlinked import PartnerIntegrationLinked
from fastmcp import FastMCP

from src.generated.models.partnerintegrationlinked import PartnerIntegrationLinkedField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPartnerIntegrationLinked"
instructions = """
PartnerIntegrationLinked MCP Server for Facebook Business API.

Provides typed access to all PartnerIntegrationLinked operations.
"""

partnerintegrationlinked_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@partnerintegrationlinked_server.tool
@wrapped_fn_tool
def get_partnerintegrationlinked(
    partnerintegrationlinked_id: str,
    fields: list[PartnerIntegrationLinkedField] = [],
) -> str:
    """Get a PartnerIntegrationLinked object by ID.

    Args:
        partnerintegrationlinked_id: The ID of the PartnerIntegrationLinked.
        fields: Fields to retrieve. Available fields: See PartnerIntegrationLinkedField type.
    """
    obj = PartnerIntegrationLinked(partnerintegrationlinked_id)
    return obj.api_get(fields=fields)
