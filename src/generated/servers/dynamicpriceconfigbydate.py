"""DynamicPriceConfigByDate MCP Server with typed wrappers."""

from facebook_business.adobjects.dynamicpriceconfigbydate import DynamicPriceConfigByDate
from fastmcp import FastMCP

from src.generated.models.dynamicpriceconfigbydate import DynamicPriceConfigByDateField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicPriceConfigByDate"
instructions = """
DynamicPriceConfigByDate MCP Server for Facebook Business API.

Provides typed access to all DynamicPriceConfigByDate operations.
"""

dynamicpriceconfigbydate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicpriceconfigbydate_server.tool
@wrapped_fn_tool
def get_dynamicpriceconfigbydate(
    dynamicpriceconfigbydate_id: str,
    fields: list[DynamicPriceConfigByDateField] = [],
) -> str:
    """Get a DynamicPriceConfigByDate object by ID.

    Args:
        dynamicpriceconfigbydate_id: The ID of the DynamicPriceConfigByDate.
        fields: Fields to retrieve. Available fields: See DynamicPriceConfigByDateField type.
    """
    obj = DynamicPriceConfigByDate(dynamicpriceconfigbydate_id)
    return obj.api_get(fields=fields)
