"""RTBDynamicPost MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.rtbdynamicpost import RTBDynamicPost
from fastmcp import FastMCP

from src.generated.models.comment import CommentField
from src.generated.models.rtbdynamicpost import RTBDynamicPostField, RTBDynamicPostGetCommentsParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookRTBDynamicPost"
instructions = """
RTBDynamicPost MCP Server for Facebook Business API.

Provides typed access to all RTBDynamicPost operations.
"""

rtbdynamicpost_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@rtbdynamicpost_server.tool
@wrapped_fn_tool
def get_rtbdynamicpost(
    rtbdynamicpost_id: str,
    fields: list[RTBDynamicPostField] = [],
) -> str:
    """Get a RTBDynamicPost object by ID.

    Args:
        rtbdynamicpost_id: The ID of the RTBDynamicPost.
        fields: Fields to retrieve. Available fields: See RTBDynamicPostField type.
    """
    obj = RTBDynamicPost(rtbdynamicpost_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@rtbdynamicpost_server.tool
@wrapped_fn_tool
def get_comments(
    rtbdynamicpost_id: str,
    fields: list[CommentField] = [],
    params: RTBDynamicPostGetCommentsParams | dict = {},
):
    """Get Comments for this RTBDynamicPost.

    Args:
        rtbdynamicpost_id: The ID of the RTBDynamicPost.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See RTBDynamicPostGetCommentsParams type.
    """
    return RTBDynamicPost(rtbdynamicpost_id).get_comments(fields=fields, params=params)
