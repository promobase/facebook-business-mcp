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
async def create_adstudycell(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_accounts_for_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets_for_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=object_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaigns_for_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyCell(fbid=object_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudycell_server = mcp
