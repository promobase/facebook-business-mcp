"""
Auto-generated MCP server for Facebook OffsiteSignalContainerBusinessObject.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offsitesignalcontainerbusinessobject import (
    OffsiteSignalContainerBusinessObject,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offsitesignalcontainerbusinessobject")


# CRUD Operations


@mcp.tool()
async def create_offsitesignalcontainerbusinessobject(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_linked_application_for_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).get_linked_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_linked_page_for_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).get_linked_page(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offsitesignalcontainerbusinessobject_server = mcp
