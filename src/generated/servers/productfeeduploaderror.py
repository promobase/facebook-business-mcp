"""ProductFeedUploadError MCP Server."""

from typing import Any

from facebook_business.adobjects.productfeeduploaderror import ProductFeedUploadError
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductFeedUploadError"
instructions = """
ProductFeedUploadError MCP Server for Facebook Business API.

Provides typed access to all ProductFeedUploadError operations.
"""

productfeeduploaderror_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productfeeduploaderror_server.tool
@wrapped_fn_tool
def get_productfeeduploaderror(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductFeedUploadError(productfeeduploaderror_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@productfeeduploaderror_server.tool
@wrapped_fn_tool
def get_samples(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeedUploadError(productfeeduploaderror_id).get_samples(
        fields=fields, params=params
    )


@productfeeduploaderror_server.tool
@wrapped_fn_tool
def get_suggested_rules(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeedUploadError(productfeeduploaderror_id).get_suggested_rules(
        fields=fields, params=params
    )
