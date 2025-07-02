"""AdColumnSizes MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adcolumnsizes import AdColumnSizes
from fastmcp import FastMCP

from src.generated.models.adcolumnsizes import AdColumnSizesField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdColumnSizes"
instructions = """
AdColumnSizes MCP Server for Facebook Business API.

Provides typed access to all AdColumnSizes operations.
"""

adcolumnsizes_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adcolumnsizes_server.tool
@wrapped_fn_tool
def get_adcolumnsizes(
    adcolumnsizes_id: str,
    fields: list[AdColumnSizesField] = [],
) -> str:
    """Get a AdColumnSizes object by ID.

    Args:
        adcolumnsizes_id: The ID of the AdColumnSizes.
        fields: Fields to retrieve. Available fields: See AdColumnSizesField type.
    """
    obj = AdColumnSizes(adcolumnsizes_id)
    return obj.api_get(fields=fields)
