"""
Auto-generated MCP server for Facebook ExtendedCreditInvoiceGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcreditinvoicegroup import ExtendedCreditInvoiceGroup
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcreditinvoicegroup")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    extendedcreditinvoicegroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditInvoiceGroup(fbid=extendedcreditinvoicegroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditInvoiceGroup(fbid=extendedcreditinvoicegroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditInvoiceGroup(fbid=extendedcreditinvoicegroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditInvoiceGroup(fbid=extendedcreditinvoicegroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_ad_account(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditInvoiceGroup(fbid=extendedcreditinvoicegroup_id).create_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_ad_accounts(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditInvoiceGroup(fbid=extendedcreditinvoicegroup_id).delete_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_accounts(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditInvoiceGroup(fbid=extendedcreditinvoicegroup_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcreditinvoicegroup_server = mcp
