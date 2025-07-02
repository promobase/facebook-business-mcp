"""
Auto-generated MCP server for Facebook OpenBridgeConfiguration.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.openbridgeconfiguration import OpenBridgeConfiguration
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-openbridgeconfiguration")


# CRUD Operations


@mcp.tool()
async def create_openbridgeconfiguration(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OpenBridgeConfiguration(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_openbridgeconfiguration(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OpenBridgeConfiguration(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_openbridgeconfiguration(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OpenBridgeConfiguration(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_openbridgeconfiguration(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OpenBridgeConfiguration(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
openbridgeconfiguration_server = mcp
