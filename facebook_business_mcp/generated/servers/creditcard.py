"""
Auto-generated MCP server for Facebook CreditCard.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.creditcard import CreditCard
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-creditcard")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    creditcard_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CreditCard(fbid=creditcard_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    creditcard_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CreditCard(fbid=creditcard_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    creditcard_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CreditCard(fbid=creditcard_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    creditcard_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CreditCard(fbid=creditcard_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
creditcard_server = mcp
