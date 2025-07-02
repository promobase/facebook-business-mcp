"""BrandRequest MCP Server with typed wrappers."""

from facebook_business.adobjects.brandrequest import BrandRequest
from fastmcp import FastMCP

from src.generated.models.brandrequest import BrandRequestField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBrandRequest"
instructions = """
BrandRequest MCP Server for Facebook Business API.

Provides typed access to all BrandRequest operations.
"""

brandrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@brandrequest_server.tool
@wrapped_fn_tool
def get_brandrequest(
    brandrequest_id: str,
    fields: list[BrandRequestField] = [],
) -> str:
    """Get a BrandRequest object by ID.

    Args:
        brandrequest_id: The ID of the BrandRequest.
        fields: Fields to retrieve. Available fields: See BrandRequestField type.
    """
    obj = BrandRequest(brandrequest_id)
    return obj.api_get(fields=fields)
