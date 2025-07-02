"""AnalyticsUserConfig MCP Server with typed wrappers."""

from facebook_business.adobjects.analyticsuserconfig import AnalyticsUserConfig
from fastmcp import FastMCP

from src.generated.models.analyticsuserconfig import AnalyticsUserConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAnalyticsUserConfig"
instructions = """
AnalyticsUserConfig MCP Server for Facebook Business API.

Provides typed access to all AnalyticsUserConfig operations.
"""

analyticsuserconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@analyticsuserconfig_server.tool
@wrapped_fn_tool
def get_analyticsuserconfig(
    analyticsuserconfig_id: str,
    fields: list[AnalyticsUserConfigField] = [],
) -> str:
    """Get a AnalyticsUserConfig object by ID.

    Args:
        analyticsuserconfig_id: The ID of the AnalyticsUserConfig.
        fields: Fields to retrieve. Available fields: See AnalyticsUserConfigField type.
    """
    obj = AnalyticsUserConfig(analyticsuserconfig_id)
    return obj.api_get(fields=fields)
