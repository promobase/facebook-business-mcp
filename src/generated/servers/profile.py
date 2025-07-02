"""Profile MCP Server with typed wrappers."""

from facebook_business.adobjects.profile import Profile
from fastmcp import FastMCP

from src.generated.models.profile import ProfileField, ProfileGetPictureParams
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProfile"
instructions = """
Profile MCP Server for Facebook Business API.

Provides typed access to all Profile operations.
"""

profile_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@profile_server.tool
@wrapped_fn_tool
def get_profile(
    profile_id: str,
    fields: list[ProfileField] = [],
) -> str:
    """Get a Profile object by ID.

    Args:
        profile_id: The ID of the Profile.
        fields: Fields to retrieve. Available fields: See ProfileField type.
    """
    obj = Profile(profile_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@profile_server.tool
@wrapped_fn_tool
def get_picture(
    profile_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: ProfileGetPictureParams | dict = {},
):
    """Get Picture for this Profile.

    Args:
        profile_id: The ID of the Profile.
        fields: Fields to retrieve. Available fields: See ProfilePictureSourceField type.
        params: Query parameters. Available params: See ProfileGetPictureParams type.
    """
    return Profile(profile_id).get_picture(fields=fields, params=params)
