"""
Auto-generated MCP server for Facebook SignalsIWLExtractor.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.signalsiwlextractor import SignalsIWLExtractor
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-signalsiwlextractor")


# CRUD Operations


@mcp.tool()
async def get_signalsiwlextractor(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a SignalsIWLExtractor.

    Args:
        object_id: The ID of the SignalsIWLExtractor
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = SignalsIWLExtractor(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
signalsiwlextractor_server = mcp
