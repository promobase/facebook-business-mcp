"""Link MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.link import Link
from fastmcp import FastMCP

from src.generated.models.comment import CommentField
from src.generated.models.link import LinkCreateCommentParams, LinkField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLink"
instructions = """
Link MCP Server for Facebook Business API.

Provides typed access to all Link operations.
"""

link_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@link_server.tool
@wrapped_fn_tool
def get_link(
    link_id: str,
    fields: list[LinkField] = [],
) -> str:
    """Get a Link object by ID.

    Args:
        link_id: The ID of the Link.
        fields: Fields to retrieve. Available fields: See LinkField type.
    """
    obj = Link(link_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@link_server.tool
@wrapped_fn_tool
def create_comment(
    link_id: str,
    fields: list[str] = [],
    params: LinkCreateCommentParams | dict = {},
):
    """Create Comment for this Link.

    Args:
        link_id: The ID of the Link.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See LinkCreateCommentParams type.
    """
    return Link(link_id).create_comment(fields=fields, params=params)
