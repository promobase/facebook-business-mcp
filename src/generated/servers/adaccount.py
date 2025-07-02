"""
Auto-generated MCP server for Facebook AdAccount.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccount")


# CRUD Operations


@mcp.tool()
async def get_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdAccount(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdAccount(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_account_control_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Account Control for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_account_control result
    """
    result = AdAccount(fbid=object_id).create_account_control(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad result
    """
    result = AdAccount(fbid=object_id).create_ad(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_creative_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Creative for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_creative result
    """
    result = AdAccount(fbid=object_id).create_ad_creative(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_image_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Image for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_image result
    """
    result = AdAccount(fbid=object_id).create_ad_image(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_label_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Label for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_label result
    """
    result = AdAccount(fbid=object_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_place_page_set_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Place Page Set for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_place_page_set result
    """
    result = AdAccount(fbid=object_id).create_ad_place_page_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_place_page_sets_async_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Place Page Sets Async for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_place_page_sets_async result
    """
    result = AdAccount(fbid=object_id).create_ad_place_page_sets_async(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_playable_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Playable for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_playable result
    """
    result = AdAccount(fbid=object_id).create_ad_playable(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_rules_library_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Rules Library for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_rules_library result
    """
    result = AdAccount(fbid=object_id).create_ad_rules_library(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_set_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Set for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_set result
    """
    result = AdAccount(fbid=object_id).create_ad_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_video_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Video for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_video result
    """
    result = AdAccount(fbid=object_id).create_ad_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ads_pixel_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ads Pixel for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ads_pixel result
    """
    result = AdAccount(fbid=object_id).create_ads_pixel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_agency_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Agency for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_agency result
    """
    result = AdAccount(fbid=object_id).create_agency(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_assigned_user_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Assigned User for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_assigned_user result
    """
    result = AdAccount(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_async_ad_creative_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Async Ad Creative for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_async_ad_creative result
    """
    result = AdAccount(fbid=object_id).create_async_ad_creative(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_async_ad_request_set_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Async Ad Request Set for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_async_ad_request_set result
    """
    result = AdAccount(fbid=object_id).create_async_ad_request_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_async_batch_request_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Async Batch Request for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_async_batch_request result
    """
    result = AdAccount(fbid=object_id).create_async_batch_request(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_block_list_draft_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Block List Draft for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_block_list_draft result
    """
    result = AdAccount(fbid=object_id).create_block_list_draft(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_brand_safety_content_filter_level_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Brand Safety Content Filter Level for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_brand_safety_content_filter_level result
    """
    result = AdAccount(fbid=object_id).create_brand_safety_content_filter_level(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_campaign_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Campaign for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_campaign result
    """
    result = AdAccount(fbid=object_id).create_campaign(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_custom_audience_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Custom Audience for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_custom_audience result
    """
    result = AdAccount(fbid=object_id).create_custom_audience(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_custom_audiences_to_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Custom Audiences To for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_custom_audiences_to result
    """
    result = AdAccount(fbid=object_id).create_custom_audiences_to(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_custom_conversion_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Custom Conversion for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_custom_conversion result
    """
    result = AdAccount(fbid=object_id).create_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_audience_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product Audience for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product_audience result
    """
    result = AdAccount(fbid=object_id).create_product_audience(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_publisher_block_list_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Publisher Block List for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_publisher_block_list result
    """
    result = AdAccount(fbid=object_id).create_publisher_block_list(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_reach_frequency_prediction_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Reach Frequency Prediction for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_reach_frequency_prediction result
    """
    result = AdAccount(fbid=object_id).create_reach_frequency_prediction(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_recommendation_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Recommendation for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_recommendation result
    """
    result = AdAccount(fbid=object_id).create_recommendation(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscribed_app_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Subscribed App for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_subscribed_app result
    """
    result = AdAccount(fbid=object_id).create_subscribed_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_tracking_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Tracking for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_tracking result
    """
    result = AdAccount(fbid=object_id).create_tracking(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_value_rule_set_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Value Rule Set for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_value_rule_set result
    """
    result = AdAccount(fbid=object_id).create_value_rule_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_ad_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Video Ad for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video_ad result
    """
    result = AdAccount(fbid=object_id).create_video_ad(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad_images_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Ad Images for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_ad_images result
    """
    result = AdAccount(fbid=object_id).delete_ad_images(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad_videos_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Ad Videos for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_ad_videos result
    """
    result = AdAccount(fbid=object_id).delete_ad_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_agencies_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Agencies for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_agencies result
    """
    result = AdAccount(fbid=object_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_assigned_users_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Assigned Users for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_assigned_users result
    """
    result = AdAccount(fbid=object_id).delete_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_campaigns_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Campaigns for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_campaigns result
    """
    result = AdAccount(fbid=object_id).delete_campaigns(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_subscribed_apps_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Subscribed Apps for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_subscribed_apps result
    """
    result = AdAccount(fbid=object_id).delete_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_users_of_any_audience_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Users Of Any Audience for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_users_of_any_audience result
    """
    result = AdAccount(fbid=object_id).delete_users_of_any_audience(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_account_controls_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Account Controls for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_account_controls result
    """
    result = AdAccount(fbid=object_id).get_account_controls(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_activities_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Activities for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_activities result
    """
    result = AdAccount(fbid=object_id).get_activities(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_cloud_playables_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Cloud Playables for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_cloud_playables result
    """
    result = AdAccount(fbid=object_id).get_ad_cloud_playables(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_creatives_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Creatives for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_creatives result
    """
    result = AdAccount(fbid=object_id).get_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_creatives_by_labels_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Creatives By Labels for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_creatives_by_labels result
    """
    result = AdAccount(fbid=object_id).get_ad_creatives_by_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_images_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Images for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_images result
    """
    result = AdAccount(fbid=object_id).get_ad_images(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_labels_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Labels for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_labels result
    """
    result = AdAccount(fbid=object_id).get_ad_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_place_page_sets_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Place Page Sets for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_place_page_sets result
    """
    result = AdAccount(fbid=object_id).get_ad_place_page_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_playables_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Playables for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_playables result
    """
    result = AdAccount(fbid=object_id).get_ad_playables(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_rules_history_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Rules History for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_rules_history result
    """
    result = AdAccount(fbid=object_id).get_ad_rules_history(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_rules_library_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Rules Library for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_rules_library result
    """
    result = AdAccount(fbid=object_id).get_ad_rules_library(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_saved_keywords_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Saved Keywords for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_saved_keywords result
    """
    result = AdAccount(fbid=object_id).get_ad_saved_keywords(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Sets for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_sets result
    """
    result = AdAccount(fbid=object_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets_by_labels_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Sets By Labels for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_sets_by_labels result
    """
    result = AdAccount(fbid=object_id).get_ad_sets_by_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_studies_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Studies for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_studies result
    """
    result = AdAccount(fbid=object_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_videos_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Videos for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_videos result
    """
    result = AdAccount(fbid=object_id).get_ad_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads result
    """
    result = AdAccount(fbid=object_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_by_labels_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads By Labels for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_by_labels result
    """
    result = AdAccount(fbid=object_id).get_ads_by_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_pixels_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads Pixels for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_pixels result
    """
    result = AdAccount(fbid=object_id).get_ads_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_reporting_mmm_reports_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads Reporting Mmm Reports for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_reporting_mmm_reports result
    """
    result = AdAccount(fbid=object_id).get_ads_reporting_mmm_reports(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_reporting_mmm_schedulers_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads Reporting Mmm Schedulers for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_reporting_mmm_schedulers result
    """
    result = AdAccount(fbid=object_id).get_ads_reporting_mmm_schedulers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_volume_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads Volume for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_volume result
    """
    result = AdAccount(fbid=object_id).get_ads_volume(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_advertisable_applications_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Advertisable Applications for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_advertisable_applications result
    """
    result = AdAccount(fbid=object_id).get_advertisable_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_affected_ad_sets_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Affected Ad Sets for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_affected_ad_sets result
    """
    result = AdAccount(fbid=object_id).get_affected_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Agencies for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
    result = AdAccount(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_applications_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Applications for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_applications result
    """
    result = AdAccount(fbid=object_id).get_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Users for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_users result
    """
    result = AdAccount(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_async_ad_creatives_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Async Ad Creatives for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_async_ad_creatives result
    """
    result = AdAccount(fbid=object_id).get_async_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_async_ad_request_sets_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Async Ad Request Sets for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_async_ad_request_sets result
    """
    result = AdAccount(fbid=object_id).get_async_ad_request_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_async_requests_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Async Requests for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_async_requests result
    """
    result = AdAccount(fbid=object_id).get_async_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_audience_funnel_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Audience Funnel for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_audience_funnel result
    """
    result = AdAccount(fbid=object_id).get_audience_funnel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_broad_targeting_categories_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Broad Targeting Categories for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_broad_targeting_categories result
    """
    result = AdAccount(fbid=object_id).get_broad_targeting_categories(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_projects_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Business Projects for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_projects result
    """
    result = AdAccount(fbid=object_id).get_business_projects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaigns_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Campaigns for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_campaigns result
    """
    result = AdAccount(fbid=object_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaigns_by_labels_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Campaigns By Labels for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_campaigns_by_labels result
    """
    result = AdAccount(fbid=object_id).get_campaigns_by_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_connected_instagram_accounts_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Connected Instagram Accounts for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_connected_instagram_accounts result
    """
    result = AdAccount(fbid=object_id).get_connected_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_connected_instagram_accounts_with_iabp_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Connected Instagram Accounts With Iabp for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_connected_instagram_accounts_with_iabp result
    """
    result = AdAccount(fbid=object_id).get_connected_instagram_accounts_with_iabp(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_conversion_goals_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Conversion Goals for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_conversion_goals result
    """
    result = AdAccount(fbid=object_id).get_conversion_goals(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_audiences_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Custom Audiences for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_audiences result
    """
    result = AdAccount(fbid=object_id).get_custom_audiences(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_audiences_tos_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Custom Audiences Tos for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_audiences_tos result
    """
    result = AdAccount(fbid=object_id).get_custom_audiences_tos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_conversions_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Custom Conversions for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_conversions result
    """
    result = AdAccount(fbid=object_id).get_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_delivery_estimate_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Delivery Estimate for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_delivery_estimate result
    """
    result = AdAccount(fbid=object_id).get_delivery_estimate(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_deprecated_targeting_ad_sets_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Deprecated Targeting Ad Sets for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_deprecated_targeting_ad_sets result
    """
    result = AdAccount(fbid=object_id).get_deprecated_targeting_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dsa_recommendations_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Dsa Recommendations for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_dsa_recommendations result
    """
    result = AdAccount(fbid=object_id).get_dsa_recommendations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_generate_previews_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Generate Previews for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_generate_previews result
    """
    result = AdAccount(fbid=object_id).get_generate_previews(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_impacting_ad_studies_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Impacting Ad Studies for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_impacting_ad_studies result
    """
    result = AdAccount(fbid=object_id).get_impacting_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = AdAccount(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_async_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights Async for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights_async result
    """
    result = AdAccount(fbid=object_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_accounts_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Instagram Accounts for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_instagram_accounts result
    """
    result = AdAccount(fbid=object_id).get_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ios_fourteen_campaign_limits_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ios Fourteen Campaign Limits for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ios_fourteen_campaign_limits result
    """
    result = AdAccount(fbid=object_id).get_ios_fourteen_campaign_limits(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_matched_search_applications_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Matched Search Applications for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_matched_search_applications result
    """
    result = AdAccount(fbid=object_id).get_matched_search_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_max_bid_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Max Bid for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_max_bid result
    """
    result = AdAccount(fbid=object_id).get_max_bid(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_mcme_conversions_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Mcme Conversions for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_mcme_conversions result
    """
    result = AdAccount(fbid=object_id).get_mcme_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_minimum_budgets_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Minimum Budgets for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_minimum_budgets result
    """
    result = AdAccount(fbid=object_id).get_minimum_budgets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_on_behalf_requests_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get On Behalf Requests for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_on_behalf_requests result
    """
    result = AdAccount(fbid=object_id).get_on_behalf_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_promote_pages_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Promote Pages for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_promote_pages result
    """
    result = AdAccount(fbid=object_id).get_promote_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_publisher_block_lists_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Publisher Block Lists for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_publisher_block_lists result
    """
    result = AdAccount(fbid=object_id).get_publisher_block_lists(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reach_estimate_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Reach Estimate for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_reach_estimate result
    """
    result = AdAccount(fbid=object_id).get_reach_estimate(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reach_frequency_predictions_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Reach Frequency Predictions for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_reach_frequency_predictions result
    """
    result = AdAccount(fbid=object_id).get_reach_frequency_predictions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_recommendations_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Recommendations for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_recommendations result
    """
    result = AdAccount(fbid=object_id).get_recommendations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_saved_audiences_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Saved Audiences for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_saved_audiences result
    """
    result = AdAccount(fbid=object_id).get_saved_audiences(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscribed_apps_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Subscribed Apps for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_subscribed_apps result
    """
    result = AdAccount(fbid=object_id).get_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_browse_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Targeting Browse for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_targeting_browse result
    """
    result = AdAccount(fbid=object_id).get_targeting_browse(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_search_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Targeting Search for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_targeting_search result
    """
    result = AdAccount(fbid=object_id).get_targeting_search(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_sentence_lines_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Targeting Sentence Lines for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_targeting_sentence_lines result
    """
    result = AdAccount(fbid=object_id).get_targeting_sentence_lines(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_suggestions_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Targeting Suggestions for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_targeting_suggestions result
    """
    result = AdAccount(fbid=object_id).get_targeting_suggestions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_valid_a_t_i_on_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Targeting Valid A T I On for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_targeting_valid_a_t_i_on result
    """
    result = AdAccount(fbid=object_id).get_targeting_valid_a_t_i_on(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tracking_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Tracking for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tracking result
    """
    result = AdAccount(fbid=object_id).get_tracking(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_users_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Users for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_users result
    """
    result = AdAccount(fbid=object_id).get_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_value_rule_set_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Value Rule Set for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_value_rule_set result
    """
    result = AdAccount(fbid=object_id).get_value_rule_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_video_ads_for_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Video Ads for AdAccount.

    Args:
        object_id: The ID of the AdAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_video_ads result
    """
    result = AdAccount(fbid=object_id).get_video_ads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccount_server = mcp
