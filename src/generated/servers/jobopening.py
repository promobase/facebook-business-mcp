"""
Auto-generated MCP server for Facebook JobOpening.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.jobopening import JobOpening
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-jobopening")


# CRUD Operations


@mcp.tool()
async def get_jobopening(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a JobOpening.

    Args:
        object_id: The ID of the JobOpening
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = JobOpening(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
jobopening_server = mcp
