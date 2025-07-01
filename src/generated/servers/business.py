"""Streamlined Business MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.business import Business
from fastmcp import FastMCP

from src.generated.models.business import BusinessField, BusinessUpdateParams
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
@wrapped_fn_tool
def get_business(
    business_id: str,
    fields: list[BusinessField] = [],
) -> str:
    """Get a Business object by ID.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
    """
    obj = Business(business_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_business(
    business_id: str,
    fields: list[BusinessField] = [],
    params: BusinessUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a Business object.

    Args:
        business_id: The ID of the Business.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return Business(business_id).api_update(fields=fields, params=params)


# ---- Edge Methods (67) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.business_wrappers import (
    create_access_token,
    create_ad_account,
    create_ad_network_analytic,
    create_ad_network_application,
    create_ad_review_request,
    create_ad_study,
    create_add_phone_number,
    create_ads_data_set,
    create_ads_pixel,
    create_block_list_draft,
    create_bm_review_request,
    create_business_user,
    create_claim_custom_conversion,
    create_client_app,
    create_client_page,
    create_collaborative_ads_collaboration_request,
    create_cpas_business_setup_config,
    create_creative_folder,
    create_custom_conversion,
    create_event_source_group,
    create_image,
    create_managed_business,
    create_managed_partner_business,
    create_managed_partner_business_setup,
    create_onboard_partners_to_mm_lite,
    create_open_bridge_configuration,
    create_owned_ad_account,
    create_owned_app,
    create_owned_business,
    create_owned_page,
    create_owned_product_catalog,
    create_partner_premium_option,
    create_self_certify_whats_app_business,
    create_setup_managed_partner_ad_account,
    create_share_pre_verified_number,
    create_system_user,
    create_system_user_access_token,
    create_video,
    delete_ad_accounts,
    delete_agencies,
    delete_clients,
    delete_instagram_accounts,
    delete_managed_businesses,
    delete_managed_partner_businesses,
    delete_owned_businesses,
    delete_pages,
    delete_share_pre_verified_numbers,
    get_ad_account_infos,
    get_ad_network_analytics,
    get_ad_network_analytics_results,
    get_ads_dataset,
    get_ads_pixels,
    get_ads_reporting_mmm_reports,
    get_business_invoices,
    get_client_ad_accounts,
    get_collaborative_ads_collaboration_requests,
    get_extended_credit_applications,
    get_extended_credits,
    get_initiated_audience_sharing_requests,
    get_managed_partner_ads_funding_source_details,
    get_owned_ad_accounts,
    get_owned_businesses,
    get_pending_users,
    get_picture,
    get_pre_verified_numbers,
    get_received_audience_sharing_requests,
    get_self_certified_whats_app_business_submissions,
)

# ---- Register tools ----
# Register CRUD operations
business_server.tool(get_business)
business_server.tool(update_business)

# Register edge methods from wrappers
business_server.tool(create_access_token)
business_server.tool(get_ad_account_infos)
business_server.tool(delete_ad_accounts)
business_server.tool(create_ad_review_request)
business_server.tool(create_ad_study)
business_server.tool(create_ad_account)
business_server.tool(create_add_phone_number)
business_server.tool(create_ad_network_application)
business_server.tool(get_ad_network_analytics)
business_server.tool(create_ad_network_analytic)
business_server.tool(get_ad_network_analytics_results)
business_server.tool(get_ads_dataset)
business_server.tool(create_ads_data_set)
business_server.tool(get_ads_reporting_mmm_reports)
business_server.tool(get_ads_pixels)
business_server.tool(create_ads_pixel)
business_server.tool(delete_agencies)
business_server.tool(create_block_list_draft)
business_server.tool(create_bm_review_request)
business_server.tool(get_business_invoices)
business_server.tool(create_business_user)
business_server.tool(create_claim_custom_conversion)
business_server.tool(get_client_ad_accounts)
business_server.tool(create_client_app)
business_server.tool(create_client_page)
business_server.tool(delete_clients)
business_server.tool(get_collaborative_ads_collaboration_requests)
business_server.tool(create_collaborative_ads_collaboration_request)
business_server.tool(create_cpas_business_setup_config)
business_server.tool(create_creative_folder)
business_server.tool(create_custom_conversion)
business_server.tool(create_event_source_group)
business_server.tool(get_extended_credit_applications)
business_server.tool(get_extended_credits)
business_server.tool(create_image)
business_server.tool(get_initiated_audience_sharing_requests)
business_server.tool(delete_instagram_accounts)
business_server.tool(delete_managed_businesses)
business_server.tool(create_managed_business)
business_server.tool(get_managed_partner_ads_funding_source_details)
business_server.tool(create_managed_partner_business_setup)
business_server.tool(delete_managed_partner_businesses)
business_server.tool(create_managed_partner_business)
business_server.tool(create_onboard_partners_to_mm_lite)
business_server.tool(create_open_bridge_configuration)
business_server.tool(get_owned_ad_accounts)
business_server.tool(create_owned_ad_account)
business_server.tool(create_owned_app)
business_server.tool(delete_owned_businesses)
business_server.tool(get_owned_businesses)
business_server.tool(create_owned_business)
business_server.tool(create_owned_page)
business_server.tool(create_owned_product_catalog)
business_server.tool(delete_pages)
business_server.tool(create_partner_premium_option)
business_server.tool(get_pending_users)
business_server.tool(get_picture)
business_server.tool(get_pre_verified_numbers)
business_server.tool(get_received_audience_sharing_requests)
business_server.tool(get_self_certified_whats_app_business_submissions)
business_server.tool(create_self_certify_whats_app_business)
business_server.tool(create_setup_managed_partner_ad_account)
business_server.tool(delete_share_pre_verified_numbers)
business_server.tool(create_share_pre_verified_number)
business_server.tool(create_system_user_access_token)
business_server.tool(create_system_user)
business_server.tool(create_video)
