"""
Auto-generated MCP server for Facebook ValueBasedEligibleSource.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.valuebasedeligiblesource import ValueBasedEligibleSource
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-valuebasedeligiblesource")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    valuebasedeligiblesource_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    valuebasedeligiblesource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    valuebasedeligiblesource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    valuebasedeligiblesource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ValueBasedEligibleSource(fbid=valuebasedeligiblesource_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
valuebasedeligiblesource_server = mcp
