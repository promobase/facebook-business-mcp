"""Stories MCP Server."""

from typing import Any

from facebook_business.adobjects.stories import Stories
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookStories"
instructions = """
Stories MCP Server for Facebook Business API.

Provides typed access to all Stories operations.
"""

stories_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@stories_server.tool
@wrapped_fn_tool
def get_stories(
    stories_id: str,
    fields: list[str] = [],
) -> str:
    obj = Stories(stories_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@stories_server.tool
@wrapped_fn_tool
def get_insights(
    stories_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Stories(stories_id).get_insights(fields=fields, params=params)
