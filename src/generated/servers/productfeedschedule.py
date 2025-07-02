"""ProductFeedSchedule MCP Server."""

from typing import Any

from facebook_business.adobjects.productfeedschedule import ProductFeedSchedule
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ProductFeedSchedule(productfeedschedule_id)
    return obj.api_get(fields=fields)
