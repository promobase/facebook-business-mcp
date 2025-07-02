"""Business MCP Server."""

from typing import Any

from facebook_business.adobjects.business import Business
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusiness"
instructions = """
Business MCP Server for Facebook Business API.

Provides typed access to all Business operations.
"""

business_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@business_server.tool
@wrapped_fn_tool
def get_business(
    business_id: str,
    fields: list[str] = [],
) -> str:
    obj = Business(business_id)
    return obj.api_get(fields=fields)


@business_server.tool
@wrapped_fn_tool
def update_business(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Business(business_id).api_update(fields=fields, params=params)


# ---- Edge Methods (109) ----
@business_server.tool
@wrapped_fn_tool
def create_access_token(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_access_token(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ad_account_infos(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_ad_account_infos(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_ad_accounts(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_ad_accounts(params=params)


@business_server.tool
@wrapped_fn_tool
def create_ad_review_request(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_ad_review_request(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ad_studies(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_ad_studies(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ad_studie(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_ad_studie(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_adaccount(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_adaccount(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_add_phone_number(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_add_phone_number(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_adnetwork_application(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_adnetwork_application(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_adnetworkanalytics(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_adnetworkanalytics(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_adnetworkanalytic(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_adnetworkanalytic(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_adnetworkanalytics_results(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_adnetworkanalytics_results(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ads_dataset(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_ads_dataset(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ads_dataset(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_ads_dataset(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ads_reporting_mmm_reports(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_ads_reporting_mmm_reports(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ads_reporting_mmm_schedulers(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_ads_reporting_mmm_schedulers(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_adspixels(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_adspixels(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_adspixel(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_adspixel(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_agencies(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_agencies(params=params)


@business_server.tool
@wrapped_fn_tool
def get_agencies(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_agencies(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_an_placements(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_an_placements(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_block_list_draft(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_block_list_draft(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_bm_review_request(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_bm_review_request(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_business_asset_groups(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_business_asset_groups(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_business_invoices(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_business_invoices(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_business_users(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_business_users(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_business_user(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_business_user(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_businessprojects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_businessprojects(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_claim_custom_conversion(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_claim_custom_conversion(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_client_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_client_ad_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_client_apps(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_client_apps(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_client_app(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_client_app(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_client_offsite_signal_container_business_objects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_client_offsite_signal_container_business_objects(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_client_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_client_pages(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_client_page(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_client_page(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_client_pixels(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_client_pixels(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_client_product_catalogs(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_client_product_catalogs(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_client_whatsapp_business_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_client_whatsapp_business_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_clients(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_clients(params=params)


@business_server.tool
@wrapped_fn_tool
def get_clients(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_clients(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_collaborative_ads_collaboration_requests(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_collaborative_ads_collaboration_requests(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_collaborative_ads_collaboration_request(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_collaborative_ads_collaboration_request(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_collaborative_ads_suggested_partners(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_collaborative_ads_suggested_partners(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_commerce_merchant_settings(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_commerce_merchant_settings(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_cpas_business_setup_config(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_cpas_business_setup_config(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_cpas_business_setup_config(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_cpas_business_setup_config(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_cpas_merchant_config(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_cpas_merchant_config(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_creative_folder(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_creative_folder(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_creditcards(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_creditcards(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_customconversion(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_customconversion(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_event_source_groups(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_event_source_groups(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_event_source_group(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_event_source_group(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_extendedcreditapplications(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_extendedcreditapplications(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_extendedcredits(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_extendedcredits(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_image(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_image(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_initiated_audience_sharing_requests(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_initiated_audience_sharing_requests(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def delete_instagram_accounts(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_instagram_accounts(params=params)


@business_server.tool
@wrapped_fn_tool
def get_instagram_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_instagram_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_instagram_business_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_instagram_business_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_managed_businesses(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_managed_businesses(params=params)


@business_server.tool
@wrapped_fn_tool
def create_managed_businesse(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_managed_businesse(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_managed_partner_ads_funding_source_details(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_managed_partner_ads_funding_source_details(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_managed_partner_business_setup(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_managed_partner_business_setup(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_managed_partner_businesses(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_managed_partner_businesses(params=params)


@business_server.tool
@wrapped_fn_tool
def create_managed_partner_businesse(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_managed_partner_businesse(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_onboard_partners_to_mm_lite(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_onboard_partners_to_mm_lite(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_openbridge_configurations(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_openbridge_configurations(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_openbridge_configuration(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_openbridge_configuration(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_ad_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_owned_ad_account(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_apps(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_apps(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_app(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_owned_app(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_owned_businesses(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_owned_businesses(params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_businesses(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_businesses(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_businesse(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_owned_businesse(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_instagram_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_instagram_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_offsite_signal_container_business_objects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_offsite_signal_container_business_objects(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_owned_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_pages(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_page(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_owned_page(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_pixels(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_pixels(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_product_catalogs(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_product_catalogs(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_product_catalog(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_owned_product_catalog(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_whatsapp_business_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_owned_whatsapp_business_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_pages(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_pages(params=params)


@business_server.tool
@wrapped_fn_tool
def get_partner_account_linking(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_partner_account_linking(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_partner_premium_option(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_partner_premium_option(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_passback_attribution_metadata_configs(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_passback_attribution_metadata_configs(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_pending_client_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_pending_client_ad_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_pending_client_apps(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_pending_client_apps(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_pending_client_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_pending_client_pages(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_pending_owned_ad_accounts(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_pending_owned_ad_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_pending_owned_pages(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_pending_owned_pages(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_pending_shared_offsite_signal_container_business_objects(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_pending_shared_offsite_signal_container_business_objects(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_pending_users(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_pending_users(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_picture(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_picture(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_pixel_to(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_pixel_to(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_preverified_numbers(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_preverified_numbers(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_received_audience_sharing_requests(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_received_audience_sharing_requests(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_reseller_guidances(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_reseller_guidances(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_self_certified_whatsapp_business_submissions(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_self_certified_whatsapp_business_submissions(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_self_certify_whatsapp_busine(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_self_certify_whatsapp_busine(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_setup_managed_partner_adaccount(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_setup_managed_partner_adaccount(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def delete_share_preverified_numbers(
    business_id: str,
    params: dict[str, Any] = {},
):
    return Business(business_id).delete_share_preverified_numbers(params=params)


@business_server.tool
@wrapped_fn_tool
def create_share_preverified_number(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_share_preverified_number(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_system_user_access_token(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_system_user_access_token(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_system_users(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_system_users(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_system_user(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_system_user(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_third_party_measurement_report_dataset(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).get_third_party_measurement_report_dataset(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_video(
    business_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Business(business_id).create_video(fields=fields, params=params)
