"""ImageCopyright MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.imagecopyright import ImageCopyright
from fastmcp import FastMCP

from src.generated.models.imagecopyright import ImageCopyrightField, ImageCopyrightUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookImageCopyright"
instructions = """
ImageCopyright MCP Server for Facebook Business API.

Provides typed access to all ImageCopyright operations.
"""

imagecopyright_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@imagecopyright_server.tool
@wrapped_fn_tool
def get_imagecopyright(
    imagecopyright_id: str,
    fields: list[ImageCopyrightField] = [],
) -> str:
    """Get a ImageCopyright object by ID.

    Args:
        imagecopyright_id: The ID of the ImageCopyright.
        fields: Fields to retrieve. Available fields: See ImageCopyrightField type.
    """
    obj = ImageCopyright(imagecopyright_id)
    return obj.api_get(fields=fields)


@imagecopyright_server.tool
@wrapped_fn_tool
def update_imagecopyright(
    imagecopyright_id: str,
    fields: list[ImageCopyrightField] = [],
    params: ImageCopyrightUpdateParams | dict = {},
) -> str:
    """Update a ImageCopyright object.

    Args:
        imagecopyright_id: The ID of the ImageCopyright.
        fields: Fields to return after update. Available fields: See ImageCopyrightField type.
        params: Parameters to update. Available params: See ImageCopyrightUpdateParams type.
    """
    return ImageCopyright(imagecopyright_id).api_update(fields=fields, params=params)
