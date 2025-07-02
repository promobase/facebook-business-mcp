"""ContentBlockList MCP Server."""

from typing import Any

from facebook_business.adobjects.contentblocklist import ContentBlockList
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookContentBlockList"
instructions = """
ContentBlockList MCP Server for Facebook Business API.

Provides typed access to all ContentBlockList operations.
"""

contentblocklist_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@contentblocklist_server.tool
@wrapped_fn_tool
def get_contentblocklist(
    contentblocklist_id: str,
    fields: list[str] = [],
) -> str:
    obj = ContentBlockList(contentblocklist_id)
    return obj.api_get(fields=fields)
