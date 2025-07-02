"""AdsMcmeConversion MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adsmcmeconversion import AdsMcmeConversion
from fastmcp import FastMCP

from src.generated.models.adsmcmeconversion import AdsMcmeConversionField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsMcmeConversion"
instructions = """
AdsMcmeConversion MCP Server for Facebook Business API.

Provides typed access to all AdsMcmeConversion operations.
"""

adsmcmeconversion_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsmcmeconversion_server.tool
@wrapped_fn_tool
def get_adsmcmeconversion(
    adsmcmeconversion_id: str,
    fields: list[AdsMcmeConversionField] = [],
) -> str:
    """Get a AdsMcmeConversion object by ID.

    Args:
        adsmcmeconversion_id: The ID of the AdsMcmeConversion.
        fields: Fields to retrieve. Available fields: See AdsMcmeConversionField type.
    """
    obj = AdsMcmeConversion(adsmcmeconversion_id)
    return obj.api_get(fields=fields)
