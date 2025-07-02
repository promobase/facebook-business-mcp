"""OfflineConversionDataSetUpload MCP Server with typed wrappers."""

from facebook_business.adobjects.offlineconversiondatasetupload import (
    OfflineConversionDataSetUpload,
)
from fastmcp import FastMCP

from src.generated.models.offlineconversiondatasetupload import OfflineConversionDataSetUploadField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOfflineConversionDataSetUpload"
instructions = """
OfflineConversionDataSetUpload MCP Server for Facebook Business API.

Provides typed access to all OfflineConversionDataSetUpload operations.
"""

offlineconversiondatasetupload_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offlineconversiondatasetupload_server.tool
@wrapped_fn_tool
def get_offlineconversiondatasetupload(
    offlineconversiondatasetupload_id: str,
    fields: list[OfflineConversionDataSetUploadField] = [],
) -> str:
    """Get a OfflineConversionDataSetUpload object by ID.

    Args:
        offlineconversiondatasetupload_id: The ID of the OfflineConversionDataSetUpload.
        fields: Fields to retrieve. Available fields: See OfflineConversionDataSetUploadField type.
    """
    obj = OfflineConversionDataSetUpload(offlineconversiondatasetupload_id)
    return obj.api_get(fields=fields)
