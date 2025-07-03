"""
Auto-generated MCP server for Facebook AppPublisher.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.apppublisher import AppPublisher
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-apppublisher")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    apppublisher_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppPublisher(fbid=apppublisher_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    apppublisher_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppPublisher(fbid=apppublisher_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    apppublisher_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppPublisher(fbid=apppublisher_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    apppublisher_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppPublisher(fbid=apppublisher_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
apppublisher_server = mcp
