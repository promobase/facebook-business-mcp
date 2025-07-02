"""ShadowIGMediaBuilder MCP Server."""

from typing import Any

from facebook_business.adobjects.shadowigmediabuilder import ShadowIGMediaBuilder
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookShadowIGMediaBuilder"
instructions = """
ShadowIGMediaBuilder MCP Server for Facebook Business API.

Provides typed access to all ShadowIGMediaBuilder operations.
"""

shadowigmediabuilder_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@shadowigmediabuilder_server.tool
@wrapped_fn_tool
def get_shadowigmediabuilder(
    shadowigmediabuilder_id: str,
    fields: list[str] = [],
) -> str:
    obj = ShadowIGMediaBuilder(shadowigmediabuilder_id)
    return obj.api_get(fields=fields)
