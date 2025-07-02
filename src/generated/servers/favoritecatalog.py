"""FavoriteCatalog MCP Server."""

from typing import Any

from facebook_business.adobjects.favoritecatalog import FavoriteCatalog
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFavoriteCatalog"
instructions = """
FavoriteCatalog MCP Server for Facebook Business API.

Provides typed access to all FavoriteCatalog operations.
"""

favoritecatalog_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@favoritecatalog_server.tool
@wrapped_fn_tool
def get_favoritecatalog(
    favoritecatalog_id: str,
    fields: list[str] = [],
) -> str:
    obj = FavoriteCatalog(favoritecatalog_id)
    return obj.api_get(fields=fields)
