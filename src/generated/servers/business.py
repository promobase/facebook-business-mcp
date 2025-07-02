"""
Auto-generated MCP server for Facebook Business.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.business import Business
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-business")


# CRUD Operations


@mcp.tool()
async def create_business(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_access_token_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_access_token(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_account_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_network_analytic_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_ad_network_analytic(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_network_application_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_ad_network_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_review_request_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_ad_review_request(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_study_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_ad_study(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_add_phone_number_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_add_phone_number(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ads_data_set_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_ads_data_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ads_pixel_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_ads_pixel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_block_list_draft_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_block_list_draft(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_bm_review_request_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_bm_review_request(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_business_user_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_business_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_claim_custom_conversion_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_claim_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_client_app_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_client_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_client_page_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_client_page(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_collaborative_ads_collaboration_request_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_collaborative_ads_collaboration_request(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_cpas_business_setup_config_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_cpas_business_setup_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_creative_folder_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_creative_folder(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_custom_conversion_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_event_source_group_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_event_source_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_image_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_image(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_managed_business_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_managed_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_managed_partner_business_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_managed_partner_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_managed_partner_business_setup_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_managed_partner_business_setup(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_onboard_partners_to_mm_lite_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_onboard_partners_to_mm_lite(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_open_bridge_configuration_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_open_bridge_configuration(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_owned_ad_account_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_owned_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_owned_app_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_owned_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_owned_business_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_owned_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_owned_page_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_owned_page(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_owned_product_catalog_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_owned_product_catalog(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_partner_premium_option_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_partner_premium_option(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_pixel_to_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_pixel_to(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_self_certify_whats_app_business_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_self_certify_whats_app_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_setup_managed_partner_ad_account_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_setup_managed_partner_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_share_pre_verified_number_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_share_pre_verified_number(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_system_user_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_system_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_system_user_access_token_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_system_user_access_token(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_agencies_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_clients_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_clients(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_instagram_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_managed_businesses_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_managed_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_managed_partner_businesses_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_managed_partner_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_owned_businesses_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_owned_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_pages_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_share_pre_verified_numbers_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).delete_share_pre_verified_numbers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_account_infos_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ad_account_infos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ad_network_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics_results_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ad_network_analytics_results(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_studies_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_dataset_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ads_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_pixels_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ads_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_reporting_mmm_reports_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ads_reporting_mmm_reports(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_reporting_mmm_schedulers_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_ads_reporting_mmm_schedulers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_an_placements_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_an_placements(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_asset_groups_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_invoices_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_business_invoices(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_projects_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_business_projects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_users_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_business_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_client_ad_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_client_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_client_apps_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_client_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_client_offsite_signal_container_business_objects_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_client_offsite_signal_container_business_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_client_pages_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_client_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_client_pixels_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_client_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_client_product_catalogs_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_client_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_client_whats_app_business_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_client_whats_app_business_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_clients_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_clients(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_collaborative_ads_collaboration_requests_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_collaborative_ads_collaboration_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_collaborative_ads_suggested_partners_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_collaborative_ads_suggested_partners(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_merchant_settings_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_commerce_merchant_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cpas_business_setup_config_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_cpas_business_setup_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cpas_merchant_config_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_cpas_merchant_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_credit_cards_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_credit_cards(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_event_source_groups_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_event_source_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_extended_credit_applications_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_extended_credit_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_extended_credits_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_extended_credits(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_initiated_audience_sharing_requests_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_initiated_audience_sharing_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_business_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_instagram_business_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_managed_partner_ads_funding_source_details_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_managed_partner_ads_funding_source_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_open_bridge_configurations_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_open_bridge_configurations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_ad_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_apps_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_businesses_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_instagram_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_offsite_signal_container_business_objects_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_offsite_signal_container_business_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_pages_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_pixels_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_product_catalogs_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owned_whats_app_business_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_owned_whats_app_business_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partner_account_linking_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_partner_account_linking(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_passback_attribution_metadata_configs_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_passback_attribution_metadata_configs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pending_client_ad_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pending_client_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pending_client_apps_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pending_client_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pending_client_pages_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pending_client_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pending_owned_ad_accounts_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pending_owned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pending_owned_pages_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pending_owned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pending_shared_offsite_signal_container_business_objects_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pending_shared_offsite_signal_container_business_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pending_users_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pending_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_picture_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pre_verified_numbers_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_pre_verified_numbers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_received_audience_sharing_requests_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_received_audience_sharing_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reseller_guidances_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_reseller_guidances(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_self_certified_whats_app_business_submissions_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_self_certified_whats_app_business_submissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_system_users_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_system_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_third_party_measurement_report_dataset_for_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Business(fbid=object_id).get_third_party_measurement_report_dataset(
        fields=fields,
        params=params,
    )

    return result


# Export the server
business_server = mcp
