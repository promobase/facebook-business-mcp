"""
Auto-generated MCP server for Facebook CustomConversion.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customconversion import CustomConversion
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-customconversion")


# CRUD Operations


@mcp.tool()
async def api_create_customconversion(
    customconversion_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomConversion(fbid=customconversion_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_customconversion(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomConversion(fbid=customconversion_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_customconversion(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomConversion(fbid=customconversion_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_customconversion(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomConversion(fbid=customconversion_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_stats(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomConversion(fbid=customconversion_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customconversion_server = mcp
