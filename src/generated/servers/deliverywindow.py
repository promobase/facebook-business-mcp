"""
Auto-generated MCP server for Facebook DeliveryWindow.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.deliverywindow import DeliveryWindow
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-deliverywindow")


# CRUD Operations


@mcp.tool()
async def api_create_deliverywindow(
    deliverywindow_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DeliveryWindow(fbid=deliverywindow_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_deliverywindow(
    deliverywindow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DeliveryWindow(fbid=deliverywindow_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_deliverywindow(
    deliverywindow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DeliveryWindow(fbid=deliverywindow_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_deliverywindow(
    deliverywindow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DeliveryWindow(fbid=deliverywindow_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
deliverywindow_server = mcp
