"""
Auto-generated MCP server for Facebook CPASLsbImageBank.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpaslsbimagebank import CPASLsbImageBank
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpaslsbimagebank")


# CRUD Operations


@mcp.tool()
async def api_create_cpaslsbimagebank(
    cpaslsbimagebank_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASLsbImageBank(fbid=cpaslsbimagebank_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_cpaslsbimagebank(
    cpaslsbimagebank_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASLsbImageBank(fbid=cpaslsbimagebank_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_cpaslsbimagebank(
    cpaslsbimagebank_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASLsbImageBank(fbid=cpaslsbimagebank_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_cpaslsbimagebank(
    cpaslsbimagebank_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASLsbImageBank(fbid=cpaslsbimagebank_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_backup_images(
    cpaslsbimagebank_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASLsbImageBank(fbid=cpaslsbimagebank_id).get_backup_images(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpaslsbimagebank_server = mcp
