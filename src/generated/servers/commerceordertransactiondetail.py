"""
Auto-generated MCP server for Facebook CommerceOrderTransactionDetail.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commerceordertransactiondetail import (
    CommerceOrderTransactionDetail,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-commerceordertransactiondetail")


# Edge Methods


@mcp.tool()
async def get_items_for_commerceordertransactiondetail(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Items for CommerceOrderTransactionDetail.

    Args:
        object_id: The ID of the CommerceOrderTransactionDetail
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_items result
    """
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
    """
    Get Tax Details for CommerceOrderTransactionDetail.

    Args:
        object_id: The ID of the CommerceOrderTransactionDetail
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tax_details result
    """
    result = CommerceOrderTransactionDetail(fbid=object_id).get_tax_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commerceordertransactiondetail_server = mcp
