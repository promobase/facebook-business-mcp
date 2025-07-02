"""LiveVideoInputStream MCP Server."""

from typing import Any

from facebook_business.adobjects.livevideoinputstream import LiveVideoInputStream
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLiveVideoInputStream"
instructions = """
LiveVideoInputStream MCP Server for Facebook Business API.

Provides typed access to all LiveVideoInputStream operations.
"""

livevideoinputstream_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@livevideoinputstream_server.tool
@wrapped_fn_tool
def get_livevideoinputstream(
    livevideoinputstream_id: str,
    fields: list[str] = [],
) -> str:
    obj = LiveVideoInputStream(livevideoinputstream_id)
    return obj.api_get(fields=fields)
