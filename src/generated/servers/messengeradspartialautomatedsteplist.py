"""MessengerAdsPartialAutomatedStepList MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.messengeradspartialautomatedsteplist import (
    MessengerAdsPartialAutomatedStepList,
)
from fastmcp import FastMCP

from src.generated.models.messengeradspartialautomatedsteplist import (
    MessengerAdsPartialAutomatedStepListField,
)
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
    fields: list[MessengerAdsPartialAutomatedStepListField] = [],
) -> str:
    """Get a MessengerAdsPartialAutomatedStepList object by ID.

    Args:
        messengeradspartialautomatedsteplist_id: The ID of the MessengerAdsPartialAutomatedStepList.
        fields: Fields to retrieve. Available fields: See MessengerAdsPartialAutomatedStepListField type.
    """
    obj = MessengerAdsPartialAutomatedStepList(messengeradspartialautomatedsteplist_id)
    return obj.api_get(fields=fields)
