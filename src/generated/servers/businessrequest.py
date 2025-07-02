"""BusinessRequest MCP Server with typed wrappers."""

from facebook_business.adobjects.businessrequest import BusinessRequest
from fastmcp import FastMCP

from src.generated.models.businessrequest import BusinessRequestField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessRequest"
instructions = """
BusinessRequest MCP Server for Facebook Business API.

Provides typed access to all BusinessRequest operations.
"""

businessrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessrequest_server.tool
@wrapped_fn_tool
def get_businessrequest(
    businessrequest_id: str,
    fields: list[BusinessRequestField] = [],
) -> str:
    """Get a BusinessRequest object by ID.

    Args:
        businessrequest_id: The ID of the BusinessRequest.
        fields: Fields to retrieve. Available fields: See BusinessRequestField type.
    """
    obj = BusinessRequest(businessrequest_id)
    return obj.api_get(fields=fields)
