"""CPASMerchantConfig MCP Server."""

from typing import Any

from facebook_business.adobjects.cpasmerchantconfig import CPASMerchantConfig
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = CPASMerchantConfig(cpasmerchantconfig_id)
    return obj.api_get(fields=fields)
