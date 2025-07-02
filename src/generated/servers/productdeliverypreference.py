"""ProductDeliveryPreference MCP Server."""

from typing import Any

from facebook_business.adobjects.productdeliverypreference import ProductDeliveryPreference
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ProductDeliveryPreference(productdeliverypreference_id)
    return obj.api_get(fields=fields)
