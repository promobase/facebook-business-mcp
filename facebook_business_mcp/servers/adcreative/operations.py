"""AdCreative additional operations.

This module provides thin wrappers around AdCreative SDK methods for various operations.
"""

from typing import Any

from facebook_business.adobjects.adcreative import AdCreative

from facebook_business_mcp.utils import wrapped_fn_tool


@wrapped_fn_tool
def adcreative_get_previews(
    creative_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get previews for an ad creative.

    This is a direct wrapper around AdCreative.get_previews().

    Args:
        creative_id: The ad creative ID
        fields: Fields to retrieve
        params: Additional parameters (e.g., ad_format, locale)

    Returns:
        List of preview data
    """
    creative = AdCreative(creative_id)
    return creative.get_previews(fields=fields, params=params)


@wrapped_fn_tool
def adcreative_create_ad_label(
    creative_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad label for an ad creative.

    This is a direct wrapper around AdCreative.create_ad_label().

    Args:
        creative_id: The ad creative ID
        params: Ad label parameters
        fields: Fields to return

    Returns:
        Created ad label data
    """
    creative = AdCreative(creative_id)
    return creative.create_ad_label(fields=fields, params=params)


@wrapped_fn_tool
def adcreative_get_creative_insights(
    creative_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get creative insights for an ad creative.

    This is a direct wrapper around AdCreative.get_creative_insights().

    Args:
        creative_id: The ad creative ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of creative insights data
    """
    creative = AdCreative(creative_id)
    return creative.get_creative_insights(fields=fields, params=params)
