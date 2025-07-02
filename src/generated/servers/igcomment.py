"""IGComment MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.igcomment import IGComment
from fastmcp import FastMCP

from src.generated.models.igcomment import (
    IGCommentCreateReplyParams,
    IGCommentField,
    IGCommentUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGComment"
instructions = """
IGComment MCP Server for Facebook Business API.

Provides typed access to all IGComment operations.
"""

igcomment_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@igcomment_server.tool
@wrapped_fn_tool
def get_igcomment(
    igcomment_id: str,
    fields: list[IGCommentField] = [],
) -> str:
    """Get a IGComment object by ID.

    Args:
        igcomment_id: The ID of the IGComment.
        fields: Fields to retrieve. Available fields: See IGCommentField type.
    """
    obj = IGComment(igcomment_id)
    return obj.api_get(fields=fields)


@igcomment_server.tool
@wrapped_fn_tool
def update_igcomment(
    igcomment_id: str,
    fields: list[IGCommentField] = [],
    params: IGCommentUpdateParams | dict = {},
) -> str:
    """Update a IGComment object.

    Args:
        igcomment_id: The ID of the IGComment.
        fields: Fields to return after update. Available fields: See IGCommentField type.
        params: Parameters to update. Available params: See IGCommentUpdateParams type.
    """
    return IGComment(igcomment_id).api_update(fields=fields, params=params)


@igcomment_server.tool
@wrapped_fn_tool
def delete_igcomment(
    igcomment_id: str,
) -> str:
    """Delete a IGComment object.

    Args:
        igcomment_id: The ID of the IGComment.
    """
    return IGComment(igcomment_id).api_delete()


# ---- Edge Methods (1) ----
@igcomment_server.tool
@wrapped_fn_tool
def create_reply(
    igcomment_id: str,
    fields: list[str] = [],
    params: IGCommentCreateReplyParams | dict = {},
):
    """Create Reply for this IGComment.

    Args:
        igcomment_id: The ID of the IGComment.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGCommentCreateReplyParams type.
    """
    return IGComment(igcomment_id).create_reply(fields=fields, params=params)
