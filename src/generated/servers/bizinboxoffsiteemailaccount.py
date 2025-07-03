"""
Auto-generated MCP server for Facebook BizInboxOffsiteEmailAccount.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.bizinboxoffsiteemailaccount import BizInboxOffsiteEmailAccount
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-bizinboxoffsiteemailaccount")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    bizinboxoffsiteemailaccount_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_users(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BizInboxOffsiteEmailAccount(fbid=bizinboxoffsiteemailaccount_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bizinboxoffsiteemailaccount_server = mcp
