"""URL MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.url import URL
from fastmcp import FastMCP

from src.generated.models.url import URLField, URLUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookURL"
instructions = """
URL MCP Server for Facebook Business API.

Provides typed access to all URL operations.
"""

url_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@url_server.tool
@wrapped_fn_tool
def get_url(
    url_id: str,
    fields: list[URLField] = [],
) -> str:
    """Get a URL object by ID.

    Args:
        url_id: The ID of the URL.
        fields: Fields to retrieve. Available fields: See URLField type.
    """
    obj = URL(url_id)
    return obj.api_get(fields=fields)


@url_server.tool
@wrapped_fn_tool
def update_url(
    url_id: str,
    fields: list[URLField] = [],
    params: URLUpdateParams | dict = {},
) -> str:
    """Update a URL object.

    Args:
        url_id: The ID of the URL.
        fields: Fields to return after update. Available fields: See URLField type.
        params: Parameters to update. Available params: See URLUpdateParams type.
    """
    return URL(url_id).api_update(fields=fields, params=params)
