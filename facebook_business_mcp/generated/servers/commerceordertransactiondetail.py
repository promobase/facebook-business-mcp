"""
Auto-generated MCP server for Facebook CommerceOrderTransactionDetail.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commerceordertransactiondetail import (
    CommerceOrderTransactionDetail,
)
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-commerceordertransactiondetail")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    commerceordertransactiondetail_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrderTransactionDetail(fbid=commerceordertransactiondetail_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    commerceordertransactiondetail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrderTransactionDetail(fbid=commerceordertransactiondetail_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    commerceordertransactiondetail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrderTransactionDetail(fbid=commerceordertransactiondetail_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    commerceordertransactiondetail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrderTransactionDetail(fbid=commerceordertransactiondetail_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_items(
    commerceordertransactiondetail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrderTransactionDetail(fbid=commerceordertransactiondetail_id).get_items(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_tax_details(
    commerceordertransactiondetail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrderTransactionDetail(fbid=commerceordertransactiondetail_id).get_tax_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commerceordertransactiondetail_server = mcp
