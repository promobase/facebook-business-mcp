from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from src.generated.models.adaccount import AdAccountField
from src.utils import wrapped_fn_tool

server_name = "FacebookAdAccount"
instructions = """
AdAccount MCP Server for Facebook Business API.

Provides typed access to all AdAccount operations.
"""

adaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adaccount_server.tool
@wrapped_fn_tool
def get_adaccount(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get a AdAccount object by ID.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
    """
    obj = AdAccount(adaccount_id)
    return obj.api_get(fields=fields, params=params)
