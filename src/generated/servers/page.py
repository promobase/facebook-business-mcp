"""
Auto-generated MCP server for Facebook Page.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.page import Page
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-page")


# CRUD Operations


@mcp.tool()
async def get_page(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
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
    """
    Update a Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
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
    """
    Create Ab Test for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ab_test result
    """
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
    """
    Create Acknowledge Order for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_acknowledge_order result
    """
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
    """
    Create Agency for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_agency result
    """
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
    """
    Create Assigned User for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_assigned_user result
    """
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
    """
    Create Blocked for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_blocked result
    """
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
    """
    Create Business Datum for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_business_datum result
    """
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
    """
    Create Call for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_call result
    """
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
    """
    Create Canvas Element for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_canvas_element result
    """
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
    """
    Create Canvase for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_canvase result
    """
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
    """
    Create Copyright Manual Claim for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_copyright_manual_claim result
    """
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
    """
    Create Custom Label for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_custom_label result
    """
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
    """
    Create Custom User Setting for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_custom_user_setting result
    """
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
    """
    Create Dataset for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_dataset result
    """
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
    """
    Create Extend Thread Control for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_extend_thread_control result
    """
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
    """
    Create Feed for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_feed result
    """
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
    """
    Create Image Copyright for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_image_copyright result
    """
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
    """
    Create Lead Gen Form for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_lead_gen_form result
    """
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
    """
    Create Live Video for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_live_video result
    """
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
    """
    Create Location for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_location result
    """
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
    """
    Create Media Fingerprint for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_media_fingerprint result
    """
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
    """
    Create Message for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_message result
    """
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
    """
    Create Message Attachment for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_message_attachment result
    """
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
    """
    Create Message Template for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_message_template result
    """
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
    """
    Create Messenger Call Setting for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_messenger_call_setting result
    """
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
    """
    Create Messenger Lead Form for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_messenger_lead_form result
    """
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
    """
    Create Messenger Profile for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_messenger_profile result
    """
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
    """
    Create Moderate Conversation for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_moderate_conversation result
    """
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
    """
    Create Nlp Config for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_nlp_config result
    """
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
    """
    Create Notification Messages Dev Support for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_notification_messages_dev_support result
    """
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
    """
    Create Page Backed Instagram Account for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_page_backed_instagram_account result
    """
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
    """
    Create Page Whats App Number Verification for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_page_whats_app_number_verification result
    """
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
    """
    Create Pass Thread Control for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_pass_thread_control result
    """
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
    """
    Create Persona for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_persona result
    """
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
    """
    Create Photo for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_photo result
    """
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
    """
    Create Photo Story for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_photo_story result
    """
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
    """
    Create Picture for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_picture result
    """
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
    """
    Create Release Thread Control for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_release_thread_control result
    """
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
    """
    Create Request Thread Control for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_request_thread_control result
    """
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
    """
    Create Setting for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_setting result
    """
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
    """
    Create Subscribed App for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_subscribed_app result
    """
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
    """
    Create Take Thread Control for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_take_thread_control result
    """
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
    """
    Create Unlink Account for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_unlink_account result
    """
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
    """
    Create Video for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video result
    """
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
    """
    Create Video Copyright for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video_copyright result
    """
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
    """
    Create Video Copyright Rule for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video_copyright_rule result
    """
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
    """
    Create Video Reel for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video_reel result
    """
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
    """
    Create Video Story for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video_story result
    """
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
    """
    Create Welcome Message Flow for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_welcome_message_flow result
    """
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
    """
    Delete Agencies for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_agencies result
    """
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
    """
    Delete Assigned Users for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_assigned_users result
    """
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
    """
    Delete Blocked for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_blocked result
    """
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
    """
    Delete Custom User Settings for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_custom_user_settings result
    """
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
    """
    Delete Locations for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_locations result
    """
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
    """
    Delete Message Templates for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_message_templates result
    """
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
    """
    Delete Messenger Profile for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_messenger_profile result
    """
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
    """
    Delete Subscribed Apps for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_subscribed_apps result
    """
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
    """
    Delete Welcome Message Flows for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_welcome_message_flows result
    """
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
    """
    Get Ab Tests for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ab_tests result
    """
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
    """
    Get Ads Posts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads_posts result
    """
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
    """
    Get Agencies for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
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
    """
    Get Albums for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_albums result
    """
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
    """
    Get Ar Experience for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ar_experience result
    """
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
    """
    Get Assigned Users for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_users result
    """
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
    """
    Get Blocked for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_blocked result
    """
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
    """
    Get Business Projects for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_projects result
    """
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
    """
    Get Call To Actions for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_call_to_actions result
    """
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
    """
    Get Canvas Elements for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_canvas_elements result
    """
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
    """
    Get Canvases for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_canvases result
    """
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
    """
    Get Chat Plugin for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_chat_plugin result
    """
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
    """
    Get Commerce Merchant Settings for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_merchant_settings result
    """
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
    """
    Get Commerce Orders for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_orders result
    """
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
    """
    Get Commerce Payouts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_payouts result
    """
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
    """
    Get Commerce Transactions for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_transactions result
    """
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
    """
    Get Conversations for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_conversations result
    """
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
    """
    Get Crosspost Whitelisted Pages for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_crosspost_whitelisted_pages result
    """
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
    """
    Get Ctx Optimization Eligibility for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ctx_optimization_eligibility result
    """
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
    """
    Get Custom Labels for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_labels result
    """
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
    """
    Get Custom User Settings for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_user_settings result
    """
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
    """
    Get Dataset for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_dataset result
    """
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
    """
    Get Events for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_events result
    """
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
    """
    Get Fantasy Games for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_fantasy_games result
    """
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
    """
    Get Feed for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_feed result
    """
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
    """
    Get Global Brand Children for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_global_brand_children result
    """
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
    """
    Get Image Copyrights for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_image_copyrights result
    """
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
    """
    Get Indexed Videos for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_indexed_videos result
    """
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
    """
    Get Insights for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
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
    """
    Get Instagram Accounts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_instagram_accounts result
    """
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
    """
    Get Lead Gen Forms for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_lead_gen_forms result
    """
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
    """
    Get Likes for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
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
    """
    Get Live Videos for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_live_videos result
    """
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
    """
    Get Locations for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_locations result
    """
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
    """
    Get Media Fingerprints for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_media_fingerprints result
    """
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
    """
    Get Message Templates for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_message_templates result
    """
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
    """
    Get Messaging Feature Review for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_messaging_feature_review result
    """
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
    """
    Get Messenger Call Settings for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_messenger_call_settings result
    """
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
    """
    Get Messenger Lead Forms for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_messenger_lead_forms result
    """
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
    """
    Get Messenger Profile for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_messenger_profile result
    """
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
    """
    Get Notification Message Tokens for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_notification_message_tokens result
    """
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
    """
    Get Page Backed Instagram Accounts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_page_backed_instagram_accounts result
    """
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
    """
    Get Personas for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_personas result
    """
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
    """
    Get Photos for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_photos result
    """
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
    """
    Get Picture for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_picture result
    """
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
    """
    Get Posts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_posts result
    """
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
    """
    Get Product Catalogs for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_catalogs result
    """
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
    """
    Get Published Posts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_published_posts result
    """
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
    """
    Get Roles for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_roles result
    """
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
    """
    Get Rtb Dynamic Posts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_rtb_dynamic_posts result
    """
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
    """
    Get Scheduled Posts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_scheduled_posts result
    """
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
    """
    Get Secondary Receivers for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_secondary_receivers result
    """
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
    """
    Get Settings for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_settings result
    """
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
    """
    Get Shop Setup Status for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shop_setup_status result
    """
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
    """
    Get Store Locations for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_store_locations result
    """
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
    """
    Get Stories for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_stories result
    """
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
    """
    Get Subscribed Apps for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_subscribed_apps result
    """
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
    """
    Get Tabs for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tabs result
    """
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
    """
    Get Tagged for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tagged result
    """
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
    """
    Get Thread Owner for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_thread_owner result
    """
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
    """
    Get Threads for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_threads result
    """
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
    """
    Get Video Copyright Rules for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_video_copyright_rules result
    """
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
    """
    Get Video Lists for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_video_lists result
    """
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
    """
    Get Video Reels for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_video_reels result
    """
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
    """
    Get Videos for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos result
    """
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
    """
    Get Visitor Posts for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_visitor_posts result
    """
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
    """
    Get Welcome Message Flows for Page.

    Args:
        object_id: The ID of the Page
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_welcome_message_flows result
    """
    result = Page(fbid=object_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
page_server = mcp
