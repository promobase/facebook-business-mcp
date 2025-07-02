"""DynamicPriceConfigByDate MCP Server."""

from typing import Any

from facebook_business.adobjects.dynamicpriceconfigbydate import DynamicPriceConfigByDate
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicPriceConfigByDate"
instructions = """
DynamicPriceConfigByDate MCP Server for Facebook Business API.

Provides typed access to all DynamicPriceConfigByDate operations.
"""

dynamicpriceconfigbydate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicpriceconfigbydate_server.tool
@wrapped_fn_tool
def get_dynamicpriceconfigbydate(
    dynamicpriceconfigbydate_id: str,
    fields: list[str] = [],
) -> str:
    obj = DynamicPriceConfigByDate(dynamicpriceconfigbydate_id)
    return obj.api_get(fields=fields)
