"""
Auto-generated MCP server for Facebook Application.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.application import Application
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-application")


# CRUD Operations


@mcp.tool()
async def create_application(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a Application.

    Args:
        object_id: The ID of the Application
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = Application(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Application(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Application(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_account_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Account for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_account result
    """
    result = Application(fbid=object_id).create_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_activity_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Activity for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_activity result
    """
    result = Application(fbid=object_id).create_activity(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_network_analytic_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Network Analytic for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_network_analytic result
    """
    result = Application(fbid=object_id).create_ad_network_analytic(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_aem_conversion_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Aem Conversion for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_aem_conversion result
    """
    result = Application(fbid=object_id).create_aem_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_aem_skan_readiness_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Aem Skan Readiness for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_aem_skan_readiness result
    """
    result = Application(fbid=object_id).create_aem_skan_readiness(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_aggregate_revenue_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Aggregate Revenue for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_aggregate_revenue result
    """
    result = Application(fbid=object_id).create_aggregate_revenue(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_app_indexing_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create App Indexing for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_app_indexing result
    """
    result = Application(fbid=object_id).create_app_indexing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_app_indexing_session_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create App Indexing Session for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_app_indexing_session result
    """
    result = Application(fbid=object_id).create_app_indexing_session(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_app_push_device_token_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create App Push Device Token for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_app_push_device_token result
    """
    result = Application(fbid=object_id).create_app_push_device_token(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_asset_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Asset for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_asset result
    """
    result = Application(fbid=object_id).create_asset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_codeless_event_mapping_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Codeless Event Mapping for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_codeless_event_mapping result
    """
    result = Application(fbid=object_id).create_codeless_event_mapping(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_domain_report_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Domain Report for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_domain_report result
    """
    result = Application(fbid=object_id).create_domain_report(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_mmp_auditing_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Mmp Auditing for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_mmp_auditing result
    """
    result = Application(fbid=object_id).create_mmp_auditing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_monetized_digital_store_object_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Monetized Digital Store Object for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_monetized_digital_store_object result
    """
    result = Application(fbid=object_id).create_monetized_digital_store_object(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_occludes_popup_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Occludes Popup for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_occludes_popup result
    """
    result = Application(fbid=object_id).create_occludes_popup(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscribed_domain_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Subscribed Domain for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_subscribed_domain result
    """
    result = Application(fbid=object_id).create_subscribed_domain(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscribed_domains_phishing_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Subscribed Domains Phishing for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_subscribed_domains_phishing result
    """
    result = Application(fbid=object_id).create_subscribed_domains_phishing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscription_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Subscription for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_subscription result
    """
    result = Application(fbid=object_id).create_subscription(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_upload_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Upload for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_upload result
    """
    result = Application(fbid=object_id).create_upload(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_whats_app_business_solution_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Whats App Business Solution for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_whats_app_business_solution result
    """
    result = Application(fbid=object_id).create_whats_app_business_solution(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_accounts_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Accounts for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_accounts result
    """
    result = Application(fbid=object_id).delete_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_subscriptions_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Subscriptions for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_subscriptions result
    """
    result = Application(fbid=object_id).delete_subscriptions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_accounts_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Accounts for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_accounts result
    """
    result = Application(fbid=object_id).get_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Network Analytics for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_network_analytics result
    """
    result = Application(fbid=object_id).get_ad_network_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics_results_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Network Analytics Results for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_network_analytics_results result
    """
    result = Application(fbid=object_id).get_ad_network_analytics_results(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_placements_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Network Placements for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_network_placements result
    """
    result = Application(fbid=object_id).get_ad_network_placements(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_placement_groups_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Placement Groups for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_placement_groups result
    """
    result = Application(fbid=object_id).get_ad_placement_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_aem_attribution_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Aem Attribution for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_aem_attribution result
    """
    result = Application(fbid=object_id).get_aem_attribution(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_aem_conversion_configs_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Aem Conversion Configs for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_aem_conversion_configs result
    """
    result = Application(fbid=object_id).get_aem_conversion_configs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_aem_conversion_filter_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Aem Conversion Filter for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_aem_conversion_filter result
    """
    result = Application(fbid=object_id).get_aem_conversion_filter(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Agencies for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
    result = Application(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_android_dialog_configs_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Android Dialog Configs for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_android_dialog_configs result
    """
    result = Application(fbid=object_id).get_android_dialog_configs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_app_assets_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get App Assets for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_app_assets result
    """
    result = Application(fbid=object_id).get_app_assets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_app_capi_settings_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get App Capi Settings for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_app_capi_settings result
    """
    result = Application(fbid=object_id).get_app_capi_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_app_event_types_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get App Event Types for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_app_event_types result
    """
    result = Application(fbid=object_id).get_app_event_types(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_app_installed_groups_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get App Installed Groups for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_app_installed_groups result
    """
    result = Application(fbid=object_id).get_app_installed_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_authorized_ad_accounts_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Authorized Ad Accounts for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_authorized_ad_accounts result
    """
    result = Application(fbid=object_id).get_authorized_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_button_auto_detection_device_selection_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Button Auto Detection Device Selection for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_button_auto_detection_device_selection result
    """
    result = Application(fbid=object_id).get_button_auto_detection_device_selection(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cloudbridge_settings_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Cloudbridge Settings for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_cloudbridge_settings result
    """
    result = Application(fbid=object_id).get_cloudbridge_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_connected_client_businesses_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Connected Client Businesses for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_connected_client_businesses result
    """
    result = Application(fbid=object_id).get_connected_client_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_da_checks_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Da Checks for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_da_checks result
    """
    result = Application(fbid=object_id).get_da_checks(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_iap_purchases_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Iap Purchases for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_iap_purchases result
    """
    result = Application(fbid=object_id).get_iap_purchases(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ios_dialog_configs_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ios Dialog Configs for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ios_dialog_configs result
    """
    result = Application(fbid=object_id).get_ios_dialog_configs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_linked_dataset_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Linked Dataset for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_linked_dataset result
    """
    result = Application(fbid=object_id).get_linked_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_message_templates_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Message Templates for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_message_templates result
    """
    result = Application(fbid=object_id).get_message_templates(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_mobile_sdk_gk_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Mobile Sdk Gk for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_mobile_sdk_gk result
    """
    result = Application(fbid=object_id).get_mobile_sdk_gk(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_monetized_digital_store_objects_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Monetized Digital Store Objects for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_monetized_digital_store_objects result
    """
    result = Application(fbid=object_id).get_monetized_digital_store_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_object_types_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Object Types for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_object_types result
    """
    result = Application(fbid=object_id).get_object_types(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_objects_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Objects for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_objects result
    """
    result = Application(fbid=object_id).get_objects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_permissions_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Permissions for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_permissions result
    """
    result = Application(fbid=object_id).get_permissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_products_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Products for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_products result
    """
    result = Application(fbid=object_id).get_products(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_purchases_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Purchases for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_purchases result
    """
    result = Application(fbid=object_id).get_purchases(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_roles_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Roles for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_roles result
    """
    result = Application(fbid=object_id).get_roles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_server_domain_infos_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Server Domain Infos for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_server_domain_infos result
    """
    result = Application(fbid=object_id).get_server_domain_infos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sgw_dataset_status_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Sgw Dataset Status for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_sgw_dataset_status result
    """
    result = Application(fbid=object_id).get_sgw_dataset_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sgw_install_deferral_link_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Sgw Install Deferral Link for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_sgw_install_deferral_link result
    """
    result = Application(fbid=object_id).get_sgw_install_deferral_link(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscribed_domains_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Subscribed Domains for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_subscribed_domains result
    """
    result = Application(fbid=object_id).get_subscribed_domains(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscribed_domains_phishing_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Subscribed Domains Phishing for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_subscribed_domains_phishing result
    """
    result = Application(fbid=object_id).get_subscribed_domains_phishing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscriptions_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Subscriptions for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_subscriptions result
    """
    result = Application(fbid=object_id).get_subscriptions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_whats_app_business_solutions_for_application(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Whats App Business Solutions for Application.

    Args:
        object_id: The ID of the Application
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_whats_app_business_solutions result
    """
    result = Application(fbid=object_id).get_whats_app_business_solutions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
application_server = mcp
