"""CallAdsPhoneData MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.calladsphonedata import CallAdsPhoneData
from fastmcp import FastMCP

from src.generated.models.calladsphonedata import CallAdsPhoneDataField
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
    fields: list[CallAdsPhoneDataField] = [],
) -> str:
    """Get a CallAdsPhoneData object by ID.

    Args:
        calladsphonedata_id: The ID of the CallAdsPhoneData.
        fields: Fields to retrieve. Available fields: See CallAdsPhoneDataField type.
    """
    obj = CallAdsPhoneData(calladsphonedata_id)
    return obj.api_get(fields=fields)
