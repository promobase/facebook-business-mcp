"""AdPreview MCP Server."""

from typing import Any

from facebook_business.adobjects.adpreview import AdPreview
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdPreview"
instructions = """
AdPreview MCP Server for Facebook Business API.

Provides typed access to all AdPreview operations.
"""

adpreview_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adpreview_server.tool
@wrapped_fn_tool
def get_endpoint(
    adpreview_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdPreview(adpreview_id).get_endpoint(fields=fields, params=params)
