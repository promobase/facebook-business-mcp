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


# ---- Edge Methods (109) ----
@adaccount_server.tool
@wrapped_fn_tool
def get_account_controls(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_account_controls(fields=fields, params=params)


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
def get_ad_place_page_sets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_place_page_sets(fields=fields, params=params)


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
def get_ad_studies(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ad_studies(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adcloudplayables(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adcloudplayables(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adcreatives(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adcreatives(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_adcreative(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_adcreative(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adcreativesbylabels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adcreativesbylabels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_adimages(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_adimages(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adimages(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adimages(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_adimage(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_adimage(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adlabels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adlabels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_adlabel(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_adlabel(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adplayables(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adplayables(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_adplayable(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_adplayable(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adrules_history(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adrules_history(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adrules_library(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adrules_library(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_adrules_library(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_adrules_library(fields=fields, params=params)


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
def get_ads_reporting_mmm_schedulers(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_ads_reporting_mmm_schedulers(fields=fields, params=params)


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
def get_adsbylabels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adsbylabels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adsets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adsets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_adset(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_adset(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adsetsbylabels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adsetsbylabels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_adspixels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_adspixels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_adspixel(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_adspixel(fields=fields, params=params)


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
def delete_advideos(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_advideos(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_advideos(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_advideos(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_advideo(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_advideo(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_affectedadsets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_affectedadsets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_agencies(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_agencies(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_agencies(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_agencies(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_agencie(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_agencie(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_applications(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_applications(fields=fields, params=params)


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
def get_asyncadcreatives(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_asyncadcreatives(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_asyncadcreative(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_asyncadcreative(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_asyncadrequestsets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_asyncadrequestsets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_asyncadrequestset(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_asyncadrequestset(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_audience_funnel(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_audience_funnel(fields=fields, params=params)


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
def get_broadtargetingcategories(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_broadtargetingcategories(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_businessprojects(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_businessprojects(fields=fields, params=params)


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
def get_campaignsbylabels(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_campaignsbylabels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_connected_instagram_accounts(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_connected_instagram_accounts(fields=fields, params=params)


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
def get_conversion_goals(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_conversion_goals(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_customaudiences(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_customaudiences(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_customaudience(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_customaudience(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_customaudiencestos(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_customaudiencestos(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_customaudiencesto(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_customaudiencesto(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_customconversions(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_customconversions(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_customconversion(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_customconversion(fields=fields, params=params)


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
def get_deprecatedtargetingadsets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_deprecatedtargetingadsets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_dsa_recommendations(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_dsa_recommendations(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_generatepreviews(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_generatepreviews(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_impacting_ad_studies(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_impacting_ad_studies(fields=fields, params=params)


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
def create_insight(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_insight(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_instagram_accounts(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_instagram_accounts(fields=fields, params=params)


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
def get_max_bid(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_max_bid(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_mcmeconversions(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_mcmeconversions(fields=fields, params=params)


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
def get_onbehalf_requests(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_onbehalf_requests(fields=fields, params=params)


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
def get_promote_pages(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_promote_pages(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_publisher_block_lists(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_publisher_block_lists(fields=fields, params=params)


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
def get_reachestimate(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_reachestimate(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_reachfrequencypredictions(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_reachfrequencypredictions(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_reachfrequencyprediction(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).create_reachfrequencyprediction(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_recommendations(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_recommendations(fields=fields, params=params)


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
def get_subscribed_apps(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_subscribed_apps(fields=fields, params=params)


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
def get_targetingbrowse(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targetingbrowse(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targetingsearch(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targetingsearch(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targetingsentencelines(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targetingsentencelines(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targetingsuggestions(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targetingsuggestions(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targetingvalidation(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_targetingvalidation(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_tracking(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_tracking(fields=fields, params=params)


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
def get_users(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).get_users(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_usersofanyaudience(
    adaccount_id: str,
    params: dict[str, Any] = {},
):
    return AdAccount(adaccount_id).delete_usersofanyaudience(params=params)


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
