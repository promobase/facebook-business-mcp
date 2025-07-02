"""
Auto-generated MCP server for Facebook Business.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.business import Business
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-business")


# CRUD Operations


@mcp.tool()
async def get_business(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
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
    """
    Update a Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
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
    """
    Create Access Token for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_access_token result
    """
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
    """
    Create Ad Account for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_account result
    """
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
    """
    Create Ad Network Analytic for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_network_analytic result
    """
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
    """
    Create Ad Network Application for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_network_application result
    """
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
    """
    Create Ad Review Request for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_review_request result
    """
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
    """
    Create Ad Study for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_study result
    """
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
    """
    Create Add Phone Number for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_add_phone_number result
    """
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
    """
    Create Ads Data Set for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ads_data_set result
    """
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
    """
    Create Ads Pixel for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ads_pixel result
    """
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
    """
    Create Block List Draft for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_block_list_draft result
    """
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
    """
    Create Bm Review Request for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_bm_review_request result
    """
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
    """
    Create Business User for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_business_user result
    """
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
    """
    Create Claim Custom Conversion for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_claim_custom_conversion result
    """
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
    """
    Create Client App for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_client_app result
    """
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
    """
    Create Client Page for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_client_page result
    """
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
    """
    Create Collaborative Ads Collaboration Request for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_collaborative_ads_collaboration_request result
    """
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
    """
    Create Cpas Business Setup Config for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_cpas_business_setup_config result
    """
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
    """
    Create Creative Folder for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_creative_folder result
    """
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
    """
    Create Custom Conversion for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_custom_conversion result
    """
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
    """
    Create Event Source Group for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_event_source_group result
    """
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
    """
    Create Image for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_image result
    """
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
    """
    Create Managed Business for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_managed_business result
    """
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
    """
    Create Managed Partner Business for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_managed_partner_business result
    """
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
    """
    Create Managed Partner Business Setup for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_managed_partner_business_setup result
    """
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
    """
    Create Onboard Partners To Mm Lite for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_onboard_partners_to_mm_lite result
    """
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
    """
    Create Open Bridge Configuration for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_open_bridge_configuration result
    """
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
    """
    Create Owned Ad Account for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_owned_ad_account result
    """
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
    """
    Create Owned App for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_owned_app result
    """
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
    """
    Create Owned Business for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_owned_business result
    """
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
    """
    Create Owned Page for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_owned_page result
    """
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
    """
    Create Owned Product Catalog for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_owned_product_catalog result
    """
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
    """
    Create Partner Premium Option for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_partner_premium_option result
    """
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
    """
    Create Pixel To for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_pixel_to result
    """
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
    """
    Create Self Certify Whats App Business for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_self_certify_whats_app_business result
    """
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
    """
    Create Setup Managed Partner Ad Account for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_setup_managed_partner_ad_account result
    """
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
    """
    Create Share Pre Verified Number for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_share_pre_verified_number result
    """
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
    """
    Create System User for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_system_user result
    """
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
    """
    Create System User Access Token for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_system_user_access_token result
    """
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
    """
    Create Video for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video result
    """
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
    """
    Delete Ad Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_ad_accounts result
    """
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
    """
    Delete Agencies for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_agencies result
    """
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
    """
    Delete Clients for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_clients result
    """
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
    """
    Delete Instagram Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_instagram_accounts result
    """
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
    """
    Delete Managed Businesses for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_managed_businesses result
    """
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
    """
    Delete Managed Partner Businesses for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_managed_partner_businesses result
    """
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
    """
    Delete Owned Businesses for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_owned_businesses result
    """
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
    """
    Delete Pages for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_pages result
    """
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
    """
    Delete Share Pre Verified Numbers for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_share_pre_verified_numbers result
    """
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
    """
    Get Ad Account Infos for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_account_infos result
    """
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
    """
    Get Ad Network Analytics for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_network_analytics result
    """
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
    """
    Get Ad Network Analytics Results for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_network_analytics_results result
    """
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
    """
    Get Ad Studies for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_studies result
    """
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
    """
    Get Ads Dataset for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_dataset result
    """
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
    """
    Get Ads Pixels for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_pixels result
    """
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
    """
    Get Ads Reporting Mmm Reports for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_reporting_mmm_reports result
    """
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
    """
    Get Ads Reporting Mmm Schedulers for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_reporting_mmm_schedulers result
    """
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
    """
    Get Agencies for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
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
    """
    Get An Placements for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_an_placements result
    """
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
    """
    Get Business Asset Groups for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_asset_groups result
    """
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
    """
    Get Business Invoices for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_invoices result
    """
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
    """
    Get Business Projects for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_projects result
    """
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
    """
    Get Business Users for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_users result
    """
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
    """
    Get Client Ad Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_client_ad_accounts result
    """
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
    """
    Get Client Apps for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_client_apps result
    """
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
    """
    Get Client Offsite Signal Container Business Objects for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_client_offsite_signal_container_business_objects result
    """
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
    """
    Get Client Pages for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_client_pages result
    """
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
    """
    Get Client Pixels for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_client_pixels result
    """
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
    """
    Get Client Product Catalogs for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_client_product_catalogs result
    """
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
    """
    Get Client Whats App Business Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_client_whats_app_business_accounts result
    """
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
    """
    Get Clients for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_clients result
    """
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
    """
    Get Collaborative Ads Collaboration Requests for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_collaborative_ads_collaboration_requests result
    """
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
    """
    Get Collaborative Ads Suggested Partners for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_collaborative_ads_suggested_partners result
    """
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
    """
    Get Commerce Merchant Settings for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_merchant_settings result
    """
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
    """
    Get Cpas Business Setup Config for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_cpas_business_setup_config result
    """
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
    """
    Get Cpas Merchant Config for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_cpas_merchant_config result
    """
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
    """
    Get Credit Cards for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_credit_cards result
    """
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
    """
    Get Event Source Groups for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_event_source_groups result
    """
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
    """
    Get Extended Credit Applications for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_extended_credit_applications result
    """
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
    """
    Get Extended Credits for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_extended_credits result
    """
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
    """
    Get Initiated Audience Sharing Requests for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_initiated_audience_sharing_requests result
    """
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
    """
    Get Instagram Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_instagram_accounts result
    """
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
    """
    Get Instagram Business Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_instagram_business_accounts result
    """
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
    """
    Get Managed Partner Ads Funding Source Details for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_managed_partner_ads_funding_source_details result
    """
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
    """
    Get Open Bridge Configurations for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_open_bridge_configurations result
    """
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
    """
    Get Owned Ad Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_ad_accounts result
    """
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
    """
    Get Owned Apps for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_apps result
    """
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
    """
    Get Owned Businesses for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_businesses result
    """
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
    """
    Get Owned Instagram Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_instagram_accounts result
    """
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
    """
    Get Owned Offsite Signal Container Business Objects for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_offsite_signal_container_business_objects result
    """
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
    """
    Get Owned Pages for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_pages result
    """
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
    """
    Get Owned Pixels for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_pixels result
    """
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
    """
    Get Owned Product Catalogs for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_product_catalogs result
    """
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
    """
    Get Owned Whats App Business Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owned_whats_app_business_accounts result
    """
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
    """
    Get Partner Account Linking for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_partner_account_linking result
    """
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
    """
    Get Passback Attribution Metadata Configs for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_passback_attribution_metadata_configs result
    """
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
    """
    Get Pending Client Ad Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pending_client_ad_accounts result
    """
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
    """
    Get Pending Client Apps for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pending_client_apps result
    """
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
    """
    Get Pending Client Pages for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pending_client_pages result
    """
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
    """
    Get Pending Owned Ad Accounts for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pending_owned_ad_accounts result
    """
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
    """
    Get Pending Owned Pages for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pending_owned_pages result
    """
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
    """
    Get Pending Shared Offsite Signal Container Business Objects for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pending_shared_offsite_signal_container_business_objects result
    """
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
    """
    Get Pending Users for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pending_users result
    """
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
    """
    Get Picture for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_picture result
    """
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
    """
    Get Pre Verified Numbers for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pre_verified_numbers result
    """
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
    """
    Get Received Audience Sharing Requests for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_received_audience_sharing_requests result
    """
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
    """
    Get Reseller Guidances for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_reseller_guidances result
    """
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
    """
    Get Self Certified Whats App Business Submissions for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_self_certified_whats_app_business_submissions result
    """
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
    """
    Get System Users for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_system_users result
    """
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
    """
    Get Third Party Measurement Report Dataset for Business.

    Args:
        object_id: The ID of the Business
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_third_party_measurement_report_dataset result
    """
    result = Business(fbid=object_id).get_third_party_measurement_report_dataset(
        fields=fields,
        params=params,
    )

    return result


# Export the server
business_server = mcp
