"""WhitehatFBDLRun MCP Server."""

from typing import Any

from facebook_business.adobjects.whitehatfbdlrun import WhitehatFBDLRun
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWhitehatFBDLRun"
instructions = """
WhitehatFBDLRun MCP Server for Facebook Business API.

Provides typed access to all WhitehatFBDLRun operations.
"""

whitehatfbdlrun_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@whitehatfbdlrun_server.tool
@wrapped_fn_tool
def get_whitehatfbdlrun(
    whitehatfbdlrun_id: str,
    fields: list[str] = [],
) -> str:
    obj = WhitehatFBDLRun(whitehatfbdlrun_id)
    return obj.api_get(fields=fields)
