"""ShadowIGHashtag MCP Server with typed wrappers."""

from facebook_business.adobjects.shadowighashtag import ShadowIGHashtag
from fastmcp import FastMCP

from src.generated.models.igmedia import IGMediaField
from src.generated.models.shadowighashtag import (
    ShadowIGHashtagField,
    ShadowIGHashtagGetRecentMediaParams,
    ShadowIGHashtagGetTopMediaParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookShadowIGHashtag"
instructions = """
ShadowIGHashtag MCP Server for Facebook Business API.

Provides typed access to all ShadowIGHashtag operations.
"""

shadowighashtag_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@shadowighashtag_server.tool
@wrapped_fn_tool
def get_shadowighashtag(
    shadowighashtag_id: str,
    fields: list[ShadowIGHashtagField] = [],
) -> str:
    """Get a ShadowIGHashtag object by ID.

    Args:
        shadowighashtag_id: The ID of the ShadowIGHashtag.
        fields: Fields to retrieve. Available fields: See ShadowIGHashtagField type.
    """
    obj = ShadowIGHashtag(shadowighashtag_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@shadowighashtag_server.tool
@wrapped_fn_tool
def get_recent_media(
    shadowighashtag_id: str,
    fields: list[IGMediaField] = [],
    params: ShadowIGHashtagGetRecentMediaParams | dict = {},
):
    """Get Recent Media for this ShadowIGHashtag.

    Args:
        shadowighashtag_id: The ID of the ShadowIGHashtag.
        fields: Fields to retrieve. Available fields: See IGMediaField type.
        params: Query parameters. Available params: See ShadowIGHashtagGetRecentMediaParams type.
    """
    return ShadowIGHashtag(shadowighashtag_id).get_recent_media(fields=fields, params=params)


@shadowighashtag_server.tool
@wrapped_fn_tool
def get_top_media(
    shadowighashtag_id: str,
    fields: list[IGMediaField] = [],
    params: ShadowIGHashtagGetTopMediaParams | dict = {},
):
    """Get Top Media for this ShadowIGHashtag.

    Args:
        shadowighashtag_id: The ID of the ShadowIGHashtag.
        fields: Fields to retrieve. Available fields: See IGMediaField type.
        params: Query parameters. Available params: See ShadowIGHashtagGetTopMediaParams type.
    """
    return ShadowIGHashtag(shadowighashtag_id).get_top_media(fields=fields, params=params)
