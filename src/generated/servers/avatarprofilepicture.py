"""AvatarProfilePicture MCP Server with typed wrappers."""

from facebook_business.adobjects.avatarprofilepicture import AvatarProfilePicture
from fastmcp import FastMCP

from src.generated.models.avatarprofilepicture import AvatarProfilePictureField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAvatarProfilePicture"
instructions = """
AvatarProfilePicture MCP Server for Facebook Business API.

Provides typed access to all AvatarProfilePicture operations.
"""

avatarprofilepicture_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@avatarprofilepicture_server.tool
@wrapped_fn_tool
def get_avatarprofilepicture(
    avatarprofilepicture_id: str,
    fields: list[AvatarProfilePictureField] = [],
) -> str:
    """Get a AvatarProfilePicture object by ID.

    Args:
        avatarprofilepicture_id: The ID of the AvatarProfilePicture.
        fields: Fields to retrieve. Available fields: See AvatarProfilePictureField type.
    """
    obj = AvatarProfilePicture(avatarprofilepicture_id)
    return obj.api_get(fields=fields)
