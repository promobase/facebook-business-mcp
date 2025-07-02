"""
Auto-generated MCP server for Facebook AdColumnSizes.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcolumnsizes import AdColumnSizes
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcolumnsizes")


# CRUD Operations


@mcp.tool()
async def api_create_adcolumnsizes(
    adcolumnsizes_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdColumnSizes(fbid=adcolumnsizes_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adcolumnsizes(
    adcolumnsizes_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdColumnSizes(fbid=adcolumnsizes_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adcolumnsizes(
    adcolumnsizes_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdColumnSizes(fbid=adcolumnsizes_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adcolumnsizes(
    adcolumnsizes_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdColumnSizes(fbid=adcolumnsizes_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcolumnsizes_server = mcp
