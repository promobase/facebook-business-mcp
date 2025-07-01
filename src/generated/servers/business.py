"""Business MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.business import Business
from fastmcp import FastMCP

from src.generated.models.adaccount import AdAccountField
from src.generated.models.adnetworkanalyticsasyncqueryresult import (
    AdNetworkAnalyticsAsyncQueryResultField,
)
from src.generated.models.adnetworkanalyticssyncqueryresult import (
    AdNetworkAnalyticsSyncQueryResultField,
)
from src.generated.models.adsdataset import AdsDatasetField
from src.generated.models.adspixel import AdsPixelField
from src.generated.models.adsreportbuildermmmreport import AdsReportBuilderMMMReportField
from src.generated.models.almadaccountinfo import ALMAdAccountInfoField
from src.generated.models.business import (
    BusinessCreateAccessTokenParams,
    BusinessCreateAdAccountParams,
    BusinessCreateAddPhoneNumberParams,
    BusinessCreateAdNetworkAnalyticParams,
    BusinessCreateAdNetworkApplicationParams,
    BusinessCreateAdReviewRequestParams,
    BusinessCreateAdsDataSetParams,
    BusinessCreateAdsPixelParams,
    BusinessCreateAdStudyParams,
    BusinessCreateBlockListDraftParams,
    BusinessCreateBmReviewRequestParams,
    BusinessCreateBusinessUserParams,
    BusinessCreateClaimCustomConversionParams,
    BusinessCreateClientAppParams,
    BusinessCreateClientPageParams,
    BusinessCreateCollaborativeAdsCollaborationRequestParams,
    BusinessCreateCpasBusinessSetupConfigParams,
    BusinessCreateCreativeFolderParams,
    BusinessCreateCustomConversionParams,
    BusinessCreateEventSourceGroupParams,
    BusinessCreateImageParams,
    BusinessCreateManagedBusinessParams,
    BusinessCreateManagedPartnerBusinessParams,
    BusinessCreateManagedPartnerBusinessSetupParams,
    BusinessCreateOnboardPartnersToMmLiteParams,
    BusinessCreateOpenBridgeConfigurationParams,
    BusinessCreateOwnedAdAccountParams,
    BusinessCreateOwnedAppParams,
    BusinessCreateOwnedBusinessParams,
    BusinessCreateOwnedPageParams,
    BusinessCreateOwnedProductCatalogParams,
    BusinessCreatePartnerPremiumOptionParams,
    BusinessCreateSelfCertifyWhatsAppBusinessParams,
    BusinessCreateSetupManagedPartnerAdAccountParams,
    BusinessCreateSharePreVerifiedNumberParams,
    BusinessCreateSystemUserAccessTokenParams,
    BusinessCreateSystemUserParams,
    BusinessCreateVideoParams,
    BusinessDeleteAdAccountsParams,
    BusinessDeleteAgenciesParams,
    BusinessDeleteClientsParams,
    BusinessDeleteInstagramAccountsParams,
    BusinessDeleteManagedBusinessesParams,
    BusinessDeleteManagedPartnerBusinessesParams,
    BusinessDeleteOwnedBusinessesParams,
    BusinessDeletePagesParams,
    BusinessDeleteSharePreVerifiedNumbersParams,
    BusinessField,
    BusinessGetAdAccountInfosParams,
    BusinessGetAdNetworkAnalyticsParams,
    BusinessGetAdNetworkAnalyticsResultsParams,
    BusinessGetAdsDatasetParams,
    BusinessGetAdsPixelsParams,
    BusinessGetAdsReportingMmmReportsParams,
    BusinessGetBusinessInvoicesParams,
    BusinessGetClientAdAccountsParams,
    BusinessGetCollaborativeAdsCollaborationRequestsParams,
    BusinessGetExtendedCreditApplicationsParams,
    BusinessGetExtendedCreditsParams,
    BusinessGetInitiatedAudienceSharingRequestsParams,
    BusinessGetManagedPartnerAdsFundingSourceDetailsParams,
    BusinessGetOwnedAdAccountsParams,
    BusinessGetOwnedBusinessesParams,
    BusinessGetPendingUsersParams,
    BusinessGetPictureParams,
    BusinessGetPreVerifiedNumbersParams,
    BusinessGetReceivedAudienceSharingRequestsParams,
    BusinessGetSelfCertifiedWhatsAppBusinessSubmissionsParams,
    BusinessUpdateParams,
)
from src.generated.models.businessassetsharingagreement import BusinessAssetSharingAgreementField
from src.generated.models.businessrolerequest import BusinessRoleRequestField
from src.generated.models.cpascollaborationrequest import CPASCollaborationRequestField
from src.generated.models.extendedcredit import ExtendedCreditField
from src.generated.models.extendedcreditapplication import ExtendedCreditApplicationField
from src.generated.models.fundingsourcedetailscoupon import FundingSourceDetailsCouponField
from src.generated.models.omegacustomertrx import OmegaCustomerTrxField
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.generated.models.whatsappbusinesspartnerclientverificationsubmission import (
    WhatsAppBusinessPartnerClientVerificationSubmissionField,
)
from src.generated.models.whatsappbusinesspreverifiedphonenumber import (
    WhatsAppBusinessPreVerifiedPhoneNumberField,
)
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


business_server.tool(get_business)


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


business_server.tool(update_business)


# ---- Edge Methods (67) ----
@wrapped_fn_tool
def create_access_token(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAccessTokenParams = {},
) -> Any:
    """Create Access Token for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_access_token(fields=fields, params=params)


business_server.tool(create_access_token)


@wrapped_fn_tool
def get_ad_account_infos(
    business_id: str,
    fields: list[ALMAdAccountInfoField] = [],
    params: BusinessGetAdAccountInfosParams = {},
) -> Any:
    """Get Ad Account Infos for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_ad_account_infos(fields=fields, params=params)


business_server.tool(get_ad_account_infos)


@wrapped_fn_tool
def delete_ad_accounts(
    business_id: str,
    params: BusinessDeleteAdAccountsParams = {},
) -> Any:
    """Delete Ad Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_ad_accounts(params=params)


business_server.tool(delete_ad_accounts)


@wrapped_fn_tool
def create_ad_review_request(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdReviewRequestParams = {},
) -> Any:
    """Create Ad Review Request for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_ad_review_request(fields=fields, params=params)


business_server.tool(create_ad_review_request)


@wrapped_fn_tool
def create_ad_study(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdStudyParams = {},
) -> Any:
    """Create Ad Study for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_ad_study(fields=fields, params=params)


business_server.tool(create_ad_study)


@wrapped_fn_tool
def create_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdAccountParams = {},
) -> Any:
    """Create Ad Account for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_ad_account(fields=fields, params=params)


business_server.tool(create_ad_account)


@wrapped_fn_tool
def create_add_phone_number(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAddPhoneNumberParams = {},
) -> Any:
    """Create Add Phone Number for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_add_phone_number(fields=fields, params=params)


business_server.tool(create_add_phone_number)


@wrapped_fn_tool
def create_ad_network_application(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdNetworkApplicationParams = {},
) -> Any:
    """Create Ad Network Application for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_ad_network_application(fields=fields, params=params)


business_server.tool(create_ad_network_application)


@wrapped_fn_tool
def get_ad_network_analytics(
    business_id: str,
    fields: list[AdNetworkAnalyticsSyncQueryResultField] = [],
    params: BusinessGetAdNetworkAnalyticsParams = {},
) -> Any:
    """Get Ad Network Analytics for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_ad_network_analytics(fields=fields, params=params)


business_server.tool(get_ad_network_analytics)


@wrapped_fn_tool
def create_ad_network_analytic(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdNetworkAnalyticParams = {},
) -> Any:
    """Create Ad Network Analytic for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_ad_network_analytic(fields=fields, params=params)


business_server.tool(create_ad_network_analytic)


@wrapped_fn_tool
def get_ad_network_analytics_results(
    business_id: str,
    fields: list[AdNetworkAnalyticsAsyncQueryResultField] = [],
    params: BusinessGetAdNetworkAnalyticsResultsParams = {},
) -> Any:
    """Get Ad Network Analytics Results for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_ad_network_analytics_results(fields=fields, params=params)


business_server.tool(get_ad_network_analytics_results)


@wrapped_fn_tool
def get_ads_dataset(
    business_id: str,
    fields: list[AdsDatasetField] = [],
    params: BusinessGetAdsDatasetParams = {},
) -> Any:
    """Get Ads Dataset for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_ads_dataset(fields=fields, params=params)


business_server.tool(get_ads_dataset)


@wrapped_fn_tool
def create_ads_data_set(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdsDataSetParams = {},
) -> Any:
    """Create Ads Data Set for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_ads_data_set(fields=fields, params=params)


business_server.tool(create_ads_data_set)


@wrapped_fn_tool
def get_ads_reporting_mmm_reports(
    business_id: str,
    fields: list[AdsReportBuilderMMMReportField] = [],
    params: BusinessGetAdsReportingMmmReportsParams = {},
) -> Any:
    """Get Ads Reporting Mmm Reports for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_ads_reporting_mmm_reports(fields=fields, params=params)


business_server.tool(get_ads_reporting_mmm_reports)


@wrapped_fn_tool
def get_ads_pixels(
    business_id: str,
    fields: list[AdsPixelField] = [],
    params: BusinessGetAdsPixelsParams = {},
) -> Any:
    """Get Ads Pixels for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_ads_pixels(fields=fields, params=params)


business_server.tool(get_ads_pixels)


@wrapped_fn_tool
def create_ads_pixel(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdsPixelParams = {},
) -> Any:
    """Create Ads Pixel for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_ads_pixel(fields=fields, params=params)


business_server.tool(create_ads_pixel)


@wrapped_fn_tool
def delete_agencies(
    business_id: str,
    params: BusinessDeleteAgenciesParams = {},
) -> Any:
    """Delete Agencies for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_agencies(params=params)


business_server.tool(delete_agencies)


@wrapped_fn_tool
def create_block_list_draft(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateBlockListDraftParams = {},
) -> Any:
    """Create Block List Draft for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_block_list_draft(fields=fields, params=params)


business_server.tool(create_block_list_draft)


@wrapped_fn_tool
def create_bm_review_request(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateBmReviewRequestParams = {},
) -> Any:
    """Create Bm Review Request for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_bm_review_request(fields=fields, params=params)


business_server.tool(create_bm_review_request)


@wrapped_fn_tool
def get_business_invoices(
    business_id: str,
    fields: list[OmegaCustomerTrxField] = [],
    params: BusinessGetBusinessInvoicesParams = {},
) -> Any:
    """Get Business Invoices for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_business_invoices(fields=fields, params=params)


business_server.tool(get_business_invoices)


@wrapped_fn_tool
def create_business_user(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateBusinessUserParams = {},
) -> Any:
    """Create Business User for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_business_user(fields=fields, params=params)


business_server.tool(create_business_user)


@wrapped_fn_tool
def create_claim_custom_conversion(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateClaimCustomConversionParams = {},
) -> Any:
    """Create Claim Custom Conversion for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_claim_custom_conversion(fields=fields, params=params)


business_server.tool(create_claim_custom_conversion)


@wrapped_fn_tool
def get_client_ad_accounts(
    business_id: str,
    fields: list[AdAccountField] = [],
    params: BusinessGetClientAdAccountsParams = {},
) -> Any:
    """Get Client Ad Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_client_ad_accounts(fields=fields, params=params)


business_server.tool(get_client_ad_accounts)


@wrapped_fn_tool
def create_client_app(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateClientAppParams = {},
) -> Any:
    """Create Client App for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_client_app(fields=fields, params=params)


business_server.tool(create_client_app)


@wrapped_fn_tool
def create_client_page(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateClientPageParams = {},
) -> Any:
    """Create Client Page for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_client_page(fields=fields, params=params)


business_server.tool(create_client_page)


@wrapped_fn_tool
def delete_clients(
    business_id: str,
    params: BusinessDeleteClientsParams = {},
) -> Any:
    """Delete Clients for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_clients(params=params)


business_server.tool(delete_clients)


@wrapped_fn_tool
def get_collaborative_ads_collaboration_requests(
    business_id: str,
    fields: list[CPASCollaborationRequestField] = [],
    params: BusinessGetCollaborativeAdsCollaborationRequestsParams = {},
) -> Any:
    """Get Collaborative Ads Collaboration Requests for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_collaborative_ads_collaboration_requests(
        fields=fields, params=params
    )


business_server.tool(get_collaborative_ads_collaboration_requests)


@wrapped_fn_tool
def create_collaborative_ads_collaboration_request(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCollaborativeAdsCollaborationRequestParams = {},
) -> Any:
    """Create Collaborative Ads Collaboration Request for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_collaborative_ads_collaboration_request(
        fields=fields, params=params
    )


business_server.tool(create_collaborative_ads_collaboration_request)


@wrapped_fn_tool
def create_cpas_business_setup_config(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCpasBusinessSetupConfigParams = {},
) -> Any:
    """Create Cpas Business Setup Config for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_cpas_business_setup_config(fields=fields, params=params)


business_server.tool(create_cpas_business_setup_config)


@wrapped_fn_tool
def create_creative_folder(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCreativeFolderParams = {},
) -> Any:
    """Create Creative Folder for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_creative_folder(fields=fields, params=params)


business_server.tool(create_creative_folder)


@wrapped_fn_tool
def create_custom_conversion(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCustomConversionParams = {},
) -> Any:
    """Create Custom Conversion for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_custom_conversion(fields=fields, params=params)


business_server.tool(create_custom_conversion)


@wrapped_fn_tool
def create_event_source_group(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateEventSourceGroupParams = {},
) -> Any:
    """Create Event Source Group for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_event_source_group(fields=fields, params=params)


business_server.tool(create_event_source_group)


@wrapped_fn_tool
def get_extended_credit_applications(
    business_id: str,
    fields: list[ExtendedCreditApplicationField] = [],
    params: BusinessGetExtendedCreditApplicationsParams = {},
) -> Any:
    """Get Extended Credit Applications for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_extended_credit_applications(fields=fields, params=params)


business_server.tool(get_extended_credit_applications)


@wrapped_fn_tool
def get_extended_credits(
    business_id: str,
    fields: list[ExtendedCreditField] = [],
    params: BusinessGetExtendedCreditsParams = {},
) -> Any:
    """Get Extended Credits for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_extended_credits(fields=fields, params=params)


business_server.tool(get_extended_credits)


@wrapped_fn_tool
def create_image(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateImageParams = {},
) -> Any:
    """Create Image for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_image(fields=fields, params=params)


business_server.tool(create_image)


@wrapped_fn_tool
def get_initiated_audience_sharing_requests(
    business_id: str,
    fields: list[BusinessAssetSharingAgreementField] = [],
    params: BusinessGetInitiatedAudienceSharingRequestsParams = {},
) -> Any:
    """Get Initiated Audience Sharing Requests for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_initiated_audience_sharing_requests(
        fields=fields, params=params
    )


business_server.tool(get_initiated_audience_sharing_requests)


@wrapped_fn_tool
def delete_instagram_accounts(
    business_id: str,
    params: BusinessDeleteInstagramAccountsParams = {},
) -> Any:
    """Delete Instagram Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_instagram_accounts(params=params)


business_server.tool(delete_instagram_accounts)


@wrapped_fn_tool
def delete_managed_businesses(
    business_id: str,
    params: BusinessDeleteManagedBusinessesParams = {},
) -> Any:
    """Delete Managed Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_managed_businesses(params=params)


business_server.tool(delete_managed_businesses)


@wrapped_fn_tool
def create_managed_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateManagedBusinessParams = {},
) -> Any:
    """Create Managed Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_managed_business(fields=fields, params=params)


business_server.tool(create_managed_business)


@wrapped_fn_tool
def get_managed_partner_ads_funding_source_details(
    business_id: str,
    fields: list[FundingSourceDetailsCouponField] = [],
    params: BusinessGetManagedPartnerAdsFundingSourceDetailsParams = {},
) -> Any:
    """Get Managed Partner Ads Funding Source Details for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_managed_partner_ads_funding_source_details(
        fields=fields, params=params
    )


business_server.tool(get_managed_partner_ads_funding_source_details)


@wrapped_fn_tool
def create_managed_partner_business_setup(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateManagedPartnerBusinessSetupParams = {},
) -> Any:
    """Create Managed Partner Business Setup for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_managed_partner_business_setup(fields=fields, params=params)


business_server.tool(create_managed_partner_business_setup)


@wrapped_fn_tool
def delete_managed_partner_businesses(
    business_id: str,
    params: BusinessDeleteManagedPartnerBusinessesParams = {},
) -> Any:
    """Delete Managed Partner Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_managed_partner_businesses(params=params)


business_server.tool(delete_managed_partner_businesses)


@wrapped_fn_tool
def create_managed_partner_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateManagedPartnerBusinessParams = {},
) -> Any:
    """Create Managed Partner Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_managed_partner_business(fields=fields, params=params)


business_server.tool(create_managed_partner_business)


@wrapped_fn_tool
def create_onboard_partners_to_mm_lite(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOnboardPartnersToMmLiteParams = {},
) -> Any:
    """Create Onboard Partners To Mm Lite for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_onboard_partners_to_mm_lite(fields=fields, params=params)


business_server.tool(create_onboard_partners_to_mm_lite)


@wrapped_fn_tool
def create_open_bridge_configuration(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOpenBridgeConfigurationParams = {},
) -> Any:
    """Create Open Bridge Configuration for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_open_bridge_configuration(fields=fields, params=params)


business_server.tool(create_open_bridge_configuration)


@wrapped_fn_tool
def get_owned_ad_accounts(
    business_id: str,
    fields: list[AdAccountField] = [],
    params: BusinessGetOwnedAdAccountsParams = {},
) -> Any:
    """Get Owned Ad Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_owned_ad_accounts(fields=fields, params=params)


business_server.tool(get_owned_ad_accounts)


@wrapped_fn_tool
def create_owned_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedAdAccountParams = {},
) -> Any:
    """Create Owned Ad Account for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_owned_ad_account(fields=fields, params=params)


business_server.tool(create_owned_ad_account)


@wrapped_fn_tool
def create_owned_app(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedAppParams = {},
) -> Any:
    """Create Owned App for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_owned_app(fields=fields, params=params)


business_server.tool(create_owned_app)


@wrapped_fn_tool
def delete_owned_businesses(
    business_id: str,
    params: BusinessDeleteOwnedBusinessesParams = {},
) -> Any:
    """Delete Owned Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_owned_businesses(params=params)


business_server.tool(delete_owned_businesses)


@wrapped_fn_tool
def get_owned_businesses(
    business_id: str,
    fields: list[BusinessField] = [],
    params: BusinessGetOwnedBusinessesParams = {},
) -> Any:
    """Get Owned Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_owned_businesses(fields=fields, params=params)


business_server.tool(get_owned_businesses)


@wrapped_fn_tool
def create_owned_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedBusinessParams = {},
) -> Any:
    """Create Owned Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_owned_business(fields=fields, params=params)


business_server.tool(create_owned_business)


@wrapped_fn_tool
def create_owned_page(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedPageParams = {},
) -> Any:
    """Create Owned Page for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_owned_page(fields=fields, params=params)


business_server.tool(create_owned_page)


@wrapped_fn_tool
def create_owned_product_catalog(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedProductCatalogParams = {},
) -> Any:
    """Create Owned Product Catalog for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_owned_product_catalog(fields=fields, params=params)


business_server.tool(create_owned_product_catalog)


@wrapped_fn_tool
def delete_pages(
    business_id: str,
    params: BusinessDeletePagesParams = {},
) -> Any:
    """Delete Pages for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_pages(params=params)


business_server.tool(delete_pages)


@wrapped_fn_tool
def create_partner_premium_option(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreatePartnerPremiumOptionParams = {},
) -> Any:
    """Create Partner Premium Option for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_partner_premium_option(fields=fields, params=params)


business_server.tool(create_partner_premium_option)


@wrapped_fn_tool
def get_pending_users(
    business_id: str,
    fields: list[BusinessRoleRequestField] = [],
    params: BusinessGetPendingUsersParams = {},
) -> Any:
    """Get Pending Users for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_pending_users(fields=fields, params=params)


business_server.tool(get_pending_users)


@wrapped_fn_tool
def get_picture(
    business_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: BusinessGetPictureParams = {},
) -> Any:
    """Get Picture for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_picture(fields=fields, params=params)


business_server.tool(get_picture)


@wrapped_fn_tool
def get_pre_verified_numbers(
    business_id: str,
    fields: list[WhatsAppBusinessPreVerifiedPhoneNumberField] = [],
    params: BusinessGetPreVerifiedNumbersParams = {},
) -> Any:
    """Get Pre Verified Numbers for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_pre_verified_numbers(fields=fields, params=params)


business_server.tool(get_pre_verified_numbers)


@wrapped_fn_tool
def get_received_audience_sharing_requests(
    business_id: str,
    fields: list[BusinessAssetSharingAgreementField] = [],
    params: BusinessGetReceivedAudienceSharingRequestsParams = {},
) -> Any:
    """Get Received Audience Sharing Requests for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_received_audience_sharing_requests(
        fields=fields, params=params
    )


business_server.tool(get_received_audience_sharing_requests)


@wrapped_fn_tool
def get_self_certified_whats_app_business_submissions(
    business_id: str,
    fields: list[WhatsAppBusinessPartnerClientVerificationSubmissionField] = [],
    params: BusinessGetSelfCertifiedWhatsAppBusinessSubmissionsParams = {},
) -> Any:
    """Get Self Certified Whats App Business Submissions for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).get_self_certified_whats_app_business_submissions(
        fields=fields, params=params
    )


business_server.tool(get_self_certified_whats_app_business_submissions)


@wrapped_fn_tool
def create_self_certify_whats_app_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSelfCertifyWhatsAppBusinessParams = {},
) -> Any:
    """Create Self Certify Whats App Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_self_certify_whats_app_business(
        fields=fields, params=params
    )


business_server.tool(create_self_certify_whats_app_business)


@wrapped_fn_tool
def create_setup_managed_partner_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSetupManagedPartnerAdAccountParams = {},
) -> Any:
    """Create Setup Managed Partner Ad Account for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_setup_managed_partner_ad_account(
        fields=fields, params=params
    )


business_server.tool(create_setup_managed_partner_ad_account)


@wrapped_fn_tool
def delete_share_pre_verified_numbers(
    business_id: str,
    params: BusinessDeleteSharePreVerifiedNumbersParams = {},
) -> Any:
    """Delete Share Pre Verified Numbers for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters.
    """
    return Business(business_id).delete_share_pre_verified_numbers(params=params)


business_server.tool(delete_share_pre_verified_numbers)


@wrapped_fn_tool
def create_share_pre_verified_number(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSharePreVerifiedNumberParams = {},
) -> Any:
    """Create Share Pre Verified Number for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_share_pre_verified_number(fields=fields, params=params)


business_server.tool(create_share_pre_verified_number)


@wrapped_fn_tool
def create_system_user_access_token(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSystemUserAccessTokenParams = {},
) -> Any:
    """Create System User Access Token for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_system_user_access_token(fields=fields, params=params)


business_server.tool(create_system_user_access_token)


@wrapped_fn_tool
def create_system_user(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSystemUserParams = {},
) -> Any:
    """Create System User for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_system_user(fields=fields, params=params)


business_server.tool(create_system_user)


@wrapped_fn_tool
def create_video(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateVideoParams = {},
) -> Any:
    """Create Video for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Business(business_id).create_video(fields=fields, params=params)


business_server.tool(create_video)
