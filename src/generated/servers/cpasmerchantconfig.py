"""CPASMerchantConfig MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.cpasmerchantconfig import CPASMerchantConfig
from fastmcp import FastMCP

from src.generated.models.cpasmerchantconfig import CPASMerchantConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASMerchantConfig"
instructions = """
CPASMerchantConfig MCP Server for Facebook Business API.

Provides typed access to all CPASMerchantConfig operations.
"""

cpasmerchantconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cpasmerchantconfig_server.tool
@wrapped_fn_tool
def get_cpasmerchantconfig(
    cpasmerchantconfig_id: str,
    fields: list[CPASMerchantConfigField] = [],
) -> str:
    """Get a CPASMerchantConfig object by ID.

    Args:
        cpasmerchantconfig_id: The ID of the CPASMerchantConfig.
        fields: Fields to retrieve. Available fields: See CPASMerchantConfigField type.
    """
    obj = CPASMerchantConfig(cpasmerchantconfig_id)
    return obj.api_get(fields=fields)
