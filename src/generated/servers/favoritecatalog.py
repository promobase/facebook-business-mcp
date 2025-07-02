"""FavoriteCatalog MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.favoritecatalog import FavoriteCatalog
from fastmcp import FastMCP

from src.generated.models.favoritecatalog import FavoriteCatalogField
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
    fields: list[FavoriteCatalogField] = [],
) -> str:
    """Get a FavoriteCatalog object by ID.

    Args:
        favoritecatalog_id: The ID of the FavoriteCatalog.
        fields: Fields to retrieve. Available fields: See FavoriteCatalogField type.
    """
    obj = FavoriteCatalog(favoritecatalog_id)
    return obj.api_get(fields=fields)
