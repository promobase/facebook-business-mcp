"""AdAccountAgencyFeeConfig MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adaccountagencyfeeconfig import AdAccountAgencyFeeConfig
from fastmcp import FastMCP

from src.generated.models.adaccountagencyfeeconfig import AdAccountAgencyFeeConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountAgencyFeeConfig"
instructions = """
AdAccountAgencyFeeConfig MCP Server for Facebook Business API.

Provides typed access to all AdAccountAgencyFeeConfig operations.
"""

adaccountagencyfeeconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adaccountagencyfeeconfig_server.tool
@wrapped_fn_tool
def get_adaccountagencyfeeconfig(
    adaccountagencyfeeconfig_id: str,
    fields: list[AdAccountAgencyFeeConfigField] = [],
) -> str:
    """Get a AdAccountAgencyFeeConfig object by ID.

    Args:
        adaccountagencyfeeconfig_id: The ID of the AdAccountAgencyFeeConfig.
        fields: Fields to retrieve. Available fields: See AdAccountAgencyFeeConfigField type.
    """
    obj = AdAccountAgencyFeeConfig(adaccountagencyfeeconfig_id)
    return obj.api_get(fields=fields)
