"""
Auto-generated MCP server for Facebook AdStudyObjective.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adstudyobjective import AdStudyObjective
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adstudyobjective")


# CRUD Operations


@mcp.tool()
async def get_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdStudyObjective(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdStudyObjective(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ads_pixels_for_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads Pixels for AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_pixels result
    """
    result = AdStudyObjective(fbid=object_id).get_ads_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_applications_for_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Applications for AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_applications result
    """
    result = AdStudyObjective(fbid=object_id).get_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_brand_requests_for_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Brand Requests for AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_brand_requests result
    """
    result = AdStudyObjective(fbid=object_id).get_brand_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_conversions_for_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Custom Conversions for AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_conversions result
    """
    result = AdStudyObjective(fbid=object_id).get_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offline_conversion_data_sets_for_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Offline Conversion Data Sets for AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_offline_conversion_data_sets result
    """
    result = AdStudyObjective(fbid=object_id).get_offline_conversion_data_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partner_private_studies_for_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Partner Private Studies for AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_partner_private_studies result
    """
    result = AdStudyObjective(fbid=object_id).get_partner_private_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partner_studies_for_adstudyobjective(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Partner Studies for AdStudyObjective.

    Args:
        object_id: The ID of the AdStudyObjective
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_partner_studies result
    """
    result = AdStudyObjective(fbid=object_id).get_partner_studies(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudyobjective_server = mcp
