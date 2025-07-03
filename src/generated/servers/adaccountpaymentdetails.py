"""
Auto-generated MCP server for Facebook AdAccountPaymentDetails.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountpaymentdetails import AdAccountPaymentDetails
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountpaymentdetails")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adaccountpaymentdetails_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountPaymentDetails(fbid=adaccountpaymentdetails_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adaccountpaymentdetails_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountPaymentDetails(fbid=adaccountpaymentdetails_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adaccountpaymentdetails_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountPaymentDetails(fbid=adaccountpaymentdetails_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adaccountpaymentdetails_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountPaymentDetails(fbid=adaccountpaymentdetails_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountpaymentdetails_server = mcp
