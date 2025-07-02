"""MediaCopyrightUpdateRecord MCP Server."""

from typing import Any

from facebook_business.adobjects.mediacopyrightupdaterecord import MediaCopyrightUpdateRecord
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMediaCopyrightUpdateRecord"
instructions = """
MediaCopyrightUpdateRecord MCP Server for Facebook Business API.

Provides typed access to all MediaCopyrightUpdateRecord operations.
"""

mediacopyrightupdaterecord_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@mediacopyrightupdaterecord_server.tool
@wrapped_fn_tool
def get_mediacopyrightupdaterecord(
    mediacopyrightupdaterecord_id: str,
    fields: list[str] = [],
) -> str:
    obj = MediaCopyrightUpdateRecord(mediacopyrightupdaterecord_id)
    return obj.api_get(fields=fields)
