"""InstagramUser MCP Server with typed wrappers."""

from facebook_business.adobjects.instagramuser import InstagramUser
from fastmcp import FastMCP

from src.generated.models.adaccount import AdAccountField
from src.generated.models.instagramuser import (
    InstagramUserField,
    InstagramUserGetAuthorizedAdAccountsParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookInstagramUser"
instructions = """
InstagramUser MCP Server for Facebook Business API.

Provides typed access to all InstagramUser operations.
"""

instagramuser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@instagramuser_server.tool
@wrapped_fn_tool
def get_instagramuser(
    instagramuser_id: str,
    fields: list[InstagramUserField] = [],
) -> str:
    """Get a InstagramUser object by ID.

    Args:
        instagramuser_id: The ID of the InstagramUser.
        fields: Fields to retrieve. Available fields: See InstagramUserField type.
    """
    obj = InstagramUser(instagramuser_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@instagramuser_server.tool
@wrapped_fn_tool
def get_authorized_ad_accounts(
    instagramuser_id: str,
    fields: list[AdAccountField] = [],
    params: InstagramUserGetAuthorizedAdAccountsParams | dict = {},
):
    """Get Authorized Ad Accounts for this InstagramUser.

    Args:
        instagramuser_id: The ID of the InstagramUser.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See InstagramUserGetAuthorizedAdAccountsParams type.
    """
    return InstagramUser(instagramuser_id).get_authorized_ad_accounts(fields=fields, params=params)
