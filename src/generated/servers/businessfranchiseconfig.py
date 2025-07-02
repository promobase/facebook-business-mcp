"""BusinessFranchiseConfig MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.businessfranchiseconfig import BusinessFranchiseConfig
from fastmcp import FastMCP

from src.generated.models.businessfranchiseconfig import BusinessFranchiseConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessFranchiseConfig"
instructions = """
BusinessFranchiseConfig MCP Server for Facebook Business API.

Provides typed access to all BusinessFranchiseConfig operations.
"""

businessfranchiseconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessfranchiseconfig_server.tool
@wrapped_fn_tool
def get_businessfranchiseconfig(
    businessfranchiseconfig_id: str,
    fields: list[BusinessFranchiseConfigField] = [],
) -> str:
    """Get a BusinessFranchiseConfig object by ID.

    Args:
        businessfranchiseconfig_id: The ID of the BusinessFranchiseConfig.
        fields: Fields to retrieve. Available fields: See BusinessFranchiseConfigField type.
    """
    obj = BusinessFranchiseConfig(businessfranchiseconfig_id)
    return obj.api_get(fields=fields)
