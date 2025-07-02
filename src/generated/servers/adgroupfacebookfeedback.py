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
async def create_adgroupfacebookfeedback(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adgroupfacebookfeedback(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adgroupfacebookfeedback(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adgroupfacebookfeedback(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_comments_for_adgroupfacebookfeedback(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdgroupFacebookFeedback(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adgroupfacebookfeedback_server = mcp
