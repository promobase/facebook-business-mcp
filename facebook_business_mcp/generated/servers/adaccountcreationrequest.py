"""
Auto-generated MCP server for Facebook AdAccountCreationRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountcreationrequest import AdAccountCreationRequest
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountcreationrequest")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adaccountcreationrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountCreationRequest(fbid=adaccountcreationrequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adaccountcreationrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountCreationRequest(fbid=adaccountcreationrequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adaccountcreationrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountCreationRequest(fbid=adaccountcreationrequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adaccountcreationrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountCreationRequest(fbid=adaccountcreationrequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_ad_accounts(
    adaccountcreationrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAccountCreationRequest(fbid=adaccountcreationrequest_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountcreationrequest_server = mcp
