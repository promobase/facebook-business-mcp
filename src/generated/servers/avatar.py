"""Avatar MCP Server with typed wrappers."""

from facebook_business.adobjects.avatar import Avatar
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.avatar import AvatarField, AvatarGetModelsParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAvatar"
instructions = """
Avatar MCP Server for Facebook Business API.

Provides typed access to all Avatar operations.
"""

avatar_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@avatar_server.tool
@wrapped_fn_tool
def get_avatar(
    avatar_id: str,
    fields: list[AvatarField] = [],
) -> str:
    """Get a Avatar object by ID.

    Args:
        avatar_id: The ID of the Avatar.
        fields: Fields to retrieve. Available fields: See AvatarField type.
    """
    obj = Avatar(avatar_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@avatar_server.tool
@wrapped_fn_tool
def get_models(
    avatar_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: AvatarGetModelsParams | dict = {},
):
    """Get Models for this Avatar.

    Args:
        avatar_id: The ID of the Avatar.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See AvatarGetModelsParams type.
    """
    return Avatar(avatar_id).get_models(fields=fields, params=params)
