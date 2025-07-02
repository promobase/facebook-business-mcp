"""IGAccessTokenForIGOnlyAPI MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.igaccesstokenforigonlyapi import IGAccessTokenForIGOnlyAPI
from fastmcp import FastMCP

from src.generated.models.igaccesstokenforigonlyapi import IGAccessTokenForIGOnlyAPIField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGAccessTokenForIGOnlyAPI"
instructions = """
IGAccessTokenForIGOnlyAPI MCP Server for Facebook Business API.

Provides typed access to all IGAccessTokenForIGOnlyAPI operations.
"""

igaccesstokenforigonlyapi_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@igaccesstokenforigonlyapi_server.tool
@wrapped_fn_tool
def get_igaccesstokenforigonlyapi(
    igaccesstokenforigonlyapi_id: str,
    fields: list[IGAccessTokenForIGOnlyAPIField] = [],
) -> str:
    """Get a IGAccessTokenForIGOnlyAPI object by ID.

    Args:
        igaccesstokenforigonlyapi_id: The ID of the IGAccessTokenForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See IGAccessTokenForIGOnlyAPIField type.
    """
    obj = IGAccessTokenForIGOnlyAPI(igaccesstokenforigonlyapi_id)
    return obj.api_get(fields=fields)
