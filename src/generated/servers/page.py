"""
Auto-generated MCP server for Facebook Page.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.page import Page
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-page")


# CRUD Operations


@mcp.tool()
async def create_page(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ab_test_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_ab_test(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_acknowledge_order_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_acknowledge_order(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_agency_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_agency(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_assigned_user_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_blocked_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_blocked(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_business_datum_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_business_datum(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_call_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_call(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_canvas_element_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_canvas_element(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_canvase_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_canvase(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_copyright_manual_claim_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_copyright_manual_claim(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_custom_label_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_custom_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_custom_user_setting_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_custom_user_setting(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_dataset_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_extend_thread_control_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_extend_thread_control(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_feed_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_image_copyright_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_image_copyright(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_lead_gen_form_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_lead_gen_form(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_live_video_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_location_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_location(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_media_fingerprint_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_media_fingerprint(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_message(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message_attachment_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_message_attachment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message_template_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_message_template(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_messenger_call_setting_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_messenger_call_setting(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_messenger_lead_form_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_messenger_lead_form(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_messenger_profile_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_moderate_conversation_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_moderate_conversation(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_nlp_config_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_nlp_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_notification_messages_dev_support_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_notification_messages_dev_support(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_page_backed_instagram_account_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_page_backed_instagram_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_page_whats_app_number_verification_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_page_whats_app_number_verification(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_pass_thread_control_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_pass_thread_control(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_persona_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_persona(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_photo_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_photo_story_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_photo_story(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_picture_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_release_thread_control_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_release_thread_control(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_request_thread_control_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_request_thread_control(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_setting_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_setting(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscribed_app_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_subscribed_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_take_thread_control_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_take_thread_control(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_unlink_account_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_unlink_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_copyright_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_video_copyright(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_copyright_rule_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_video_copyright_rule(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_reel_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_video_reel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_story_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_video_story(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_welcome_message_flow_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).create_welcome_message_flow(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_agencies_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_assigned_users_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_blocked_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_blocked(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_custom_user_settings_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_custom_user_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_locations_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_locations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_message_templates_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_message_templates(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_messenger_profile_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_subscribed_apps_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_welcome_message_flows_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).delete_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ab_tests_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_ab_tests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_posts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_ads_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_albums_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_albums(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ar_experience_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_ar_experience(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_blocked_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_blocked(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_projects_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_business_projects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_call_to_actions_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_call_to_actions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_canvas_elements_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_canvas_elements(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_canvases_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_canvases(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_chat_plugin_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_chat_plugin(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_merchant_settings_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_commerce_merchant_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_orders_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_commerce_orders(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_payouts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_commerce_payouts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_transactions_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_commerce_transactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_conversations_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_conversations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_crosspost_whitelisted_pages_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_crosspost_whitelisted_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ctx_optimization_eligibility_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_ctx_optimization_eligibility(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_labels_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_custom_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_user_settings_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_custom_user_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dataset_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_events_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_fantasy_games_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_fantasy_games(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_feed_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_global_brand_children_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_global_brand_children(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_image_copyrights_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_image_copyrights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_indexed_videos_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_indexed_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_accounts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_lead_gen_forms_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_lead_gen_forms(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_videos_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_locations_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_locations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_media_fingerprints_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_media_fingerprints(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_message_templates_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_message_templates(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_messaging_feature_review_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_messaging_feature_review(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_messenger_call_settings_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_messenger_call_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_messenger_lead_forms_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_messenger_lead_forms(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_messenger_profile_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_notification_message_tokens_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_notification_message_tokens(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_page_backed_instagram_accounts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_page_backed_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_personas_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_personas(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_photos_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_photos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_picture_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_posts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_catalogs_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_published_posts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_published_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_roles_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_roles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_rtb_dynamic_posts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_rtb_dynamic_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_scheduled_posts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_scheduled_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_secondary_receivers_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_secondary_receivers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_settings_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shop_setup_status_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_shop_setup_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_store_locations_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_store_locations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stories_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_stories(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscribed_apps_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tabs_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_tabs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tagged_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_tagged(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_thread_owner_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_thread_owner(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_threads_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_threads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_video_copyright_rules_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_video_copyright_rules(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_video_lists_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_video_lists(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_video_reels_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_video_reels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_visitor_posts_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_visitor_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_welcome_message_flows_for_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Page(fbid=object_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
page_server = mcp
