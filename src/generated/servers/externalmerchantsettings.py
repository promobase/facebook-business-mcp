"""ExternalMerchantSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.externalmerchantsettings import ExternalMerchantSettings
from fastmcp import FastMCP

from src.generated.models.externalmerchantsettings import ExternalMerchantSettingsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookExternalMerchantSettings"
instructions = """
ExternalMerchantSettings MCP Server for Facebook Business API.

Provides typed access to all ExternalMerchantSettings operations.
"""

externalmerchantsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@externalmerchantsettings_server.tool
@wrapped_fn_tool
def get_externalmerchantsettings(
    externalmerchantsettings_id: str,
    fields: list[ExternalMerchantSettingsField] = [],
) -> str:
    """Get a ExternalMerchantSettings object by ID.

    Args:
        externalmerchantsettings_id: The ID of the ExternalMerchantSettings.
        fields: Fields to retrieve. Available fields: See ExternalMerchantSettingsField type.
    """
    obj = ExternalMerchantSettings(externalmerchantsettings_id)
    return obj.api_get(fields=fields)
