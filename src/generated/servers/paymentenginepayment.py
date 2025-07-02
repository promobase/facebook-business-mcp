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
async def api_create_paymentenginepayment(
    paymentenginepayment_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=paymentenginepayment_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_paymentenginepayment(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=paymentenginepayment_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_paymentenginepayment(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=paymentenginepayment_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_paymentenginepayment(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=paymentenginepayment_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_dispute(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=paymentenginepayment_id).create_dispute(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_refund(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PaymentEnginePayment(fbid=paymentenginepayment_id).create_refund(
        fields=fields,
        params=params,
    )

    return result


# Export the server
paymentenginepayment_server = mcp
