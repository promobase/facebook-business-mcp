"""WifiInformation MCP Server with typed wrappers."""

from facebook_business.adobjects.wifiinformation import WifiInformation
from fastmcp import FastMCP

from src.generated.models.wifiinformation import WifiInformationField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWifiInformation"
instructions = """
WifiInformation MCP Server for Facebook Business API.

Provides typed access to all WifiInformation operations.
"""

wifiinformation_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@wifiinformation_server.tool
@wrapped_fn_tool
def get_wifiinformation(
    wifiinformation_id: str,
    fields: list[WifiInformationField] = [],
) -> str:
    """Get a WifiInformation object by ID.

    Args:
        wifiinformation_id: The ID of the WifiInformation.
        fields: Fields to retrieve. Available fields: See WifiInformationField type.
    """
    obj = WifiInformation(wifiinformation_id)
    return obj.api_get(fields=fields)
