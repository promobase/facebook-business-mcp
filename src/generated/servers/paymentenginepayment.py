"""
Auto-generated MCP server for Facebook PaymentEnginePayment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.paymentenginepayment import PaymentEnginePayment
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-paymentenginepayment")


# CRUD Operations


@mcp.tool()
async def create_paymentenginepayment(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_dispute_for_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=object_id).create_dispute(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_refund_for_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=object_id).create_refund(
        fields=fields,
        params=params,
    )

    return result


# Export the server
paymentenginepayment_server = mcp
