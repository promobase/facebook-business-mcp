"""ProductFeedUploadErrorSample MCP Server."""

from typing import Any

from facebook_business.adobjects.productfeeduploaderrorsample import ProductFeedUploadErrorSample
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductFeedUploadErrorSample"
instructions = """
ProductFeedUploadErrorSample MCP Server for Facebook Business API.

Provides typed access to all ProductFeedUploadErrorSample operations.
"""

productfeeduploaderrorsample_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productfeeduploaderrorsample_server.tool
@wrapped_fn_tool
def get_productfeeduploaderrorsample(
    productfeeduploaderrorsample_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductFeedUploadErrorSample(productfeeduploaderrorsample_id)
    return obj.api_get(fields=fields)
