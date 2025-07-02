"""WhitehatFBDLRun MCP Server with typed wrappers."""

from facebook_business.adobjects.whitehatfbdlrun import WhitehatFBDLRun
from fastmcp import FastMCP

from src.generated.models.whitehatfbdlrun import WhitehatFBDLRunField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWhitehatFBDLRun"
instructions = """
WhitehatFBDLRun MCP Server for Facebook Business API.

Provides typed access to all WhitehatFBDLRun operations.
"""

whitehatfbdlrun_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@whitehatfbdlrun_server.tool
@wrapped_fn_tool
def get_whitehatfbdlrun(
    whitehatfbdlrun_id: str,
    fields: list[WhitehatFBDLRunField] = [],
) -> str:
    """Get a WhitehatFBDLRun object by ID.

    Args:
        whitehatfbdlrun_id: The ID of the WhitehatFBDLRun.
        fields: Fields to retrieve. Available fields: See WhitehatFBDLRunField type.
    """
    obj = WhitehatFBDLRun(whitehatfbdlrun_id)
    return obj.api_get(fields=fields)
