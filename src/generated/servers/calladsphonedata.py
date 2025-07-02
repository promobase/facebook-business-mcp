"""
Auto-generated MCP server for Facebook CallAdsPhoneData.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.calladsphonedata import CallAdsPhoneData
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-calladsphonedata")


# CRUD Operations


@mcp.tool()
async def api_create_calladsphonedata(
    calladsphonedata_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CallAdsPhoneData(fbid=calladsphonedata_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_calladsphonedata(
    calladsphonedata_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CallAdsPhoneData(fbid=calladsphonedata_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_calladsphonedata(
    calladsphonedata_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CallAdsPhoneData(fbid=calladsphonedata_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_calladsphonedata(
    calladsphonedata_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CallAdsPhoneData(fbid=calladsphonedata_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
calladsphonedata_server = mcp
