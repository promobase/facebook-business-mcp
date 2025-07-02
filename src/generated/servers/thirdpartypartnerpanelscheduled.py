"""ThirdPartyPartnerPanelScheduled MCP Server."""

from typing import Any

from facebook_business.adobjects.thirdpartypartnerpanelscheduled import (
    ThirdPartyPartnerPanelScheduled,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookThirdPartyPartnerPanelScheduled"
instructions = """
ThirdPartyPartnerPanelScheduled MCP Server for Facebook Business API.

Provides typed access to all ThirdPartyPartnerPanelScheduled operations.
"""

thirdpartypartnerpanelscheduled_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@thirdpartypartnerpanelscheduled_server.tool
@wrapped_fn_tool
def get_thirdpartypartnerpanelscheduled(
    thirdpartypartnerpanelscheduled_id: str,
    fields: list[str] = [],
) -> str:
    obj = ThirdPartyPartnerPanelScheduled(thirdpartypartnerpanelscheduled_id)
    return obj.api_get(fields=fields)
