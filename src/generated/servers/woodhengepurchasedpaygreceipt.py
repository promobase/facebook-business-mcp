"""
Auto-generated MCP server for Facebook WoodhengePurchasedPAYGReceipt.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.woodhengepurchasedpaygreceipt import WoodhengePurchasedPAYGReceipt
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-woodhengepurchasedpaygreceipt")


# CRUD Operations


@mcp.tool()
async def api_create_woodhengepurchasedpaygreceipt(
    woodhengepurchasedpaygreceipt_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_woodhengepurchasedpaygreceipt(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_woodhengepurchasedpaygreceipt(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_woodhengepurchasedpaygreceipt(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
woodhengepurchasedpaygreceipt_server = mcp
