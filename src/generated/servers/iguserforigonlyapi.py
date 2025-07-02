"""IGUserForIGOnlyAPI MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.iguserforigonlyapi import IGUserForIGOnlyAPI
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.contentpublishinglimitresponse import ContentPublishingLimitResponseField
from src.generated.models.ctxpartnerappwelcomemessageflow import (
    CTXPartnerAppWelcomeMessageFlowField,
)
from src.generated.models.iguserforigonlyapi import (
    IGUserForIGOnlyAPICreateMediaParams,
    IGUserForIGOnlyAPICreateMediaPublishParams,
    IGUserForIGOnlyAPICreateMentionParams,
    IGUserForIGOnlyAPICreateMessageAttachmentParams,
    IGUserForIGOnlyAPICreateMessageParams,
    IGUserForIGOnlyAPICreateMessengerProfileParams,
    IGUserForIGOnlyAPICreateSubscribedAppParams,
    IGUserForIGOnlyAPICreateWelcomeMessageFlowParams,
    IGUserForIGOnlyAPIDeleteMessengerProfileParams,
    IGUserForIGOnlyAPIDeleteWelcomeMessageFlowsParams,
    IGUserForIGOnlyAPIField,
    IGUserForIGOnlyAPIGetBusinessMessagingFeatureStatusParams,
    IGUserForIGOnlyAPIGetContentPublishingLimitParams,
    IGUserForIGOnlyAPIGetConversationsParams,
    IGUserForIGOnlyAPIGetInsightsParams,
    IGUserForIGOnlyAPIGetMediaParams,
    IGUserForIGOnlyAPIGetWelcomeMessageFlowsParams,
)
from src.generated.models.insightsresult import InsightsResultField
from src.generated.models.unifiedthread import UnifiedThreadField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUserForIGOnlyAPI"
instructions = """
IGUserForIGOnlyAPI MCP Server for Facebook Business API.

Provides typed access to all IGUserForIGOnlyAPI operations.
"""

iguserforigonlyapi_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_iguserforigonlyapi(
    iguserforigonlyapi_id: str,
    fields: list[IGUserForIGOnlyAPIField] = [],
) -> str:
    """Get a IGUserForIGOnlyAPI object by ID.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See IGUserForIGOnlyAPIField type.
    """
    obj = IGUserForIGOnlyAPI(iguserforigonlyapi_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (16) ----
@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_business_messaging_feature_status(
    iguserforigonlyapi_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: IGUserForIGOnlyAPIGetBusinessMessagingFeatureStatusParams | dict = {},
):
    """Get Business Messaging Feature Status for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIGetBusinessMessagingFeatureStatusParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_business_messaging_feature_status(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_content_publishing_limit(
    iguserforigonlyapi_id: str,
    fields: list[ContentPublishingLimitResponseField] = [],
    params: IGUserForIGOnlyAPIGetContentPublishingLimitParams | dict = {},
):
    """Get Content Publishing Limit for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See ContentPublishingLimitResponseField type.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIGetContentPublishingLimitParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_content_publishing_limit(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_conversations(
    iguserforigonlyapi_id: str,
    fields: list[UnifiedThreadField] = [],
    params: IGUserForIGOnlyAPIGetConversationsParams | dict = {},
):
    """Get Conversations for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See UnifiedThreadField type.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIGetConversationsParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_conversations(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_insights(
    iguserforigonlyapi_id: str,
    fields: list[InsightsResultField] = [],
    params: IGUserForIGOnlyAPIGetInsightsParams | dict = {},
):
    """Get Insights for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIGetInsightsParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_insights(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_media(
    iguserforigonlyapi_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: IGUserForIGOnlyAPIGetMediaParams | dict = {},
):
    """Get Media for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIGetMediaParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_media(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_media(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateMediaParams | dict = {},
):
    """Create Media for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateMediaParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_media(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_media_publish(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateMediaPublishParams | dict = {},
):
    """Create Media Publish for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateMediaPublishParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_media_publish(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_mention(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateMentionParams | dict = {},
):
    """Create Mention for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateMentionParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_mention(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_message_attachment(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateMessageAttachmentParams | dict = {},
):
    """Create Message Attachment for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateMessageAttachmentParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_message_attachment(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_message(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateMessageParams | dict = {},
):
    """Create Message for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateMessageParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_message(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def delete_messenger_profile(
    iguserforigonlyapi_id: str,
    params: IGUserForIGOnlyAPIDeleteMessengerProfileParams | dict = {},
):
    """Delete Messenger Profile for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIDeleteMessengerProfileParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).delete_messenger_profile(params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_messenger_profile(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateMessengerProfileParams | dict = {},
):
    """Create Messenger Profile for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateMessengerProfileParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_messenger_profile(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateSubscribedAppParams | dict = {},
):
    """Create Subscribed App for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateSubscribedAppParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_subscribed_app(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def delete_welcome_message_flows(
    iguserforigonlyapi_id: str,
    params: IGUserForIGOnlyAPIDeleteWelcomeMessageFlowsParams | dict = {},
):
    """Delete Welcome Message Flows for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIDeleteWelcomeMessageFlowsParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).delete_welcome_message_flows(params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_welcome_message_flows(
    iguserforigonlyapi_id: str,
    fields: list[CTXPartnerAppWelcomeMessageFlowField] = [],
    params: IGUserForIGOnlyAPIGetWelcomeMessageFlowsParams | dict = {},
):
    """Get Welcome Message Flows for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See CTXPartnerAppWelcomeMessageFlowField type.
        params: Query parameters. Available params: See IGUserForIGOnlyAPIGetWelcomeMessageFlowsParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_welcome_message_flows(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_welcome_message_flow(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGUserForIGOnlyAPICreateWelcomeMessageFlowParams | dict = {},
):
    """Create Welcome Message Flow for this IGUserForIGOnlyAPI.

    Args:
        iguserforigonlyapi_id: The ID of the IGUserForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserForIGOnlyAPICreateWelcomeMessageFlowParams type.
    """
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_welcome_message_flow(
        fields=fields, params=params
    )
