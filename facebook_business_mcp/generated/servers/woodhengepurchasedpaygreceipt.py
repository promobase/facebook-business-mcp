"""
Auto-generated MCP server for Facebook WoodhengePurchasedPAYGReceipt.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.woodhengepurchasedpaygreceipt import WoodhengePurchasedPAYGReceipt
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-woodhengepurchasedpaygreceipt")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    woodhengepurchasedpaygreceipt_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WoodhengePurchasedPAYGReceipt(fbid=woodhengepurchasedpaygreceipt_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
woodhengepurchasedpaygreceipt_server = mcp
