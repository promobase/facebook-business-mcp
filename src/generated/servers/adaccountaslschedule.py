"""
Auto-generated MCP server for Facebook AdAccountASLSchedule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountaslschedule import AdAccountASLSchedule
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountaslschedule")


# CRUD Operations


@mcp.tool()
async def api_create_adaccountaslschedule(
    adaccountaslschedule_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountASLSchedule(fbid=adaccountaslschedule_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adaccountaslschedule(
    adaccountaslschedule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountASLSchedule(fbid=adaccountaslschedule_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adaccountaslschedule(
    adaccountaslschedule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountASLSchedule(fbid=adaccountaslschedule_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adaccountaslschedule(
    adaccountaslschedule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountASLSchedule(fbid=adaccountaslschedule_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountaslschedule_server = mcp
