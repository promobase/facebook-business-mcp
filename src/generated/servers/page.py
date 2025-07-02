"""Page MCP Server."""

from typing import Any

from facebook_business.adobjects.page import Page
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = Page(page_id)
    return obj.api_get(fields=fields)


@page_server.tool
@wrapped_fn_tool
def update_page(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Page(page_id).api_update(fields=fields, params=params)


# ---- Edge Methods (88) ----
@page_server.tool
@wrapped_fn_tool
def create_ab_test(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_ab_test(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_acknowledge_order(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_acknowledge_order(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_ads_posts(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_ads_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_agencies(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_agencies(params=params)


@page_server.tool
@wrapped_fn_tool
def create_agency(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_agency(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_assigned_users(params=params)


@page_server.tool
@wrapped_fn_tool
def get_assigned_users(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_assigned_users(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_assigned_user(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_assigned_user(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_blocked(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_blocked(params=params)


@page_server.tool
@wrapped_fn_tool
def get_blocked(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_blocked(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_blocked(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_blocked(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_business_datum(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_business_datum(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_business_projects(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_business_projects(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_call(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_call(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_canvas_element(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_canvas_element(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_canvases(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_canvases(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_canvase(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_canvase(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_commerce_orders(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_commerce_orders(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_commerce_payouts(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_commerce_payouts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_commerce_transactions(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_commerce_transactions(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_conversations(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_conversations(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_copyright_manual_claim(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_copyright_manual_claim(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_custom_label(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_custom_label(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_custom_user_settings(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_custom_user_settings(params=params)


@page_server.tool
@wrapped_fn_tool
def get_custom_user_settings(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_custom_user_settings(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_custom_user_setting(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_custom_user_setting(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_dataset(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_dataset(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_events(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_events(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_extend_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_extend_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_feed(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_feed(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_feed(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_feed(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_image_copyright(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_image_copyright(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_insights(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_insights(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_lead_gen_form(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_lead_gen_form(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_likes(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_likes(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_live_videos(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_live_videos(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_live_video(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_live_video(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_locations(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_locations(params=params)


@page_server.tool
@wrapped_fn_tool
def create_location(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_location(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_media_fingerprints(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_media_fingerprints(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_media_fingerprint(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_media_fingerprint(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_message_attachment(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_message_attachment(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_message_templates(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_message_templates(params=params)


@page_server.tool
@wrapped_fn_tool
def get_message_templates(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_message_templates(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_message_template(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_message_template(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_message(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_message(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_messenger_call_setting(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_messenger_call_setting(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_messenger_lead_form(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_messenger_lead_form(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_messenger_profile(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_messenger_profile(params=params)


@page_server.tool
@wrapped_fn_tool
def get_messenger_profile(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_messenger_profile(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_messenger_profile(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_messenger_profile(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_moderate_conversation(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_moderate_conversation(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_nlp_config(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_nlp_config(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_notification_messages_dev_support(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_notification_messages_dev_support(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_page_whats_app_number_verification(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_page_whats_app_number_verification(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_pass_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_pass_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_persona(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_persona(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_photo_story(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_photo_story(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_photos(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_photos(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_photo(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_photo(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_picture(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_picture(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_picture(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_picture(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_posts(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_published_posts(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_published_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_release_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_release_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_request_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_request_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_roles(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_roles(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_secondary_receivers(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_secondary_receivers(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_setting(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_setting(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_stories(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_stories(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_subscribed_app(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_tabs(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_tabs(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_take_thread_control(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_take_thread_control(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_thread_owner(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_thread_owner(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_threads(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_threads(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_unlink_account(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_unlink_account(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_video_copyright_rules(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_video_copyright_rules(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_copyright_rule(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_video_copyright_rule(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_copyright(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_video_copyright(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_video_reels(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_video_reels(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_reel(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_video_reel(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video_story(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_video_story(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_videos(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_videos(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_video(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_video(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def get_visitor_posts(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_visitor_posts(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def delete_welcome_message_flows(
    page_id: str,
    params: dict[str, Any] = {},
):
    return Page(page_id).delete_welcome_message_flows(params=params)


@page_server.tool
@wrapped_fn_tool
def get_welcome_message_flows(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).get_welcome_message_flows(fields=fields, params=params)


@page_server.tool
@wrapped_fn_tool
def create_welcome_message_flow(
    page_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Page(page_id).create_welcome_message_flow(fields=fields, params=params)
