"""
Auto-generated MCP server for Facebook WhatsAppBusinessAccount.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whatsappbusinessaccount import WhatsAppBusinessAccount
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-whatsappbusinessaccount")


# CRUD Operations


@mcp.tool()
async def get_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_assigned_user_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Assigned User for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_assigned_user result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_dataset_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Dataset for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_dataset result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_flow_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Flow for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_flow result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_flow(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_generate_payment_configuration_oauth_link_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Generate Payment Configuration Oauth Link for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_generate_payment_configuration_oauth_link result
    """
    result = WhatsAppBusinessAccount(
        fbid=object_id
    ).create_generate_payment_configuration_oauth_link(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message_template_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Message Template for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_message_template result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_message_template(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_migrate_flow_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Migrate Flow for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_migrate_flow result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_migrate_flow(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_migrate_message_template_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Migrate Message Template for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_migrate_message_template result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_migrate_message_template(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_payment_configuration_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Payment Configuration for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_payment_configuration result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_payment_configuration(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_phone_number_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Phone Number for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_phone_number result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_phone_number(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_catalog_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product Catalog for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product_catalog result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_product_catalog(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_set_obo_mobility_intent_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Set Obo Mobility Intent for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_set_obo_mobility_intent result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_set_obo_mobility_intent(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_set_solution_migration_intent_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Set Solution Migration Intent for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_set_solution_migration_intent result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_set_solution_migration_intent(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscribed_app_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Subscribed App for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_subscribed_app result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_subscribed_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_template_group_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Template Group for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_template_group result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_template_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_upsert_message_template_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Upsert Message Template for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_upsert_message_template result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).create_upsert_message_template(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_assigned_users_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Assigned Users for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_assigned_users result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).delete_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_message_templates_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Message Templates for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_message_templates result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).delete_message_templates(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_payment_configuration_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Payment Configuration for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_payment_configuration result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).delete_payment_configuration(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_product_catalogs_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Product Catalogs for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_product_catalogs result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).delete_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_subscribed_apps_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Subscribed Apps for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_subscribed_apps result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).delete_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_activities_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Activities for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_activities result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_activities(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Users for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_users result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_audiences_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Audiences for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_audiences result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_audiences(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_call_analytics_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Call Analytics for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_call_analytics result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_call_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_conversation_analytics_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Conversation Analytics for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_conversation_analytics result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_conversation_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dataset_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Dataset for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_dataset result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_flows_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Flows for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_flows result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_flows(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_message_campaigns_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Message Campaigns for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_message_campaigns result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_message_campaigns(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_message_template_previews_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Message Template Previews for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_message_template_previews result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_message_template_previews(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_message_templates_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Message Templates for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_message_templates result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_message_templates(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_payment_configuration_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Payment Configuration for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_payment_configuration result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_payment_configuration(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_payment_configurations_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Payment Configurations for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_payment_configurations result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_payment_configurations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_phone_numbers_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Phone Numbers for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_phone_numbers result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_phone_numbers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pricing_analytics_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Pricing Analytics for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pricing_analytics result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_pricing_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_catalogs_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Catalogs for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_catalogs result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_schedules_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Schedules for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_schedules result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_schedules(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_solutions_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Solutions for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_solutions result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_solutions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscribed_apps_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Subscribed Apps for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_subscribed_apps result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_template_analytics_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Template Analytics for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_template_analytics result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_template_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_template_group_analytics_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Template Group Analytics for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_template_group_analytics result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_template_group_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_template_groups_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Template Groups for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_template_groups result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_template_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_template_performance_metrics_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Template Performance Metrics for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_template_performance_metrics result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_template_performance_metrics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_welcome_message_sequences_for_whatsappbusinessaccount(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Welcome Message Sequences for WhatsAppBusinessAccount.

    Args:
        object_id: The ID of the WhatsAppBusinessAccount
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_welcome_message_sequences result
    """
    result = WhatsAppBusinessAccount(fbid=object_id).get_welcome_message_sequences(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whatsappbusinessaccount_server = mcp
