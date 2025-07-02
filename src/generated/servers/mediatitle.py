"""MediaTitle MCP Server with typed wrappers."""

from facebook_business.adobjects.mediatitle import MediaTitle
from fastmcp import FastMCP

from src.generated.models.mediatitle import (
    MediaTitleField,
    MediaTitleGetOverrideDetailsParams,
    MediaTitleUpdateParams,
)
from src.generated.models.overridedetails import OverrideDetailsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMediaTitle"
instructions = """
MediaTitle MCP Server for Facebook Business API.

Provides typed access to all MediaTitle operations.
"""

mediatitle_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@mediatitle_server.tool
@wrapped_fn_tool
def get_mediatitle(
    mediatitle_id: str,
    fields: list[MediaTitleField] = [],
) -> str:
    """Get a MediaTitle object by ID.

    Args:
        mediatitle_id: The ID of the MediaTitle.
        fields: Fields to retrieve. Available fields: See MediaTitleField type.
    """
    obj = MediaTitle(mediatitle_id)
    return obj.api_get(fields=fields)


@mediatitle_server.tool
@wrapped_fn_tool
def update_mediatitle(
    mediatitle_id: str,
    fields: list[MediaTitleField] = [],
    params: MediaTitleUpdateParams | dict = {},
) -> str:
    """Update a MediaTitle object.

    Args:
        mediatitle_id: The ID of the MediaTitle.
        fields: Fields to return after update. Available fields: See MediaTitleField type.
        params: Parameters to update. Available params: See MediaTitleUpdateParams type.
    """
    return MediaTitle(mediatitle_id).api_update(fields=fields, params=params)


@mediatitle_server.tool
@wrapped_fn_tool
def delete_mediatitle(
    mediatitle_id: str,
) -> str:
    """Delete a MediaTitle object.

    Args:
        mediatitle_id: The ID of the MediaTitle.
    """
    return MediaTitle(mediatitle_id).api_delete()


# ---- Edge Methods (1) ----
@mediatitle_server.tool
@wrapped_fn_tool
def get_override_details(
    mediatitle_id: str,
    fields: list[OverrideDetailsField] = [],
    params: MediaTitleGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this MediaTitle.

    Args:
        mediatitle_id: The ID of the MediaTitle.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See MediaTitleGetOverrideDetailsParams type.
    """
    return MediaTitle(mediatitle_id).get_override_details(fields=fields, params=params)
