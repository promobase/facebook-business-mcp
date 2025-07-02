"""ThirdPartyPartnerViewabilityRequest MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.thirdpartypartnerviewabilityrequest import (
    ThirdPartyPartnerViewabilityRequest,
)
from fastmcp import FastMCP

from src.generated.models.thirdpartypartnerviewabilityrequest import (
    ThirdPartyPartnerViewabilityRequestField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookThirdPartyPartnerViewabilityRequest"
instructions = """
ThirdPartyPartnerViewabilityRequest MCP Server for Facebook Business API.

Provides typed access to all ThirdPartyPartnerViewabilityRequest operations.
"""

thirdpartypartnerviewabilityrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@thirdpartypartnerviewabilityrequest_server.tool
@wrapped_fn_tool
def get_thirdpartypartnerviewabilityrequest(
    thirdpartypartnerviewabilityrequest_id: str,
    fields: list[ThirdPartyPartnerViewabilityRequestField] = [],
) -> str:
    """Get a ThirdPartyPartnerViewabilityRequest object by ID.

    Args:
        thirdpartypartnerviewabilityrequest_id: The ID of the ThirdPartyPartnerViewabilityRequest.
        fields: Fields to retrieve. Available fields: See ThirdPartyPartnerViewabilityRequestField type.
    """
    obj = ThirdPartyPartnerViewabilityRequest(thirdpartypartnerviewabilityrequest_id)
    return obj.api_get(fields=fields)
