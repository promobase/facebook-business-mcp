"""WhatsAppBusinessAccount MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.whatsappbusinessaccount import WhatsAppBusinessAccount
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.ctxpartnerappwelcomemessageflow import (
    CTXPartnerAppWelcomeMessageFlowField,
)
from src.generated.models.dataset import DatasetField
from src.generated.models.productcatalog import ProductCatalogField
from src.generated.models.whatsappbusinessaccount import (
    WhatsAppBusinessAccountCreateAssignedUserParams,
    WhatsAppBusinessAccountCreateDatasetParams,
    WhatsAppBusinessAccountCreateFlowParams,
    WhatsAppBusinessAccountCreateGeneratePaymentConfigurationOauthLinkParams,
    WhatsAppBusinessAccountCreateMessageTemplateParams,
    WhatsAppBusinessAccountCreateMigrateFlowParams,
    WhatsAppBusinessAccountCreateMigrateMessageTemplateParams,
    WhatsAppBusinessAccountCreatePaymentConfigurationParams,
    WhatsAppBusinessAccountCreatePhoneNumberParams,
    WhatsAppBusinessAccountCreateProductCatalogParams,
    WhatsAppBusinessAccountCreateSetOboMobilityIntentParams,
    WhatsAppBusinessAccountCreateSetSolutionMigrationIntentParams,
    WhatsAppBusinessAccountCreateSubscribedAppParams,
    WhatsAppBusinessAccountCreateTemplateGroupParams,
    WhatsAppBusinessAccountCreateUpsertMessageTemplateParams,
    WhatsAppBusinessAccountDeleteAssignedUsersParams,
    WhatsAppBusinessAccountDeleteMessageTemplatesParams,
    WhatsAppBusinessAccountDeletePaymentConfigurationParams,
    WhatsAppBusinessAccountDeleteProductCatalogsParams,
    WhatsAppBusinessAccountField,
    WhatsAppBusinessAccountGetAssignedUsersParams,
    WhatsAppBusinessAccountGetCallAnalyticsParams,
    WhatsAppBusinessAccountGetConversationAnalyticsParams,
    WhatsAppBusinessAccountGetMessageTemplatePreviewsParams,
    WhatsAppBusinessAccountGetMessageTemplatesParams,
    WhatsAppBusinessAccountGetPaymentConfigurationParams,
    WhatsAppBusinessAccountGetPricingAnalyticsParams,
    WhatsAppBusinessAccountGetTemplateAnalyticsParams,
    WhatsAppBusinessAccountGetTemplateGroupAnalyticsParams,
    WhatsAppBusinessAccountGetTemplatePerformanceMetricsParams,
    WhatsAppBusinessAccountGetWelcomeMessageSequencesParams,
    WhatsAppBusinessAccountUpdateParams,
)
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
    fields: list[WhatsAppBusinessAccountField] = [],
) -> str:
    """Get a WhatsAppBusinessAccount object by ID.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See WhatsAppBusinessAccountField type.
    """
    obj = WhatsAppBusinessAccount(whatsappbusinessaccount_id)
    return obj.api_get(fields=fields)


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def update_whatsappbusinessaccount(
    whatsappbusinessaccount_id: str,
    fields: list[WhatsAppBusinessAccountField] = [],
    params: WhatsAppBusinessAccountUpdateParams | dict = {},
) -> str:
    """Update a WhatsAppBusinessAccount object.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to return after update. Available fields: See WhatsAppBusinessAccountField type.
        params: Parameters to update. Available params: See WhatsAppBusinessAccountUpdateParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).api_update(
        fields=fields, params=params
    )


# ---- Edge Methods (30) ----
@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    whatsappbusinessaccount_id: str,
    params: WhatsAppBusinessAccountDeleteAssignedUsersParams | dict = {},
):
    """Delete Assigned Users for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        params: Query parameters. Available params: See WhatsAppBusinessAccountDeleteAssignedUsersParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_assigned_users(params=params)


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_assigned_users(
    whatsappbusinessaccount_id: str,
    fields: list[AssignedUserField] = [],
    params: WhatsAppBusinessAccountGetAssignedUsersParams | dict = {},
):
    """Get Assigned Users for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AssignedUserField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetAssignedUsersParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_assigned_users(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_assigned_user(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateAssignedUserParams | dict = {},
):
    """Create Assigned User for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateAssignedUserParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_assigned_user(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_call_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetCallAnalyticsParams | dict = {},
):
    """Get Call Analytics for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetCallAnalyticsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_call_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_conversation_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetConversationAnalyticsParams | dict = {},
):
    """Get Conversation Analytics for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetConversationAnalyticsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_conversation_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_dataset(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateDatasetParams | dict = {},
):
    """Create Dataset for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateDatasetParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_dataset(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_flow(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateFlowParams | dict = {},
):
    """Create Flow for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateFlowParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_flow(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_generate_payment_configuration_oauth_link(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateGeneratePaymentConfigurationOauthLinkParams | dict = {},
):
    """Create Generate Payment Configuration Oauth Link for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateGeneratePaymentConfigurationOauthLinkParams type.
    """
    return WhatsAppBusinessAccount(
        whatsappbusinessaccount_id
    ).create_generate_payment_configuration_oauth_link(fields=fields, params=params)


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_message_template_previews(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetMessageTemplatePreviewsParams | dict = {},
):
    """Get Message Template Previews for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetMessageTemplatePreviewsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_message_template_previews(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_message_templates(
    whatsappbusinessaccount_id: str,
    params: WhatsAppBusinessAccountDeleteMessageTemplatesParams | dict = {},
):
    """Delete Message Templates for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        params: Query parameters. Available params: See WhatsAppBusinessAccountDeleteMessageTemplatesParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_message_templates(
        params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_message_templates(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetMessageTemplatesParams | dict = {},
):
    """Get Message Templates for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetMessageTemplatesParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_message_templates(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_message_template(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateMessageTemplateParams | dict = {},
):
    """Create Message Template for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateMessageTemplateParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_message_template(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_migrate_flow(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateMigrateFlowParams | dict = {},
):
    """Create Migrate Flow for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateMigrateFlowParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_migrate_flow(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_migrate_message_template(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateMigrateMessageTemplateParams | dict = {},
):
    """Create Migrate Message Template for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateMigrateMessageTemplateParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_migrate_message_template(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_payment_configuration(
    whatsappbusinessaccount_id: str,
    params: WhatsAppBusinessAccountDeletePaymentConfigurationParams | dict = {},
):
    """Delete Payment Configuration for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        params: Query parameters. Available params: See WhatsAppBusinessAccountDeletePaymentConfigurationParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_payment_configuration(
        params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_payment_configuration(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetPaymentConfigurationParams | dict = {},
):
    """Get Payment Configuration for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetPaymentConfigurationParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_payment_configuration(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_payment_configuration(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreatePaymentConfigurationParams | dict = {},
):
    """Create Payment Configuration for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreatePaymentConfigurationParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_payment_configuration(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_phone_number(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreatePhoneNumberParams | dict = {},
):
    """Create Phone Number for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreatePhoneNumberParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_phone_number(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_pricing_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetPricingAnalyticsParams | dict = {},
):
    """Get Pricing Analytics for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetPricingAnalyticsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_pricing_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def delete_product_catalogs(
    whatsappbusinessaccount_id: str,
    params: WhatsAppBusinessAccountDeleteProductCatalogsParams | dict = {},
):
    """Delete Product Catalogs for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        params: Query parameters. Available params: See WhatsAppBusinessAccountDeleteProductCatalogsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).delete_product_catalogs(
        params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_product_catalog(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateProductCatalogParams | dict = {},
):
    """Create Product Catalog for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateProductCatalogParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_product_catalog(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_set_obo_mobility_intent(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateSetOboMobilityIntentParams | dict = {},
):
    """Create Set Obo Mobility Intent for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateSetOboMobilityIntentParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_set_obo_mobility_intent(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_set_solution_migration_intent(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateSetSolutionMigrationIntentParams | dict = {},
):
    """Create Set Solution Migration Intent for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateSetSolutionMigrationIntentParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_set_solution_migration_intent(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateSubscribedAppParams | dict = {},
):
    """Create Subscribed App for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateSubscribedAppParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_subscribed_app(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_template_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetTemplateAnalyticsParams | dict = {},
):
    """Get Template Analytics for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetTemplateAnalyticsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_template_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_template_group_analytics(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetTemplateGroupAnalyticsParams | dict = {},
):
    """Get Template Group Analytics for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetTemplateGroupAnalyticsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_template_group_analytics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_template_group(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateTemplateGroupParams | dict = {},
):
    """Create Template Group for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateTemplateGroupParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_template_group(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_template_performance_metrics(
    whatsappbusinessaccount_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: WhatsAppBusinessAccountGetTemplatePerformanceMetricsParams | dict = {},
):
    """Get Template Performance Metrics for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetTemplatePerformanceMetricsParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_template_performance_metrics(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def create_upsert_message_template(
    whatsappbusinessaccount_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessAccountCreateUpsertMessageTemplateParams | dict = {},
):
    """Create Upsert Message Template for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessAccountCreateUpsertMessageTemplateParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).create_upsert_message_template(
        fields=fields, params=params
    )


@whatsappbusinessaccount_server.tool
@wrapped_fn_tool
def get_welcome_message_sequences(
    whatsappbusinessaccount_id: str,
    fields: list[CTXPartnerAppWelcomeMessageFlowField] = [],
    params: WhatsAppBusinessAccountGetWelcomeMessageSequencesParams | dict = {},
):
    """Get Welcome Message Sequences for this WhatsAppBusinessAccount.

    Args:
        whatsappbusinessaccount_id: The ID of the WhatsAppBusinessAccount.
        fields: Fields to retrieve. Available fields: See CTXPartnerAppWelcomeMessageFlowField type.
        params: Query parameters. Available params: See WhatsAppBusinessAccountGetWelcomeMessageSequencesParams type.
    """
    return WhatsAppBusinessAccount(whatsappbusinessaccount_id).get_welcome_message_sequences(
        fields=fields, params=params
    )
