"""
Auto-generated MCP server for Facebook ExtendedCredit.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcredit import ExtendedCredit
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcredit")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    extendedcredit_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_extended_credit_invoice_group(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).create_extended_credit_invoice_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_owning_credit_allocation_config(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).create_owning_credit_allocation_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_whats_app_credit_attach(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).create_whats_app_credit_attach(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_whats_app_credit_sharing(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).create_whats_app_credit_sharing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_whats_app_credit_sharing_and_attach(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).create_whats_app_credit_sharing_and_attach(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_extended_credit_invoice_groups(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).get_extended_credit_invoice_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owning_credit_allocation_configs(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExtendedCredit(fbid=extendedcredit_id).get_owning_credit_allocation_configs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcredit_server = mcp
