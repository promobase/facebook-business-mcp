"""ThirdPartyPartnerLiftRequest MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.thirdpartypartnerliftrequest import ThirdPartyPartnerLiftRequest
from fastmcp import FastMCP

from src.generated.models.thirdpartypartnerliftrequest import ThirdPartyPartnerLiftRequestField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookThirdPartyPartnerLiftRequest"
instructions = """
ThirdPartyPartnerLiftRequest MCP Server for Facebook Business API.

Provides typed access to all ThirdPartyPartnerLiftRequest operations.
"""

thirdpartypartnerliftrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@thirdpartypartnerliftrequest_server.tool
@wrapped_fn_tool
def get_thirdpartypartnerliftrequest(
    thirdpartypartnerliftrequest_id: str,
    fields: list[ThirdPartyPartnerLiftRequestField] = [],
) -> str:
    """Get a ThirdPartyPartnerLiftRequest object by ID.

    Args:
        thirdpartypartnerliftrequest_id: The ID of the ThirdPartyPartnerLiftRequest.
        fields: Fields to retrieve. Available fields: See ThirdPartyPartnerLiftRequestField type.
    """
    obj = ThirdPartyPartnerLiftRequest(thirdpartypartnerliftrequest_id)
    return obj.api_get(fields=fields)
