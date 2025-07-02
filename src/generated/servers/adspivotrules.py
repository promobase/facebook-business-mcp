"""AdsPivotRules MCP Server."""

from typing import Any

from facebook_business.adobjects.adspivotrules import AdsPivotRules
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsPivotRules"
instructions = """
AdsPivotRules MCP Server for Facebook Business API.

Provides typed access to all AdsPivotRules operations.
"""

adspivotrules_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adspivotrules_server.tool
@wrapped_fn_tool
def get_adspivotrules(
    adspivotrules_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsPivotRules(adspivotrules_id)
    return obj.api_get(fields=fields)
