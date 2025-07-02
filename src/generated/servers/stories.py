"""Stories MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.stories import Stories
from fastmcp import FastMCP

from src.generated.models.insightsresult import InsightsResultField
from src.generated.models.stories import StoriesField, StoriesGetInsightsParams
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
    fields: list[StoriesField] = [],
) -> str:
    """Get a Stories object by ID.

    Args:
        stories_id: The ID of the Stories.
        fields: Fields to retrieve. Available fields: See StoriesField type.
    """
    obj = Stories(stories_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@stories_server.tool
@wrapped_fn_tool
def get_insights(
    stories_id: str,
    fields: list[InsightsResultField] = [],
    params: StoriesGetInsightsParams | dict = {},
):
    """Get Insights for this Stories.

    Args:
        stories_id: The ID of the Stories.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See StoriesGetInsightsParams type.
    """
    return Stories(stories_id).get_insights(fields=fields, params=params)
