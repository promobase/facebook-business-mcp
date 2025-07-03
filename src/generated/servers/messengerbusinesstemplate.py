"""
Auto-generated MCP server for Facebook MessengerBusinessTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messengerbusinesstemplate import MessengerBusinessTemplate
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-messengerbusinesstemplate")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    messengerbusinesstemplate_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengerbusinesstemplate_server = mcp
