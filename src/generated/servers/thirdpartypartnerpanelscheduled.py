"""ThirdPartyPartnerPanelScheduled MCP Server with typed wrappers."""

from facebook_business.adobjects.thirdpartypartnerpanelscheduled import (
    ThirdPartyPartnerPanelScheduled,
)
from fastmcp import FastMCP

from src.generated.models.thirdpartypartnerpanelscheduled import (
    ThirdPartyPartnerPanelScheduledField,
)
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
    fields: list[ThirdPartyPartnerPanelScheduledField] = [],
) -> str:
    """Get a ThirdPartyPartnerPanelScheduled object by ID.

    Args:
        thirdpartypartnerpanelscheduled_id: The ID of the ThirdPartyPartnerPanelScheduled.
        fields: Fields to retrieve. Available fields: See ThirdPartyPartnerPanelScheduledField type.
    """
    obj = ThirdPartyPartnerPanelScheduled(thirdpartypartnerpanelscheduled_id)
    return obj.api_get(fields=fields)
