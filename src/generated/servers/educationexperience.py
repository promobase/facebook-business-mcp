"""
Auto-generated MCP server for Facebook EducationExperience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.educationexperience import EducationExperience
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-educationexperience")


# CRUD Operations


@mcp.tool()
async def get_educationexperience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a EducationExperience.

    Args:
        object_id: The ID of the EducationExperience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = EducationExperience(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
educationexperience_server = mcp
