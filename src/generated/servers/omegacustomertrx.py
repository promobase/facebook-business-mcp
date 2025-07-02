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
async def api_create_omegacustomertrx(
    omegacustomertrx_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_omegacustomertrx(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_omegacustomertrx(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_omegacustomertrx(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_campaigns(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
omegacustomertrx_server = mcp
