"""OwnedDomain MCP Server with typed wrappers."""

from facebook_business.adobjects.owneddomain import OwnedDomain
from fastmcp import FastMCP

from src.generated.models.owneddomain import OwnedDomainField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOwnedDomain"
instructions = """
OwnedDomain MCP Server for Facebook Business API.

Provides typed access to all OwnedDomain operations.
"""

owneddomain_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@owneddomain_server.tool
@wrapped_fn_tool
def get_owneddomain(
    owneddomain_id: str,
    fields: list[OwnedDomainField] = [],
) -> str:
    """Get a OwnedDomain object by ID.

    Args:
        owneddomain_id: The ID of the OwnedDomain.
        fields: Fields to retrieve. Available fields: See OwnedDomainField type.
    """
    obj = OwnedDomain(owneddomain_id)
    return obj.api_get(fields=fields)
