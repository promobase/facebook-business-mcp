"""ProductFeedUploadError MCP Server with typed wrappers."""

from facebook_business.adobjects.productfeeduploaderror import ProductFeedUploadError
from fastmcp import FastMCP

from src.generated.models.productfeeduploaderror import ProductFeedUploadErrorField
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
    fields: list[ProductFeedUploadErrorField] = [],
) -> str:
    """Get a ProductFeedUploadError object by ID.

    Args:
        productfeeduploaderror_id: The ID of the ProductFeedUploadError.
        fields: Fields to retrieve. Available fields: See ProductFeedUploadErrorField type.
    """
    obj = ProductFeedUploadError(productfeeduploaderror_id)
    return obj.api_get(fields=fields)
