"""
Auto-generated MCP server for Facebook CopyrightReferenceContainer.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.copyrightreferencecontainer import CopyrightReferenceContainer
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-copyrightreferencecontainer")


# CRUD Operations


@mcp.tool()
async def api_create_copyrightreferencecontainer(
    copyrightreferencecontainer_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightReferenceContainer(fbid=copyrightreferencecontainer_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_copyrightreferencecontainer(
    copyrightreferencecontainer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightReferenceContainer(fbid=copyrightreferencecontainer_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_copyrightreferencecontainer(
    copyrightreferencecontainer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightReferenceContainer(fbid=copyrightreferencecontainer_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_copyrightreferencecontainer(
    copyrightreferencecontainer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightReferenceContainer(fbid=copyrightreferencecontainer_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
copyrightreferencecontainer_server = mcp
