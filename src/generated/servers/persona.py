"""
Auto-generated MCP server for Facebook Persona.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.persona import Persona
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-persona")


# CRUD Operations


@mcp.tool()
async def delete_persona(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a Persona.

    Args:
        object_id: The ID of the Persona
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = Persona(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_persona(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Persona.

    Args:
        object_id: The ID of the Persona
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Persona(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
persona_server = mcp
