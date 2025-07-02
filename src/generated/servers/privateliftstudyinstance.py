"""
Auto-generated MCP server for Facebook PrivateLiftStudyInstance.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.privateliftstudyinstance import PrivateLiftStudyInstance
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-privateliftstudyinstance")


# CRUD Operations


@mcp.tool()
async def api_create_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivateLiftStudyInstance(fbid=privateliftstudyinstance_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivateLiftStudyInstance(fbid=privateliftstudyinstance_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivateLiftStudyInstance(fbid=privateliftstudyinstance_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivateLiftStudyInstance(fbid=privateliftstudyinstance_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
privateliftstudyinstance_server = mcp
