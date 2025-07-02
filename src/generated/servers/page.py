"""Page MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.page import Page
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.advideo import AdVideoField
from src.generated.models.application import ApplicationField
from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.businessproject import BusinessProjectField
from src.generated.models.canvas import CanvasField
from src.generated.models.canvasbodyelement import CanvasBodyElementField
from src.generated.models.commerceorder import CommerceOrderField
from src.generated.models.commerceordertransactiondetail import CommerceOrderTransactionDetailField
from src.generated.models.commercepayout import CommercePayoutField
from src.generated.models.ctxpartnerappwelcomemessageflow import (
    CTXPartnerAppWelcomeMessageFlowField,
)
from src.generated.models.customusersettings import CustomUserSettingsField
from src.generated.models.dataset import DatasetField
from src.generated.models.event import EventField
from src.generated.models.imagecopyright import ImageCopyrightField
from src.generated.models.insightsresult import InsightsResultField
from src.generated.models.leadgenform import LeadgenFormField
from src.generated.models.livevideo import LiveVideoField
from src.generated.models.mediafingerprint import MediaFingerprintField
from src.generated.models.messengerbusinesstemplate import MessengerBusinessTemplateField
from src.generated.models.messengerprofile import MessengerProfileField
from src.generated.models.page import (
    PageCreateAbTestParams,
    PageCreateAcknowledgeOrderParams,
    PageCreateAgencyParams,
    PageCreateAssignedUserParams,
    PageCreateBlockedParams,
    PageCreateBusinessDatumParams,
    PageCreateCallParams,
    PageCreateCanvasElementParams,
    PageCreateCanvaseParams,
    PageCreateCopyrightManualClaimParams,
    PageCreateCustomLabelParams,
    PageCreateCustomUserSettingParams,
    PageCreateDatasetParams,
    PageCreateExtendThreadControlParams,
    PageCreateFeedParams,
    PageCreateImageCopyrightParams,
    PageCreateLeadGenFormParams,
    PageCreateLiveVideoParams,
    PageCreateLocationParams,
    PageCreateMediaFingerprintParams,
    PageCreateMessageAttachmentParams,
    PageCreateMessageParams,
    PageCreateMessageTemplateParams,
    PageCreateMessengerCallSettingParams,
    PageCreateMessengerLeadFormParams,
    PageCreateMessengerProfileParams,
    PageCreateModerateConversationParams,
    PageCreateNlpConfigParams,
    PageCreateNotificationMessagesDevSupportParams,
    PageCreatePageWhatsAppNumberVerificationParams,
    PageCreatePassThreadControlParams,
    PageCreatePersonaParams,
    PageCreatePhotoParams,
    PageCreatePhotoStoryParams,
    PageCreatePictureParams,
    PageCreateReleaseThreadControlParams,
    PageCreateRequestThreadControlParams,
    PageCreateSettingParams,
    PageCreateSubscribedAppParams,
    PageCreateTakeThreadControlParams,
    PageCreateUnlinkAccountParams,
    PageCreateVideoCopyrightParams,
    PageCreateVideoCopyrightRuleParams,
    PageCreateVideoParams,
    PageCreateVideoReelParams,
    PageCreateVideoStoryParams,
    PageCreateWelcomeMessageFlowParams,
    PageDeleteAgenciesParams,
    PageDeleteAssignedUsersParams,
    PageDeleteBlockedParams,
    PageDeleteCustomUserSettingsParams,
    PageDeleteLocationsParams,
    PageDeleteMessageTemplatesParams,
    PageDeleteMessengerProfileParams,
    PageDeleteWelcomeMessageFlowsParams,
    PageField,
    PageGetAdsPostsParams,
    PageGetAssignedUsersParams,
    PageGetBlockedParams,
    PageGetBusinessProjectsParams,
    PageGetCanvasesParams,
    PageGetCommerceOrdersParams,
    PageGetCommercePayoutsParams,
    PageGetCommerceTransactionsParams,
    PageGetConversationsParams,
    PageGetCustomUserSettingsParams,
    PageGetEventsParams,
    PageGetFeedParams,
    PageGetInsightsParams,
    PageGetLikesParams,
    PageGetLiveVideosParams,
    PageGetMediaFingerprintsParams,
    PageGetMessageTemplatesParams,
    PageGetMessengerProfileParams,
    PageGetPhotosParams,
    PageGetPictureParams,
    PageGetPostsParams,
    PageGetPublishedPostsParams,
    PageGetRolesParams,
    PageGetSecondaryReceiversParams,
    PageGetStoriesParams,
    PageGetTabsParams,
    PageGetThreadOwnerParams,
    PageGetThreadsParams,
    PageGetVideoCopyrightRulesParams,
    PageGetVideoReelsParams,
    PageGetVideosParams,
    PageGetVisitorPostsParams,
    PageGetWelcomeMessageFlowsParams,
    PageUpdateParams,
)
from src.generated.models.pagepost import PagePostField
from src.generated.models.pagepostexperiment import PagePostExperimentField
from src.generated.models.pagethreadowner import PageThreadOwnerField
from src.generated.models.pageusermessagethreadlabel import PageUserMessageThreadLabelField
from src.generated.models.persona import PersonaField
from src.generated.models.photo import PhotoField
from src.generated.models.profile import ProfileField
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.generated.models.stories import StoriesField
from src.generated.models.tab import TabField
from src.generated.models.unifiedthread import UnifiedThreadField
from src.generated.models.user import UserField
from src.generated.models.videocopyright import VideoCopyrightField
from src.generated.models.videocopyrightmatch import VideoCopyrightMatchField
from src.generated.models.videocopyrightrule import VideoCopyrightRuleField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPage"
instructions = """
Page MCP Server for Facebook Business API.

Provides typed access to all Page operations.
"""

page_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@page_server.tool
@wrapped_fn_tool
def get_page(
    page_id: str,
    fields: list[PageField] = [],
) -> str:
    """Get a Page object by ID.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PageField type.
    """
    obj = Page(page_id)
    return obj.api_get(fields=fields)


@page_server.tool
@wrapped_fn_tool
def update_page(
    page_id: str,
    fields: list[PageField] = [],
    params: PageUpdateParams | dict = {},
) -> str:
    """Update a Page object.

    Args:
        page_id: The ID of the Page.
        fields: Fields to return after update. Available fields: See PageField type.
        params: Parameters to update. Available params: See PageUpdateParams type.
    """
    return Page(page_id).api_update(fields=fields, params=params)


# ---- Edge Methods (88) ----
@page_server.tool
@wrapped_fn_tool
def create_ab_test(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAbTestParams | dict = {},
):
    """Create Ab Test for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateAbTestParams type.
    """
    return Page(page_id).create_ab_test(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_acknowledge_order(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAcknowledgeOrderParams | dict = {},
):
    """Create Acknowledge Order for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateAcknowledgeOrderParams type.
    """
    return Page(page_id).create_acknowledge_order(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_ads_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetAdsPostsParams | dict = {},
):
    """Get Ads Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PagePostField type.
        params: Query parameters. Available params: See PageGetAdsPostsParams type.
    """
    return Page(page_id).get_ads_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_agencies(
    page_id: str,
    params: PageDeleteAgenciesParams | dict = {},
):
    """Delete Agencies for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteAgenciesParams type.
    """
    return Page(page_id).delete_agencies(params=params)


@page_server.tool
@wrapped_fn_tool
def create_agency(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAgencyParams | dict = {},
):
    """Create Agency for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateAgencyParams type.
    """
    return Page(page_id).create_agency(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    page_id: str,
    params: PageDeleteAssignedUsersParams | dict = {},
):
    """Delete Assigned Users for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteAssignedUsersParams type.
    """
    return Page(page_id).delete_assigned_users(params=params)


@page_server.tool
@wrapped_fn_tool
def get_assigned_users(
    page_id: str,
    fields: list[AssignedUserField] = [],
    params: PageGetAssignedUsersParams | dict = {},
):
    """Get Assigned Users for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See AssignedUserField type.
        params: Query parameters. Available params: See PageGetAssignedUsersParams type.
    """
    return Page(page_id).get_assigned_users(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_assigned_user(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAssignedUserParams | dict = {},
):
    """Create Assigned User for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateAssignedUserParams type.
    """
    return Page(page_id).create_assigned_user(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_blocked(
    page_id: str,
    params: PageDeleteBlockedParams | dict = {},
):
    """Delete Blocked for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteBlockedParams type.
    """
    return Page(page_id).delete_blocked(params=params)


@page_server.tool
@wrapped_fn_tool
def get_blocked(
    page_id: str,
    fields: list[ProfileField] = [],
    params: PageGetBlockedParams | dict = {},
):
    """Get Blocked for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See ProfileField type.
        params: Query parameters. Available params: See PageGetBlockedParams type.
    """
    return Page(page_id).get_blocked(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_blocked(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateBlockedParams | dict = {},
):
    """Create Blocked for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateBlockedParams type.
    """
    return Page(page_id).create_blocked(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_business_datum(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateBusinessDatumParams | dict = {},
):
    """Create Business Datum for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateBusinessDatumParams type.
    """
    return Page(page_id).create_business_datum(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_business_projects(
    page_id: str,
    fields: list[BusinessProjectField] = [],
    params: PageGetBusinessProjectsParams | dict = {},
):
    """Get Business Projects for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See BusinessProjectField type.
        params: Query parameters. Available params: See PageGetBusinessProjectsParams type.
    """
    return Page(page_id).get_business_projects(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_call(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCallParams | dict = {},
):
    """Create Call for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateCallParams type.
    """
    return Page(page_id).create_call(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_canvas_element(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCanvasElementParams | dict = {},
):
    """Create Canvas Element for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateCanvasElementParams type.
    """
    return Page(page_id).create_canvas_element(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_canvases(
    page_id: str,
    fields: list[CanvasField] = [],
    params: PageGetCanvasesParams | dict = {},
):
    """Get Canvases for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See CanvasField type.
        params: Query parameters. Available params: See PageGetCanvasesParams type.
    """
    return Page(page_id).get_canvases(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_canvase(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCanvaseParams | dict = {},
):
    """Create Canvase for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateCanvaseParams type.
    """
    return Page(page_id).create_canvase(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_commerce_orders(
    page_id: str,
    fields: list[CommerceOrderField] = [],
    params: PageGetCommerceOrdersParams | dict = {},
):
    """Get Commerce Orders for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See CommerceOrderField type.
        params: Query parameters. Available params: See PageGetCommerceOrdersParams type.
    """
    return Page(page_id).get_commerce_orders(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_commerce_payouts(
    page_id: str,
    fields: list[CommercePayoutField] = [],
    params: PageGetCommercePayoutsParams | dict = {},
):
    """Get Commerce Payouts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See CommercePayoutField type.
        params: Query parameters. Available params: See PageGetCommercePayoutsParams type.
    """
    return Page(page_id).get_commerce_payouts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_commerce_transactions(
    page_id: str,
    fields: list[CommerceOrderTransactionDetailField] = [],
    params: PageGetCommerceTransactionsParams | dict = {},
):
    """Get Commerce Transactions for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See CommerceOrderTransactionDetailField type.
        params: Query parameters. Available params: See PageGetCommerceTransactionsParams type.
    """
    return Page(page_id).get_commerce_transactions(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_conversations(
    page_id: str,
    fields: list[UnifiedThreadField] = [],
    params: PageGetConversationsParams | dict = {},
):
    """Get Conversations for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See UnifiedThreadField type.
        params: Query parameters. Available params: See PageGetConversationsParams type.
    """
    return Page(page_id).get_conversations(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_copyright_manual_claim(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCopyrightManualClaimParams | dict = {},
):
    """Create Copyright Manual Claim for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateCopyrightManualClaimParams type.
    """
    return Page(page_id).create_copyright_manual_claim(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_custom_label(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCustomLabelParams | dict = {},
):
    """Create Custom Label for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateCustomLabelParams type.
    """
    return Page(page_id).create_custom_label(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_custom_user_settings(
    page_id: str,
    params: PageDeleteCustomUserSettingsParams | dict = {},
):
    """Delete Custom User Settings for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteCustomUserSettingsParams type.
    """
    return Page(page_id).delete_custom_user_settings(params=params)


@page_server.tool
@wrapped_fn_tool
def get_custom_user_settings(
    page_id: str,
    fields: list[CustomUserSettingsField] = [],
    params: PageGetCustomUserSettingsParams | dict = {},
):
    """Get Custom User Settings for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See CustomUserSettingsField type.
        params: Query parameters. Available params: See PageGetCustomUserSettingsParams type.
    """
    return Page(page_id).get_custom_user_settings(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_custom_user_setting(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCustomUserSettingParams | dict = {},
):
    """Create Custom User Setting for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateCustomUserSettingParams type.
    """
    return Page(page_id).create_custom_user_setting(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_dataset(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateDatasetParams | dict = {},
):
    """Create Dataset for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateDatasetParams type.
    """
    return Page(page_id).create_dataset(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_events(
    page_id: str,
    fields: list[EventField] = [],
    params: PageGetEventsParams | dict = {},
):
    """Get Events for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See EventField type.
        params: Query parameters. Available params: See PageGetEventsParams type.
    """
    return Page(page_id).get_events(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_extend_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateExtendThreadControlParams | dict = {},
):
    """Create Extend Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateExtendThreadControlParams type.
    """
    return Page(page_id).create_extend_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_feed(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetFeedParams | dict = {},
):
    """Get Feed for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PagePostField type.
        params: Query parameters. Available params: See PageGetFeedParams type.
    """
    return Page(page_id).get_feed(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_feed(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateFeedParams | dict = {},
):
    """Create Feed for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateFeedParams type.
    """
    return Page(page_id).create_feed(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_image_copyright(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateImageCopyrightParams | dict = {},
):
    """Create Image Copyright for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateImageCopyrightParams type.
    """
    return Page(page_id).create_image_copyright(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_insights(
    page_id: str,
    fields: list[InsightsResultField] = [],
    params: PageGetInsightsParams | dict = {},
):
    """Get Insights for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See PageGetInsightsParams type.
    """
    return Page(page_id).get_insights(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_lead_gen_form(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateLeadGenFormParams | dict = {},
):
    """Create Lead Gen Form for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateLeadGenFormParams type.
    """
    return Page(page_id).create_lead_gen_form(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_likes(
    page_id: str,
    fields: list[PageField] = [],
    params: PageGetLikesParams | dict = {},
):
    """Get Likes for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PageField type.
        params: Query parameters. Available params: See PageGetLikesParams type.
    """
    return Page(page_id).get_likes(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_live_videos(
    page_id: str,
    fields: list[LiveVideoField] = [],
    params: PageGetLiveVideosParams | dict = {},
):
    """Get Live Videos for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See LiveVideoField type.
        params: Query parameters. Available params: See PageGetLiveVideosParams type.
    """
    return Page(page_id).get_live_videos(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_live_video(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateLiveVideoParams | dict = {},
):
    """Create Live Video for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateLiveVideoParams type.
    """
    return Page(page_id).create_live_video(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_locations(
    page_id: str,
    params: PageDeleteLocationsParams | dict = {},
):
    """Delete Locations for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteLocationsParams type.
    """
    return Page(page_id).delete_locations(params=params)


@page_server.tool
@wrapped_fn_tool
def create_location(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateLocationParams | dict = {},
):
    """Create Location for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateLocationParams type.
    """
    return Page(page_id).create_location(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_media_fingerprints(
    page_id: str,
    fields: list[MediaFingerprintField] = [],
    params: PageGetMediaFingerprintsParams | dict = {},
):
    """Get Media Fingerprints for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See MediaFingerprintField type.
        params: Query parameters. Available params: See PageGetMediaFingerprintsParams type.
    """
    return Page(page_id).get_media_fingerprints(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_media_fingerprint(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMediaFingerprintParams | dict = {},
):
    """Create Media Fingerprint for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateMediaFingerprintParams type.
    """
    return Page(page_id).create_media_fingerprint(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_message_attachment(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessageAttachmentParams | dict = {},
):
    """Create Message Attachment for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateMessageAttachmentParams type.
    """
    return Page(page_id).create_message_attachment(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_message_templates(
    page_id: str,
    params: PageDeleteMessageTemplatesParams | dict = {},
):
    """Delete Message Templates for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteMessageTemplatesParams type.
    """
    return Page(page_id).delete_message_templates(params=params)


@page_server.tool
@wrapped_fn_tool
def get_message_templates(
    page_id: str,
    fields: list[MessengerBusinessTemplateField] = [],
    params: PageGetMessageTemplatesParams | dict = {},
):
    """Get Message Templates for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See MessengerBusinessTemplateField type.
        params: Query parameters. Available params: See PageGetMessageTemplatesParams type.
    """
    return Page(page_id).get_message_templates(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_message_template(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessageTemplateParams | dict = {},
):
    """Create Message Template for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateMessageTemplateParams type.
    """
    return Page(page_id).create_message_template(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_message(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessageParams | dict = {},
):
    """Create Message for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateMessageParams type.
    """
    return Page(page_id).create_message(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_messenger_call_setting(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessengerCallSettingParams | dict = {},
):
    """Create Messenger Call Setting for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateMessengerCallSettingParams type.
    """
    return Page(page_id).create_messenger_call_setting(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_messenger_lead_form(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessengerLeadFormParams | dict = {},
):
    """Create Messenger Lead Form for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateMessengerLeadFormParams type.
    """
    return Page(page_id).create_messenger_lead_form(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_messenger_profile(
    page_id: str,
    params: PageDeleteMessengerProfileParams | dict = {},
):
    """Delete Messenger Profile for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteMessengerProfileParams type.
    """
    return Page(page_id).delete_messenger_profile(params=params)


@page_server.tool
@wrapped_fn_tool
def get_messenger_profile(
    page_id: str,
    fields: list[MessengerProfileField] = [],
    params: PageGetMessengerProfileParams | dict = {},
):
    """Get Messenger Profile for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See MessengerProfileField type.
        params: Query parameters. Available params: See PageGetMessengerProfileParams type.
    """
    return Page(page_id).get_messenger_profile(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_messenger_profile(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessengerProfileParams | dict = {},
):
    """Create Messenger Profile for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateMessengerProfileParams type.
    """
    return Page(page_id).create_messenger_profile(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_moderate_conversation(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateModerateConversationParams | dict = {},
):
    """Create Moderate Conversation for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateModerateConversationParams type.
    """
    return Page(page_id).create_moderate_conversation(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_nlp_config(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateNlpConfigParams | dict = {},
):
    """Create Nlp Config for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateNlpConfigParams type.
    """
    return Page(page_id).create_nlp_config(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_notification_messages_dev_support(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateNotificationMessagesDevSupportParams | dict = {},
):
    """Create Notification Messages Dev Support for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateNotificationMessagesDevSupportParams type.
    """
    return Page(page_id).create_notification_messages_dev_support(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_page_whats_app_number_verification(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePageWhatsAppNumberVerificationParams | dict = {},
):
    """Create Page Whats App Number Verification for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreatePageWhatsAppNumberVerificationParams type.
    """
    return Page(page_id).create_page_whats_app_number_verification(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_pass_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePassThreadControlParams | dict = {},
):
    """Create Pass Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreatePassThreadControlParams type.
    """
    return Page(page_id).create_pass_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_persona(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePersonaParams | dict = {},
):
    """Create Persona for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreatePersonaParams type.
    """
    return Page(page_id).create_persona(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_photo_story(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePhotoStoryParams | dict = {},
):
    """Create Photo Story for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreatePhotoStoryParams type.
    """
    return Page(page_id).create_photo_story(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_photos(
    page_id: str,
    fields: list[PhotoField] = [],
    params: PageGetPhotosParams | dict = {},
):
    """Get Photos for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PhotoField type.
        params: Query parameters. Available params: See PageGetPhotosParams type.
    """
    return Page(page_id).get_photos(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_photo(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePhotoParams | dict = {},
):
    """Create Photo for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreatePhotoParams type.
    """
    return Page(page_id).create_photo(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_picture(
    page_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: PageGetPictureParams | dict = {},
):
    """Get Picture for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See ProfilePictureSourceField type.
        params: Query parameters. Available params: See PageGetPictureParams type.
    """
    return Page(page_id).get_picture(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_picture(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePictureParams | dict = {},
):
    """Create Picture for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreatePictureParams type.
    """
    return Page(page_id).create_picture(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetPostsParams | dict = {},
):
    """Get Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PagePostField type.
        params: Query parameters. Available params: See PageGetPostsParams type.
    """
    return Page(page_id).get_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_published_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetPublishedPostsParams | dict = {},
):
    """Get Published Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PagePostField type.
        params: Query parameters. Available params: See PageGetPublishedPostsParams type.
    """
    return Page(page_id).get_published_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_release_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateReleaseThreadControlParams | dict = {},
):
    """Create Release Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateReleaseThreadControlParams type.
    """
    return Page(page_id).create_release_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_request_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateRequestThreadControlParams | dict = {},
):
    """Create Request Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateRequestThreadControlParams type.
    """
    return Page(page_id).create_request_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_roles(
    page_id: str,
    fields: list[UserField] = [],
    params: PageGetRolesParams | dict = {},
):
    """Get Roles for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See UserField type.
        params: Query parameters. Available params: See PageGetRolesParams type.
    """
    return Page(page_id).get_roles(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_secondary_receivers(
    page_id: str,
    fields: list[ApplicationField] = [],
    params: PageGetSecondaryReceiversParams | dict = {},
):
    """Get Secondary Receivers for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See ApplicationField type.
        params: Query parameters. Available params: See PageGetSecondaryReceiversParams type.
    """
    return Page(page_id).get_secondary_receivers(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_setting(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateSettingParams | dict = {},
):
    """Create Setting for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateSettingParams type.
    """
    return Page(page_id).create_setting(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_stories(
    page_id: str,
    fields: list[StoriesField] = [],
    params: PageGetStoriesParams | dict = {},
):
    """Get Stories for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See StoriesField type.
        params: Query parameters. Available params: See PageGetStoriesParams type.
    """
    return Page(page_id).get_stories(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateSubscribedAppParams | dict = {},
):
    """Create Subscribed App for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateSubscribedAppParams type.
    """
    return Page(page_id).create_subscribed_app(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_tabs(
    page_id: str,
    fields: list[TabField] = [],
    params: PageGetTabsParams | dict = {},
):
    """Get Tabs for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See TabField type.
        params: Query parameters. Available params: See PageGetTabsParams type.
    """
    return Page(page_id).get_tabs(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_take_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateTakeThreadControlParams | dict = {},
):
    """Create Take Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateTakeThreadControlParams type.
    """
    return Page(page_id).create_take_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_thread_owner(
    page_id: str,
    fields: list[PageThreadOwnerField] = [],
    params: PageGetThreadOwnerParams | dict = {},
):
    """Get Thread Owner for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PageThreadOwnerField type.
        params: Query parameters. Available params: See PageGetThreadOwnerParams type.
    """
    return Page(page_id).get_thread_owner(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_threads(
    page_id: str,
    fields: list[UnifiedThreadField] = [],
    params: PageGetThreadsParams | dict = {},
):
    """Get Threads for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See UnifiedThreadField type.
        params: Query parameters. Available params: See PageGetThreadsParams type.
    """
    return Page(page_id).get_threads(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_unlink_account(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateUnlinkAccountParams | dict = {},
):
    """Create Unlink Account for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateUnlinkAccountParams type.
    """
    return Page(page_id).create_unlink_account(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_video_copyright_rules(
    page_id: str,
    fields: list[VideoCopyrightRuleField] = [],
    params: PageGetVideoCopyrightRulesParams | dict = {},
):
    """Get Video Copyright Rules for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See VideoCopyrightRuleField type.
        params: Query parameters. Available params: See PageGetVideoCopyrightRulesParams type.
    """
    return Page(page_id).get_video_copyright_rules(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_copyright_rule(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoCopyrightRuleParams | dict = {},
):
    """Create Video Copyright Rule for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateVideoCopyrightRuleParams type.
    """
    return Page(page_id).create_video_copyright_rule(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_copyright(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoCopyrightParams | dict = {},
):
    """Create Video Copyright for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateVideoCopyrightParams type.
    """
    return Page(page_id).create_video_copyright(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_video_reels(
    page_id: str,
    fields: list[AdVideoField] = [],
    params: PageGetVideoReelsParams | dict = {},
):
    """Get Video Reels for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See AdVideoField type.
        params: Query parameters. Available params: See PageGetVideoReelsParams type.
    """
    return Page(page_id).get_video_reels(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_reel(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoReelParams | dict = {},
):
    """Create Video Reel for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateVideoReelParams type.
    """
    return Page(page_id).create_video_reel(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_story(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoStoryParams | dict = {},
):
    """Create Video Story for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateVideoStoryParams type.
    """
    return Page(page_id).create_video_story(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_videos(
    page_id: str,
    fields: list[AdVideoField] = [],
    params: PageGetVideosParams | dict = {},
):
    """Get Videos for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See AdVideoField type.
        params: Query parameters. Available params: See PageGetVideosParams type.
    """
    return Page(page_id).get_videos(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoParams | dict = {},
):
    """Create Video for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateVideoParams type.
    """
    return Page(page_id).create_video(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_visitor_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetVisitorPostsParams | dict = {},
):
    """Get Visitor Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See PagePostField type.
        params: Query parameters. Available params: See PageGetVisitorPostsParams type.
    """
    return Page(page_id).get_visitor_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_welcome_message_flows(
    page_id: str,
    params: PageDeleteWelcomeMessageFlowsParams | dict = {},
):
    """Delete Welcome Message Flows for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters. Available params: See PageDeleteWelcomeMessageFlowsParams type.
    """
    return Page(page_id).delete_welcome_message_flows(params=params)


@page_server.tool
@wrapped_fn_tool
def get_welcome_message_flows(
    page_id: str,
    fields: list[CTXPartnerAppWelcomeMessageFlowField] = [],
    params: PageGetWelcomeMessageFlowsParams | dict = {},
):
    """Get Welcome Message Flows for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve. Available fields: See CTXPartnerAppWelcomeMessageFlowField type.
        params: Query parameters. Available params: See PageGetWelcomeMessageFlowsParams type.
    """
    return Page(page_id).get_welcome_message_flows(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_welcome_message_flow(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateWelcomeMessageFlowParams | dict = {},
):
    """Create Welcome Message Flow for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageCreateWelcomeMessageFlowParams type.
    """
    return Page(page_id).create_welcome_message_flow(fields=fields, params=params)
