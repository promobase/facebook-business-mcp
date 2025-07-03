"""
Auto-generated MCP server for Facebook ExtendedCreditApplication.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcreditapplication import ExtendedCreditApplication
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcreditapplication")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    extendedcreditapplication_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditApplication(fbid=extendedcreditapplication_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    extendedcreditapplication_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditApplication(fbid=extendedcreditapplication_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    extendedcreditapplication_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditApplication(fbid=extendedcreditapplication_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    extendedcreditapplication_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCreditApplication(fbid=extendedcreditapplication_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcreditapplication_server = mcp
