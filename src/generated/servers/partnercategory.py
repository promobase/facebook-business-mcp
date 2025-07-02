"""PartnerCategory MCP Server."""

from typing import Any

from facebook_business.adobjects.partnercategory import PartnerCategory
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPartnerCategory"
instructions = """
PartnerCategory MCP Server for Facebook Business API.

Provides typed access to all PartnerCategory operations.
"""

partnercategory_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@partnercategory_server.tool
@wrapped_fn_tool
def get_endpoint(
    partnercategory_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PartnerCategory(partnercategory_id).get_endpoint(fields=fields, params=params)
