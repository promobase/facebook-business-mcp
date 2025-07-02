"""OmegaCustomerTrx MCP Server with typed wrappers."""

from facebook_business.adobjects.omegacustomertrx import OmegaCustomerTrx
from fastmcp import FastMCP

from src.generated.models.omegacustomertrx import OmegaCustomerTrxField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOmegaCustomerTrx"
instructions = """
OmegaCustomerTrx MCP Server for Facebook Business API.

Provides typed access to all OmegaCustomerTrx operations.
"""

omegacustomertrx_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@omegacustomertrx_server.tool
@wrapped_fn_tool
def get_omegacustomertrx(
    omegacustomertrx_id: str,
    fields: list[OmegaCustomerTrxField] = [],
) -> str:
    """Get a OmegaCustomerTrx object by ID.

    Args:
        omegacustomertrx_id: The ID of the OmegaCustomerTrx.
        fields: Fields to retrieve. Available fields: See OmegaCustomerTrxField type.
    """
    obj = OmegaCustomerTrx(omegacustomertrx_id)
    return obj.api_get(fields=fields)
