"""LeadGenDirectCRMIntegrationConfig MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.leadgendirectcrmintegrationconfig import (
    LeadGenDirectCRMIntegrationConfig,
)
from fastmcp import FastMCP

from src.generated.models.leadgendirectcrmintegrationconfig import (
    LeadGenDirectCRMIntegrationConfigField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLeadGenDirectCRMIntegrationConfig"
instructions = """
LeadGenDirectCRMIntegrationConfig MCP Server for Facebook Business API.

Provides typed access to all LeadGenDirectCRMIntegrationConfig operations.
"""

leadgendirectcrmintegrationconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@leadgendirectcrmintegrationconfig_server.tool
@wrapped_fn_tool
def get_leadgendirectcrmintegrationconfig(
    leadgendirectcrmintegrationconfig_id: str,
    fields: list[LeadGenDirectCRMIntegrationConfigField] = [],
) -> str:
    """Get a LeadGenDirectCRMIntegrationConfig object by ID.

    Args:
        leadgendirectcrmintegrationconfig_id: The ID of the LeadGenDirectCRMIntegrationConfig.
        fields: Fields to retrieve. Available fields: See LeadGenDirectCRMIntegrationConfigField type.
    """
    obj = LeadGenDirectCRMIntegrationConfig(leadgendirectcrmintegrationconfig_id)
    return obj.api_get(fields=fields)
