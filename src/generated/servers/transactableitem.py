"""
Auto-generated MCP server for Facebook TransactableItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.transactableitem import TransactableItem
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-transactableitem")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    transactableitem_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TransactableItem(fbid=transactableitem_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    transactableitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TransactableItem(fbid=transactableitem_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    transactableitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TransactableItem(fbid=transactableitem_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    transactableitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TransactableItem(fbid=transactableitem_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    transactableitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TransactableItem(fbid=transactableitem_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    transactableitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TransactableItem(fbid=transactableitem_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
transactableitem_server = mcp
