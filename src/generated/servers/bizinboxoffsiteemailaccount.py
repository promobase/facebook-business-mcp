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
async def api_create_bizinboxoffsiteemailaccount(
    bizinboxoffsiteemailaccount_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_bizinboxoffsiteemailaccount(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_bizinboxoffsiteemailaccount(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_bizinboxoffsiteemailaccount(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_assigned_users(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bizinboxoffsiteemailaccount_server = mcp
