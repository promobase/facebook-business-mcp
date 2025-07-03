"""
Auto-generated MCP server for Facebook MailingAddress.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mailingaddress import MailingAddress
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-mailingaddress")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    mailingaddress_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MailingAddress(fbid=mailingaddress_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    mailingaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MailingAddress(fbid=mailingaddress_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    mailingaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MailingAddress(fbid=mailingaddress_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    mailingaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MailingAddress(fbid=mailingaddress_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mailingaddress_server = mcp
