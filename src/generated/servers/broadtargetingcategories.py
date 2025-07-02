"""
Auto-generated MCP server for Facebook BroadTargetingCategories.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.broadtargetingcategories import BroadTargetingCategories
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-broadtargetingcategories")


# CRUD Operations


@mcp.tool()
async def create_broadtargetingcategories(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BroadTargetingCategories(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_broadtargetingcategories(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BroadTargetingCategories(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_broadtargetingcategories(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BroadTargetingCategories(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_broadtargetingcategories(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BroadTargetingCategories(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
broadtargetingcategories_server = mcp
