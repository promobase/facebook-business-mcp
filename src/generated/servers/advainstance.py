"""AdvAInstance MCP Server with typed wrappers."""

from facebook_business.adobjects.advainstance import AdvAInstance
from fastmcp import FastMCP

from src.generated.models.advainstance import AdvAInstanceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdvAInstance"
instructions = """
AdvAInstance MCP Server for Facebook Business API.

Provides typed access to all AdvAInstance operations.
"""

advainstance_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@advainstance_server.tool
@wrapped_fn_tool
def get_advainstance(
    advainstance_id: str,
    fields: list[AdvAInstanceField] = [],
) -> str:
    """Get a AdvAInstance object by ID.

    Args:
        advainstance_id: The ID of the AdvAInstance.
        fields: Fields to retrieve. Available fields: See AdvAInstanceField type.
    """
    obj = AdvAInstance(advainstance_id)
    return obj.api_get(fields=fields)
