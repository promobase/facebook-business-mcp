"""CallAdsPhoneData MCP Server."""

from typing import Any

from facebook_business.adobjects.calladsphonedata import CallAdsPhoneData
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCallAdsPhoneData"
instructions = """
CallAdsPhoneData MCP Server for Facebook Business API.

Provides typed access to all CallAdsPhoneData operations.
"""

calladsphonedata_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@calladsphonedata_server.tool
@wrapped_fn_tool
def get_calladsphonedata(
    calladsphonedata_id: str,
    fields: list[str] = [],
) -> str:
    obj = CallAdsPhoneData(calladsphonedata_id)
    return obj.api_get(fields=fields)
