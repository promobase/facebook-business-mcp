"""LeadGenDirectCRMIntegrationConfig MCP Server."""

from typing import Any

from facebook_business.adobjects.leadgendirectcrmintegrationconfig import (
    LeadGenDirectCRMIntegrationConfig,
)
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = LeadGenDirectCRMIntegrationConfig(leadgendirectcrmintegrationconfig_id)
    return obj.api_get(fields=fields)
