"""
Auto-generated MCP server for Facebook PaymentSubscription.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.paymentsubscription import PaymentSubscription
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-paymentsubscription")


# CRUD Operations


@mcp.tool()
async def create_paymentsubscription(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_paymentsubscription(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_paymentsubscription(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_paymentsubscription(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
paymentsubscription_server = mcp
