"""IGRefreshAccessTokenForIGOnlyAPI MCP Server with typed wrappers."""

from facebook_business.adobjects.igrefreshaccesstokenforigonlyapi import (
    IGRefreshAccessTokenForIGOnlyAPI,
)
from fastmcp import FastMCP

from src.generated.models.igrefreshaccesstokenforigonlyapi import (
    IGRefreshAccessTokenForIGOnlyAPIField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGRefreshAccessTokenForIGOnlyAPI"
instructions = """
IGRefreshAccessTokenForIGOnlyAPI MCP Server for Facebook Business API.

Provides typed access to all IGRefreshAccessTokenForIGOnlyAPI operations.
"""

igrefreshaccesstokenforigonlyapi_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@igrefreshaccesstokenforigonlyapi_server.tool
@wrapped_fn_tool
def get_igrefreshaccesstokenforigonlyapi(
    igrefreshaccesstokenforigonlyapi_id: str,
    fields: list[IGRefreshAccessTokenForIGOnlyAPIField] = [],
) -> str:
    """Get a IGRefreshAccessTokenForIGOnlyAPI object by ID.

    Args:
        igrefreshaccesstokenforigonlyapi_id: The ID of the IGRefreshAccessTokenForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See IGRefreshAccessTokenForIGOnlyAPIField type.
    """
    obj = IGRefreshAccessTokenForIGOnlyAPI(igrefreshaccesstokenforigonlyapi_id)
    return obj.api_get(fields=fields)
