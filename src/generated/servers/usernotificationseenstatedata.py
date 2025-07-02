"""
Auto-generated MCP server for Facebook UserNotificationSeenStateData.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.usernotificationseenstatedata import UserNotificationSeenStateData
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-usernotificationseenstatedata")


# CRUD Operations


@mcp.tool()
async def api_create_usernotificationseenstatedata(
    usernotificationseenstatedata_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserNotificationSeenStateData(fbid=usernotificationseenstatedata_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_usernotificationseenstatedata(
    usernotificationseenstatedata_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserNotificationSeenStateData(fbid=usernotificationseenstatedata_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_usernotificationseenstatedata(
    usernotificationseenstatedata_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserNotificationSeenStateData(fbid=usernotificationseenstatedata_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_usernotificationseenstatedata(
    usernotificationseenstatedata_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserNotificationSeenStateData(fbid=usernotificationseenstatedata_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
usernotificationseenstatedata_server = mcp
