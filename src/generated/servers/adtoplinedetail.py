"""
Auto-generated MCP server for Facebook AdToplineDetail.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adtoplinedetail import AdToplineDetail
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adtoplinedetail")


# CRUD Operations


@mcp.tool()
async def create_adtoplinedetail(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdToplineDetail(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adtoplinedetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdToplineDetail(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adtoplinedetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdToplineDetail(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adtoplinedetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdToplineDetail(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adtoplinedetail_server = mcp
