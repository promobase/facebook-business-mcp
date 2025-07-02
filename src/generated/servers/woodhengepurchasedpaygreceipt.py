"""WoodhengePurchasedPAYGReceipt MCP Server with typed wrappers."""

from facebook_business.adobjects.woodhengepurchasedpaygreceipt import WoodhengePurchasedPAYGReceipt
from fastmcp import FastMCP

from src.generated.models.woodhengepurchasedpaygreceipt import WoodhengePurchasedPAYGReceiptField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWoodhengePurchasedPAYGReceipt"
instructions = """
WoodhengePurchasedPAYGReceipt MCP Server for Facebook Business API.

Provides typed access to all WoodhengePurchasedPAYGReceipt operations.
"""

woodhengepurchasedpaygreceipt_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@woodhengepurchasedpaygreceipt_server.tool
@wrapped_fn_tool
def get_woodhengepurchasedpaygreceipt(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[WoodhengePurchasedPAYGReceiptField] = [],
) -> str:
    """Get a WoodhengePurchasedPAYGReceipt object by ID.

    Args:
        woodhengepurchasedpaygreceipt_id: The ID of the WoodhengePurchasedPAYGReceipt.
        fields: Fields to retrieve. Available fields: See WoodhengePurchasedPAYGReceiptField type.
    """
    obj = WoodhengePurchasedPAYGReceipt(woodhengepurchasedpaygreceipt_id)
    return obj.api_get(fields=fields)
