"""
Auto-generated MCP server for Facebook LeadGenDataDraft.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgendatadraft import LeadGenDataDraft
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgendatadraft")


# CRUD Operations


@mcp.tool()
async def get_leadgendatadraft(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LeadGenDataDraft.

    Args:
        object_id: The ID of the LeadGenDataDraft
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LeadGenDataDraft(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgendatadraft_server = mcp
