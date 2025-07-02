"""ALMAdAccountInfo MCP Server with typed wrappers."""

from facebook_business.adobjects.almadaccountinfo import ALMAdAccountInfo
from fastmcp import FastMCP

from src.generated.models.almadaccountinfo import ALMAdAccountInfoField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookALMAdAccountInfo"
instructions = """
ALMAdAccountInfo MCP Server for Facebook Business API.

Provides typed access to all ALMAdAccountInfo operations.
"""

almadaccountinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@almadaccountinfo_server.tool
@wrapped_fn_tool
def get_almadaccountinfo(
    almadaccountinfo_id: str,
    fields: list[ALMAdAccountInfoField] = [],
) -> str:
    """Get a ALMAdAccountInfo object by ID.

    Args:
        almadaccountinfo_id: The ID of the ALMAdAccountInfo.
        fields: Fields to retrieve. Available fields: See ALMAdAccountInfoField type.
    """
    obj = ALMAdAccountInfo(almadaccountinfo_id)
    return obj.api_get(fields=fields)
