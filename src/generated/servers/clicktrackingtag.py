"""
Auto-generated MCP server for Facebook ClickTrackingTag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.clicktrackingtag import ClickTrackingTag
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-clicktrackingtag")


# CRUD Operations


@mcp.tool()
async def api_create_clicktrackingtag(
    clicktrackingtag_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ClickTrackingTag(fbid=clicktrackingtag_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_clicktrackingtag(
    clicktrackingtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ClickTrackingTag(fbid=clicktrackingtag_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_clicktrackingtag(
    clicktrackingtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ClickTrackingTag(fbid=clicktrackingtag_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_clicktrackingtag(
    clicktrackingtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ClickTrackingTag(fbid=clicktrackingtag_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
clicktrackingtag_server = mcp
