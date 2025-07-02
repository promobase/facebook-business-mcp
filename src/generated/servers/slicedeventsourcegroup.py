"""
Auto-generated MCP server for Facebook SlicedEventSourceGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.slicedeventsourcegroup import SlicedEventSourceGroup
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-slicedeventsourcegroup")


# CRUD Operations


@mcp.tool()
async def api_create_slicedeventsourcegroup(
    slicedeventsourcegroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SlicedEventSourceGroup(fbid=slicedeventsourcegroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_slicedeventsourcegroup(
    slicedeventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SlicedEventSourceGroup(fbid=slicedeventsourcegroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_slicedeventsourcegroup(
    slicedeventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SlicedEventSourceGroup(fbid=slicedeventsourcegroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_slicedeventsourcegroup(
    slicedeventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SlicedEventSourceGroup(fbid=slicedeventsourcegroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
slicedeventsourcegroup_server = mcp
