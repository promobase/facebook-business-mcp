"""
Auto-generated MCP server for Facebook FranchiseProgramMember.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.franchiseprogrammember import FranchiseProgramMember
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-franchiseprogrammember")


# CRUD Operations


@mcp.tool()
async def get_franchiseprogrammember(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a FranchiseProgramMember.

    Args:
        object_id: The ID of the FranchiseProgramMember
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = FranchiseProgramMember(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
franchiseprogrammember_server = mcp
