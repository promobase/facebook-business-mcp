"""
Auto-generated MCP server for Facebook Shop.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shop import Shop
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-shop")


# CRUD Operations


@mcp.tool()
async def api_create_shop(
    shop_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Shop(fbid=shop_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_shop(
    shop_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Shop(fbid=shop_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_shop(
    shop_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Shop(fbid=shop_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_shop(
    shop_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Shop(fbid=shop_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shop_server = mcp
