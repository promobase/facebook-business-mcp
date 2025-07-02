"""
Auto-generated MCP server for Facebook AdsSegments.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adssegments import AdsSegments
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adssegments")


# CRUD Operations


@mcp.tool()
async def api_create_adssegments(
    adssegments_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsSegments(fbid=adssegments_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adssegments(
    adssegments_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsSegments(fbid=adssegments_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adssegments(
    adssegments_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsSegments(fbid=adssegments_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adssegments(
    adssegments_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsSegments(fbid=adssegments_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adssegments_server = mcp
