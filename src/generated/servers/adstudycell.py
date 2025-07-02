"""
Auto-generated MCP server for Facebook AdStudyCell.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adstudycell import AdStudyCell
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adstudycell")


# CRUD Operations


@mcp.tool()
async def api_create_adstudycell(
    adstudycell_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=adstudycell_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adstudycell(
    adstudycell_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=adstudycell_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adstudycell(
    adstudycell_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=adstudycell_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adstudycell(
    adstudycell_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=adstudycell_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_accounts(
    adstudycell_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=adstudycell_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets(
    adstudycell_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=adstudycell_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaigns(
    adstudycell_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=adstudycell_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudycell_server = mcp
