"""CopyrightOwnershipTransfer MCP Server with typed wrappers."""

from facebook_business.adobjects.copyrightownershiptransfer import CopyrightOwnershipTransfer
from fastmcp import FastMCP

from src.generated.models.copyrightownershiptransfer import CopyrightOwnershipTransferField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCopyrightOwnershipTransfer"
instructions = """
CopyrightOwnershipTransfer MCP Server for Facebook Business API.

Provides typed access to all CopyrightOwnershipTransfer operations.
"""

copyrightownershiptransfer_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@copyrightownershiptransfer_server.tool
@wrapped_fn_tool
def get_copyrightownershiptransfer(
    copyrightownershiptransfer_id: str,
    fields: list[CopyrightOwnershipTransferField] = [],
) -> str:
    """Get a CopyrightOwnershipTransfer object by ID.

    Args:
        copyrightownershiptransfer_id: The ID of the CopyrightOwnershipTransfer.
        fields: Fields to retrieve. Available fields: See CopyrightOwnershipTransferField type.
    """
    obj = CopyrightOwnershipTransfer(copyrightownershiptransfer_id)
    return obj.api_get(fields=fields)
