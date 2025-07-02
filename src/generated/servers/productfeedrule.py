"""
Auto-generated MCP server for Facebook ProductFeedRule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeedrule import ProductFeedRule
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeedrule")


# CRUD Operations


@mcp.tool()
async def api_create_productfeedrule(
    productfeedrule_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedRule(fbid=productfeedrule_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_productfeedrule(
    productfeedrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedRule(fbid=productfeedrule_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_productfeedrule(
    productfeedrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedRule(fbid=productfeedrule_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_productfeedrule(
    productfeedrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedRule(fbid=productfeedrule_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeedrule_server = mcp
