"""
Auto-generated MCP server for Facebook MessengerBusinessTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messengerbusinesstemplate import MessengerBusinessTemplate
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-messengerbusinesstemplate")


# CRUD Operations


@mcp.tool()
async def api_create_messengerbusinesstemplate(
    messengerbusinesstemplate_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_messengerbusinesstemplate(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_messengerbusinesstemplate(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_messengerbusinesstemplate(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerBusinessTemplate(fbid=messengerbusinesstemplate_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengerbusinesstemplate_server = mcp
