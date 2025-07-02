"""AREffect MCP Server with typed wrappers."""

from facebook_business.adobjects.areffect import AREffect
from fastmcp import FastMCP

from src.generated.models.areffect import AREffectField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAREffect"
instructions = """
AREffect MCP Server for Facebook Business API.

Provides typed access to all AREffect operations.
"""

areffect_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@areffect_server.tool
@wrapped_fn_tool
def get_areffect(
    areffect_id: str,
    fields: list[AREffectField] = [],
) -> str:
    """Get a AREffect object by ID.

    Args:
        areffect_id: The ID of the AREffect.
        fields: Fields to retrieve. Available fields: See AREffectField type.
    """
    obj = AREffect(areffect_id)
    return obj.api_get(fields=fields)
