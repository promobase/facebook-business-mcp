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


# ---- Edge Methods (60) ----
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
def create_activitie(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_activitie(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_ad_placement_groups(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_ad_placement_groups(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_adnetwork_placements(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_adnetwork_placements(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_adnetworkanalytics(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_adnetworkanalytics(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_adnetworkanalytic(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_adnetworkanalytic(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_adnetworkanalytics_results(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_adnetworkanalytics_results(fields=fields, params=params)


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
def create_aem_skan_readine(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_aem_skan_readine(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_agencies(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_agencies(fields=fields, params=params)


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
def get_android_dialog_configs(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_android_dialog_configs(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_app_capi_settings(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_app_capi_settings(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_app_event_types(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_app_event_types(fields=fields, params=params)


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
def get_appassets(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_appassets(fields=fields, params=params)


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
def get_authorized_adaccounts(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_authorized_adaccounts(fields=fields, params=params)


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
def get_cloudbridge_settings(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_cloudbridge_settings(fields=fields, params=params)


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
def get_connected_client_businesses(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_connected_client_businesses(fields=fields, params=params)


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
def get_ios_dialog_configs(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_ios_dialog_configs(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_linked_dataset(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_linked_dataset(fields=fields, params=params)


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
def get_monetized_digital_store_objects(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_monetized_digital_store_objects(
        fields=fields, params=params
    )


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
def get_object_types(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_object_types(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_objects(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_objects(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def create_occludespopup(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_occludespopup(fields=fields, params=params)


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
def get_purchases(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_purchases(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_roles(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_roles(fields=fields, params=params)


@application_server.tool
@wrapped_fn_tool
def get_server_domain_infos(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_server_domain_infos(fields=fields, params=params)


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
def get_subscribed_domains(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_subscribed_domains(fields=fields, params=params)


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
def get_subscribed_domains_phishing(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_subscribed_domains_phishing(fields=fields, params=params)


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
def get_subscriptions(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_subscriptions(fields=fields, params=params)


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
def create_whatsapp_business_solution(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).create_whatsapp_business_solution(
        fields=fields, params=params
    )


@application_server.tool
@wrapped_fn_tool
def get_whatsapp_business_solutions(
    application_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Application(application_id).get_whatsapp_business_solutions(fields=fields, params=params)
