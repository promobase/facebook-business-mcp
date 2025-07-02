"""ImageCopyright MCP Server."""

from typing import Any

from facebook_business.adobjects.imagecopyright import ImageCopyright
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ImageCopyright(imagecopyright_id)
    return obj.api_get(fields=fields)


@imagecopyright_server.tool
@wrapped_fn_tool
def update_imagecopyright(
    imagecopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ImageCopyright(imagecopyright_id).api_update(fields=fields, params=params)
