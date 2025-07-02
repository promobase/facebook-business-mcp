"""
Auto-generated MCP server for Facebook AdProposal.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adproposal import AdProposal
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adproposal")


# CRUD Operations


@mcp.tool()
async def get_adproposal(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdProposal.

    Args:
        object_id: The ID of the AdProposal
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdProposal(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adproposal_server = mcp
