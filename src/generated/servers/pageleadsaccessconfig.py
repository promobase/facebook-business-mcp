"""PageLeadsAccessConfig MCP Server with typed wrappers."""

from facebook_business.adobjects.pageleadsaccessconfig import PageLeadsAccessConfig
from fastmcp import FastMCP

from src.generated.models.pageleadsaccessconfig import PageLeadsAccessConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageLeadsAccessConfig"
instructions = """
PageLeadsAccessConfig MCP Server for Facebook Business API.

Provides typed access to all PageLeadsAccessConfig operations.
"""

pageleadsaccessconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@pageleadsaccessconfig_server.tool
@wrapped_fn_tool
def get_pageleadsaccessconfig(
    pageleadsaccessconfig_id: str,
    fields: list[PageLeadsAccessConfigField] = [],
) -> str:
    """Get a PageLeadsAccessConfig object by ID.

    Args:
        pageleadsaccessconfig_id: The ID of the PageLeadsAccessConfig.
        fields: Fields to retrieve. Available fields: See PageLeadsAccessConfigField type.
    """
    obj = PageLeadsAccessConfig(pageleadsaccessconfig_id)
    return obj.api_get(fields=fields)
