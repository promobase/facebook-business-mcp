"""
Auto-generated MCP server for Facebook AdStudyObjective.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adstudyobjective import AdStudyObjective
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adstudyobjective")


# CRUD Operations


@mcp.tool()
async def api_create_adstudyobjective(
    adstudyobjective_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ads_pixels(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).get_ads_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_applications(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).get_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_brand_requests(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).get_brand_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_conversions(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).get_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offline_conversion_data_sets(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).get_offline_conversion_data_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partner_private_studies(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).get_partner_private_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partner_studies(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudyObjective(fbid=adstudyobjective_id).get_partner_studies(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudyobjective_server = mcp
