"""
Auto-generated MCP server for Facebook CPASAdCreationTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasadcreationtemplate import CPASAdCreationTemplate
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasadcreationtemplate")


# CRUD Operations


@mcp.tool()
async def get_cpasadcreationtemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CPASAdCreationTemplate.

    Args:
        object_id: The ID of the CPASAdCreationTemplate
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CPASAdCreationTemplate(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasadcreationtemplate_server = mcp
