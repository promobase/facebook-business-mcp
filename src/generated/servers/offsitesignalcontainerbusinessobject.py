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
async def api_create_offsitesignalcontainerbusinessobject(
    offsitesignalcontainerbusinessobject_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(
        fbid=offsitesignalcontainerbusinessobject_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_offsitesignalcontainerbusinessobject(
    offsitesignalcontainerbusinessobject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(
        fbid=offsitesignalcontainerbusinessobject_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_offsitesignalcontainerbusinessobject(
    offsitesignalcontainerbusinessobject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(
        fbid=offsitesignalcontainerbusinessobject_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_offsitesignalcontainerbusinessobject(
    offsitesignalcontainerbusinessobject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(
        fbid=offsitesignalcontainerbusinessobject_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_linked_application(
    offsitesignalcontainerbusinessobject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(
        fbid=offsitesignalcontainerbusinessobject_id
    ).get_linked_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_linked_page(
    offsitesignalcontainerbusinessobject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OffsiteSignalContainerBusinessObject(
        fbid=offsitesignalcontainerbusinessobject_id
    ).get_linked_page(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offsitesignalcontainerbusinessobject_server = mcp
