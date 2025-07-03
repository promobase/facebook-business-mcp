"""
Auto-generated MCP server for Facebook DeliveryWindow.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.deliverywindow import DeliveryWindow
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-deliverywindow")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    deliverywindow_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DeliveryWindow(fbid=deliverywindow_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    deliverywindow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DeliveryWindow(fbid=deliverywindow_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    deliverywindow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DeliveryWindow(fbid=deliverywindow_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    deliverywindow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DeliveryWindow(fbid=deliverywindow_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
deliverywindow_server = mcp
