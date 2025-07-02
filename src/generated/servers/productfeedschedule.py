"""ProductFeedSchedule MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productfeedschedule import ProductFeedSchedule
from fastmcp import FastMCP

from src.generated.models.productfeedschedule import ProductFeedScheduleField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductFeedSchedule"
instructions = """
ProductFeedSchedule MCP Server for Facebook Business API.

Provides typed access to all ProductFeedSchedule operations.
"""

productfeedschedule_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productfeedschedule_server.tool
@wrapped_fn_tool
def get_productfeedschedule(
    productfeedschedule_id: str,
    fields: list[ProductFeedScheduleField] = [],
) -> str:
    """Get a ProductFeedSchedule object by ID.

    Args:
        productfeedschedule_id: The ID of the ProductFeedSchedule.
        fields: Fields to retrieve. Available fields: See ProductFeedScheduleField type.
    """
    obj = ProductFeedSchedule(productfeedschedule_id)
    return obj.api_get(fields=fields)
