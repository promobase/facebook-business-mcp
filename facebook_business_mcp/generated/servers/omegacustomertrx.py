"""
Auto-generated MCP server for Facebook OmegaCustomerTrx.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.omegacustomertrx import OmegaCustomerTrx
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-omegacustomertrx")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    omegacustomertrx_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_campaigns(
    omegacustomertrx_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OmegaCustomerTrx(fbid=omegacustomertrx_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
omegacustomertrx_server = mcp
