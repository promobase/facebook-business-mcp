"""BrandSafetyDownloadable MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.brandsafetydownloadable import BrandSafetyDownloadable
from fastmcp import FastMCP

from src.generated.models.brandsafetydownloadable import BrandSafetyDownloadableField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBrandSafetyDownloadable"
instructions = """
BrandSafetyDownloadable MCP Server for Facebook Business API.

Provides typed access to all BrandSafetyDownloadable operations.
"""

brandsafetydownloadable_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@brandsafetydownloadable_server.tool
@wrapped_fn_tool
def get_brandsafetydownloadable(
    brandsafetydownloadable_id: str,
    fields: list[BrandSafetyDownloadableField] = [],
) -> str:
    """Get a BrandSafetyDownloadable object by ID.

    Args:
        brandsafetydownloadable_id: The ID of the BrandSafetyDownloadable.
        fields: Fields to retrieve. Available fields: See BrandSafetyDownloadableField type.
    """
    obj = BrandSafetyDownloadable(brandsafetydownloadable_id)
    return obj.api_get(fields=fields)
