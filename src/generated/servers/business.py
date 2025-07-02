"""Business MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.business import Business
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
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
from src.generated.models.adstudy import AdStudyField
from src.generated.models.advideo import AdVideoField
from src.generated.models.almadaccountinfo import ALMAdAccountInfoField
from src.generated.models.application import ApplicationField
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
from src.generated.models.businesscreativefolder import BusinessCreativeFolderField
from src.generated.models.businessimage import BusinessImageField
from src.generated.models.businessrolerequest import BusinessRoleRequestField
from src.generated.models.businessuser import BusinessUserField
from src.generated.models.cpasbusinesssetupconfig import CPASBusinessSetupConfigField
from src.generated.models.cpascollaborationrequest import CPASCollaborationRequestField
from src.generated.models.customconversion import CustomConversionField
from src.generated.models.eventsourcegroup import EventSourceGroupField
from src.generated.models.extendedcredit import ExtendedCreditField
from src.generated.models.extendedcreditapplication import ExtendedCreditApplicationField
from src.generated.models.fundingsourcedetailscoupon import FundingSourceDetailsCouponField
from src.generated.models.managedpartnerbusiness import ManagedPartnerBusinessField
from src.generated.models.omegacustomertrx import OmegaCustomerTrxField
from src.generated.models.openbridgeconfiguration import OpenBridgeConfigurationField
from src.generated.models.productcatalog import ProductCatalogField
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.generated.models.systemuser import SystemUserField
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
@business_server.tool
@wrapped_fn_tool
def get_business(
    business_id: str,
    fields: list[BusinessField] = [],
) -> str:
    """Get a Business object by ID.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See BusinessField type.
    """
    obj = Business(business_id)
    return obj.api_get(fields=fields)


@business_server.tool
@wrapped_fn_tool
def update_business(
    business_id: str,
    fields: list[BusinessField] = [],
    params: BusinessUpdateParams | dict = {},
) -> str:
    """Update a Business object.

    Args:
        business_id: The ID of the Business.
        fields: Fields to return after update. Available fields: See BusinessField type.
        params: Parameters to update. Available params: See BusinessUpdateParams type.
    """
    return Business(business_id).api_update(fields=fields, params=params)


# ---- Edge Methods (67) ----
@business_server.tool
@wrapped_fn_tool
def create_access_token(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAccessTokenParams | dict = {},
):
    """Create Access Token for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAccessTokenParams type.
    """
    return Business(business_id).create_access_token(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ad_account_infos(
    business_id: str,
    fields: list[ALMAdAccountInfoField] = [],
    params: BusinessGetAdAccountInfosParams | dict = {},
):
    """Get Ad Account Infos for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See ALMAdAccountInfoField type.
        params: Query parameters. Available params: See BusinessGetAdAccountInfosParams type.
    """
    return Business(business_id).get_ad_account_infos(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_ad_accounts(
    business_id: str,
    params: BusinessDeleteAdAccountsParams | dict = {},
):
    """Delete Ad Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteAdAccountsParams type.
    """
    return Business(business_id).delete_ad_accounts(params=params)


@business_server.tool
@wrapped_fn_tool
def create_ad_review_request(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdReviewRequestParams | dict = {},
):
    """Create Ad Review Request for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAdReviewRequestParams type.
    """
    return Business(business_id).create_ad_review_request(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ad_study(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdStudyParams | dict = {},
):
    """Create Ad Study for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAdStudyParams type.
    """
    return Business(business_id).create_ad_study(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdAccountParams | dict = {},
):
    """Create Ad Account for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAdAccountParams type.
    """
    return Business(business_id).create_ad_account(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_add_phone_number(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAddPhoneNumberParams | dict = {},
):
    """Create Add Phone Number for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAddPhoneNumberParams type.
    """
    return Business(business_id).create_add_phone_number(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ad_network_application(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdNetworkApplicationParams | dict = {},
):
    """Create Ad Network Application for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAdNetworkApplicationParams type.
    """
    return Business(business_id).create_ad_network_application(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ad_network_analytics(
    business_id: str,
    fields: list[AdNetworkAnalyticsSyncQueryResultField] = [],
    params: BusinessGetAdNetworkAnalyticsParams | dict = {},
):
    """Get Ad Network Analytics for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See AdNetworkAnalyticsSyncQueryResultField type.
        params: Query parameters. Available params: See BusinessGetAdNetworkAnalyticsParams type.
    """
    return Business(business_id).get_ad_network_analytics(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ad_network_analytic(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdNetworkAnalyticParams | dict = {},
):
    """Create Ad Network Analytic for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAdNetworkAnalyticParams type.
    """
    return Business(business_id).create_ad_network_analytic(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ad_network_analytics_results(
    business_id: str,
    fields: list[AdNetworkAnalyticsAsyncQueryResultField] = [],
    params: BusinessGetAdNetworkAnalyticsResultsParams | dict = {},
):
    """Get Ad Network Analytics Results for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See AdNetworkAnalyticsAsyncQueryResultField type.
        params: Query parameters. Available params: See BusinessGetAdNetworkAnalyticsResultsParams type.
    """
    return Business(business_id).get_ad_network_analytics_results(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ads_dataset(
    business_id: str,
    fields: list[AdsDatasetField] = [],
    params: BusinessGetAdsDatasetParams | dict = {},
):
    """Get Ads Dataset for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See AdsDatasetField type.
        params: Query parameters. Available params: See BusinessGetAdsDatasetParams type.
    """
    return Business(business_id).get_ads_dataset(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ads_data_set(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdsDataSetParams | dict = {},
):
    """Create Ads Data Set for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAdsDataSetParams type.
    """
    return Business(business_id).create_ads_data_set(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ads_reporting_mmm_reports(
    business_id: str,
    fields: list[AdsReportBuilderMMMReportField] = [],
    params: BusinessGetAdsReportingMmmReportsParams | dict = {},
):
    """Get Ads Reporting Mmm Reports for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See AdsReportBuilderMMMReportField type.
        params: Query parameters. Available params: See BusinessGetAdsReportingMmmReportsParams type.
    """
    return Business(business_id).get_ads_reporting_mmm_reports(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_ads_pixels(
    business_id: str,
    fields: list[AdsPixelField] = [],
    params: BusinessGetAdsPixelsParams | dict = {},
):
    """Get Ads Pixels for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See AdsPixelField type.
        params: Query parameters. Available params: See BusinessGetAdsPixelsParams type.
    """
    return Business(business_id).get_ads_pixels(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_ads_pixel(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateAdsPixelParams | dict = {},
):
    """Create Ads Pixel for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateAdsPixelParams type.
    """
    return Business(business_id).create_ads_pixel(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_agencies(
    business_id: str,
    params: BusinessDeleteAgenciesParams | dict = {},
):
    """Delete Agencies for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteAgenciesParams type.
    """
    return Business(business_id).delete_agencies(params=params)


@business_server.tool
@wrapped_fn_tool
def create_block_list_draft(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateBlockListDraftParams | dict = {},
):
    """Create Block List Draft for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateBlockListDraftParams type.
    """
    return Business(business_id).create_block_list_draft(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_bm_review_request(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateBmReviewRequestParams | dict = {},
):
    """Create Bm Review Request for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateBmReviewRequestParams type.
    """
    return Business(business_id).create_bm_review_request(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_business_invoices(
    business_id: str,
    fields: list[OmegaCustomerTrxField] = [],
    params: BusinessGetBusinessInvoicesParams | dict = {},
):
    """Get Business Invoices for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See OmegaCustomerTrxField type.
        params: Query parameters. Available params: See BusinessGetBusinessInvoicesParams type.
    """
    return Business(business_id).get_business_invoices(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_business_user(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateBusinessUserParams | dict = {},
):
    """Create Business User for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateBusinessUserParams type.
    """
    return Business(business_id).create_business_user(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_claim_custom_conversion(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateClaimCustomConversionParams | dict = {},
):
    """Create Claim Custom Conversion for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateClaimCustomConversionParams type.
    """
    return Business(business_id).create_claim_custom_conversion(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_client_ad_accounts(
    business_id: str,
    fields: list[AdAccountField] = [],
    params: BusinessGetClientAdAccountsParams | dict = {},
):
    """Get Client Ad Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See BusinessGetClientAdAccountsParams type.
    """
    return Business(business_id).get_client_ad_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_client_app(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateClientAppParams | dict = {},
):
    """Create Client App for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateClientAppParams type.
    """
    return Business(business_id).create_client_app(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_client_page(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateClientPageParams | dict = {},
):
    """Create Client Page for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateClientPageParams type.
    """
    return Business(business_id).create_client_page(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_clients(
    business_id: str,
    params: BusinessDeleteClientsParams | dict = {},
):
    """Delete Clients for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteClientsParams type.
    """
    return Business(business_id).delete_clients(params=params)


@business_server.tool
@wrapped_fn_tool
def get_collaborative_ads_collaboration_requests(
    business_id: str,
    fields: list[CPASCollaborationRequestField] = [],
    params: BusinessGetCollaborativeAdsCollaborationRequestsParams | dict = {},
):
    """Get Collaborative Ads Collaboration Requests for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See CPASCollaborationRequestField type.
        params: Query parameters. Available params: See BusinessGetCollaborativeAdsCollaborationRequestsParams type.
    """
    return Business(business_id).get_collaborative_ads_collaboration_requests(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_collaborative_ads_collaboration_request(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCollaborativeAdsCollaborationRequestParams | dict = {},
):
    """Create Collaborative Ads Collaboration Request for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateCollaborativeAdsCollaborationRequestParams type.
    """
    return Business(business_id).create_collaborative_ads_collaboration_request(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_cpas_business_setup_config(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCpasBusinessSetupConfigParams | dict = {},
):
    """Create Cpas Business Setup Config for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateCpasBusinessSetupConfigParams type.
    """
    return Business(business_id).create_cpas_business_setup_config(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_creative_folder(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCreativeFolderParams | dict = {},
):
    """Create Creative Folder for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateCreativeFolderParams type.
    """
    return Business(business_id).create_creative_folder(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_custom_conversion(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateCustomConversionParams | dict = {},
):
    """Create Custom Conversion for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateCustomConversionParams type.
    """
    return Business(business_id).create_custom_conversion(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_event_source_group(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateEventSourceGroupParams | dict = {},
):
    """Create Event Source Group for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateEventSourceGroupParams type.
    """
    return Business(business_id).create_event_source_group(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_extended_credit_applications(
    business_id: str,
    fields: list[ExtendedCreditApplicationField] = [],
    params: BusinessGetExtendedCreditApplicationsParams | dict = {},
):
    """Get Extended Credit Applications for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See ExtendedCreditApplicationField type.
        params: Query parameters. Available params: See BusinessGetExtendedCreditApplicationsParams type.
    """
    return Business(business_id).get_extended_credit_applications(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_extended_credits(
    business_id: str,
    fields: list[ExtendedCreditField] = [],
    params: BusinessGetExtendedCreditsParams | dict = {},
):
    """Get Extended Credits for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See ExtendedCreditField type.
        params: Query parameters. Available params: See BusinessGetExtendedCreditsParams type.
    """
    return Business(business_id).get_extended_credits(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_image(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateImageParams | dict = {},
):
    """Create Image for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateImageParams type.
    """
    return Business(business_id).create_image(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_initiated_audience_sharing_requests(
    business_id: str,
    fields: list[BusinessAssetSharingAgreementField] = [],
    params: BusinessGetInitiatedAudienceSharingRequestsParams | dict = {},
):
    """Get Initiated Audience Sharing Requests for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See BusinessAssetSharingAgreementField type.
        params: Query parameters. Available params: See BusinessGetInitiatedAudienceSharingRequestsParams type.
    """
    return Business(business_id).get_initiated_audience_sharing_requests(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def delete_instagram_accounts(
    business_id: str,
    params: BusinessDeleteInstagramAccountsParams | dict = {},
):
    """Delete Instagram Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteInstagramAccountsParams type.
    """
    return Business(business_id).delete_instagram_accounts(params=params)


@business_server.tool
@wrapped_fn_tool
def delete_managed_businesses(
    business_id: str,
    params: BusinessDeleteManagedBusinessesParams | dict = {},
):
    """Delete Managed Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteManagedBusinessesParams type.
    """
    return Business(business_id).delete_managed_businesses(params=params)


@business_server.tool
@wrapped_fn_tool
def create_managed_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateManagedBusinessParams | dict = {},
):
    """Create Managed Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateManagedBusinessParams type.
    """
    return Business(business_id).create_managed_business(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_managed_partner_ads_funding_source_details(
    business_id: str,
    fields: list[FundingSourceDetailsCouponField] = [],
    params: BusinessGetManagedPartnerAdsFundingSourceDetailsParams | dict = {},
):
    """Get Managed Partner Ads Funding Source Details for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See FundingSourceDetailsCouponField type.
        params: Query parameters. Available params: See BusinessGetManagedPartnerAdsFundingSourceDetailsParams type.
    """
    return Business(business_id).get_managed_partner_ads_funding_source_details(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_managed_partner_business_setup(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateManagedPartnerBusinessSetupParams | dict = {},
):
    """Create Managed Partner Business Setup for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateManagedPartnerBusinessSetupParams type.
    """
    return Business(business_id).create_managed_partner_business_setup(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_managed_partner_businesses(
    business_id: str,
    params: BusinessDeleteManagedPartnerBusinessesParams | dict = {},
):
    """Delete Managed Partner Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteManagedPartnerBusinessesParams type.
    """
    return Business(business_id).delete_managed_partner_businesses(params=params)


@business_server.tool
@wrapped_fn_tool
def create_managed_partner_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateManagedPartnerBusinessParams | dict = {},
):
    """Create Managed Partner Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateManagedPartnerBusinessParams type.
    """
    return Business(business_id).create_managed_partner_business(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_onboard_partners_to_mm_lite(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOnboardPartnersToMmLiteParams | dict = {},
):
    """Create Onboard Partners To Mm Lite for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateOnboardPartnersToMmLiteParams type.
    """
    return Business(business_id).create_onboard_partners_to_mm_lite(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_open_bridge_configuration(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOpenBridgeConfigurationParams | dict = {},
):
    """Create Open Bridge Configuration for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateOpenBridgeConfigurationParams type.
    """
    return Business(business_id).create_open_bridge_configuration(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_ad_accounts(
    business_id: str,
    fields: list[AdAccountField] = [],
    params: BusinessGetOwnedAdAccountsParams | dict = {},
):
    """Get Owned Ad Accounts for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See BusinessGetOwnedAdAccountsParams type.
    """
    return Business(business_id).get_owned_ad_accounts(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedAdAccountParams | dict = {},
):
    """Create Owned Ad Account for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateOwnedAdAccountParams type.
    """
    return Business(business_id).create_owned_ad_account(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_app(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedAppParams | dict = {},
):
    """Create Owned App for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateOwnedAppParams type.
    """
    return Business(business_id).create_owned_app(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_owned_businesses(
    business_id: str,
    params: BusinessDeleteOwnedBusinessesParams | dict = {},
):
    """Delete Owned Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteOwnedBusinessesParams type.
    """
    return Business(business_id).delete_owned_businesses(params=params)


@business_server.tool
@wrapped_fn_tool
def get_owned_businesses(
    business_id: str,
    fields: list[BusinessField] = [],
    params: BusinessGetOwnedBusinessesParams | dict = {},
):
    """Get Owned Businesses for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See BusinessField type.
        params: Query parameters. Available params: See BusinessGetOwnedBusinessesParams type.
    """
    return Business(business_id).get_owned_businesses(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedBusinessParams | dict = {},
):
    """Create Owned Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateOwnedBusinessParams type.
    """
    return Business(business_id).create_owned_business(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_page(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedPageParams | dict = {},
):
    """Create Owned Page for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateOwnedPageParams type.
    """
    return Business(business_id).create_owned_page(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_owned_product_catalog(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateOwnedProductCatalogParams | dict = {},
):
    """Create Owned Product Catalog for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateOwnedProductCatalogParams type.
    """
    return Business(business_id).create_owned_product_catalog(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def delete_pages(
    business_id: str,
    params: BusinessDeletePagesParams | dict = {},
):
    """Delete Pages for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeletePagesParams type.
    """
    return Business(business_id).delete_pages(params=params)


@business_server.tool
@wrapped_fn_tool
def create_partner_premium_option(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreatePartnerPremiumOptionParams | dict = {},
):
    """Create Partner Premium Option for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreatePartnerPremiumOptionParams type.
    """
    return Business(business_id).create_partner_premium_option(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_pending_users(
    business_id: str,
    fields: list[BusinessRoleRequestField] = [],
    params: BusinessGetPendingUsersParams | dict = {},
):
    """Get Pending Users for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See BusinessRoleRequestField type.
        params: Query parameters. Available params: See BusinessGetPendingUsersParams type.
    """
    return Business(business_id).get_pending_users(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_picture(
    business_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: BusinessGetPictureParams | dict = {},
):
    """Get Picture for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See ProfilePictureSourceField type.
        params: Query parameters. Available params: See BusinessGetPictureParams type.
    """
    return Business(business_id).get_picture(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_pre_verified_numbers(
    business_id: str,
    fields: list[WhatsAppBusinessPreVerifiedPhoneNumberField] = [],
    params: BusinessGetPreVerifiedNumbersParams | dict = {},
):
    """Get Pre Verified Numbers for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See WhatsAppBusinessPreVerifiedPhoneNumberField type.
        params: Query parameters. Available params: See BusinessGetPreVerifiedNumbersParams type.
    """
    return Business(business_id).get_pre_verified_numbers(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def get_received_audience_sharing_requests(
    business_id: str,
    fields: list[BusinessAssetSharingAgreementField] = [],
    params: BusinessGetReceivedAudienceSharingRequestsParams | dict = {},
):
    """Get Received Audience Sharing Requests for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See BusinessAssetSharingAgreementField type.
        params: Query parameters. Available params: See BusinessGetReceivedAudienceSharingRequestsParams type.
    """
    return Business(business_id).get_received_audience_sharing_requests(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def get_self_certified_whats_app_business_submissions(
    business_id: str,
    fields: list[WhatsAppBusinessPartnerClientVerificationSubmissionField] = [],
    params: BusinessGetSelfCertifiedWhatsAppBusinessSubmissionsParams | dict = {},
):
    """Get Self Certified Whats App Business Submissions for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve. Available fields: See WhatsAppBusinessPartnerClientVerificationSubmissionField type.
        params: Query parameters. Available params: See BusinessGetSelfCertifiedWhatsAppBusinessSubmissionsParams type.
    """
    return Business(business_id).get_self_certified_whats_app_business_submissions(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_self_certify_whats_app_business(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSelfCertifyWhatsAppBusinessParams | dict = {},
):
    """Create Self Certify Whats App Business for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateSelfCertifyWhatsAppBusinessParams type.
    """
    return Business(business_id).create_self_certify_whats_app_business(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def create_setup_managed_partner_ad_account(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSetupManagedPartnerAdAccountParams | dict = {},
):
    """Create Setup Managed Partner Ad Account for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateSetupManagedPartnerAdAccountParams type.
    """
    return Business(business_id).create_setup_managed_partner_ad_account(
        fields=fields, params=params
    )


@business_server.tool
@wrapped_fn_tool
def delete_share_pre_verified_numbers(
    business_id: str,
    params: BusinessDeleteSharePreVerifiedNumbersParams | dict = {},
):
    """Delete Share Pre Verified Numbers for this Business.

    Args:
        business_id: The ID of the Business.
        params: Query parameters. Available params: See BusinessDeleteSharePreVerifiedNumbersParams type.
    """
    return Business(business_id).delete_share_pre_verified_numbers(params=params)


@business_server.tool
@wrapped_fn_tool
def create_share_pre_verified_number(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSharePreVerifiedNumberParams | dict = {},
):
    """Create Share Pre Verified Number for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateSharePreVerifiedNumberParams type.
    """
    return Business(business_id).create_share_pre_verified_number(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_system_user_access_token(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSystemUserAccessTokenParams | dict = {},
):
    """Create System User Access Token for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateSystemUserAccessTokenParams type.
    """
    return Business(business_id).create_system_user_access_token(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_system_user(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateSystemUserParams | dict = {},
):
    """Create System User for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateSystemUserParams type.
    """
    return Business(business_id).create_system_user(fields=fields, params=params)


@business_server.tool
@wrapped_fn_tool
def create_video(
    business_id: str,
    fields: list[str] = [],
    params: BusinessCreateVideoParams | dict = {},
):
    """Create Video for this Business.

    Args:
        business_id: The ID of the Business.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessCreateVideoParams type.
    """
    return Business(business_id).create_video(fields=fields, params=params)
