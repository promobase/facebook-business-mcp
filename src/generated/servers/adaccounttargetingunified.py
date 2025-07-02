"""
Auto-generated MCP server for Facebook AdAccountTargetingUnified.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccounttargetingunified import AdAccountTargetingUnified
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccounttargetingunified")


# CRUD Operations


@mcp.tool()
async def api_create_adaccounttargetingunified(
    adaccounttargetingunified_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountTargetingUnified(fbid=adaccounttargetingunified_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adaccounttargetingunified(
    adaccounttargetingunified_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountTargetingUnified(fbid=adaccounttargetingunified_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adaccounttargetingunified(
    adaccounttargetingunified_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountTargetingUnified(fbid=adaccounttargetingunified_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adaccounttargetingunified(
    adaccounttargetingunified_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountTargetingUnified(fbid=adaccounttargetingunified_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccounttargetingunified_server = mcp
