"""AdAccountUserSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.adaccountusersettings import AdAccountUserSettings
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountUserSettings"
instructions = """
AdAccountUserSettings MCP Server for Facebook Business API.

Provides typed access to all AdAccountUserSettings operations.
"""

adaccountusersettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adaccountusersettings_server.tool
@wrapped_fn_tool
def get_adaccountusersettings(
    adaccountusersettings_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdAccountUserSettings(adaccountusersettings_id)
    return obj.api_get(fields=fields)
