"""ProductCatalogLocalizationSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.productcataloglocalizationsettings import (
    ProductCatalogLocalizationSettings,
)
from fastmcp import FastMCP

from src.generated.models.productcataloglocalizationsettings import (
    ProductCatalogLocalizationSettingsField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductCatalogLocalizationSettings"
instructions = """
ProductCatalogLocalizationSettings MCP Server for Facebook Business API.

Provides typed access to all ProductCatalogLocalizationSettings operations.
"""

productcataloglocalizationsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productcataloglocalizationsettings_server.tool
@wrapped_fn_tool
def get_productcataloglocalizationsettings(
    productcataloglocalizationsettings_id: str,
    fields: list[ProductCatalogLocalizationSettingsField] = [],
) -> str:
    """Get a ProductCatalogLocalizationSettings object by ID.

    Args:
        productcataloglocalizationsettings_id: The ID of the ProductCatalogLocalizationSettings.
        fields: Fields to retrieve. Available fields: See ProductCatalogLocalizationSettingsField type.
    """
    obj = ProductCatalogLocalizationSettings(productcataloglocalizationsettings_id)
    return obj.api_get(fields=fields)
