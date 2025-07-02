"""OfflineConversionDataSetUpload MCP Server."""

from typing import Any

from facebook_business.adobjects.offlineconversiondatasetupload import (
    OfflineConversionDataSetUpload,
)
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = OfflineConversionDataSetUpload(offlineconversiondatasetupload_id)
    return obj.api_get(fields=fields)
