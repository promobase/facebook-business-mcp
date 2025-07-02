"""
Auto-generated MCP server for Facebook AdAccountBusinessConstraints.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountbusinessconstraints import AdAccountBusinessConstraints
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountbusinessconstraints")


# CRUD Operations


@mcp.tool()
async def create_adaccountbusinessconstraints(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdAccountBusinessConstraints.

    Args:
        object_id: The ID of the AdAccountBusinessConstraints
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdAccountBusinessConstraints(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountbusinessconstraints_server = mcp
