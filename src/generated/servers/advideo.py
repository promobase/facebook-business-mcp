"""Streamlined AdVideo MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.advideo import AdVideo
from fastmcp import FastMCP

from src.generated.models.advideo import AdVideoField, AdVideoUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdVideo"
instructions = """
AdVideo MCP Server for Facebook Business API.

Provides typed access to all AdVideo operations.
"""

advideo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_advideo(
    advideo_id: str,
    fields: list[AdVideoField] = [],
) -> str:
    """Get a AdVideo object by ID.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
    """
    obj = AdVideo(advideo_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_advideo(
    advideo_id: str,
    fields: list[AdVideoField] = [],
    params: AdVideoUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdVideo object.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdVideo(advideo_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_advideo(
    advideo_id: str,
) -> str:
    """Delete a AdVideo object.

    Args:
        advideo_id: The ID of the AdVideo.
    """
    return AdVideo(advideo_id).api_delete()


# ---- Edge Methods (9) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.advideo_wrappers import (
    create_cap_t_i_on,
    create_collaborator,
    create_comment,
    create_gaming_clip_create,
    create_like,
    create_poll,
    create_thumbnail,
    get_comments,
    get_video_insights,
)

# ---- Register tools ----
# Register CRUD operations
advideo_server.tool(get_advideo)
advideo_server.tool(update_advideo)
advideo_server.tool(delete_advideo)

# Register edge methods from wrappers
advideo_server.tool(create_cap_t_i_on)
advideo_server.tool(create_collaborator)
advideo_server.tool(get_comments)
advideo_server.tool(create_comment)
advideo_server.tool(create_gaming_clip_create)
advideo_server.tool(create_like)
advideo_server.tool(create_poll)
advideo_server.tool(create_thumbnail)
advideo_server.tool(get_video_insights)
