"""ThirdPartyPartnerPanelRequest MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.thirdpartypartnerpanelrequest import ThirdPartyPartnerPanelRequest
from fastmcp import FastMCP

from src.generated.models.thirdpartypartnerpanelrequest import ThirdPartyPartnerPanelRequestField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookThirdPartyPartnerPanelRequest"
instructions = """
ThirdPartyPartnerPanelRequest MCP Server for Facebook Business API.

Provides typed access to all ThirdPartyPartnerPanelRequest operations.
"""

thirdpartypartnerpanelrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@thirdpartypartnerpanelrequest_server.tool
@wrapped_fn_tool
def get_thirdpartypartnerpanelrequest(
    thirdpartypartnerpanelrequest_id: str,
    fields: list[ThirdPartyPartnerPanelRequestField] = [],
) -> str:
    """Get a ThirdPartyPartnerPanelRequest object by ID.

    Args:
        thirdpartypartnerpanelrequest_id: The ID of the ThirdPartyPartnerPanelRequest.
        fields: Fields to retrieve. Available fields: See ThirdPartyPartnerPanelRequestField type.
    """
    obj = ThirdPartyPartnerPanelRequest(thirdpartypartnerpanelrequest_id)
    return obj.api_get(fields=fields)
