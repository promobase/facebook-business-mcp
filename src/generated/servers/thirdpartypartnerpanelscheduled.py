"""
Auto-generated MCP server for Facebook ThirdPartyPartnerPanelScheduled.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.thirdpartypartnerpanelscheduled import (
    ThirdPartyPartnerPanelScheduled,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-thirdpartypartnerpanelscheduled")


# CRUD Operations


@mcp.tool()
async def api_create_thirdpartypartnerpanelscheduled(
    thirdpartypartnerpanelscheduled_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyPartnerPanelScheduled(fbid=thirdpartypartnerpanelscheduled_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_thirdpartypartnerpanelscheduled(
    thirdpartypartnerpanelscheduled_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyPartnerPanelScheduled(fbid=thirdpartypartnerpanelscheduled_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_thirdpartypartnerpanelscheduled(
    thirdpartypartnerpanelscheduled_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyPartnerPanelScheduled(fbid=thirdpartypartnerpanelscheduled_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_thirdpartypartnerpanelscheduled(
    thirdpartypartnerpanelscheduled_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyPartnerPanelScheduled(fbid=thirdpartypartnerpanelscheduled_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
thirdpartypartnerpanelscheduled_server = mcp
