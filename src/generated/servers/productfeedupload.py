"""ProductFeedUpload MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productfeedupload import ProductFeedUpload
from fastmcp import FastMCP

from src.generated.models.productfeedupload import (
    ProductFeedUploadField,
    ProductFeedUploadGetErrorsParams,
)
from src.generated.models.productfeeduploaderror import ProductFeedUploadErrorField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductFeedUpload"
instructions = """
ProductFeedUpload MCP Server for Facebook Business API.

Provides typed access to all ProductFeedUpload operations.
"""

productfeedupload_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productfeedupload_server.tool
@wrapped_fn_tool
def get_productfeedupload(
    productfeedupload_id: str,
    fields: list[ProductFeedUploadField] = [],
) -> str:
    """Get a ProductFeedUpload object by ID.

    Args:
        productfeedupload_id: The ID of the ProductFeedUpload.
        fields: Fields to retrieve. Available fields: See ProductFeedUploadField type.
    """
    obj = ProductFeedUpload(productfeedupload_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@productfeedupload_server.tool
@wrapped_fn_tool
def get_errors(
    productfeedupload_id: str,
    fields: list[ProductFeedUploadErrorField] = [],
    params: ProductFeedUploadGetErrorsParams | dict = {},
):
    """Get Errors for this ProductFeedUpload.

    Args:
        productfeedupload_id: The ID of the ProductFeedUpload.
        fields: Fields to retrieve. Available fields: See ProductFeedUploadErrorField type.
        params: Query parameters. Available params: See ProductFeedUploadGetErrorsParams type.
    """
    return ProductFeedUpload(productfeedupload_id).get_errors(fields=fields, params=params)
