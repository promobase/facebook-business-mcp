"""AdAccountUserSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.adaccountusersettings import AdAccountUserSettings
from fastmcp import FastMCP

from src.generated.models.adaccountusersettings import AdAccountUserSettingsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountUserSettings"
instructions = """
AdAccountUserSettings MCP Server for Facebook Business API.

Provides typed access to all AdAccountUserSettings operations.
"""

adaccountusersettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adaccountusersettings_server.tool
@wrapped_fn_tool
def get_adaccountusersettings(
    adaccountusersettings_id: str,
    fields: list[AdAccountUserSettingsField] = [],
) -> str:
    """Get a AdAccountUserSettings object by ID.

    Args:
        adaccountusersettings_id: The ID of the AdAccountUserSettings.
        fields: Fields to retrieve. Available fields: See AdAccountUserSettingsField type.
    """
    obj = AdAccountUserSettings(adaccountusersettings_id)
    return obj.api_get(fields=fields)
