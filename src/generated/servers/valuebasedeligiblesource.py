"""
Auto-generated MCP server for Facebook ValueBasedEligibleSource.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.valuebasedeligiblesource import ValueBasedEligibleSource
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-valuebasedeligiblesource")


# CRUD Operations


@mcp.tool()
async def api_create_valuebasedeligiblesource(
    valuebasedeligiblesource_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_valuebasedeligiblesource(
    valuebasedeligiblesource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_valuebasedeligiblesource(
    valuebasedeligiblesource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_valuebasedeligiblesource(
    valuebasedeligiblesource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
valuebasedeligiblesource_server = mcp
