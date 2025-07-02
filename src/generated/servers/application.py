"""Application MCP Server with typed wrappers."""

from facebook_business.adobjects.application import Application
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.adaccount import AdAccountField
from src.generated.models.adnetworkanalyticsasyncqueryresult import (
    AdNetworkAnalyticsAsyncQueryResultField,
)
from src.generated.models.adnetworkanalyticssyncqueryresult import (
    AdNetworkAnalyticsSyncQueryResultField,
)
from src.generated.models.adplacement import AdPlacementField
from src.generated.models.application import (
    ApplicationCreateAccountParams,
    ApplicationCreateActivityParams,
    ApplicationCreateAdNetworkAnalyticParams,
    ApplicationCreateAemConversionParams,
    ApplicationCreateAemSkanReadinessParams,
    ApplicationCreateAggregateRevenueParams,
    ApplicationCreateAppIndexingParams,
    ApplicationCreateAppIndexingSessionParams,
    ApplicationCreateAppPushDeviceTokenParams,
    ApplicationCreateAssetParams,
    ApplicationCreateCodelessEventMappingParams,
    ApplicationCreateDomainReportParams,
    ApplicationCreateMmpAuditingParams,
    ApplicationCreateMonetizedDigitalStoreObjectParams,
    ApplicationCreateOccludesPopupParams,
    ApplicationCreateSubscribedDomainParams,
    ApplicationCreateSubscribedDomainsPhishingParams,
    ApplicationCreateSubscriptionParams,
    ApplicationCreateUploadParams,
    ApplicationCreateWhatsAppBusinessSolutionParams,
    ApplicationDeleteAccountsParams,
    ApplicationDeleteSubscriptionsParams,
    ApplicationField,
    ApplicationGetAccountsParams,
    ApplicationGetAdNetworkAnalyticsParams,
    ApplicationGetAdNetworkAnalyticsResultsParams,
    ApplicationGetAdNetworkPlacementsParams,
    ApplicationGetAemAttributionParams,
    ApplicationGetAemConversionConfigsParams,
    ApplicationGetAemConversionFilterParams,
    ApplicationGetAppInstalledGroupsParams,
    ApplicationGetAuthorizedAdAccountsParams,
    ApplicationGetButtonAutoDetectionDeviceSelectionParams,
    ApplicationGetDaChecksParams,
    ApplicationGetIapPurchasesParams,
    ApplicationGetMessageTemplatesParams,
    ApplicationGetMobileSdkGkParams,
    ApplicationGetPermissionsParams,
    ApplicationGetProductsParams,
    ApplicationGetSgwDatasetStatusParams,
    ApplicationGetSgwInstallDeferralLinkParams,
    ApplicationGetWhatsAppBusinessSolutionsParams,
    ApplicationUpdateParams,
)
from src.generated.models.dacheck import DACheckField
from src.generated.models.group import GroupField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookApplication"
instructions = """
Application MCP Server for Facebook Business API.

Provides typed access to all Application operations.
"""

application_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@application_server.tool
@wrapped_fn_tool
def get_application(
    application_id: str,
    fields: list[ApplicationField] = [],
) -> str:
    """Get a Application object by ID.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See ApplicationField type.
    """
    obj = Application(application_id)
    return obj.api_get(fields=fields)


@application_server.tool
@wrapped_fn_tool
def update_application(
    application_id: str,
    fields: list[ApplicationField] = [],
    params: ApplicationUpdateParams | dict = {},
) -> str:
    """Update a Application object.

    Args:
        application_id: The ID of the Application.
        fields: Fields to return after update. Available fields: See ApplicationField type.
        params: Parameters to update. Available params: See ApplicationUpdateParams type.
    """
    return Application(application_id).api_update(fields=fields, params=params)


# ---- Edge Methods (41) ----
@application_server.tool
@wrapped_fn_tool
def delete_accounts(
    application_id: str,
    params: ApplicationDeleteAccountsParams | dict = {},
):
    """Delete Accounts for this Application.

    Args:
        application_id: The ID of the Application.
        params: Query parameters. Available params: See ApplicationDeleteAccountsParams type.
    """
    return Application(application_id).delete_accounts(params=params)


@application_server.tool
@wrapped_fn_tool
def get_accounts(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetAccountsParams | dict = {},
):
    """Get Accounts for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetAccountsParams type.
    """
    return Application(application_id).get_accounts(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_account(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAccountParams | dict = {},
):
    """Create Account for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAccountParams type.
    """
    return Application(application_id).create_account(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_activity(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateActivityParams | dict = {},
):
    """Create Activity for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateActivityParams type.
    """
    return Application(application_id).create_activity(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_ad_network_placements(
    application_id: str,
    fields: list[AdPlacementField] = [],
    params: ApplicationGetAdNetworkPlacementsParams | dict = {},
):
    """Get Ad Network Placements for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AdPlacementField type.
        params: Query parameters. Available params: See ApplicationGetAdNetworkPlacementsParams type.
    """
    return Application(application_id).get_ad_network_placements(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_ad_network_analytics(
    application_id: str,
    fields: list[AdNetworkAnalyticsSyncQueryResultField] = [],
    params: ApplicationGetAdNetworkAnalyticsParams | dict = {},
):
    """Get Ad Network Analytics for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AdNetworkAnalyticsSyncQueryResultField type.
        params: Query parameters. Available params: See ApplicationGetAdNetworkAnalyticsParams type.
    """
    return Application(application_id).get_ad_network_analytics(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_ad_network_analytic(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAdNetworkAnalyticParams | dict = {},
):
    """Create Ad Network Analytic for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAdNetworkAnalyticParams type.
    """
    return Application(application_id).create_ad_network_analytic(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_ad_network_analytics_results(
    application_id: str,
    fields: list[AdNetworkAnalyticsAsyncQueryResultField] = [],
    params: ApplicationGetAdNetworkAnalyticsResultsParams | dict = {},
):
    """Get Ad Network Analytics Results for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AdNetworkAnalyticsAsyncQueryResultField type.
        params: Query parameters. Available params: See ApplicationGetAdNetworkAnalyticsResultsParams type.
    """
    return Application(application_id).get_ad_network_analytics_results(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def get_aem_attribution(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetAemAttributionParams | dict = {},
):
    """Get Aem Attribution for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetAemAttributionParams type.
    """
    return Application(application_id).get_aem_attribution(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_aem_conversion_configs(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetAemConversionConfigsParams | dict = {},
):
    """Get Aem Conversion Configs for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetAemConversionConfigsParams type.
    """
    return Application(application_id).get_aem_conversion_configs(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_aem_conversion_filter(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetAemConversionFilterParams | dict = {},
):
    """Get Aem Conversion Filter for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetAemConversionFilterParams type.
    """
    return Application(application_id).get_aem_conversion_filter(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_aem_conversion(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAemConversionParams | dict = {},
):
    """Create Aem Conversion for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAemConversionParams type.
    """
    return Application(application_id).create_aem_conversion(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_aem_skan_readiness(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAemSkanReadinessParams | dict = {},
):
    """Create Aem Skan Readiness for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAemSkanReadinessParams type.
    """
    return Application(application_id).create_aem_skan_readiness(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_aggregate_revenue(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAggregateRevenueParams | dict = {},
):
    """Create Aggregate Revenue for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAggregateRevenueParams type.
    """
    return Application(application_id).create_aggregate_revenue(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_app_indexing(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAppIndexingParams | dict = {},
):
    """Create App Indexing for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAppIndexingParams type.
    """
    return Application(application_id).create_app_indexing(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_app_indexing_session(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAppIndexingSessionParams | dict = {},
):
    """Create App Indexing Session for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAppIndexingSessionParams type.
    """
    return Application(application_id).create_app_indexing_session(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_app_installed_groups(
    application_id: str,
    fields: list[GroupField] = [],
    params: ApplicationGetAppInstalledGroupsParams | dict = {},
):
    """Get App Installed Groups for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See GroupField type.
        params: Query parameters. Available params: See ApplicationGetAppInstalledGroupsParams type.
    """
    return Application(application_id).get_app_installed_groups(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_app_push_device_token(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAppPushDeviceTokenParams | dict = {},
):
    """Create App Push Device Token for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAppPushDeviceTokenParams type.
    """
    return Application(application_id).create_app_push_device_token(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_asset(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateAssetParams | dict = {},
):
    """Create Asset for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateAssetParams type.
    """
    return Application(application_id).create_asset(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_authorized_ad_accounts(
    application_id: str,
    fields: list[AdAccountField] = [],
    params: ApplicationGetAuthorizedAdAccountsParams | dict = {},
):
    """Get Authorized Ad Accounts for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See ApplicationGetAuthorizedAdAccountsParams type.
    """
    return Application(application_id).get_authorized_ad_accounts(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_button_auto_detection_device_selection(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetButtonAutoDetectionDeviceSelectionParams | dict = {},
):
    """Get Button Auto Detection Device Selection for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetButtonAutoDetectionDeviceSelectionParams type.
    """
    return Application(application_id).get_button_auto_detection_device_selection(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def create_codeless_event_mapping(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateCodelessEventMappingParams | dict = {},
):
    """Create Codeless Event Mapping for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateCodelessEventMappingParams type.
    """
    return Application(application_id).create_codeless_event_mapping(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_da_checks(
    application_id: str,
    fields: list[DACheckField] = [],
    params: ApplicationGetDaChecksParams | dict = {},
):
    """Get Da Checks for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See DACheckField type.
        params: Query parameters. Available params: See ApplicationGetDaChecksParams type.
    """
    return Application(application_id).get_da_checks(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_domain_report(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateDomainReportParams | dict = {},
):
    """Create Domain Report for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateDomainReportParams type.
    """
    return Application(application_id).create_domain_report(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_iap_purchases(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetIapPurchasesParams | dict = {},
):
    """Get Iap Purchases for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetIapPurchasesParams type.
    """
    return Application(application_id).get_iap_purchases(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_message_templates(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetMessageTemplatesParams | dict = {},
):
    """Get Message Templates for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetMessageTemplatesParams type.
    """
    return Application(application_id).get_message_templates(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_mmp_auditing(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateMmpAuditingParams | dict = {},
):
    """Create Mmp Auditing for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateMmpAuditingParams type.
    """
    return Application(application_id).create_mmp_auditing(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_mobile_sdk_gk(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetMobileSdkGkParams | dict = {},
):
    """Get Mobile Sdk Gk for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetMobileSdkGkParams type.
    """
    return Application(application_id).get_mobile_sdk_gk(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_monetized_digital_store_object(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateMonetizedDigitalStoreObjectParams | dict = {},
):
    """Create Monetized Digital Store Object for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateMonetizedDigitalStoreObjectParams type.
    """
    return Application(application_id).create_monetized_digital_store_object(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def create_occludes_popup(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateOccludesPopupParams | dict = {},
):
    """Create Occludes Popup for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateOccludesPopupParams type.
    """
    return Application(application_id).create_occludes_popup(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_permissions(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetPermissionsParams | dict = {},
):
    """Get Permissions for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetPermissionsParams type.
    """
    return Application(application_id).get_permissions(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_products(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetProductsParams | dict = {},
):
    """Get Products for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetProductsParams type.
    """
    return Application(application_id).get_products(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_sgw_dataset_status(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetSgwDatasetStatusParams | dict = {},
):
    """Get Sgw Dataset Status for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetSgwDatasetStatusParams type.
    """
    return Application(application_id).get_sgw_dataset_status(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_sgw_install_deferral_link(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetSgwInstallDeferralLinkParams | dict = {},
):
    """Get Sgw Install Deferral Link for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetSgwInstallDeferralLinkParams type.
    """
    return Application(application_id).get_sgw_install_deferral_link(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_subscribed_domain(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateSubscribedDomainParams | dict = {},
):
    """Create Subscribed Domain for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateSubscribedDomainParams type.
    """
    return Application(application_id).create_subscribed_domain(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_subscribed_domains_phishing(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateSubscribedDomainsPhishingParams | dict = {},
):
    """Create Subscribed Domains Phishing for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateSubscribedDomainsPhishingParams type.
    """
    return Application(application_id).create_subscribed_domains_phishing(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def delete_subscriptions(
    application_id: str,
    params: ApplicationDeleteSubscriptionsParams | dict = {},
):
    """Delete Subscriptions for this Application.

    Args:
        application_id: The ID of the Application.
        params: Query parameters. Available params: See ApplicationDeleteSubscriptionsParams type.
    """
    return Application(application_id).delete_subscriptions(params=params)


@application_server.tool
@wrapped_fn_tool
def create_subscription(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateSubscriptionParams | dict = {},
):
    """Create Subscription for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateSubscriptionParams type.
    """
    return Application(application_id).create_subscription(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_upload(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateUploadParams | dict = {},
):
    """Create Upload for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateUploadParams type.
    """
    return Application(application_id).create_upload(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_whats_app_business_solution(
    application_id: str,
    fields: list[str] = [],
    params: ApplicationCreateWhatsAppBusinessSolutionParams | dict = {},
):
    """Create Whats App Business Solution for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ApplicationCreateWhatsAppBusinessSolutionParams type.
    """
    return Application(application_id).create_whats_app_business_solution(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def get_whats_app_business_solutions(
    application_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: ApplicationGetWhatsAppBusinessSolutionsParams | dict = {},
):
    """Get Whats App Business Solutions for this Application.

    Args:
        application_id: The ID of the Application.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See ApplicationGetWhatsAppBusinessSolutionsParams type.
    """
    return Application(application_id).get_whats_app_business_solutions(
        fields=fields, params=params
    )
