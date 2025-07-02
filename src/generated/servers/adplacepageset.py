"""
Auto-generated MCP server for Facebook AdPlacePageSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adplacepageset import AdPlacePageSet
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adplacepageset")


# CRUD Operations


@mcp.tool()
async def api_create_adplacepageset(
    adplacepageset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adplacepageset(
    adplacepageset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adplacepageset(
    adplacepageset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adplacepageset(
    adplacepageset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacePageSet(fbid=adplacepageset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adplacepageset_server = mcp
