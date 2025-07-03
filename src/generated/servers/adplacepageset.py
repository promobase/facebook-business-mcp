"""
Auto-generated MCP server for Facebook AdPlacePageSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adplacepageset import AdPlacePageSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adplacepageset")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adplacepageset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adplacepageset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adplacepageset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adplacepageset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adplacepageset_server = mcp
