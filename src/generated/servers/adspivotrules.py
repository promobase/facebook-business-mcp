"""AdsPivotRules MCP Server with typed wrappers."""

from facebook_business.adobjects.adspivotrules import AdsPivotRules
from fastmcp import FastMCP

from src.generated.models.adspivotrules import AdsPivotRulesField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsPivotRules"
instructions = """
AdsPivotRules MCP Server for Facebook Business API.

Provides typed access to all AdsPivotRules operations.
"""

adspivotrules_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adspivotrules_server.tool
@wrapped_fn_tool
def get_adspivotrules(
    adspivotrules_id: str,
    fields: list[AdsPivotRulesField] = [],
) -> str:
    """Get a AdsPivotRules object by ID.

    Args:
        adspivotrules_id: The ID of the AdsPivotRules.
        fields: Fields to retrieve. Available fields: See AdsPivotRulesField type.
    """
    obj = AdsPivotRules(adspivotrules_id)
    return obj.api_get(fields=fields)
