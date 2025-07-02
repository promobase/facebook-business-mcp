"""AdAccount MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.ad import AdField
from src.generated.models.adaccount import (
    AdAccountCreateAccountControlParams,
    AdAccountCreateAdCreativeParams,
    AdAccountCreateAdImageParams,
    AdAccountCreateAdLabelParams,
    AdAccountCreateAdParams,
    AdAccountCreateAdPlacePageSetParams,
    AdAccountCreateAdPlacePageSetsAsyncParams,
    AdAccountCreateAdPlayableParams,
    AdAccountCreateAdRulesLibraryParams,
    AdAccountCreateAdSetParams,
    AdAccountCreateAdsPixelParams,
    AdAccountCreateAdVideoParams,
    AdAccountCreateAgencyParams,
    AdAccountCreateAssignedUserParams,
    AdAccountCreateAsyncAdCreativeParams,
    AdAccountCreateAsyncAdRequestSetParams,
    AdAccountCreateAsyncBatchRequestParams,
    AdAccountCreateBlockListDraftParams,
    AdAccountCreateBrandSafetyContentFilterLevelParams,
    AdAccountCreateCampaignParams,
    AdAccountCreateCustomAudienceParams,
    AdAccountCreateCustomAudiencesToParams,
    AdAccountCreateCustomConversionParams,
    AdAccountCreateProductAudienceParams,
    AdAccountCreatePublisherBlockListParams,
    AdAccountCreateReachFrequencyPredictionParams,
    AdAccountCreateRecommendationParams,
    AdAccountCreateSubscribedAppParams,
    AdAccountCreateTrackingParams,
    AdAccountCreateValueRuleSetParams,
    AdAccountCreateVideoAdParams,
    AdAccountDeleteAdImagesParams,
    AdAccountDeleteAdVideosParams,
    AdAccountDeleteAgenciesParams,
    AdAccountDeleteAssignedUsersParams,
    AdAccountDeleteCampaignsParams,
    AdAccountDeleteSubscribedAppsParams,
    AdAccountDeleteUsersOfAnyAudienceParams,
    AdAccountField,
    AdAccountGetActivitiesParams,
    AdAccountGetAdCreativesByLabelsParams,
    AdAccountGetAdImagesParams,
    AdAccountGetAdRulesHistoryParams,
    AdAccountGetAdSavedKeywordsParams,
    AdAccountGetAdsByLabelsParams,
    AdAccountGetAdSetsByLabelsParams,
    AdAccountGetAdSetsParams,
    AdAccountGetAdsParams,
    AdAccountGetAdsPixelsParams,
    AdAccountGetAdsReportingMmmReportsParams,
    AdAccountGetAdsVolumeParams,
    AdAccountGetAdvertisableApplicationsParams,
    AdAccountGetAdVideosParams,
    AdAccountGetAssignedUsersParams,
    AdAccountGetAsyncAdCreativesParams,
    AdAccountGetAsyncAdRequestSetsParams,
    AdAccountGetAsyncRequestsParams,
    AdAccountGetBroadTargetingCategoriesParams,
    AdAccountGetBusinessProjectsParams,
    AdAccountGetCampaignsByLabelsParams,
    AdAccountGetCampaignsParams,
    AdAccountGetConnectedInstagramAccountsWithIabpParams,
    AdAccountGetCustomAudiencesParams,
    AdAccountGetDeliveryEstimateParams,
    AdAccountGetDeprecatedTargetingAdSetsParams,
    AdAccountGetGeneratePreviewsParams,
    AdAccountGetInsightsAsyncParams,
    AdAccountGetInsightsParams,
    AdAccountGetIosFourteenCampaignLimitsParams,
    AdAccountGetMatchedSearchApplicationsParams,
    AdAccountGetMinimumBudgetsParams,
    AdAccountGetOnBehalfRequestsParams,
    AdAccountGetReachEstimateParams,
    AdAccountGetSavedAudiencesParams,
    AdAccountGetTargetingBrowseParams,
    AdAccountGetTargetingSearchParams,
    AdAccountGetTargetingSentenceLinesParams,
    AdAccountGetTargetingSuggestionsParams,
    AdAccountGetTargetingValidATIOnParams,
    AdAccountGetValueRuleSetParams,
    AdAccountGetVideoAdsParams,
    AdAccountUpdateParams,
)
from src.generated.models.adaccountadruleshistory import AdAccountAdRulesHistoryField
from src.generated.models.adaccountadvolume import AdAccountAdVolumeField
from src.generated.models.adaccountbusinessconstraints import AdAccountBusinessConstraintsField
from src.generated.models.adaccountdeliveryestimate import AdAccountDeliveryEstimateField
from src.generated.models.adaccountiosfourteencampaignlimits import (
    AdAccountIosFourteenCampaignLimitsField,
)
from src.generated.models.adaccountmatchedsearchapplicationsedgedata import (
    AdAccountMatchedSearchApplicationsEdgeDataField,
)
from src.generated.models.adaccountreachestimate import AdAccountReachEstimateField
from src.generated.models.adaccountrecommendations import AdAccountRecommendationsField
from src.generated.models.adaccountsubscribedapps import AdAccountSubscribedAppsField
from src.generated.models.adaccounttargetingunified import AdAccountTargetingUnifiedField
from src.generated.models.adactivity import AdActivityField
from src.generated.models.adasyncrequestset import AdAsyncRequestSetField
from src.generated.models.adcreative import AdCreativeField
from src.generated.models.adimage import AdImageField
from src.generated.models.adlabel import AdLabelField
from src.generated.models.adplacepageset import AdPlacePageSetField
from src.generated.models.adpreview import AdPreviewField
from src.generated.models.adreportrun import AdReportRunField
from src.generated.models.adrule import AdRuleField
from src.generated.models.adsavedkeywords import AdSavedKeywordsField
from src.generated.models.adset import AdSetField
from src.generated.models.adsinsights import AdsInsightsField
from src.generated.models.adspixel import AdsPixelField
from src.generated.models.adsreportbuildermmmreport import AdsReportBuilderMMMReportField
from src.generated.models.adsvalueadjustmentrulecollection import (
    AdsValueAdjustmentRuleCollectionField,
)
from src.generated.models.advideo import AdVideoField
from src.generated.models.application import ApplicationField
from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.asyncrequest import AsyncRequestField
from src.generated.models.broadtargetingcategories import BroadTargetingCategoriesField
from src.generated.models.businessownedobjectonbehalfofrequest import (
    BusinessOwnedObjectOnBehalfOfRequestField,
)
from src.generated.models.businessproject import BusinessProjectField
from src.generated.models.campaign import CampaignField
from src.generated.models.customaudience import CustomAudienceField
from src.generated.models.customconversion import CustomConversionField
from src.generated.models.iguser import IGUserField
from src.generated.models.minimumbudget import MinimumBudgetField
from src.generated.models.playablecontent import PlayableContentField
from src.generated.models.publisherblocklist import PublisherBlockListField
from src.generated.models.reachfrequencyprediction import ReachFrequencyPredictionField
from src.generated.models.savedaudience import SavedAudienceField
from src.generated.models.targetingsentenceline import TargetingSentenceLineField
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
    fields: list[AdAccountField] = [],
) -> str:
    """Get a AdAccount object by ID.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
    """
    obj = AdAccount(adaccount_id)
    return obj.api_get(fields=fields)


@adaccount_server.tool
@wrapped_fn_tool
def update_adaccount(
    adaccount_id: str,
    fields: list[AdAccountField] = [],
    params: AdAccountUpdateParams | dict = {},
) -> str:
    """Update a AdAccount object.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to return after update. Available fields: See AdAccountField type.
        params: Parameters to update. Available params: See AdAccountUpdateParams type.
    """
    return AdAccount(adaccount_id).api_update(fields=fields, params=params)


# ---- Edge Methods (80) ----
@adaccount_server.tool
@wrapped_fn_tool
def create_account_control(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAccountControlParams | dict = {},
):
    """Create Account Control for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAccountControlParams type.
    """
    return AdAccount(adaccount_id).create_account_control(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_activities(
    adaccount_id: str,
    fields: list[AdActivityField] = [],
    params: AdAccountGetActivitiesParams | dict = {},
):
    """Get Activities for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdActivityField type.
        params: Query parameters. Available params: See AdAccountGetActivitiesParams type.
    """
    return AdAccount(adaccount_id).get_activities(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_place_page_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdPlacePageSetParams | dict = {},
):
    """Create Ad Place Page Set for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdPlacePageSetParams type.
    """
    return AdAccount(adaccount_id).create_ad_place_page_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_place_page_sets_async(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdPlacePageSetsAsyncParams | dict = {},
):
    """Create Ad Place Page Sets Async for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdPlacePageSetsAsyncParams type.
    """
    return AdAccount(adaccount_id).create_ad_place_page_sets_async(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_saved_keywords(
    adaccount_id: str,
    fields: list[AdSavedKeywordsField] = [],
    params: AdAccountGetAdSavedKeywordsParams | dict = {},
):
    """Get Ad Saved Keywords for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdSavedKeywordsField type.
        params: Query parameters. Available params: See AdAccountGetAdSavedKeywordsParams type.
    """
    return AdAccount(adaccount_id).get_ad_saved_keywords(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_creative(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdCreativeParams | dict = {},
):
    """Create Ad Creative for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdCreativeParams type.
    """
    return AdAccount(adaccount_id).create_ad_creative(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_creatives_by_labels(
    adaccount_id: str,
    fields: list[AdCreativeField] = [],
    params: AdAccountGetAdCreativesByLabelsParams | dict = {},
):
    """Get Ad Creatives By Labels for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdCreativeField type.
        params: Query parameters. Available params: See AdAccountGetAdCreativesByLabelsParams type.
    """
    return AdAccount(adaccount_id).get_ad_creatives_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_ad_images(
    adaccount_id: str,
    params: AdAccountDeleteAdImagesParams | dict = {},
):
    """Delete Ad Images for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        params: Query parameters. Available params: See AdAccountDeleteAdImagesParams type.
    """
    return AdAccount(adaccount_id).delete_ad_images(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_images(
    adaccount_id: str,
    fields: list[AdImageField] = [],
    params: AdAccountGetAdImagesParams | dict = {},
):
    """Get Ad Images for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdImageField type.
        params: Query parameters. Available params: See AdAccountGetAdImagesParams type.
    """
    return AdAccount(adaccount_id).get_ad_images(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_image(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdImageParams | dict = {},
):
    """Create Ad Image for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdImageParams type.
    """
    return AdAccount(adaccount_id).create_ad_image(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_label(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdLabelParams | dict = {},
):
    """Create Ad Label for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdLabelParams type.
    """
    return AdAccount(adaccount_id).create_ad_label(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_playable(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdPlayableParams | dict = {},
):
    """Create Ad Playable for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdPlayableParams type.
    """
    return AdAccount(adaccount_id).create_ad_playable(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_rules_history(
    adaccount_id: str,
    fields: list[AdAccountAdRulesHistoryField] = [],
    params: AdAccountGetAdRulesHistoryParams | dict = {},
):
    """Get Ad Rules History for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountAdRulesHistoryField type.
        params: Query parameters. Available params: See AdAccountGetAdRulesHistoryParams type.
    """
    return AdAccount(adaccount_id).get_ad_rules_history(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_rules_library(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdRulesLibraryParams | dict = {},
):
    """Create Ad Rules Library for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdRulesLibraryParams type.
    """
    return AdAccount(adaccount_id).create_ad_rules_library(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads(
    adaccount_id: str,
    fields: list[AdField] = [],
    params: AdAccountGetAdsParams | dict = {},
):
    """Get Ads for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdField type.
        params: Query parameters. Available params: See AdAccountGetAdsParams type.
    """
    return AdAccount(adaccount_id).get_ads(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdParams | dict = {},
):
    """Create Ad for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdParams type.
    """
    return AdAccount(adaccount_id).create_ad(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_reporting_mmm_reports(
    adaccount_id: str,
    fields: list[AdsReportBuilderMMMReportField] = [],
    params: AdAccountGetAdsReportingMmmReportsParams | dict = {},
):
    """Get Ads Reporting Mmm Reports for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdsReportBuilderMMMReportField type.
        params: Query parameters. Available params: See AdAccountGetAdsReportingMmmReportsParams type.
    """
    return AdAccount(adaccount_id).get_ads_reporting_mmm_reports(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_volume(
    adaccount_id: str,
    fields: list[AdAccountAdVolumeField] = [],
    params: AdAccountGetAdsVolumeParams | dict = {},
):
    """Get Ads Volume for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountAdVolumeField type.
        params: Query parameters. Available params: See AdAccountGetAdsVolumeParams type.
    """
    return AdAccount(adaccount_id).get_ads_volume(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_by_labels(
    adaccount_id: str,
    fields: list[AdField] = [],
    params: AdAccountGetAdsByLabelsParams | dict = {},
):
    """Get Ads By Labels for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdField type.
        params: Query parameters. Available params: See AdAccountGetAdsByLabelsParams type.
    """
    return AdAccount(adaccount_id).get_ads_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_sets(
    adaccount_id: str,
    fields: list[AdSetField] = [],
    params: AdAccountGetAdSetsParams | dict = {},
):
    """Get Ad Sets for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdSetField type.
        params: Query parameters. Available params: See AdAccountGetAdSetsParams type.
    """
    return AdAccount(adaccount_id).get_ad_sets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdSetParams | dict = {},
):
    """Create Ad Set for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdSetParams type.
    """
    return AdAccount(adaccount_id).create_ad_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_sets_by_labels(
    adaccount_id: str,
    fields: list[AdSetField] = [],
    params: AdAccountGetAdSetsByLabelsParams | dict = {},
):
    """Get Ad Sets By Labels for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdSetField type.
        params: Query parameters. Available params: See AdAccountGetAdSetsByLabelsParams type.
    """
    return AdAccount(adaccount_id).get_ad_sets_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ads_pixels(
    adaccount_id: str,
    fields: list[AdsPixelField] = [],
    params: AdAccountGetAdsPixelsParams | dict = {},
):
    """Get Ads Pixels for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdsPixelField type.
        params: Query parameters. Available params: See AdAccountGetAdsPixelsParams type.
    """
    return AdAccount(adaccount_id).get_ads_pixels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ads_pixel(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdsPixelParams | dict = {},
):
    """Create Ads Pixel for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdsPixelParams type.
    """
    return AdAccount(adaccount_id).create_ads_pixel(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_advertisable_applications(
    adaccount_id: str,
    fields: list[ApplicationField] = [],
    params: AdAccountGetAdvertisableApplicationsParams | dict = {},
):
    """Get Advertisable Applications for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See ApplicationField type.
        params: Query parameters. Available params: See AdAccountGetAdvertisableApplicationsParams type.
    """
    return AdAccount(adaccount_id).get_advertisable_applications(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_ad_videos(
    adaccount_id: str,
    params: AdAccountDeleteAdVideosParams | dict = {},
):
    """Delete Ad Videos for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        params: Query parameters. Available params: See AdAccountDeleteAdVideosParams type.
    """
    return AdAccount(adaccount_id).delete_ad_videos(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ad_videos(
    adaccount_id: str,
    fields: list[AdVideoField] = [],
    params: AdAccountGetAdVideosParams | dict = {},
):
    """Get Ad Videos for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdVideoField type.
        params: Query parameters. Available params: See AdAccountGetAdVideosParams type.
    """
    return AdAccount(adaccount_id).get_ad_videos(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_ad_video(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdVideoParams | dict = {},
):
    """Create Ad Video for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAdVideoParams type.
    """
    return AdAccount(adaccount_id).create_ad_video(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_agencies(
    adaccount_id: str,
    params: AdAccountDeleteAgenciesParams | dict = {},
):
    """Delete Agencies for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        params: Query parameters. Available params: See AdAccountDeleteAgenciesParams type.
    """
    return AdAccount(adaccount_id).delete_agencies(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_agency(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAgencyParams | dict = {},
):
    """Create Agency for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAgencyParams type.
    """
    return AdAccount(adaccount_id).create_agency(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    adaccount_id: str,
    params: AdAccountDeleteAssignedUsersParams | dict = {},
):
    """Delete Assigned Users for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        params: Query parameters. Available params: See AdAccountDeleteAssignedUsersParams type.
    """
    return AdAccount(adaccount_id).delete_assigned_users(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_assigned_users(
    adaccount_id: str,
    fields: list[AssignedUserField] = [],
    params: AdAccountGetAssignedUsersParams | dict = {},
):
    """Get Assigned Users for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AssignedUserField type.
        params: Query parameters. Available params: See AdAccountGetAssignedUsersParams type.
    """
    return AdAccount(adaccount_id).get_assigned_users(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_assigned_user(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAssignedUserParams | dict = {},
):
    """Create Assigned User for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAssignedUserParams type.
    """
    return AdAccount(adaccount_id).create_assigned_user(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_async_batch_request(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAsyncBatchRequestParams | dict = {},
):
    """Create Async Batch Request for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAsyncBatchRequestParams type.
    """
    return AdAccount(adaccount_id).create_async_batch_request(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_async_requests(
    adaccount_id: str,
    fields: list[AsyncRequestField] = [],
    params: AdAccountGetAsyncRequestsParams | dict = {},
):
    """Get Async Requests for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AsyncRequestField type.
        params: Query parameters. Available params: See AdAccountGetAsyncRequestsParams type.
    """
    return AdAccount(adaccount_id).get_async_requests(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_async_ad_creatives(
    adaccount_id: str,
    fields: list[AdAsyncRequestSetField] = [],
    params: AdAccountGetAsyncAdCreativesParams | dict = {},
):
    """Get Async Ad Creatives for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAsyncRequestSetField type.
        params: Query parameters. Available params: See AdAccountGetAsyncAdCreativesParams type.
    """
    return AdAccount(adaccount_id).get_async_ad_creatives(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_async_ad_creative(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAsyncAdCreativeParams | dict = {},
):
    """Create Async Ad Creative for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAsyncAdCreativeParams type.
    """
    return AdAccount(adaccount_id).create_async_ad_creative(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_async_ad_request_sets(
    adaccount_id: str,
    fields: list[AdAsyncRequestSetField] = [],
    params: AdAccountGetAsyncAdRequestSetsParams | dict = {},
):
    """Get Async Ad Request Sets for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAsyncRequestSetField type.
        params: Query parameters. Available params: See AdAccountGetAsyncAdRequestSetsParams type.
    """
    return AdAccount(adaccount_id).get_async_ad_request_sets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_async_ad_request_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAsyncAdRequestSetParams | dict = {},
):
    """Create Async Ad Request Set for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateAsyncAdRequestSetParams type.
    """
    return AdAccount(adaccount_id).create_async_ad_request_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_block_list_draft(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateBlockListDraftParams | dict = {},
):
    """Create Block List Draft for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateBlockListDraftParams type.
    """
    return AdAccount(adaccount_id).create_block_list_draft(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_brand_safety_content_filter_level(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateBrandSafetyContentFilterLevelParams | dict = {},
):
    """Create Brand Safety Content Filter Level for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateBrandSafetyContentFilterLevelParams type.
    """
    return AdAccount(adaccount_id).create_brand_safety_content_filter_level(
        fields=fields, params=params
    )


@adaccount_server.tool
@wrapped_fn_tool
def get_broad_targeting_categories(
    adaccount_id: str,
    fields: list[BroadTargetingCategoriesField] = [],
    params: AdAccountGetBroadTargetingCategoriesParams | dict = {},
):
    """Get Broad Targeting Categories for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See BroadTargetingCategoriesField type.
        params: Query parameters. Available params: See AdAccountGetBroadTargetingCategoriesParams type.
    """
    return AdAccount(adaccount_id).get_broad_targeting_categories(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_business_projects(
    adaccount_id: str,
    fields: list[BusinessProjectField] = [],
    params: AdAccountGetBusinessProjectsParams | dict = {},
):
    """Get Business Projects for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See BusinessProjectField type.
        params: Query parameters. Available params: See AdAccountGetBusinessProjectsParams type.
    """
    return AdAccount(adaccount_id).get_business_projects(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_campaigns(
    adaccount_id: str,
    params: AdAccountDeleteCampaignsParams | dict = {},
):
    """Delete Campaigns for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        params: Query parameters. Available params: See AdAccountDeleteCampaignsParams type.
    """
    return AdAccount(adaccount_id).delete_campaigns(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_campaigns(
    adaccount_id: str,
    fields: list[CampaignField] = [],
    params: AdAccountGetCampaignsParams | dict = {},
):
    """Get Campaigns for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See CampaignField type.
        params: Query parameters. Available params: See AdAccountGetCampaignsParams type.
    """
    return AdAccount(adaccount_id).get_campaigns(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_campaign(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateCampaignParams | dict = {},
):
    """Create Campaign for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateCampaignParams type.
    """
    return AdAccount(adaccount_id).create_campaign(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_campaigns_by_labels(
    adaccount_id: str,
    fields: list[CampaignField] = [],
    params: AdAccountGetCampaignsByLabelsParams | dict = {},
):
    """Get Campaigns By Labels for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See CampaignField type.
        params: Query parameters. Available params: See AdAccountGetCampaignsByLabelsParams type.
    """
    return AdAccount(adaccount_id).get_campaigns_by_labels(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_connected_instagram_accounts_with_iabp(
    adaccount_id: str,
    fields: list[IGUserField] = [],
    params: AdAccountGetConnectedInstagramAccountsWithIabpParams | dict = {},
):
    """Get Connected Instagram Accounts With Iabp for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See IGUserField type.
        params: Query parameters. Available params: See AdAccountGetConnectedInstagramAccountsWithIabpParams type.
    """
    return AdAccount(adaccount_id).get_connected_instagram_accounts_with_iabp(
        fields=fields, params=params
    )


@adaccount_server.tool
@wrapped_fn_tool
def get_custom_audiences(
    adaccount_id: str,
    fields: list[CustomAudienceField] = [],
    params: AdAccountGetCustomAudiencesParams | dict = {},
):
    """Get Custom Audiences for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See CustomAudienceField type.
        params: Query parameters. Available params: See AdAccountGetCustomAudiencesParams type.
    """
    return AdAccount(adaccount_id).get_custom_audiences(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_custom_audience(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateCustomAudienceParams | dict = {},
):
    """Create Custom Audience for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateCustomAudienceParams type.
    """
    return AdAccount(adaccount_id).create_custom_audience(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_custom_audiences_to(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateCustomAudiencesToParams | dict = {},
):
    """Create Custom Audiences To for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateCustomAudiencesToParams type.
    """
    return AdAccount(adaccount_id).create_custom_audiences_to(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_custom_conversion(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateCustomConversionParams | dict = {},
):
    """Create Custom Conversion for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateCustomConversionParams type.
    """
    return AdAccount(adaccount_id).create_custom_conversion(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_delivery_estimate(
    adaccount_id: str,
    fields: list[AdAccountDeliveryEstimateField] = [],
    params: AdAccountGetDeliveryEstimateParams | dict = {},
):
    """Get Delivery Estimate for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountDeliveryEstimateField type.
        params: Query parameters. Available params: See AdAccountGetDeliveryEstimateParams type.
    """
    return AdAccount(adaccount_id).get_delivery_estimate(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_deprecated_targeting_ad_sets(
    adaccount_id: str,
    fields: list[AdSetField] = [],
    params: AdAccountGetDeprecatedTargetingAdSetsParams | dict = {},
):
    """Get Deprecated Targeting Ad Sets for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdSetField type.
        params: Query parameters. Available params: See AdAccountGetDeprecatedTargetingAdSetsParams type.
    """
    return AdAccount(adaccount_id).get_deprecated_targeting_ad_sets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_generate_previews(
    adaccount_id: str,
    fields: list[AdPreviewField] = [],
    params: AdAccountGetGeneratePreviewsParams | dict = {},
):
    """Get Generate Previews for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdPreviewField type.
        params: Query parameters. Available params: See AdAccountGetGeneratePreviewsParams type.
    """
    return AdAccount(adaccount_id).get_generate_previews(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_insights(
    adaccount_id: str,
    fields: list[AdsInsightsField] = [],
    params: AdAccountGetInsightsParams | dict = {},
):
    """Get Insights for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdsInsightsField type.
        params: Query parameters. Available params: See AdAccountGetInsightsParams type.
    """
    return AdAccount(adaccount_id).get_insights(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_insights_async(
    adaccount_id: str,
    fields: list[AdReportRunField] = [],
    params: AdAccountGetInsightsAsyncParams | dict = {},
):
    """Get Insights Async for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdReportRunField type.
        params: Query parameters. Available params: See AdAccountGetInsightsAsyncParams type.
    """
    return AdAccount(adaccount_id).get_insights_async(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_ios_fourteen_campaign_limits(
    adaccount_id: str,
    fields: list[AdAccountIosFourteenCampaignLimitsField] = [],
    params: AdAccountGetIosFourteenCampaignLimitsParams | dict = {},
):
    """Get Ios Fourteen Campaign Limits for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountIosFourteenCampaignLimitsField type.
        params: Query parameters. Available params: See AdAccountGetIosFourteenCampaignLimitsParams type.
    """
    return AdAccount(adaccount_id).get_ios_fourteen_campaign_limits(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_matched_search_applications(
    adaccount_id: str,
    fields: list[AdAccountMatchedSearchApplicationsEdgeDataField] = [],
    params: AdAccountGetMatchedSearchApplicationsParams | dict = {},
):
    """Get Matched Search Applications for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountMatchedSearchApplicationsEdgeDataField type.
        params: Query parameters. Available params: See AdAccountGetMatchedSearchApplicationsParams type.
    """
    return AdAccount(adaccount_id).get_matched_search_applications(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_minimum_budgets(
    adaccount_id: str,
    fields: list[MinimumBudgetField] = [],
    params: AdAccountGetMinimumBudgetsParams | dict = {},
):
    """Get Minimum Budgets for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See MinimumBudgetField type.
        params: Query parameters. Available params: See AdAccountGetMinimumBudgetsParams type.
    """
    return AdAccount(adaccount_id).get_minimum_budgets(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_on_behalf_requests(
    adaccount_id: str,
    fields: list[BusinessOwnedObjectOnBehalfOfRequestField] = [],
    params: AdAccountGetOnBehalfRequestsParams | dict = {},
):
    """Get On Behalf Requests for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See BusinessOwnedObjectOnBehalfOfRequestField type.
        params: Query parameters. Available params: See AdAccountGetOnBehalfRequestsParams type.
    """
    return AdAccount(adaccount_id).get_on_behalf_requests(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_product_audience(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateProductAudienceParams | dict = {},
):
    """Create Product Audience for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateProductAudienceParams type.
    """
    return AdAccount(adaccount_id).create_product_audience(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_publisher_block_list(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreatePublisherBlockListParams | dict = {},
):
    """Create Publisher Block List for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreatePublisherBlockListParams type.
    """
    return AdAccount(adaccount_id).create_publisher_block_list(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_reach_estimate(
    adaccount_id: str,
    fields: list[AdAccountReachEstimateField] = [],
    params: AdAccountGetReachEstimateParams | dict = {},
):
    """Get Reach Estimate for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountReachEstimateField type.
        params: Query parameters. Available params: See AdAccountGetReachEstimateParams type.
    """
    return AdAccount(adaccount_id).get_reach_estimate(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_reach_frequency_prediction(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateReachFrequencyPredictionParams | dict = {},
):
    """Create Reach Frequency Prediction for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateReachFrequencyPredictionParams type.
    """
    return AdAccount(adaccount_id).create_reach_frequency_prediction(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_recommendation(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateRecommendationParams | dict = {},
):
    """Create Recommendation for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateRecommendationParams type.
    """
    return AdAccount(adaccount_id).create_recommendation(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_saved_audiences(
    adaccount_id: str,
    fields: list[SavedAudienceField] = [],
    params: AdAccountGetSavedAudiencesParams | dict = {},
):
    """Get Saved Audiences for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See SavedAudienceField type.
        params: Query parameters. Available params: See AdAccountGetSavedAudiencesParams type.
    """
    return AdAccount(adaccount_id).get_saved_audiences(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_subscribed_apps(
    adaccount_id: str,
    params: AdAccountDeleteSubscribedAppsParams | dict = {},
):
    """Delete Subscribed Apps for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        params: Query parameters. Available params: See AdAccountDeleteSubscribedAppsParams type.
    """
    return AdAccount(adaccount_id).delete_subscribed_apps(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateSubscribedAppParams | dict = {},
):
    """Create Subscribed App for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateSubscribedAppParams type.
    """
    return AdAccount(adaccount_id).create_subscribed_app(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_browse(
    adaccount_id: str,
    fields: list[AdAccountTargetingUnifiedField] = [],
    params: AdAccountGetTargetingBrowseParams | dict = {},
):
    """Get Targeting Browse for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountTargetingUnifiedField type.
        params: Query parameters. Available params: See AdAccountGetTargetingBrowseParams type.
    """
    return AdAccount(adaccount_id).get_targeting_browse(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_search(
    adaccount_id: str,
    fields: list[AdAccountTargetingUnifiedField] = [],
    params: AdAccountGetTargetingSearchParams | dict = {},
):
    """Get Targeting Search for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountTargetingUnifiedField type.
        params: Query parameters. Available params: See AdAccountGetTargetingSearchParams type.
    """
    return AdAccount(adaccount_id).get_targeting_search(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_sentence_lines(
    adaccount_id: str,
    fields: list[TargetingSentenceLineField] = [],
    params: AdAccountGetTargetingSentenceLinesParams | dict = {},
):
    """Get Targeting Sentence Lines for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See TargetingSentenceLineField type.
        params: Query parameters. Available params: See AdAccountGetTargetingSentenceLinesParams type.
    """
    return AdAccount(adaccount_id).get_targeting_sentence_lines(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_suggestions(
    adaccount_id: str,
    fields: list[AdAccountTargetingUnifiedField] = [],
    params: AdAccountGetTargetingSuggestionsParams | dict = {},
):
    """Get Targeting Suggestions for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountTargetingUnifiedField type.
        params: Query parameters. Available params: See AdAccountGetTargetingSuggestionsParams type.
    """
    return AdAccount(adaccount_id).get_targeting_suggestions(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_targeting_valid_a_t_i_on(
    adaccount_id: str,
    fields: list[AdAccountTargetingUnifiedField] = [],
    params: AdAccountGetTargetingValidATIOnParams | dict = {},
):
    """Get Targeting Valid A T I On for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdAccountTargetingUnifiedField type.
        params: Query parameters. Available params: See AdAccountGetTargetingValidATIOnParams type.
    """
    return AdAccount(adaccount_id).get_targeting_valid_a_t_i_on(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_tracking(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateTrackingParams | dict = {},
):
    """Create Tracking for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateTrackingParams type.
    """
    return AdAccount(adaccount_id).create_tracking(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def delete_users_of_any_audience(
    adaccount_id: str,
    params: AdAccountDeleteUsersOfAnyAudienceParams | dict = {},
):
    """Delete Users Of Any Audience for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        params: Query parameters. Available params: See AdAccountDeleteUsersOfAnyAudienceParams type.
    """
    return AdAccount(adaccount_id).delete_users_of_any_audience(params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_value_rule_set(
    adaccount_id: str,
    fields: list[AdsValueAdjustmentRuleCollectionField] = [],
    params: AdAccountGetValueRuleSetParams | dict = {},
):
    """Get Value Rule Set for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdsValueAdjustmentRuleCollectionField type.
        params: Query parameters. Available params: See AdAccountGetValueRuleSetParams type.
    """
    return AdAccount(adaccount_id).get_value_rule_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_value_rule_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateValueRuleSetParams | dict = {},
):
    """Create Value Rule Set for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateValueRuleSetParams type.
    """
    return AdAccount(adaccount_id).create_value_rule_set(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def get_video_ads(
    adaccount_id: str,
    fields: list[AdVideoField] = [],
    params: AdAccountGetVideoAdsParams | dict = {},
):
    """Get Video Ads for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve. Available fields: See AdVideoField type.
        params: Query parameters. Available params: See AdAccountGetVideoAdsParams type.
    """
    return AdAccount(adaccount_id).get_video_ads(fields=fields, params=params)


@adaccount_server.tool
@wrapped_fn_tool
def create_video_ad(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateVideoAdParams | dict = {},
):
    """Create Video Ad for this AdAccount.

    Args:
        adaccount_id: The ID of the AdAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdAccountCreateVideoAdParams type.
    """
    return AdAccount(adaccount_id).create_video_ad(fields=fields, params=params)
