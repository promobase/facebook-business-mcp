"""
Auto-generated MCP server for Facebook LeadGenThankYouPageGatedPromo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgenthankyoupagegatedpromo import LeadGenThankYouPageGatedPromo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgenthankyoupagegatedpromo")


# CRUD Operations


@mcp.tool()
async def api_create_leadgenthankyoupagegatedpromo(
    leadgenthankyoupagegatedpromo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenThankYouPageGatedPromo(fbid=leadgenthankyoupagegatedpromo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_leadgenthankyoupagegatedpromo(
    leadgenthankyoupagegatedpromo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenThankYouPageGatedPromo(fbid=leadgenthankyoupagegatedpromo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_leadgenthankyoupagegatedpromo(
    leadgenthankyoupagegatedpromo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenThankYouPageGatedPromo(fbid=leadgenthankyoupagegatedpromo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_leadgenthankyoupagegatedpromo(
    leadgenthankyoupagegatedpromo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenThankYouPageGatedPromo(fbid=leadgenthankyoupagegatedpromo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgenthankyoupagegatedpromo_server = mcp
