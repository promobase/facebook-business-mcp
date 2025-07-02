"""
Auto-generated MCP server for Facebook CPASAdvertiserPartnershipRecommendation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasadvertiserpartnershiprecommendation import (
    CPASAdvertiserPartnershipRecommendation,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasadvertiserpartnershiprecommendation")


# CRUD Operations


@mcp.tool()
async def api_create_cpasadvertiserpartnershiprecommendation(
    cpasadvertiserpartnershiprecommendation_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdvertiserPartnershipRecommendation(
        fbid=cpasadvertiserpartnershiprecommendation_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_cpasadvertiserpartnershiprecommendation(
    cpasadvertiserpartnershiprecommendation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdvertiserPartnershipRecommendation(
        fbid=cpasadvertiserpartnershiprecommendation_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_cpasadvertiserpartnershiprecommendation(
    cpasadvertiserpartnershiprecommendation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdvertiserPartnershipRecommendation(
        fbid=cpasadvertiserpartnershiprecommendation_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_cpasadvertiserpartnershiprecommendation(
    cpasadvertiserpartnershiprecommendation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdvertiserPartnershipRecommendation(
        fbid=cpasadvertiserpartnershiprecommendation_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasadvertiserpartnershiprecommendation_server = mcp
