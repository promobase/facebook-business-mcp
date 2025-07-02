"""AnalyticsUserConfig MCP Server."""

from typing import Any

from facebook_business.adobjects.analyticsuserconfig import AnalyticsUserConfig
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAnalyticsUserConfig"
instructions = """
AnalyticsUserConfig MCP Server for Facebook Business API.

Provides typed access to all AnalyticsUserConfig operations.
"""

analyticsuserconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@analyticsuserconfig_server.tool
@wrapped_fn_tool
def get_analyticsuserconfig(
    analyticsuserconfig_id: str,
    fields: list[str] = [],
) -> str:
    obj = AnalyticsUserConfig(analyticsuserconfig_id)
    return obj.api_get(fields=fields)
