"""
Auto-generated MCP server for Facebook DirectDebit.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.directdebit import DirectDebit
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-directdebit")


# CRUD Operations


@mcp.tool()
async def api_create_directdebit(
    directdebit_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DirectDebit(fbid=directdebit_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_directdebit(
    directdebit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DirectDebit(fbid=directdebit_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_directdebit(
    directdebit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DirectDebit(fbid=directdebit_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_directdebit(
    directdebit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DirectDebit(fbid=directdebit_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
directdebit_server = mcp
