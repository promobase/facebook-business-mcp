"""MediaCopyrightUpdateRecord MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.mediacopyrightupdaterecord import MediaCopyrightUpdateRecord
from fastmcp import FastMCP

from src.generated.models.mediacopyrightupdaterecord import MediaCopyrightUpdateRecordField
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
    fields: list[MediaCopyrightUpdateRecordField] = [],
) -> str:
    """Get a MediaCopyrightUpdateRecord object by ID.

    Args:
        mediacopyrightupdaterecord_id: The ID of the MediaCopyrightUpdateRecord.
        fields: Fields to retrieve. Available fields: See MediaCopyrightUpdateRecordField type.
    """
    obj = MediaCopyrightUpdateRecord(mediacopyrightupdaterecord_id)
    return obj.api_get(fields=fields)
