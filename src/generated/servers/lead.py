"""
Auto-generated MCP server for Facebook Lead.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.lead import Lead
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-lead")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    lead_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Lead(fbid=lead_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    lead_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Lead(fbid=lead_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    lead_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Lead(fbid=lead_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    lead_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Lead(fbid=lead_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
lead_server = mcp
