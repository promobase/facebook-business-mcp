"""WhatsAppBusinessAccount MCP Server."""

from typing import Any

from facebook_business.adobjects.whatsappbusinessaccount import WhatsAppBusinessAccount
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWhatsAppBusinessAccount"
instructions = """
WhatsAppBusinessAccount MCP Server for Facebook Business API.

Provides typed access to all WhatsAppBusinessAccount operations.
"""

whatsappbusinessaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_whatsappbusinessaccount(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
) -> str:
    obj = WhatsAppBusinessAccount(whatsappbusinessaccount_id)
    return obj.api_get(fields=fields)


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def update_whatsappbusinessaccount(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).api_update(
        fields=fields, params=params
    )


# ---- Edge Methods (43) ----
@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_activities(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_activities(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    whatsappbusinessaccount_id: str,
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_assigned_users(params=params)


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_assigned_users(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_assigned_users(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_assigned_user(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_assigned_user(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_audiences(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_audiences(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_call_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_call_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_conversation_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_conversation_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_dataset(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_dataset(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_dataset(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_dataset(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_flows(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_flows(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_flow(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_flow(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_generate_payment_configuration_oauth_link(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(
        whatsappbusinessaccount_id
    ).create_generate_payment_configuration_oauth_link(fields=fields, params=params)


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_message_campaigns(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_message_campaigns(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_message_template_previews(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_message_template_previews(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_message_templates(
    whatsappbusinessaccount_id: str,
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_message_templates(
        params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_message_templates(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_message_templates(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_message_template(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_message_template(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_migrate_flow(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_migrate_flow(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_migrate_message_template(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_migrate_message_template(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_payment_configuration(
    whatsappbusinessaccount_id: str,
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_payment_configuration(
        params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_payment_configuration(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_payment_configuration(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_payment_configuration(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_payment_configuration(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_payment_configurations(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_payment_configurations(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_phone_numbers(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_phone_numbers(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_phone_number(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_phone_number(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_pricing_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_pricing_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_product_catalogs(
    whatsappbusinessaccount_id: str,
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_product_catalogs(
        params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_product_catalogs(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_product_catalogs(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_product_catalog(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_product_catalog(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_schedules(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_schedules(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_set_obo_mobility_intent(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_set_obo_mobility_intent(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_set_solution_migration_intent(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_set_solution_migration_intent(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_solutions(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_solutions(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_subscribed_apps(
    whatsappbusinessaccount_id: str,
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_subscribed_apps(params=params)


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_subscribed_apps(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_subscribed_apps(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_subscribed_app(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_template_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_template_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_template_group_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_template_group_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_template_groups(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_template_groups(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_template_group(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_template_group(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_template_performance_metrics(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_template_performance_metrics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_upsert_message_template(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_upsert_message_template(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_welcome_message_sequences(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_welcome_message_sequences(
        fields=fields, params=params
    )
