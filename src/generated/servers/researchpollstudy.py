"""
Auto-generated MCP server for Facebook ResearchPollStudy.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.researchpollstudy import ResearchPollStudy
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-researchpollstudy")


# CRUD Operations


@mcp.tool()
async def get_researchpollstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ResearchPollStudy.

    Args:
        object_id: The ID of the ResearchPollStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ResearchPollStudy(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
researchpollstudy_server = mcp
