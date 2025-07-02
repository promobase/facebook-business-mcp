"""OfflineTermsOfService MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.offlinetermsofservice import OfflineTermsOfService
from fastmcp import FastMCP

from src.generated.models.offlinetermsofservice import OfflineTermsOfServiceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOfflineTermsOfService"
instructions = """
OfflineTermsOfService MCP Server for Facebook Business API.

Provides typed access to all OfflineTermsOfService operations.
"""

offlinetermsofservice_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offlinetermsofservice_server.tool
@wrapped_fn_tool
def get_offlinetermsofservice(
    offlinetermsofservice_id: str,
    fields: list[OfflineTermsOfServiceField] = [],
) -> str:
    """Get a OfflineTermsOfService object by ID.

    Args:
        offlinetermsofservice_id: The ID of the OfflineTermsOfService.
        fields: Fields to retrieve. Available fields: See OfflineTermsOfServiceField type.
    """
    obj = OfflineTermsOfService(offlinetermsofservice_id)
    return obj.api_get(fields=fields)
