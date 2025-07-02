"""
Auto-generated MCP server for Facebook ExtendedCreditEmail.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcreditemail import ExtendedCreditEmail
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcreditemail")


# CRUD Operations


@mcp.tool()
async def api_create_extendedcreditemail(
    extendedcreditemail_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCreditEmail(fbid=extendedcreditemail_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_extendedcreditemail(
    extendedcreditemail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCreditEmail(fbid=extendedcreditemail_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_extendedcreditemail(
    extendedcreditemail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCreditEmail(fbid=extendedcreditemail_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_extendedcreditemail(
    extendedcreditemail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExtendedCreditEmail(fbid=extendedcreditemail_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcreditemail_server = mcp
