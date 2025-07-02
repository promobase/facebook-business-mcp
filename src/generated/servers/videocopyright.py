"""VideoCopyright MCP Server with typed wrappers."""

from facebook_business.adobjects.videocopyright import VideoCopyright
from fastmcp import FastMCP

from src.generated.models.videocopyright import VideoCopyrightField, VideoCopyrightUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoCopyright"
instructions = """
VideoCopyright MCP Server for Facebook Business API.

Provides typed access to all VideoCopyright operations.
"""

videocopyright_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@videocopyright_server.tool
@wrapped_fn_tool
def get_videocopyright(
    videocopyright_id: str,
    fields: list[VideoCopyrightField] = [],
) -> str:
    """Get a VideoCopyright object by ID.

    Args:
        videocopyright_id: The ID of the VideoCopyright.
        fields: Fields to retrieve. Available fields: See VideoCopyrightField type.
    """
    obj = VideoCopyright(videocopyright_id)
    return obj.api_get(fields=fields)


@videocopyright_server.tool
@wrapped_fn_tool
def update_videocopyright(
    videocopyright_id: str,
    fields: list[VideoCopyrightField] = [],
    params: VideoCopyrightUpdateParams | dict = {},
) -> str:
    """Update a VideoCopyright object.

    Args:
        videocopyright_id: The ID of the VideoCopyright.
        fields: Fields to return after update. Available fields: See VideoCopyrightField type.
        params: Parameters to update. Available params: See VideoCopyrightUpdateParams type.
    """
    return VideoCopyright(videocopyright_id).api_update(fields=fields, params=params)
