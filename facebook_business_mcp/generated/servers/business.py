"""
Auto-generated MCP server for Facebook Business.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.business import Business
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-business")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    business_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_access_token(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_access_token(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ad_network_analytic(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_ad_network_analytic(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ad_network_application(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_ad_network_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ad_review_request(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_ad_review_request(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ad_study(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_ad_study(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_add_phone_number(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_add_phone_number(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ads_data_set(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_ads_data_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ads_pixel(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_ads_pixel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_block_list_draft(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_block_list_draft(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_bm_review_request(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_bm_review_request(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_business_user(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_business_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_claim_custom_conversion(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_claim_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_client_app(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_client_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_client_page(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_client_page(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_collaborative_ads_collaboration_request(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_collaborative_ads_collaboration_request(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_cpas_business_setup_config(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_cpas_business_setup_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_creative_folder(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_creative_folder(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_custom_conversion(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_event_source_group(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_event_source_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_image(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_image(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_managed_business(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_managed_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_managed_partner_business(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_managed_partner_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_managed_partner_business_setup(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_managed_partner_business_setup(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_onboard_partners_to_mm_lite(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_onboard_partners_to_mm_lite(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_open_bridge_configuration(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_open_bridge_configuration(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_owned_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_owned_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_owned_app(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_owned_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_owned_business(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_owned_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_owned_page(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_owned_page(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_owned_product_catalog(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_owned_product_catalog(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_partner_premium_option(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_partner_premium_option(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_pixel_to(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_pixel_to(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_self_certify_whats_app_business(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_self_certify_whats_app_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_setup_managed_partner_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_setup_managed_partner_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_share_pre_verified_number(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_share_pre_verified_number(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_system_user(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_system_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_system_user_access_token(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_system_user_access_token(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_video(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_agencies(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_clients(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_clients(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_instagram_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_managed_businesses(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_managed_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_managed_partner_businesses(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_managed_partner_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_owned_businesses(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_owned_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_share_pre_verified_numbers(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).delete_share_pre_verified_numbers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_account_infos(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ad_account_infos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_network_analytics(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ad_network_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_network_analytics_results(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ad_network_analytics_results(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_studies(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ads_dataset(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ads_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ads_pixels(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ads_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ads_reporting_mmm_reports(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ads_reporting_mmm_reports(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ads_reporting_mmm_schedulers(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_ads_reporting_mmm_schedulers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_agencies(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_an_placements(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_an_placements(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_business_asset_groups(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_business_invoices(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_business_invoices(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_business_projects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_business_projects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_business_users(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_business_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_client_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_client_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_client_apps(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_client_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_client_offsite_signal_container_business_objects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_client_offsite_signal_container_business_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_client_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_client_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_client_pixels(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_client_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_client_product_catalogs(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_client_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_client_whats_app_business_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_client_whats_app_business_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_clients(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_clients(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_collaborative_ads_collaboration_requests(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_collaborative_ads_collaboration_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_collaborative_ads_suggested_partners(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_collaborative_ads_suggested_partners(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_commerce_merchant_settings(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_commerce_merchant_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_cpas_business_setup_config(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_cpas_business_setup_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_cpas_merchant_config(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_cpas_merchant_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_credit_cards(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_credit_cards(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_event_source_groups(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_event_source_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_extended_credit_applications(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_extended_credit_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_extended_credits(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_extended_credits(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_initiated_audience_sharing_requests(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_initiated_audience_sharing_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_instagram_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_instagram_business_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_instagram_business_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_managed_partner_ads_funding_source_details(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_managed_partner_ads_funding_source_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_open_bridge_configurations(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_open_bridge_configurations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_apps(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_businesses(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_instagram_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_offsite_signal_container_business_objects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_offsite_signal_container_business_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_pixels(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_product_catalogs(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_owned_whats_app_business_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_owned_whats_app_business_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_partner_account_linking(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_partner_account_linking(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_passback_attribution_metadata_configs(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_passback_attribution_metadata_configs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pending_client_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_pending_client_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pending_client_apps(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_pending_client_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pending_client_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_pending_client_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pending_owned_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_pending_owned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pending_owned_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_pending_owned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pending_shared_offsite_signal_container_business_objects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(
        fbid=business_id
    ).get_pending_shared_offsite_signal_container_business_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pending_users(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_pending_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_picture(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pre_verified_numbers(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_pre_verified_numbers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_received_audience_sharing_requests(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_received_audience_sharing_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_reseller_guidances(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_reseller_guidances(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_self_certified_whats_app_business_submissions(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_self_certified_whats_app_business_submissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_system_users(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_system_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_third_party_measurement_report_dataset(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Business(fbid=business_id).get_third_party_measurement_report_dataset(
        fields=fields,
        params=params,
    )

    return result


# Export the server
business_server = mcp
