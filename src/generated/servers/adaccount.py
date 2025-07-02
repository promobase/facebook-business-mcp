"""
Auto-generated MCP server for Facebook AdAccount.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccount")


# CRUD Operations


@mcp.tool()
async def create_adaccount(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccount(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccount(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
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
    result = AdAccount(fbid=object_id).get_video_ads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccount_server = mcp
