"""Application MCP Server."""

from typing import Any

from facebook_business.adobjects.application import Application
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookApplication"
instructions = """
Application MCP Server for Facebook Business API.

Provides typed access to all Application operations.
"""

application_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@application_server.tool
@wrapped_fn_tool
def get_application(
    application_id: str,
    fields: list[str] = [],
) -> str:
    obj = Application(application_id)
    return obj.api_get(fields=fields)


@application_server.tool
@wrapped_fn_tool
def update_application(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Application(application_id).api_update(fields=fields, params=params)


# ---- Edge Methods (41) ----
@application_server.tool
@wrapped_fn_tool
def delete_accounts(
    application_id: str,
    params: dict[str, Any] = {},
):
    return Application(application_id).delete_accounts(params=params)


@application_server.tool
@wrapped_fn_tool
def get_accounts(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_accounts(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_account(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_account(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_activity(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_activity(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_ad_network_placements(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_ad_network_placements(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_ad_network_analytics(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_ad_network_analytics(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_ad_network_analytic(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_ad_network_analytic(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_ad_network_analytics_results(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_ad_network_analytics_results(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def get_aem_attribution(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_aem_attribution(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_aem_conversion_configs(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_aem_conversion_configs(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_aem_conversion_filter(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_aem_conversion_filter(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_aem_conversion(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_aem_conversion(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_aem_skan_readiness(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_aem_skan_readiness(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_aggregate_revenue(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_aggregate_revenue(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_app_indexing(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_app_indexing(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_app_indexing_session(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_app_indexing_session(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_app_installed_groups(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_app_installed_groups(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_app_push_device_token(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_app_push_device_token(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_asset(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_asset(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_authorized_ad_accounts(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_authorized_ad_accounts(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_button_auto_detection_device_selection(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_button_auto_detection_device_selection(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def create_codeless_event_mapping(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_codeless_event_mapping(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_da_checks(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_da_checks(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_domain_report(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_domain_report(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_iap_purchases(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_iap_purchases(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_message_templates(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_message_templates(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_mmp_auditing(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_mmp_auditing(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_mobile_sdk_gk(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_mobile_sdk_gk(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_monetized_digital_store_object(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_monetized_digital_store_object(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def create_occludes_popup(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_occludes_popup(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_permissions(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_permissions(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_products(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_products(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_sgw_dataset_status(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_sgw_dataset_status(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_sgw_install_deferral_link(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_sgw_install_deferral_link(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_subscribed_domain(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_subscribed_domain(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_subscribed_domains_phishing(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_subscribed_domains_phishing(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def delete_subscriptions(
    application_id: str,
    params: dict[str, Any] = {},
):
    return Application(application_id).delete_subscriptions(params=params)


@application_server.tool
@wrapped_fn_tool
def create_subscription(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_subscription(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_upload(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_upload(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_whats_app_business_solution(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_whats_app_business_solution(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def get_whats_app_business_solutions(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_whats_app_business_solutions(
        fields=fields, params=params
    )
