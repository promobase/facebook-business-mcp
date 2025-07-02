"""AppEventConfig MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.appeventconfig import AppEventConfig
from fastmcp import FastMCP

from src.generated.models.appeventconfig import AppEventConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAppEventConfig"
instructions = """
AppEventConfig MCP Server for Facebook Business API.

Provides typed access to all AppEventConfig operations.
"""

appeventconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@appeventconfig_server.tool
@wrapped_fn_tool
def get_appeventconfig(
    appeventconfig_id: str,
    fields: list[AppEventConfigField] = [],
) -> str:
    """Get a AppEventConfig object by ID.

    Args:
        appeventconfig_id: The ID of the AppEventConfig.
        fields: Fields to retrieve. Available fields: See AppEventConfigField type.
    """
    obj = AppEventConfig(appeventconfig_id)
    return obj.api_get(fields=fields)
