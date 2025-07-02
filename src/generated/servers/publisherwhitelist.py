"""PublisherWhiteList MCP Server."""

from typing import Any

from facebook_business.adobjects.publisherwhitelist import PublisherWhiteList
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPublisherWhiteList"
instructions = """
PublisherWhiteList MCP Server for Facebook Business API.

Provides typed access to all PublisherWhiteList operations.
"""

publisherwhitelist_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@publisherwhitelist_server.tool
@wrapped_fn_tool
def get_publisherwhitelist(
    publisherwhitelist_id: str,
    fields: list[str] = [],
) -> str:
    obj = PublisherWhiteList(publisherwhitelist_id)
    return obj.api_get(fields=fields)
