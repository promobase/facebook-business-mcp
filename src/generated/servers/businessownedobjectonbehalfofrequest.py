"""BusinessOwnedObjectOnBehalfOfRequest MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.businessownedobjectonbehalfofrequest import (
    BusinessOwnedObjectOnBehalfOfRequest,
)
from fastmcp import FastMCP

from src.generated.models.businessownedobjectonbehalfofrequest import (
    BusinessOwnedObjectOnBehalfOfRequestField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessOwnedObjectOnBehalfOfRequest"
instructions = """
BusinessOwnedObjectOnBehalfOfRequest MCP Server for Facebook Business API.

Provides typed access to all BusinessOwnedObjectOnBehalfOfRequest operations.
"""

businessownedobjectonbehalfofrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessownedobjectonbehalfofrequest_server.tool
@wrapped_fn_tool
def get_businessownedobjectonbehalfofrequest(
    businessownedobjectonbehalfofrequest_id: str,
    fields: list[BusinessOwnedObjectOnBehalfOfRequestField] = [],
) -> str:
    """Get a BusinessOwnedObjectOnBehalfOfRequest object by ID.

    Args:
        businessownedobjectonbehalfofrequest_id: The ID of the BusinessOwnedObjectOnBehalfOfRequest.
        fields: Fields to retrieve. Available fields: See BusinessOwnedObjectOnBehalfOfRequestField type.
    """
    obj = BusinessOwnedObjectOnBehalfOfRequest(businessownedobjectonbehalfofrequest_id)
    return obj.api_get(fields=fields)
