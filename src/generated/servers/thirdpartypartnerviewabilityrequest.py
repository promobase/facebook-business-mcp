"""ThirdPartyPartnerViewabilityRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.thirdpartypartnerviewabilityrequest import (
    ThirdPartyPartnerViewabilityRequest,
)
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ThirdPartyPartnerViewabilityRequest(thirdpartypartnerviewabilityrequest_id)
    return obj.api_get(fields=fields)
