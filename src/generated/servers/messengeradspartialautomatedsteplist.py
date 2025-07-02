"""MessengerAdsPartialAutomatedStepList MCP Server."""

from typing import Any

from facebook_business.adobjects.messengeradspartialautomatedsteplist import (
    MessengerAdsPartialAutomatedStepList,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMessengerAdsPartialAutomatedStepList"
instructions = """
MessengerAdsPartialAutomatedStepList MCP Server for Facebook Business API.

Provides typed access to all MessengerAdsPartialAutomatedStepList operations.
"""

messengeradspartialautomatedsteplist_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@messengeradspartialautomatedsteplist_server.tool
@wrapped_fn_tool
def get_messengeradspartialautomatedsteplist(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
) -> str:
    obj = MessengerAdsPartialAutomatedStepList(messengeradspartialautomatedsteplist_id)
    return obj.api_get(fields=fields)
