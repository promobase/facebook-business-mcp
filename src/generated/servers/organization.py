"""Organization MCP Server with typed wrappers."""

from facebook_business.adobjects.organization import Organization
from fastmcp import FastMCP

from src.generated.models.organization import OrganizationField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOrganization"
instructions = """
Organization MCP Server for Facebook Business API.

Provides typed access to all Organization operations.
"""

organization_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@organization_server.tool
@wrapped_fn_tool
def get_organization(
    organization_id: str,
    fields: list[OrganizationField] = [],
) -> str:
    """Get a Organization object by ID.

    Args:
        organization_id: The ID of the Organization.
        fields: Fields to retrieve. Available fields: See OrganizationField type.
    """
    obj = Organization(organization_id)
    return obj.api_get(fields=fields)
