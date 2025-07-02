"""
Auto-generated MCP server for Facebook ExtendedCredit.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcredit import ExtendedCredit
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcredit")


# CRUD Operations


@mcp.tool()
async def create_extendedcredit(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_extended_credit_invoice_group_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).create_extended_credit_invoice_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_owning_credit_allocation_config_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).create_owning_credit_allocation_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_whats_app_credit_attach_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).create_whats_app_credit_attach(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_whats_app_credit_sharing_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).create_whats_app_credit_sharing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_whats_app_credit_sharing_and_attach_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).create_whats_app_credit_sharing_and_attach(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_extended_credit_invoice_groups_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).get_extended_credit_invoice_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owning_credit_allocation_configs_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCredit(fbid=object_id).get_owning_credit_allocation_configs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcredit_server = mcp
