"""
Auto-generated MCP server for Facebook AdgroupFacebookFeedback.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adgroupfacebookfeedback import AdgroupFacebookFeedback
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adgroupfacebookfeedback")


# CRUD Operations


@mcp.tool()
async def api_create_adgroupfacebookfeedback(
    adgroupfacebookfeedback_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=adgroupfacebookfeedback_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adgroupfacebookfeedback(
    adgroupfacebookfeedback_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=adgroupfacebookfeedback_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adgroupfacebookfeedback(
    adgroupfacebookfeedback_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=adgroupfacebookfeedback_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adgroupfacebookfeedback(
    adgroupfacebookfeedback_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=adgroupfacebookfeedback_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_comments(
    adgroupfacebookfeedback_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=adgroupfacebookfeedback_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adgroupfacebookfeedback_server = mcp
