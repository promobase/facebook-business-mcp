"""ThirdPartyPartnerLiftRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.thirdpartypartnerliftrequest import ThirdPartyPartnerLiftRequest
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ThirdPartyPartnerLiftRequest(thirdpartypartnerliftrequest_id)
    return obj.api_get(fields=fields)
