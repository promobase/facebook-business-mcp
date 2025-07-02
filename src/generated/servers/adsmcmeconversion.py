"""
Auto-generated MCP server for Facebook AdsMcmeConversion.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsmcmeconversion import AdsMcmeConversion
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsmcmeconversion")


# CRUD Operations


@mcp.tool()
async def api_create_adsmcmeconversion(
    adsmcmeconversion_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsMcmeConversion(fbid=adsmcmeconversion_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsmcmeconversion(
    adsmcmeconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsMcmeConversion(fbid=adsmcmeconversion_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsmcmeconversion(
    adsmcmeconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsMcmeConversion(fbid=adsmcmeconversion_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsmcmeconversion(
    adsmcmeconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsMcmeConversion(fbid=adsmcmeconversion_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsmcmeconversion_server = mcp
