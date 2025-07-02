"""AdCreationPackageConfig MCP Server."""

from typing import Any

from facebook_business.adobjects.adcreationpackageconfig import AdCreationPackageConfig
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdCreationPackageConfig"
instructions = """
AdCreationPackageConfig MCP Server for Facebook Business API.

Provides typed access to all AdCreationPackageConfig operations.
"""

adcreationpackageconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adcreationpackageconfig_server.tool
@wrapped_fn_tool
def get_adcreationpackageconfig(
    adcreationpackageconfig_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdCreationPackageConfig(adcreationpackageconfig_id)
    return obj.api_get(fields=fields)
