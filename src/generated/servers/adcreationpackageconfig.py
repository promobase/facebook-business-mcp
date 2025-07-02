"""
Auto-generated MCP server for Facebook AdCreationPackageConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcreationpackageconfig import AdCreationPackageConfig
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcreationpackageconfig")


# CRUD Operations


@mcp.tool()
async def api_create_adcreationpackageconfig(
    adcreationpackageconfig_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreationPackageConfig(fbid=adcreationpackageconfig_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adcreationpackageconfig(
    adcreationpackageconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreationPackageConfig(fbid=adcreationpackageconfig_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adcreationpackageconfig(
    adcreationpackageconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreationPackageConfig(fbid=adcreationpackageconfig_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adcreationpackageconfig(
    adcreationpackageconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreationPackageConfig(fbid=adcreationpackageconfig_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcreationpackageconfig_server = mcp
