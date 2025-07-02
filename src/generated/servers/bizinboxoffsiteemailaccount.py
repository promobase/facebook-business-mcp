"""
Auto-generated MCP server for Facebook BizInboxOffsiteEmailAccount.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.bizinboxoffsiteemailaccount import BizInboxOffsiteEmailAccount
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-bizinboxoffsiteemailaccount")


# CRUD Operations


@mcp.tool()
async def create_bizinboxoffsiteemailaccount(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_bizinboxoffsiteemailaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_bizinboxoffsiteemailaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_bizinboxoffsiteemailaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_assigned_users_for_bizinboxoffsiteemailaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bizinboxoffsiteemailaccount_server = mcp
