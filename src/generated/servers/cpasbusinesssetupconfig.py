"""CPASBusinessSetupConfig MCP Server with typed wrappers."""

from facebook_business.adobjects.cpasbusinesssetupconfig import CPASBusinessSetupConfig
from fastmcp import FastMCP

from src.generated.models.cpasbusinesssetupconfig import CPASBusinessSetupConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASBusinessSetupConfig"
instructions = """
CPASBusinessSetupConfig MCP Server for Facebook Business API.

Provides typed access to all CPASBusinessSetupConfig operations.
"""

cpasbusinesssetupconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cpasbusinesssetupconfig_server.tool
@wrapped_fn_tool
def get_cpasbusinesssetupconfig(
    cpasbusinesssetupconfig_id: str,
    fields: list[CPASBusinessSetupConfigField] = [],
) -> str:
    """Get a CPASBusinessSetupConfig object by ID.

    Args:
        cpasbusinesssetupconfig_id: The ID of the CPASBusinessSetupConfig.
        fields: Fields to retrieve. Available fields: See CPASBusinessSetupConfigField type.
    """
    obj = CPASBusinessSetupConfig(cpasbusinesssetupconfig_id)
    return obj.api_get(fields=fields)
