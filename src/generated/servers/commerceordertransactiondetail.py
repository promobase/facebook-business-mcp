"""
Auto-generated MCP server for Facebook CommerceOrderTransactionDetail.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commerceordertransactiondetail import (
    CommerceOrderTransactionDetail,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-commerceordertransactiondetail")


# CRUD Operations


@mcp.tool()
async def create_commerceordertransactiondetail(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrderTransactionDetail(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_commerceordertransactiondetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrderTransactionDetail(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerceordertransactiondetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrderTransactionDetail(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_commerceordertransactiondetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrderTransactionDetail(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_items_for_commerceordertransactiondetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrderTransactionDetail(fbid=object_id).get_items(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tax_details_for_commerceordertransactiondetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrderTransactionDetail(fbid=object_id).get_tax_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commerceordertransactiondetail_server = mcp
