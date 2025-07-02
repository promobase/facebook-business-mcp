"""AdAccountSubscribedApps MCP Server."""

from typing import Any

from facebook_business.adobjects.adaccountsubscribedapps import AdAccountSubscribedApps
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountSubscribedApps"
instructions = """
AdAccountSubscribedApps MCP Server for Facebook Business API.

Provides typed access to all AdAccountSubscribedApps operations.
"""

adaccountsubscribedapps_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adaccountsubscribedapps_server.tool
@wrapped_fn_tool
def get_endpoint(
    adaccountsubscribedapps_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccountSubscribedApps(adaccountsubscribedapps_id).get_endpoint(
        fields=fields, params=params
    )
