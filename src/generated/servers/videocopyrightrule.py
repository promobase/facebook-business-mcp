"""VideoCopyrightRule MCP Server with typed wrappers."""

from facebook_business.adobjects.videocopyrightrule import VideoCopyrightRule
from fastmcp import FastMCP

from src.generated.models.videocopyrightrule import VideoCopyrightRuleField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoCopyrightRule"
instructions = """
VideoCopyrightRule MCP Server for Facebook Business API.

Provides typed access to all VideoCopyrightRule operations.
"""

videocopyrightrule_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@videocopyrightrule_server.tool
@wrapped_fn_tool
def get_videocopyrightrule(
    videocopyrightrule_id: str,
    fields: list[VideoCopyrightRuleField] = [],
) -> str:
    """Get a VideoCopyrightRule object by ID.

    Args:
        videocopyrightrule_id: The ID of the VideoCopyrightRule.
        fields: Fields to retrieve. Available fields: See VideoCopyrightRuleField type.
    """
    obj = VideoCopyrightRule(videocopyrightrule_id)
    return obj.api_get(fields=fields)
