"""Page MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.page import Page
from fastmcp import FastMCP

from src.generated.models.advideo import AdVideoField
from src.generated.models.application import ApplicationField
from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.businessproject import BusinessProjectField
from src.generated.models.canvas import CanvasField
from src.generated.models.commerceorder import CommerceOrderField
from src.generated.models.commerceordertransactiondetail import CommerceOrderTransactionDetailField
from src.generated.models.commercepayout import CommercePayoutField
from src.generated.models.ctxpartnerappwelcomemessageflow import (
    CTXPartnerAppWelcomeMessageFlowField,
)
from src.generated.models.customusersettings import CustomUserSettingsField
from src.generated.models.event import EventField
from src.generated.models.insightsresult import InsightsResultField
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
from src.generated.models.pagethreadowner import PageThreadOwnerField
from src.generated.models.photo import PhotoField
from src.generated.models.profile import ProfileField
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.generated.models.stories import StoriesField
from src.generated.models.tab import TabField
from src.generated.models.unifiedthread import UnifiedThreadField
from src.generated.models.user import UserField
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
@wrapped_fn_tool
def get_page(
    page_id: str,
    fields: list[PageField] = [],
) -> str:
    """Get a Page object by ID.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
    """
    obj = Page(page_id)
    return obj.api_get(fields=fields)


page_server.tool(get_page)


@wrapped_fn_tool
def update_page(
    page_id: str,
    fields: list[PageField] = [],
    params: PageUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a Page object.

    Args:
        page_id: The ID of the Page.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return Page(page_id).api_update(fields=fields, params=params)


page_server.tool(update_page)


# ---- Edge Methods (88) ----
@wrapped_fn_tool
def create_ab_test(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAbTestParams = {},
) -> Any:
    """Create Ab Test for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_ab_test(fields=fields, params=params)


page_server.tool(create_ab_test)


@wrapped_fn_tool
def create_acknowledge_order(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAcknowledgeOrderParams = {},
) -> Any:
    """Create Acknowledge Order for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_acknowledge_order(fields=fields, params=params)


page_server.tool(create_acknowledge_order)


@wrapped_fn_tool
def get_ads_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetAdsPostsParams = {},
) -> Any:
    """Get Ads Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_ads_posts(fields=fields, params=params)


page_server.tool(get_ads_posts)


@wrapped_fn_tool
def delete_agencies(
    page_id: str,
    params: PageDeleteAgenciesParams = {},
) -> Any:
    """Delete Agencies for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_agencies(params=params)


page_server.tool(delete_agencies)


@wrapped_fn_tool
def create_agency(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAgencyParams = {},
) -> Any:
    """Create Agency for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_agency(fields=fields, params=params)


page_server.tool(create_agency)


@wrapped_fn_tool
def delete_assigned_users(
    page_id: str,
    params: PageDeleteAssignedUsersParams = {},
) -> Any:
    """Delete Assigned Users for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_assigned_users(params=params)


page_server.tool(delete_assigned_users)


@wrapped_fn_tool
def get_assigned_users(
    page_id: str,
    fields: list[AssignedUserField] = [],
    params: PageGetAssignedUsersParams = {},
) -> Any:
    """Get Assigned Users for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_assigned_users(fields=fields, params=params)


page_server.tool(get_assigned_users)


@wrapped_fn_tool
def create_assigned_user(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateAssignedUserParams = {},
) -> Any:
    """Create Assigned User for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_assigned_user(fields=fields, params=params)


page_server.tool(create_assigned_user)


@wrapped_fn_tool
def delete_blocked(
    page_id: str,
    params: PageDeleteBlockedParams = {},
) -> Any:
    """Delete Blocked for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_blocked(params=params)


page_server.tool(delete_blocked)


@wrapped_fn_tool
def get_blocked(
    page_id: str,
    fields: list[ProfileField] = [],
    params: PageGetBlockedParams = {},
) -> Any:
    """Get Blocked for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_blocked(fields=fields, params=params)


page_server.tool(get_blocked)


@wrapped_fn_tool
def create_blocked(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateBlockedParams = {},
) -> Any:
    """Create Blocked for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_blocked(fields=fields, params=params)


page_server.tool(create_blocked)


@wrapped_fn_tool
def create_business_datum(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateBusinessDatumParams = {},
) -> Any:
    """Create Business Datum for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_business_datum(fields=fields, params=params)


page_server.tool(create_business_datum)


@wrapped_fn_tool
def get_business_projects(
    page_id: str,
    fields: list[BusinessProjectField] = [],
    params: PageGetBusinessProjectsParams = {},
) -> Any:
    """Get Business Projects for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_business_projects(fields=fields, params=params)


page_server.tool(get_business_projects)


@wrapped_fn_tool
def create_call(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCallParams = {},
) -> Any:
    """Create Call for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_call(fields=fields, params=params)


page_server.tool(create_call)


@wrapped_fn_tool
def create_canvas_element(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCanvasElementParams = {},
) -> Any:
    """Create Canvas Element for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_canvas_element(fields=fields, params=params)


page_server.tool(create_canvas_element)


@wrapped_fn_tool
def get_canvases(
    page_id: str,
    fields: list[CanvasField] = [],
    params: PageGetCanvasesParams = {},
) -> Any:
    """Get Canvases for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_canvases(fields=fields, params=params)


page_server.tool(get_canvases)


@wrapped_fn_tool
def create_canvase(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCanvaseParams = {},
) -> Any:
    """Create Canvase for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_canvase(fields=fields, params=params)


page_server.tool(create_canvase)


@wrapped_fn_tool
def get_commerce_orders(
    page_id: str,
    fields: list[CommerceOrderField] = [],
    params: PageGetCommerceOrdersParams = {},
) -> Any:
    """Get Commerce Orders for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_commerce_orders(fields=fields, params=params)


page_server.tool(get_commerce_orders)


@wrapped_fn_tool
def get_commerce_payouts(
    page_id: str,
    fields: list[CommercePayoutField] = [],
    params: PageGetCommercePayoutsParams = {},
) -> Any:
    """Get Commerce Payouts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_commerce_payouts(fields=fields, params=params)


page_server.tool(get_commerce_payouts)


@wrapped_fn_tool
def get_commerce_transactions(
    page_id: str,
    fields: list[CommerceOrderTransactionDetailField] = [],
    params: PageGetCommerceTransactionsParams = {},
) -> Any:
    """Get Commerce Transactions for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_commerce_transactions(fields=fields, params=params)


page_server.tool(get_commerce_transactions)


@wrapped_fn_tool
def get_conversations(
    page_id: str,
    fields: list[UnifiedThreadField] = [],
    params: PageGetConversationsParams = {},
) -> Any:
    """Get Conversations for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_conversations(fields=fields, params=params)


page_server.tool(get_conversations)


@wrapped_fn_tool
def create_copyright_manual_claim(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCopyrightManualClaimParams = {},
) -> Any:
    """Create Copyright Manual Claim for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_copyright_manual_claim(fields=fields, params=params)


page_server.tool(create_copyright_manual_claim)


@wrapped_fn_tool
def create_custom_label(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCustomLabelParams = {},
) -> Any:
    """Create Custom Label for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_custom_label(fields=fields, params=params)


page_server.tool(create_custom_label)


@wrapped_fn_tool
def delete_custom_user_settings(
    page_id: str,
    params: PageDeleteCustomUserSettingsParams = {},
) -> Any:
    """Delete Custom User Settings for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_custom_user_settings(params=params)


page_server.tool(delete_custom_user_settings)


@wrapped_fn_tool
def get_custom_user_settings(
    page_id: str,
    fields: list[CustomUserSettingsField] = [],
    params: PageGetCustomUserSettingsParams = {},
) -> Any:
    """Get Custom User Settings for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_custom_user_settings(fields=fields, params=params)


page_server.tool(get_custom_user_settings)


@wrapped_fn_tool
def create_custom_user_setting(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateCustomUserSettingParams = {},
) -> Any:
    """Create Custom User Setting for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_custom_user_setting(fields=fields, params=params)


page_server.tool(create_custom_user_setting)


@wrapped_fn_tool
def create_dataset(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateDatasetParams = {},
) -> Any:
    """Create Dataset for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_dataset(fields=fields, params=params)


page_server.tool(create_dataset)


@wrapped_fn_tool
def get_events(
    page_id: str,
    fields: list[EventField] = [],
    params: PageGetEventsParams = {},
) -> Any:
    """Get Events for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_events(fields=fields, params=params)


page_server.tool(get_events)


@wrapped_fn_tool
def create_extend_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateExtendThreadControlParams = {},
) -> Any:
    """Create Extend Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_extend_thread_control(fields=fields, params=params)


page_server.tool(create_extend_thread_control)


@wrapped_fn_tool
def get_feed(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetFeedParams = {},
) -> Any:
    """Get Feed for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_feed(fields=fields, params=params)


page_server.tool(get_feed)


@wrapped_fn_tool
def create_feed(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateFeedParams = {},
) -> Any:
    """Create Feed for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_feed(fields=fields, params=params)


page_server.tool(create_feed)


@wrapped_fn_tool
def create_image_copyright(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateImageCopyrightParams = {},
) -> Any:
    """Create Image Copyright for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_image_copyright(fields=fields, params=params)


page_server.tool(create_image_copyright)


@wrapped_fn_tool
def get_insights(
    page_id: str,
    fields: list[InsightsResultField] = [],
    params: PageGetInsightsParams = {},
) -> Any:
    """Get Insights for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_insights(fields=fields, params=params)


page_server.tool(get_insights)


@wrapped_fn_tool
def create_lead_gen_form(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateLeadGenFormParams = {},
) -> Any:
    """Create Lead Gen Form for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_lead_gen_form(fields=fields, params=params)


page_server.tool(create_lead_gen_form)


@wrapped_fn_tool
def get_likes(
    page_id: str,
    fields: list[PageField] = [],
    params: PageGetLikesParams = {},
) -> Any:
    """Get Likes for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_likes(fields=fields, params=params)


page_server.tool(get_likes)


@wrapped_fn_tool
def get_live_videos(
    page_id: str,
    fields: list[LiveVideoField] = [],
    params: PageGetLiveVideosParams = {},
) -> Any:
    """Get Live Videos for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_live_videos(fields=fields, params=params)


page_server.tool(get_live_videos)


@wrapped_fn_tool
def create_live_video(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateLiveVideoParams = {},
) -> Any:
    """Create Live Video for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_live_video(fields=fields, params=params)


page_server.tool(create_live_video)


@wrapped_fn_tool
def delete_locations(
    page_id: str,
    params: PageDeleteLocationsParams = {},
) -> Any:
    """Delete Locations for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_locations(params=params)


page_server.tool(delete_locations)


@wrapped_fn_tool
def create_location(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateLocationParams = {},
) -> Any:
    """Create Location for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_location(fields=fields, params=params)


page_server.tool(create_location)


@wrapped_fn_tool
def get_media_fingerprints(
    page_id: str,
    fields: list[MediaFingerprintField] = [],
    params: PageGetMediaFingerprintsParams = {},
) -> Any:
    """Get Media Fingerprints for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_media_fingerprints(fields=fields, params=params)


page_server.tool(get_media_fingerprints)


@wrapped_fn_tool
def create_media_fingerprint(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMediaFingerprintParams = {},
) -> Any:
    """Create Media Fingerprint for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_media_fingerprint(fields=fields, params=params)


page_server.tool(create_media_fingerprint)


@wrapped_fn_tool
def create_message_attachment(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessageAttachmentParams = {},
) -> Any:
    """Create Message Attachment for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_message_attachment(fields=fields, params=params)


page_server.tool(create_message_attachment)


@wrapped_fn_tool
def delete_message_templates(
    page_id: str,
    params: PageDeleteMessageTemplatesParams = {},
) -> Any:
    """Delete Message Templates for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_message_templates(params=params)


page_server.tool(delete_message_templates)


@wrapped_fn_tool
def get_message_templates(
    page_id: str,
    fields: list[MessengerBusinessTemplateField] = [],
    params: PageGetMessageTemplatesParams = {},
) -> Any:
    """Get Message Templates for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_message_templates(fields=fields, params=params)


page_server.tool(get_message_templates)


@wrapped_fn_tool
def create_message_template(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessageTemplateParams = {},
) -> Any:
    """Create Message Template for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_message_template(fields=fields, params=params)


page_server.tool(create_message_template)


@wrapped_fn_tool
def create_message(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessageParams = {},
) -> Any:
    """Create Message for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_message(fields=fields, params=params)


page_server.tool(create_message)


@wrapped_fn_tool
def create_messenger_call_setting(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessengerCallSettingParams = {},
) -> Any:
    """Create Messenger Call Setting for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_messenger_call_setting(fields=fields, params=params)


page_server.tool(create_messenger_call_setting)


@wrapped_fn_tool
def create_messenger_lead_form(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessengerLeadFormParams = {},
) -> Any:
    """Create Messenger Lead Form for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_messenger_lead_form(fields=fields, params=params)


page_server.tool(create_messenger_lead_form)


@wrapped_fn_tool
def delete_messenger_profile(
    page_id: str,
    params: PageDeleteMessengerProfileParams = {},
) -> Any:
    """Delete Messenger Profile for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_messenger_profile(params=params)


page_server.tool(delete_messenger_profile)


@wrapped_fn_tool
def get_messenger_profile(
    page_id: str,
    fields: list[MessengerProfileField] = [],
    params: PageGetMessengerProfileParams = {},
) -> Any:
    """Get Messenger Profile for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_messenger_profile(fields=fields, params=params)


page_server.tool(get_messenger_profile)


@wrapped_fn_tool
def create_messenger_profile(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateMessengerProfileParams = {},
) -> Any:
    """Create Messenger Profile for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_messenger_profile(fields=fields, params=params)


page_server.tool(create_messenger_profile)


@wrapped_fn_tool
def create_moderate_conversation(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateModerateConversationParams = {},
) -> Any:
    """Create Moderate Conversation for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_moderate_conversation(fields=fields, params=params)


page_server.tool(create_moderate_conversation)


@wrapped_fn_tool
def create_nlp_config(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateNlpConfigParams = {},
) -> Any:
    """Create Nlp Config for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_nlp_config(fields=fields, params=params)


page_server.tool(create_nlp_config)


@wrapped_fn_tool
def create_notification_messages_dev_support(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateNotificationMessagesDevSupportParams = {},
) -> Any:
    """Create Notification Messages Dev Support for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_notification_messages_dev_support(fields=fields, params=params)


page_server.tool(create_notification_messages_dev_support)


@wrapped_fn_tool
def create_page_whats_app_number_verification(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePageWhatsAppNumberVerificationParams = {},
) -> Any:
    """Create Page Whats App Number Verification for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_page_whats_app_number_verification(fields=fields, params=params)


page_server.tool(create_page_whats_app_number_verification)


@wrapped_fn_tool
def create_pass_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePassThreadControlParams = {},
) -> Any:
    """Create Pass Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_pass_thread_control(fields=fields, params=params)


page_server.tool(create_pass_thread_control)


@wrapped_fn_tool
def create_persona(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePersonaParams = {},
) -> Any:
    """Create Persona for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_persona(fields=fields, params=params)


page_server.tool(create_persona)


@wrapped_fn_tool
def create_photo_story(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePhotoStoryParams = {},
) -> Any:
    """Create Photo Story for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_photo_story(fields=fields, params=params)


page_server.tool(create_photo_story)


@wrapped_fn_tool
def get_photos(
    page_id: str,
    fields: list[PhotoField] = [],
    params: PageGetPhotosParams = {},
) -> Any:
    """Get Photos for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_photos(fields=fields, params=params)


page_server.tool(get_photos)


@wrapped_fn_tool
def create_photo(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePhotoParams = {},
) -> Any:
    """Create Photo for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_photo(fields=fields, params=params)


page_server.tool(create_photo)


@wrapped_fn_tool
def get_picture(
    page_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: PageGetPictureParams = {},
) -> Any:
    """Get Picture for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_picture(fields=fields, params=params)


page_server.tool(get_picture)


@wrapped_fn_tool
def create_picture(
    page_id: str,
    fields: list[str] = [],
    params: PageCreatePictureParams = {},
) -> Any:
    """Create Picture for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_picture(fields=fields, params=params)


page_server.tool(create_picture)


@wrapped_fn_tool
def get_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetPostsParams = {},
) -> Any:
    """Get Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_posts(fields=fields, params=params)


page_server.tool(get_posts)


@wrapped_fn_tool
def get_published_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetPublishedPostsParams = {},
) -> Any:
    """Get Published Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_published_posts(fields=fields, params=params)


page_server.tool(get_published_posts)


@wrapped_fn_tool
def create_release_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateReleaseThreadControlParams = {},
) -> Any:
    """Create Release Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_release_thread_control(fields=fields, params=params)


page_server.tool(create_release_thread_control)


@wrapped_fn_tool
def create_request_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateRequestThreadControlParams = {},
) -> Any:
    """Create Request Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_request_thread_control(fields=fields, params=params)


page_server.tool(create_request_thread_control)


@wrapped_fn_tool
def get_roles(
    page_id: str,
    fields: list[UserField] = [],
    params: PageGetRolesParams = {},
) -> Any:
    """Get Roles for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_roles(fields=fields, params=params)


page_server.tool(get_roles)


@wrapped_fn_tool
def get_secondary_receivers(
    page_id: str,
    fields: list[ApplicationField] = [],
    params: PageGetSecondaryReceiversParams = {},
) -> Any:
    """Get Secondary Receivers for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_secondary_receivers(fields=fields, params=params)


page_server.tool(get_secondary_receivers)


@wrapped_fn_tool
def create_setting(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateSettingParams = {},
) -> Any:
    """Create Setting for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_setting(fields=fields, params=params)


page_server.tool(create_setting)


@wrapped_fn_tool
def get_stories(
    page_id: str,
    fields: list[StoriesField] = [],
    params: PageGetStoriesParams = {},
) -> Any:
    """Get Stories for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_stories(fields=fields, params=params)


page_server.tool(get_stories)


@wrapped_fn_tool
def create_subscribed_app(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateSubscribedAppParams = {},
) -> Any:
    """Create Subscribed App for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_subscribed_app(fields=fields, params=params)


page_server.tool(create_subscribed_app)


@wrapped_fn_tool
def get_tabs(
    page_id: str,
    fields: list[TabField] = [],
    params: PageGetTabsParams = {},
) -> Any:
    """Get Tabs for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_tabs(fields=fields, params=params)


page_server.tool(get_tabs)


@wrapped_fn_tool
def create_take_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateTakeThreadControlParams = {},
) -> Any:
    """Create Take Thread Control for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_take_thread_control(fields=fields, params=params)


page_server.tool(create_take_thread_control)


@wrapped_fn_tool
def get_thread_owner(
    page_id: str,
    fields: list[PageThreadOwnerField] = [],
    params: PageGetThreadOwnerParams = {},
) -> Any:
    """Get Thread Owner for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_thread_owner(fields=fields, params=params)


page_server.tool(get_thread_owner)


@wrapped_fn_tool
def get_threads(
    page_id: str,
    fields: list[UnifiedThreadField] = [],
    params: PageGetThreadsParams = {},
) -> Any:
    """Get Threads for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_threads(fields=fields, params=params)


page_server.tool(get_threads)


@wrapped_fn_tool
def create_unlink_account(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateUnlinkAccountParams = {},
) -> Any:
    """Create Unlink Account for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_unlink_account(fields=fields, params=params)


page_server.tool(create_unlink_account)


@wrapped_fn_tool
def get_video_copyright_rules(
    page_id: str,
    fields: list[VideoCopyrightRuleField] = [],
    params: PageGetVideoCopyrightRulesParams = {},
) -> Any:
    """Get Video Copyright Rules for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_video_copyright_rules(fields=fields, params=params)


page_server.tool(get_video_copyright_rules)


@wrapped_fn_tool
def create_video_copyright_rule(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoCopyrightRuleParams = {},
) -> Any:
    """Create Video Copyright Rule for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_video_copyright_rule(fields=fields, params=params)


page_server.tool(create_video_copyright_rule)


@wrapped_fn_tool
def create_video_copyright(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoCopyrightParams = {},
) -> Any:
    """Create Video Copyright for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_video_copyright(fields=fields, params=params)


page_server.tool(create_video_copyright)


@wrapped_fn_tool
def get_video_reels(
    page_id: str,
    fields: list[AdVideoField] = [],
    params: PageGetVideoReelsParams = {},
) -> Any:
    """Get Video Reels for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_video_reels(fields=fields, params=params)


page_server.tool(get_video_reels)


@wrapped_fn_tool
def create_video_reel(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoReelParams = {},
) -> Any:
    """Create Video Reel for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_video_reel(fields=fields, params=params)


page_server.tool(create_video_reel)


@wrapped_fn_tool
def create_video_story(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoStoryParams = {},
) -> Any:
    """Create Video Story for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_video_story(fields=fields, params=params)


page_server.tool(create_video_story)


@wrapped_fn_tool
def get_videos(
    page_id: str,
    fields: list[AdVideoField] = [],
    params: PageGetVideosParams = {},
) -> Any:
    """Get Videos for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_videos(fields=fields, params=params)


page_server.tool(get_videos)


@wrapped_fn_tool
def create_video(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateVideoParams = {},
) -> Any:
    """Create Video for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_video(fields=fields, params=params)


page_server.tool(create_video)


@wrapped_fn_tool
def get_visitor_posts(
    page_id: str,
    fields: list[PagePostField] = [],
    params: PageGetVisitorPostsParams = {},
) -> Any:
    """Get Visitor Posts for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_visitor_posts(fields=fields, params=params)


page_server.tool(get_visitor_posts)


@wrapped_fn_tool
def delete_welcome_message_flows(
    page_id: str,
    params: PageDeleteWelcomeMessageFlowsParams = {},
) -> Any:
    """Delete Welcome Message Flows for this Page.

    Args:
        page_id: The ID of the Page.
        params: Query parameters.
    """
    return Page(page_id).delete_welcome_message_flows(params=params)


page_server.tool(delete_welcome_message_flows)


@wrapped_fn_tool
def get_welcome_message_flows(
    page_id: str,
    fields: list[CTXPartnerAppWelcomeMessageFlowField] = [],
    params: PageGetWelcomeMessageFlowsParams = {},
) -> Any:
    """Get Welcome Message Flows for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).get_welcome_message_flows(fields=fields, params=params)


page_server.tool(get_welcome_message_flows)


@wrapped_fn_tool
def create_welcome_message_flow(
    page_id: str,
    fields: list[str] = [],
    params: PageCreateWelcomeMessageFlowParams = {},
) -> Any:
    """Create Welcome Message Flow for this Page.

    Args:
        page_id: The ID of the Page.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Page(page_id).create_welcome_message_flow(fields=fields, params=params)


page_server.tool(create_welcome_message_flow)
