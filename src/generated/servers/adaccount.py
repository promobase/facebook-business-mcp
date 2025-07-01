"""Streamlined AdAccount MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from src.generated.models.adaccount import AdAccountField, AdAccountUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccount"
instructions = """
AdAccount MCP Server for Facebook Business API.

Provides typed access to all AdAccount operations.
"""

adaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@wrapped_fn_tool
def get_adaccount(
    adaccount_id: str,
    fields: list[AdAccountField] = [],
) -> str:
    """Get a AdAccount object by ID.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
    """
    obj = AdAccount(adaccount_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_adaccount(
    adaccount_id: str,
    fields: list[AdAccountField] = [],
    params: AdAccountUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdAccount object.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdAccount(adaccount_id).api_update(fields=fields, params=params)


# ---- Edge Methods (80) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.adaccount_wrappers import (
    create_account_control,
    create_ad,
    create_ad_creative,
    create_ad_image,
    create_ad_label,
    create_ad_place_page_set,
    create_ad_place_page_sets_async,
    create_ad_playable,
    create_ad_rules_library,
    create_ad_set,
    create_ad_video,
    create_ads_pixel,
    create_agency,
    create_assigned_user,
    create_async_ad_creative,
    create_async_ad_request_set,
    create_async_batch_request,
    create_block_list_draft,
    create_brand_safety_content_filter_level,
    create_campaign,
    create_custom_audience,
    create_custom_audiences_to,
    create_custom_conversion,
    create_product_audience,
    create_publisher_block_list,
    create_reach_frequency_prediction,
    create_recommendation,
    create_subscribed_app,
    create_tracking,
    create_value_rule_set,
    create_video_ad,
    delete_ad_images,
    delete_ad_videos,
    delete_agencies,
    delete_assigned_users,
    delete_campaigns,
    delete_subscribed_apps,
    delete_users_of_any_audience,
    get_activities,
    get_ad_creatives_by_labels,
    get_ad_images,
    get_ad_rules_history,
    get_ad_saved_keywords,
    get_ad_sets,
    get_ad_sets_by_labels,
    get_ad_videos,
    get_ads,
    get_ads_by_labels,
    get_ads_pixels,
    get_ads_reporting_mmm_reports,
    get_ads_volume,
    get_advertisable_applications,
    get_assigned_users,
    get_async_ad_creatives,
    get_async_ad_request_sets,
    get_async_requests,
    get_broad_targeting_categories,
    get_business_projects,
    get_campaigns,
    get_campaigns_by_labels,
    get_connected_instagram_accounts_with_iabp,
    get_custom_audiences,
    get_delivery_estimate,
    get_deprecated_targeting_ad_sets,
    get_generate_previews,
    get_insights,
    get_insights_async,
    get_ios_fourteen_campaign_limits,
    get_matched_search_applications,
    get_minimum_budgets,
    get_on_behalf_requests,
    get_reach_estimate,
    get_saved_audiences,
    get_targeting_browse,
    get_targeting_search,
    get_targeting_sentence_lines,
    get_targeting_suggestions,
    get_targeting_valid_a_t_i_on,
    get_value_rule_set,
    get_video_ads,
)

# ---- Register tools ----
# Register CRUD operations
adaccount_server.tool(get_adaccount)
adaccount_server.tool(update_adaccount)

# Register edge methods from wrappers
adaccount_server.tool(create_account_control)
adaccount_server.tool(get_activities)
adaccount_server.tool(create_ad_place_page_set)
adaccount_server.tool(create_ad_place_page_sets_async)
adaccount_server.tool(get_ad_saved_keywords)
adaccount_server.tool(create_ad_creative)
adaccount_server.tool(get_ad_creatives_by_labels)
adaccount_server.tool(delete_ad_images)
adaccount_server.tool(get_ad_images)
adaccount_server.tool(create_ad_image)
adaccount_server.tool(create_ad_label)
adaccount_server.tool(create_ad_playable)
adaccount_server.tool(get_ad_rules_history)
adaccount_server.tool(create_ad_rules_library)
adaccount_server.tool(get_ads)
adaccount_server.tool(create_ad)
adaccount_server.tool(get_ads_reporting_mmm_reports)
adaccount_server.tool(get_ads_volume)
adaccount_server.tool(get_ads_by_labels)
adaccount_server.tool(get_ad_sets)
adaccount_server.tool(create_ad_set)
adaccount_server.tool(get_ad_sets_by_labels)
adaccount_server.tool(get_ads_pixels)
adaccount_server.tool(create_ads_pixel)
adaccount_server.tool(get_advertisable_applications)
adaccount_server.tool(delete_ad_videos)
adaccount_server.tool(get_ad_videos)
adaccount_server.tool(create_ad_video)
adaccount_server.tool(delete_agencies)
adaccount_server.tool(create_agency)
adaccount_server.tool(delete_assigned_users)
adaccount_server.tool(get_assigned_users)
adaccount_server.tool(create_assigned_user)
adaccount_server.tool(create_async_batch_request)
adaccount_server.tool(get_async_requests)
adaccount_server.tool(get_async_ad_creatives)
adaccount_server.tool(create_async_ad_creative)
adaccount_server.tool(get_async_ad_request_sets)
adaccount_server.tool(create_async_ad_request_set)
adaccount_server.tool(create_block_list_draft)
adaccount_server.tool(create_brand_safety_content_filter_level)
adaccount_server.tool(get_broad_targeting_categories)
adaccount_server.tool(get_business_projects)
adaccount_server.tool(delete_campaigns)
adaccount_server.tool(get_campaigns)
adaccount_server.tool(create_campaign)
adaccount_server.tool(get_campaigns_by_labels)
adaccount_server.tool(get_connected_instagram_accounts_with_iabp)
adaccount_server.tool(get_custom_audiences)
adaccount_server.tool(create_custom_audience)
adaccount_server.tool(create_custom_audiences_to)
adaccount_server.tool(create_custom_conversion)
adaccount_server.tool(get_delivery_estimate)
adaccount_server.tool(get_deprecated_targeting_ad_sets)
adaccount_server.tool(get_generate_previews)
adaccount_server.tool(get_insights)
adaccount_server.tool(get_insights_async)
adaccount_server.tool(get_ios_fourteen_campaign_limits)
adaccount_server.tool(get_matched_search_applications)
adaccount_server.tool(get_minimum_budgets)
adaccount_server.tool(get_on_behalf_requests)
adaccount_server.tool(create_product_audience)
adaccount_server.tool(create_publisher_block_list)
adaccount_server.tool(get_reach_estimate)
adaccount_server.tool(create_reach_frequency_prediction)
adaccount_server.tool(create_recommendation)
adaccount_server.tool(get_saved_audiences)
adaccount_server.tool(delete_subscribed_apps)
adaccount_server.tool(create_subscribed_app)
adaccount_server.tool(get_targeting_browse)
adaccount_server.tool(get_targeting_search)
adaccount_server.tool(get_targeting_sentence_lines)
adaccount_server.tool(get_targeting_suggestions)
adaccount_server.tool(get_targeting_valid_a_t_i_on)
adaccount_server.tool(create_tracking)
adaccount_server.tool(delete_users_of_any_audience)
adaccount_server.tool(get_value_rule_set)
adaccount_server.tool(create_value_rule_set)
adaccount_server.tool(get_video_ads)
adaccount_server.tool(create_video_ad)
