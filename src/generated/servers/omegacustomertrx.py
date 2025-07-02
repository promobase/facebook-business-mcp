"""
Auto-generated MCP server for Facebook OmegaCustomerTrx.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.omegacustomertrx import OmegaCustomerTrx
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-omegacustomertrx")


# CRUD Operations


@mcp.tool()
async def create_omegacustomertrx(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_omegacustomertrx(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_omegacustomertrx(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_omegacustomertrx(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_campaigns_for_omegacustomertrx(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=object_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
omegacustomertrx_server = mcp
