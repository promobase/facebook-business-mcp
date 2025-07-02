"""
Auto-generated MCP server for Facebook AdAccountRecommendations.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountrecommendations import AdAccountRecommendations
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountrecommendations")


# CRUD Operations


@mcp.tool()
async def api_create_adaccountrecommendations(
    adaccountrecommendations_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountRecommendations(fbid=adaccountrecommendations_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adaccountrecommendations(
    adaccountrecommendations_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountRecommendations(fbid=adaccountrecommendations_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adaccountrecommendations(
    adaccountrecommendations_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountRecommendations(fbid=adaccountrecommendations_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adaccountrecommendations(
    adaccountrecommendations_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountRecommendations(fbid=adaccountrecommendations_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountrecommendations_server = mcp
