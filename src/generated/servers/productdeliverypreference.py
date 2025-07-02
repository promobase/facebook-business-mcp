"""ProductDeliveryPreference MCP Server with typed wrappers."""

from facebook_business.adobjects.productdeliverypreference import ProductDeliveryPreference
from fastmcp import FastMCP

from src.generated.models.productdeliverypreference import ProductDeliveryPreferenceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductDeliveryPreference"
instructions = """
ProductDeliveryPreference MCP Server for Facebook Business API.

Provides typed access to all ProductDeliveryPreference operations.
"""

productdeliverypreference_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productdeliverypreference_server.tool
@wrapped_fn_tool
def get_productdeliverypreference(
    productdeliverypreference_id: str,
    fields: list[ProductDeliveryPreferenceField] = [],
) -> str:
    """Get a ProductDeliveryPreference object by ID.

    Args:
        productdeliverypreference_id: The ID of the ProductDeliveryPreference.
        fields: Fields to retrieve. Available fields: See ProductDeliveryPreferenceField type.
    """
    obj = ProductDeliveryPreference(productdeliverypreference_id)
    return obj.api_get(fields=fields)
