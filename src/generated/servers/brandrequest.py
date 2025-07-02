"""BrandRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.brandrequest import BrandRequest
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBrandRequest"
instructions = """
BrandRequest MCP Server for Facebook Business API.

Provides typed access to all BrandRequest operations.
"""

brandrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@brandrequest_server.tool
@wrapped_fn_tool
def get_brandrequest(
    brandrequest_id: str,
    fields: list[str] = [],
) -> str:
    obj = BrandRequest(brandrequest_id)
    return obj.api_get(fields=fields)
