"""AdAccount MCP Server."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

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
@adaccount_server.tool
@wrapped_fn_tool
def get_adaccount(
    adaccount_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdAccount(adaccount_id)
    return obj.api_get(fields=fields)


@adaccount_server.tool
@wrapped_fn_tool
def update_adaccount(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(adaccount_id).api_update(fields=fields, params=params)


# ---- Edge Methods (80) ----
@adaccount_server.tool
@wrapped_fn_tool
def create_account_control(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_account_control(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_activities(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_activities(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_place_page_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_place_page_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_place_page_sets_async(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_place_page_sets_async(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_saved_keywords(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_saved_keywords(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_creative(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_creative(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_creatives_by_labels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_creatives_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_ad_images(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_ad_images(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_images(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_images(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_image(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_image(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_label(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_label(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_playable(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_playable(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_rules_history(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_rules_history(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_rules_library(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_rules_library(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ads(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_reporting_mmm_reports(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ads_reporting_mmm_reports(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_volume(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ads_volume(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_by_labels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ads_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_sets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_sets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_sets_by_labels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_sets_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_pixels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ads_pixels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ads_pixel(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ads_pixel(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_advertisable_applications(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_advertisable_applications(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_ad_videos(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_ad_videos(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_videos(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_videos(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_video(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_ad_video(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_agencies(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_agencies(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_agency(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_agency(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_assigned_users(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_assigned_users(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_assigned_users(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_assigned_user(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_assigned_user(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_async_batch_request(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_async_batch_request(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_async_requests(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_async_requests(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_async_ad_creatives(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_async_ad_creatives(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_async_ad_creative(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_async_ad_creative(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_async_ad_request_sets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_async_ad_request_sets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_async_ad_request_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_async_ad_request_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_block_list_draft(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_block_list_draft(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_brand_safety_content_filter_level(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_brand_safety_content_filter_level(
        fields=fields, params=params
    )


@adaccount_server.tool
@wrapped_fn_tool
def get_broad_targeting_categories(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_broad_targeting_categories(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_business_projects(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_business_projects(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_campaigns(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_campaigns(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_campaigns(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_campaigns(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_campaign(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_campaign(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_campaigns_by_labels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_campaigns_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_connected_instagram_accounts_with_iabp(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_connected_instagram_accounts_with_iabp(
        fields=fields, params=params
    )


@adaccount_server.tool
@wrapped_fn_tool
def get_custom_audiences(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_custom_audiences(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_custom_audience(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_custom_audience(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_custom_audiences_to(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_custom_audiences_to(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_custom_conversion(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_custom_conversion(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_delivery_estimate(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_delivery_estimate(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_deprecated_targeting_ad_sets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_deprecated_targeting_ad_sets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_generate_previews(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_generate_previews(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_insights(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_insights(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_insights_async(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_insights_async(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ios_fourteen_campaign_limits(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ios_fourteen_campaign_limits(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_matched_search_applications(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_matched_search_applications(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_minimum_budgets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_minimum_budgets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_on_behalf_requests(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_on_behalf_requests(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_product_audience(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_product_audience(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_publisher_block_list(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_publisher_block_list(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_reach_estimate(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_reach_estimate(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_reach_frequency_prediction(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_reach_frequency_prediction(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_recommendation(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_recommendation(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_saved_audiences(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_saved_audiences(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_subscribed_apps(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_subscribed_apps(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_subscribed_app(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_browse(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targeting_browse(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_search(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targeting_search(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_sentence_lines(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targeting_sentence_lines(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_suggestions(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targeting_suggestions(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_valid_a_t_i_on(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targeting_valid_a_t_i_on(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_tracking(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_tracking(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_users_of_any_audience(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_users_of_any_audience(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_value_rule_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_value_rule_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_value_rule_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_value_rule_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_video_ads(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_video_ads(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_video_ad(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_video_ad(fields=fields, params=params)
