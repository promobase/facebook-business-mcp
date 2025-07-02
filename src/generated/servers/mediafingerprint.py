"""MediaFingerprint MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.mediafingerprint import MediaFingerprint
from fastmcp import FastMCP

from src.generated.models.mediafingerprint import (
    MediaFingerprintField,
    MediaFingerprintUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMediaFingerprint"
instructions = """
MediaFingerprint MCP Server for Facebook Business API.

Provides typed access to all MediaFingerprint operations.
"""

mediafingerprint_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@mediafingerprint_server.tool
@wrapped_fn_tool
def get_mediafingerprint(
    mediafingerprint_id: str,
    fields: list[MediaFingerprintField] = [],
) -> str:
    """Get a MediaFingerprint object by ID.

    Args:
        mediafingerprint_id: The ID of the MediaFingerprint.
        fields: Fields to retrieve. Available fields: See MediaFingerprintField type.
    """
    obj = MediaFingerprint(mediafingerprint_id)
    return obj.api_get(fields=fields)


@mediafingerprint_server.tool
@wrapped_fn_tool
def update_mediafingerprint(
    mediafingerprint_id: str,
    fields: list[MediaFingerprintField] = [],
    params: MediaFingerprintUpdateParams | dict = {},
) -> str:
    """Update a MediaFingerprint object.

    Args:
        mediafingerprint_id: The ID of the MediaFingerprint.
        fields: Fields to return after update. Available fields: See MediaFingerprintField type.
        params: Parameters to update. Available params: See MediaFingerprintUpdateParams type.
    """
    return MediaFingerprint(mediafingerprint_id).api_update(fields=fields, params=params)
