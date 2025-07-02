"""DynamicARMetadata MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.dynamicarmetadata import DynamicARMetadata
from fastmcp import FastMCP

from src.generated.models.dynamicarmetadata import DynamicARMetadataField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicARMetadata"
instructions = """
DynamicARMetadata MCP Server for Facebook Business API.

Provides typed access to all DynamicARMetadata operations.
"""

dynamicarmetadata_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicarmetadata_server.tool
@wrapped_fn_tool
def get_dynamicarmetadata(
    dynamicarmetadata_id: str,
    fields: list[DynamicARMetadataField] = [],
) -> str:
    """Get a DynamicARMetadata object by ID.

    Args:
        dynamicarmetadata_id: The ID of the DynamicARMetadata.
        fields: Fields to retrieve. Available fields: See DynamicARMetadataField type.
    """
    obj = DynamicARMetadata(dynamicarmetadata_id)
    return obj.api_get(fields=fields)
