"""Streamlined Page MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.page import Page
from fastmcp import FastMCP

from src.generated.models.page import PageField, PageUpdateParams
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


# ---- Edge Methods (88) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.page_wrappers import (
    create_ab_test,
    create_acknowledge_order,
    create_agency,
    create_assigned_user,
    create_blocked,
    create_business_datum,
    create_call,
    create_canvas_element,
    create_canvase,
    create_copyright_manual_claim,
    create_custom_label,
    create_custom_user_setting,
    create_dataset,
    create_extend_thread_control,
    create_feed,
    create_image_copyright,
    create_lead_gen_form,
    create_live_video,
    create_location,
    create_media_fingerprint,
    create_message,
    create_message_attachment,
    create_message_template,
    create_messenger_call_setting,
    create_messenger_lead_form,
    create_messenger_profile,
    create_moderate_conversation,
    create_nlp_config,
    create_notification_messages_dev_support,
    create_page_whats_app_number_verification,
    create_pass_thread_control,
    create_persona,
    create_photo,
    create_photo_story,
    create_picture,
    create_release_thread_control,
    create_request_thread_control,
    create_setting,
    create_subscribed_app,
    create_take_thread_control,
    create_unlink_account,
    create_video,
    create_video_copyright,
    create_video_copyright_rule,
    create_video_reel,
    create_video_story,
    create_welcome_message_flow,
    delete_agencies,
    delete_assigned_users,
    delete_blocked,
    delete_custom_user_settings,
    delete_locations,
    delete_message_templates,
    delete_messenger_profile,
    delete_welcome_message_flows,
    get_ads_posts,
    get_assigned_users,
    get_blocked,
    get_business_projects,
    get_canvases,
    get_commerce_orders,
    get_commerce_payouts,
    get_commerce_transactions,
    get_conversations,
    get_custom_user_settings,
    get_events,
    get_feed,
    get_insights,
    get_likes,
    get_live_videos,
    get_media_fingerprints,
    get_message_templates,
    get_messenger_profile,
    get_photos,
    get_picture,
    get_posts,
    get_published_posts,
    get_roles,
    get_secondary_receivers,
    get_stories,
    get_tabs,
    get_thread_owner,
    get_threads,
    get_video_copyright_rules,
    get_video_reels,
    get_videos,
    get_visitor_posts,
    get_welcome_message_flows,
)

# ---- Register tools ----
# Register CRUD operations
page_server.tool(get_page)
page_server.tool(update_page)

# Register edge methods from wrappers
page_server.tool(create_ab_test)
page_server.tool(create_acknowledge_order)
page_server.tool(get_ads_posts)
page_server.tool(delete_agencies)
page_server.tool(create_agency)
page_server.tool(delete_assigned_users)
page_server.tool(get_assigned_users)
page_server.tool(create_assigned_user)
page_server.tool(delete_blocked)
page_server.tool(get_blocked)
page_server.tool(create_blocked)
page_server.tool(create_business_datum)
page_server.tool(get_business_projects)
page_server.tool(create_call)
page_server.tool(create_canvas_element)
page_server.tool(get_canvases)
page_server.tool(create_canvase)
page_server.tool(get_commerce_orders)
page_server.tool(get_commerce_payouts)
page_server.tool(get_commerce_transactions)
page_server.tool(get_conversations)
page_server.tool(create_copyright_manual_claim)
page_server.tool(create_custom_label)
page_server.tool(delete_custom_user_settings)
page_server.tool(get_custom_user_settings)
page_server.tool(create_custom_user_setting)
page_server.tool(create_dataset)
page_server.tool(get_events)
page_server.tool(create_extend_thread_control)
page_server.tool(get_feed)
page_server.tool(create_feed)
page_server.tool(create_image_copyright)
page_server.tool(get_insights)
page_server.tool(create_lead_gen_form)
page_server.tool(get_likes)
page_server.tool(get_live_videos)
page_server.tool(create_live_video)
page_server.tool(delete_locations)
page_server.tool(create_location)
page_server.tool(get_media_fingerprints)
page_server.tool(create_media_fingerprint)
page_server.tool(create_message_attachment)
page_server.tool(delete_message_templates)
page_server.tool(get_message_templates)
page_server.tool(create_message_template)
page_server.tool(create_message)
page_server.tool(create_messenger_call_setting)
page_server.tool(create_messenger_lead_form)
page_server.tool(delete_messenger_profile)
page_server.tool(get_messenger_profile)
page_server.tool(create_messenger_profile)
page_server.tool(create_moderate_conversation)
page_server.tool(create_nlp_config)
page_server.tool(create_notification_messages_dev_support)
page_server.tool(create_page_whats_app_number_verification)
page_server.tool(create_pass_thread_control)
page_server.tool(create_persona)
page_server.tool(create_photo_story)
page_server.tool(get_photos)
page_server.tool(create_photo)
page_server.tool(get_picture)
page_server.tool(create_picture)
page_server.tool(get_posts)
page_server.tool(get_published_posts)
page_server.tool(create_release_thread_control)
page_server.tool(create_request_thread_control)
page_server.tool(get_roles)
page_server.tool(get_secondary_receivers)
page_server.tool(create_setting)
page_server.tool(get_stories)
page_server.tool(create_subscribed_app)
page_server.tool(get_tabs)
page_server.tool(create_take_thread_control)
page_server.tool(get_thread_owner)
page_server.tool(get_threads)
page_server.tool(create_unlink_account)
page_server.tool(get_video_copyright_rules)
page_server.tool(create_video_copyright_rule)
page_server.tool(create_video_copyright)
page_server.tool(get_video_reels)
page_server.tool(create_video_reel)
page_server.tool(create_video_story)
page_server.tool(get_videos)
page_server.tool(create_video)
page_server.tool(get_visitor_posts)
page_server.tool(delete_welcome_message_flows)
page_server.tool(get_welcome_message_flows)
page_server.tool(create_welcome_message_flow)
