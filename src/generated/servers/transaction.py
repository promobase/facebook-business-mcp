"""
Auto-generated MCP server for Facebook Transaction.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.transaction import Transaction
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-transaction")


# CRUD Operations


@mcp.tool()
async def api_create_transaction(
    transaction_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Transaction(fbid=transaction_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_transaction(
    transaction_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Transaction(fbid=transaction_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_transaction(
    transaction_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Transaction(fbid=transaction_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_transaction(
    transaction_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Transaction(fbid=transaction_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
transaction_server = mcp
