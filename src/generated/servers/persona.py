"""
Auto-generated MCP server for Facebook Persona.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.persona import Persona
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-persona")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    persona_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Persona(fbid=persona_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    persona_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Persona(fbid=persona_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    persona_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Persona(fbid=persona_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    persona_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Persona(fbid=persona_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
persona_server = mcp
