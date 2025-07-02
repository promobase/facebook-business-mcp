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
async def api_create_paymentsubscription(
    paymentsubscription_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=paymentsubscription_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_paymentsubscription(
    paymentsubscription_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=paymentsubscription_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_paymentsubscription(
    paymentsubscription_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=paymentsubscription_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_paymentsubscription(
    paymentsubscription_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentSubscription(fbid=paymentsubscription_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
paymentsubscription_server = mcp
