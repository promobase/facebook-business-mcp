"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .commercemerchantsettings import CommerceMerchantSettingsFields
    from .whatsappbusinesshealthstatusformessagesend import (
        WhatsAppBusinessHealthStatusForMessageSendFields,
    )


class WhatsAppBusinessAccount_business_verification_status(str, Enum):
    """WhatsAppBusinessAccount_business_verification_status enum values."""

    expired = "expired"
    failed = "failed"
    ineligible = "ineligible"
    not_verified = "not_verified"
    pending = "pending"
    pending_need_more_info = "pending_need_more_info"
    pending_submission = "pending_submission"
    rejected = "rejected"
    revoked = "revoked"
    verified = "verified"


class whatsappbusinessaccountpricing_analytics_dimensions_enum_param(str, Enum):
    """whatsappbusinessaccountpricing_analytics_dimensions_enum_param enum values."""

    COUNTRY = "COUNTRY"
    PHONE = "PHONE"
    PRICING_CATEGORY = "PRICING_CATEGORY"
    PRICING_TYPE = "PRICING_TYPE"
    TIER = "TIER"


class whatsappbusinessaccountcall_analytics_granularity_enum_param(str, Enum):
    """whatsappbusinessaccountcall_analytics_granularity_enum_param enum values."""

    DAILY = "DAILY"
    HALF_HOUR = "HALF_HOUR"
    MONTHLY = "MONTHLY"


class whatsappbusinessaccountmessage_templates_display_format_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_templates_display_format_enum_param enum values."""

    ORDER_DETAILS = "ORDER_DETAILS"


class whatsappbusinessaccountcall_analytics_dimensions_enum_param(str, Enum):
    """whatsappbusinessaccountcall_analytics_dimensions_enum_param enum values."""

    COUNTRY = "COUNTRY"
    DIRECTION = "DIRECTION"
    PHONE = "PHONE"
    TIER = "TIER"
    UNKNOWN = "UNKNOWN"


class whatsappbusinessaccountpricing_analytics_pricing_types_enum_param(str, Enum):
    """whatsappbusinessaccountpricing_analytics_pricing_types_enum_param enum values."""

    FREE_CUSTOMER_SERVICE = "FREE_CUSTOMER_SERVICE"
    FREE_ENTRY_POINT = "FREE_ENTRY_POINT"
    REGULAR = "REGULAR"


class whatsappbusinessaccountmessage_templates_quality_score_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_templates_quality_score_enum_param enum values."""

    GREEN = "GREEN"
    RED = "RED"
    UNKNOWN = "UNKNOWN"
    YELLOW = "YELLOW"


class whatsappbusinessaccountcall_analytics_metric_types_enum_param(str, Enum):
    """whatsappbusinessaccountcall_analytics_metric_types_enum_param enum values."""

    AVERAGE_DURATION = "AVERAGE_DURATION"
    COST = "COST"
    COUNT = "COUNT"
    UNKNOWN = "UNKNOWN"


class whatsappbusinessaccountconversation_analytics_granularity_enum_param(str, Enum):
    """whatsappbusinessaccountconversation_analytics_granularity_enum_param enum values."""

    DAILY = "DAILY"
    HALF_HOUR = "HALF_HOUR"
    MONTHLY = "MONTHLY"


class whatsappbusinessaccountmessage_templates_status_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_templates_status_enum_param enum values."""

    APPROVED = "APPROVED"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    DISABLED = "DISABLED"
    IN_APPEAL = "IN_APPEAL"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"
    PAUSED = "PAUSED"
    PENDING = "PENDING"
    PENDING_DELETION = "PENDING_DELETION"
    REJECTED = "REJECTED"


class whatsappbusinessaccounttemplate_analytics_metric_types_enum_param(str, Enum):
    """whatsappbusinessaccounttemplate_analytics_metric_types_enum_param enum values."""

    CLICKED = "CLICKED"
    COST = "COST"
    DELIVERED = "DELIVERED"
    READ = "READ"
    REPLIED = "REPLIED"
    SENT = "SENT"


class whatsappbusinessaccountconversation_analytics_conversation_types_enum_param(str, Enum):
    """whatsappbusinessaccountconversation_analytics_conversation_types_enum_param enum values."""

    FREE_ENTRY_POINT = "FREE_ENTRY_POINT"
    FREE_TIER = "FREE_TIER"
    REGULAR = "REGULAR"
    UNKNOWN = "UNKNOWN"


class whatsappbusinessaccountflows_categories_enum_param(str, Enum):
    """whatsappbusinessaccountflows_categories_enum_param enum values."""

    APPOINTMENT_BOOKING = "APPOINTMENT_BOOKING"
    CONTACT_US = "CONTACT_US"
    CUSTOMER_SUPPORT = "CUSTOMER_SUPPORT"
    LEAD_GENERATION = "LEAD_GENERATION"
    OTHER = "OTHER"
    SHOPPING = "SHOPPING"
    SIGN_IN = "SIGN_IN"
    SIGN_UP = "SIGN_UP"
    SURVEY = "SURVEY"


class whatsappbusinessaccounttemplate_group_analytics_metric_types_enum_param(str, Enum):
    """whatsappbusinessaccounttemplate_group_analytics_metric_types_enum_param enum values."""

    CLICKED = "CLICKED"
    COST = "COST"
    DELIVERED = "DELIVERED"
    READ = "READ"
    REPLIED = "REPLIED"
    SENT = "SENT"


class whatsappbusinessaccountmessage_templates_category_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_templates_category_enum_param enum values."""

    AUTHENTICATION = "AUTHENTICATION"
    MARKETING = "MARKETING"
    UTILITY = "UTILITY"


class whatsappbusinessaccountmessage_templates_parameter_format_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_templates_parameter_format_enum_param enum values."""

    NAMED = "NAMED"
    POSITIONAL = "POSITIONAL"


class whatsappbusinessaccountassigned_users_tasks_enum_param(str, Enum):
    """whatsappbusinessaccountassigned_users_tasks_enum_param enum values."""

    DEVELOP = "DEVELOP"
    MANAGE = "MANAGE"
    MANAGE_EXTENSIONS = "MANAGE_EXTENSIONS"
    MANAGE_PHONE = "MANAGE_PHONE"
    MANAGE_PHONE_ASSETS = "MANAGE_PHONE_ASSETS"
    MANAGE_TEMPLATES = "MANAGE_TEMPLATES"
    MESSAGING = "MESSAGING"
    VIEW_COST = "VIEW_COST"
    VIEW_PHONE_ASSETS = "VIEW_PHONE_ASSETS"
    VIEW_TEMPLATES = "VIEW_TEMPLATES"


class whatsappbusinessaccounttemplate_analytics_granularity_enum_param(str, Enum):
    """whatsappbusinessaccounttemplate_analytics_granularity_enum_param enum values."""

    DAILY = "DAILY"


class whatsappbusinessaccountpricing_analytics_metric_types_enum_param(str, Enum):
    """whatsappbusinessaccountpricing_analytics_metric_types_enum_param enum values."""

    COST = "COST"
    VOLUME = "VOLUME"


class whatsappbusinessaccounttemplate_group_analytics_granularity_enum_param(str, Enum):
    """whatsappbusinessaccounttemplate_group_analytics_granularity_enum_param enum values."""

    DAILY = "DAILY"


class whatsappbusinessaccountupsert_message_templates_category_enum_param(str, Enum):
    """whatsappbusinessaccountupsert_message_templates_category_enum_param enum values."""

    AUTHENTICATION = "AUTHENTICATION"


class whatsappbusinessaccountmessage_templates_sub_category_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_templates_sub_category_enum_param enum values."""

    ORDER_DETAILS = "ORDER_DETAILS"
    ORDER_STATUS = "ORDER_STATUS"


class whatsappbusinessaccountpayment_configuration_provider_name_enum_param(str, Enum):
    """whatsappbusinessaccountpayment_configuration_provider_name_enum_param enum values."""

    BILLDESK = "BILLDESK"
    PAYU = "PAYU"
    RAZORPAY = "RAZORPAY"
    UPI_VPA = "UPI_VPA"
    ZAAKPAY = "ZAAKPAY"


class whatsappbusinessaccountpricing_analytics_pricing_categories_enum_param(str, Enum):
    """whatsappbusinessaccountpricing_analytics_pricing_categories_enum_param enum values."""

    AUTHENTICATION = "AUTHENTICATION"
    AUTHENTICATION_INTERNATIONAL = "AUTHENTICATION_INTERNATIONAL"
    GROUP_MARKETING = "GROUP_MARKETING"
    GROUP_SERVICE = "GROUP_SERVICE"
    GROUP_UTILITY = "GROUP_UTILITY"
    MARKETING = "MARKETING"
    MARKETING_LITE = "MARKETING_LITE"
    SERVICE = "SERVICE"
    UTILITY = "UTILITY"


class whatsappbusinessaccountcall_analytics_directions_enum_param(str, Enum):
    """whatsappbusinessaccountcall_analytics_directions_enum_param enum values."""

    BUSINESS_INITIATED = "BUSINESS_INITIATED"
    UNKNOWN = "UNKNOWN"
    USER_INITIATED = "USER_INITIATED"


class whatsappbusinessaccountconversation_analytics_dimensions_enum_param(str, Enum):
    """whatsappbusinessaccountconversation_analytics_dimensions_enum_param enum values."""

    CONVERSATION_CATEGORY = "CONVERSATION_CATEGORY"
    CONVERSATION_DIRECTION = "CONVERSATION_DIRECTION"
    CONVERSATION_TYPE = "CONVERSATION_TYPE"
    COUNTRY = "COUNTRY"
    PHONE = "PHONE"
    UNKNOWN = "UNKNOWN"


class whatsappbusinessaccountconversation_analytics_metric_types_enum_param(str, Enum):
    """whatsappbusinessaccountconversation_analytics_metric_types_enum_param enum values."""

    CONVERSATION = "CONVERSATION"
    COST = "COST"
    UNKNOWN = "UNKNOWN"


class whatsappbusinessaccountconversation_analytics_conversation_categories_enum_param(str, Enum):
    """whatsappbusinessaccountconversation_analytics_conversation_categories_enum_param enum values."""

    AUTHENTICATION = "AUTHENTICATION"
    AUTHENTICATION_INTERNATIONAL = "AUTHENTICATION_INTERNATIONAL"
    MARKETING = "MARKETING"
    MARKETING_LITE = "MARKETING_LITE"
    SERVICE = "SERVICE"
    UTILITY = "UTILITY"


class whatsappbusinessaccountconversation_analytics_conversation_directions_enum_param(str, Enum):
    """whatsappbusinessaccountconversation_analytics_conversation_directions_enum_param enum values."""

    BUSINESS_INITIATED = "BUSINESS_INITIATED"
    UNKNOWN = "UNKNOWN"
    USER_INITIATED = "USER_INITIATED"


class whatsappbusinessaccountmessage_template_previews_button_types_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_template_previews_button_types_enum_param enum values."""

    OTP = "OTP"


class whatsappbusinessaccountmessage_template_previews_category_enum_param(str, Enum):
    """whatsappbusinessaccountmessage_template_previews_category_enum_param enum values."""

    AUTHENTICATION = "AUTHENTICATION"


class whatsappbusinessaccounttemplate_analytics_product_type_enum_param(str, Enum):
    """whatsappbusinessaccounttemplate_analytics_product_type_enum_param enum values."""

    CLOUD_API = "CLOUD_API"
    MARKETING_MESSAGES_LITE_API = "MARKETING_MESSAGES_LITE_API"


class whatsappbusinessaccountpricing_analytics_granularity_enum_param(str, Enum):
    """whatsappbusinessaccountpricing_analytics_granularity_enum_param enum values."""

    DAILY = "DAILY"
    HALF_HOUR = "HALF_HOUR"
    MONTHLY = "MONTHLY"


# Field literal type
WhatsAppBusinessAccountField = Literal[
    "account_review_status",
    "analytics",
    "auth_international_rate_eligibility",
    "business_verification_status",
    "country",
    "creation_time",
    "currency",
    "health_status",
    "id",
    "is_enabled_for_insights",
    "is_shared_with_partners",
    "linked_commerce_account",
    "marketing_messages_lite_api_status",
    "message_template_namespace",
    "name",
    "on_behalf_of_business_info",
    "owner_business",
    "owner_business_info",
    "ownership_type",
    "primary_business_location",
    "primary_funding_id",
    "purchase_order_number",
    "status",
    "timezone_id",
]


class WhatsAppBusinessAccountFields(BaseModel):
    """Pydantic model for WhatsAppBusinessAccount fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_review_status: str = Field(None, alias="account_review_status")
    analytics: dict[str, Any] = Field(None, alias="analytics")
    auth_international_rate_eligibility: dict[str, Any] = Field(
        None, alias="auth_international_rate_eligibility"
    )
    business_verification_status: dict[str, Any] = Field(None, alias="business_verification_status")
    country: str = Field(None, alias="country")
    creation_time: int = Field(None, alias="creation_time")
    currency: str = Field(None, alias="currency")
    health_status: WhatsAppBusinessHealthStatusForMessageSendFields = Field(
        None, alias="health_status"
    )
    id: str = Field(None, alias="id")
    is_enabled_for_insights: bool = Field(None, alias="is_enabled_for_insights")
    is_shared_with_partners: bool = Field(None, alias="is_shared_with_partners")
    linked_commerce_account: CommerceMerchantSettingsFields = Field(
        None, alias="linked_commerce_account"
    )
    marketing_messages_lite_api_status: str = Field(
        None, alias="marketing_messages_lite_api_status"
    )
    message_template_namespace: str = Field(None, alias="message_template_namespace")
    name: str = Field(None, alias="name")
    on_behalf_of_business_info: dict[str, Any] = Field(None, alias="on_behalf_of_business_info")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    owner_business_info: dict[str, Any] = Field(None, alias="owner_business_info")
    ownership_type: str = Field(None, alias="ownership_type")
    primary_business_location: str = Field(None, alias="primary_business_location")
    primary_funding_id: str = Field(None, alias="primary_funding_id")
    purchase_order_number: str = Field(None, alias="purchase_order_number")
    status: str = Field(None, alias="status")
    timezone_id: str = Field(None, alias="timezone_id")


class WhatsAppBusinessAccountDeleteAssignedUsersParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.delete_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    user: int | None = Field(None, description="user parameter")


class WhatsAppBusinessAccountGetAssignedUsersParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class WhatsAppBusinessAccountCreateAssignedUserParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_assigned_user()."""

    model_config = ConfigDict(extra="forbid")
    tasks: list[whatsappbusinessaccountassigned_users_tasks_enum_param] | None = Field(
        None, description="tasks parameter"
    )
    user: int | None = Field(None, description="user parameter")


class WhatsAppBusinessAccountGetCallAnalyticsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_call_analytics()."""

    model_config = ConfigDict(extra="forbid")
    country_codes: list[str] | None = Field(None, description="country_codes parameter")
    dimensions: list[whatsappbusinessaccountcall_analytics_dimensions_enum_param] | None = Field(
        None, description="dimensions parameter"
    )
    directions: list[whatsappbusinessaccountcall_analytics_directions_enum_param] | None = Field(
        None, description="directions parameter"
    )
    end: int | None = Field(None, description="end parameter")
    granularity: whatsappbusinessaccountcall_analytics_granularity_enum_param | None = Field(
        None, description="granularity parameter"
    )
    metric_types: list[whatsappbusinessaccountcall_analytics_metric_types_enum_param] | None = (
        Field(None, description="metric_types parameter")
    )
    phone_numbers: list[str] | None = Field(None, description="phone_numbers parameter")
    start: int | None = Field(None, description="start parameter")


class WhatsAppBusinessAccountGetConversationAnalyticsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_conversation_analytics()."""

    model_config = ConfigDict(extra="forbid")
    conversation_categories: (
        list[whatsappbusinessaccountconversation_analytics_conversation_categories_enum_param]
        | None
    ) = Field(None, description="conversation_categories parameter")
    conversation_directions: (
        list[whatsappbusinessaccountconversation_analytics_conversation_directions_enum_param]
        | None
    ) = Field(None, description="conversation_directions parameter")
    conversation_types: (
        list[whatsappbusinessaccountconversation_analytics_conversation_types_enum_param] | None
    ) = Field(None, description="conversation_types parameter")
    country_codes: list[str] | None = Field(None, description="country_codes parameter")
    dimensions: list[whatsappbusinessaccountconversation_analytics_dimensions_enum_param] | None = (
        Field(None, description="dimensions parameter")
    )
    end: int | None = Field(None, description="end parameter")
    granularity: whatsappbusinessaccountconversation_analytics_granularity_enum_param | None = (
        Field(None, description="granularity parameter")
    )
    metric_types: (
        list[whatsappbusinessaccountconversation_analytics_metric_types_enum_param] | None
    ) = Field(None, description="metric_types parameter")
    phone_numbers: list[str] | None = Field(None, description="phone_numbers parameter")
    start: int | None = Field(None, description="start parameter")


class WhatsAppBusinessAccountCreateDatasetParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_dataset()."""

    model_config = ConfigDict(extra="forbid")
    dataset_name: str | None = Field(None, description="dataset_name parameter")


class WhatsAppBusinessAccountCreateFlowParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_flow()."""

    model_config = ConfigDict(extra="forbid")
    categories: list[whatsappbusinessaccountflows_categories_enum_param] | None = Field(
        None, description="categories parameter"
    )
    clone_flow_id: str | None = Field(None, description="clone_flow_id parameter")
    endpoint_uri: str | None = Field(None, description="endpoint_uri parameter")
    flow_json: str | None = Field(None, description="flow_json parameter")
    name: str | None = Field(None, description="name parameter")
    publish: bool | None = Field(None, description="publish parameter")


class WhatsAppBusinessAccountCreateGeneratePaymentConfigurationOauthLinkParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_generate_payment_configuration_oauth_link()."""

    model_config = ConfigDict(extra="forbid")
    configuration_name: str | None = Field(None, description="configuration_name parameter")
    redirect_url: str | None = Field(None, description="redirect_url parameter")


class WhatsAppBusinessAccountGetMessageTemplatePreviewsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_message_template_previews()."""

    model_config = ConfigDict(extra="forbid")
    add_security_recommendation: bool | None = Field(
        None, description="add_security_recommendation parameter"
    )
    button_types: (
        list[whatsappbusinessaccountmessage_template_previews_button_types_enum_param] | None
    ) = Field(None, description="button_types parameter")
    category: whatsappbusinessaccountmessage_template_previews_category_enum_param | None = Field(
        None, description="category parameter"
    )
    code_expiration_minutes: int | None = Field(
        None, description="code_expiration_minutes parameter"
    )
    languages: list[str] | None = Field(None, description="languages parameter")


class WhatsAppBusinessAccountDeleteMessageTemplatesParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.delete_message_templates()."""

    model_config = ConfigDict(extra="forbid")
    hsm_id: str | None = Field(None, description="hsm_id parameter")
    name: str | None = Field(None, description="name parameter")


class WhatsAppBusinessAccountGetMessageTemplatesParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_message_templates()."""

    model_config = ConfigDict(extra="forbid")
    category: list[whatsappbusinessaccountmessage_templates_category_enum_param] | None = Field(
        None, description="category parameter"
    )
    content: str | None = Field(None, description="content parameter")
    language: list[str] | None = Field(None, description="language parameter")
    name: str | None = Field(None, description="name parameter")
    name_or_content: str | None = Field(None, description="name_or_content parameter")
    quality_score: (
        list[whatsappbusinessaccountmessage_templates_quality_score_enum_param] | None
    ) = Field(None, description="quality_score parameter")
    status: list[whatsappbusinessaccountmessage_templates_status_enum_param] | None = Field(
        None, description="status parameter"
    )


class WhatsAppBusinessAccountCreateMessageTemplateParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_message_template()."""

    model_config = ConfigDict(extra="forbid")
    allow_category_change: bool | None = Field(None, description="allow_category_change parameter")
    category: whatsappbusinessaccountmessage_templates_category_enum_param | None = Field(
        None, description="category parameter"
    )
    components: list[dict[str, Any]] | None = Field(None, description="components parameter")
    cta_url_link_tracking_opted_out: bool | None = Field(
        None, description="cta_url_link_tracking_opted_out parameter"
    )
    degrees_of_freedom_spec: dict[str, Any] | None = Field(
        None, description="degrees_of_freedom_spec parameter"
    )
    display_format: whatsappbusinessaccountmessage_templates_display_format_enum_param | None = (
        Field(None, description="display_format parameter")
    )
    language: str | None = Field(None, description="language parameter")
    library_template_body_inputs: dict[str, Any] | None = Field(
        None, description="library_template_body_inputs parameter"
    )
    library_template_button_inputs: list[dict[str, Any]] | None = Field(
        None, description="library_template_button_inputs parameter"
    )
    library_template_name: str | None = Field(None, description="library_template_name parameter")
    message_send_ttl_seconds: int | None = Field(
        None, description="message_send_ttl_seconds parameter"
    )
    name: str | None = Field(None, description="name parameter")
    parameter_format: (
        whatsappbusinessaccountmessage_templates_parameter_format_enum_param | None
    ) = Field(None, description="parameter_format parameter")
    sub_category: whatsappbusinessaccountmessage_templates_sub_category_enum_param | None = Field(
        None, description="sub_category parameter"
    )


class WhatsAppBusinessAccountCreateMigrateFlowParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_migrate_flow()."""

    model_config = ConfigDict(extra="forbid")
    source_flow_names: list[str] | None = Field(None, description="source_flow_names parameter")
    source_waba_id: str | None = Field(None, description="source_waba_id parameter")


class WhatsAppBusinessAccountCreateMigrateMessageTemplateParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_migrate_message_template()."""

    model_config = ConfigDict(extra="forbid")
    page_number: int | None = Field(None, description="page_number parameter")
    source_waba_id: str | None = Field(None, description="source_waba_id parameter")


class WhatsAppBusinessAccountDeletePaymentConfigurationParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.delete_payment_configuration()."""

    model_config = ConfigDict(extra="forbid")
    configuration_name: str | None = Field(None, description="configuration_name parameter")


class WhatsAppBusinessAccountGetPaymentConfigurationParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_payment_configuration()."""

    model_config = ConfigDict(extra="forbid")
    configuration_name: str | None = Field(None, description="configuration_name parameter")


class WhatsAppBusinessAccountCreatePaymentConfigurationParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_payment_configuration()."""

    model_config = ConfigDict(extra="forbid")
    configuration_name: str | None = Field(None, description="configuration_name parameter")
    data_endpoint_url: str | None = Field(None, description="data_endpoint_url parameter")
    merchant_category_code: str | None = Field(None, description="merchant_category_code parameter")
    merchant_vpa: str | None = Field(None, description="merchant_vpa parameter")
    provider_name: whatsappbusinessaccountpayment_configuration_provider_name_enum_param | None = (
        Field(None, description="provider_name parameter")
    )
    purpose_code: str | None = Field(None, description="purpose_code parameter")
    redirect_url: str | None = Field(None, description="redirect_url parameter")


class WhatsAppBusinessAccountCreatePhoneNumberParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_phone_number()."""

    model_config = ConfigDict(extra="forbid")
    cc: str | None = Field(None, description="cc parameter")
    migrate_phone_number: bool | None = Field(None, description="migrate_phone_number parameter")
    phone_number: str | None = Field(None, description="phone_number parameter")
    preverified_id: str | None = Field(None, description="preverified_id parameter")
    verified_name: str | None = Field(None, description="verified_name parameter")


class WhatsAppBusinessAccountGetPricingAnalyticsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_pricing_analytics()."""

    model_config = ConfigDict(extra="forbid")
    country_codes: list[str] | None = Field(None, description="country_codes parameter")
    dimensions: list[whatsappbusinessaccountpricing_analytics_dimensions_enum_param] | None = Field(
        None, description="dimensions parameter"
    )
    end: int | None = Field(None, description="end parameter")
    granularity: whatsappbusinessaccountpricing_analytics_granularity_enum_param | None = Field(
        None, description="granularity parameter"
    )
    metric_types: list[whatsappbusinessaccountpricing_analytics_metric_types_enum_param] | None = (
        Field(None, description="metric_types parameter")
    )
    phone_numbers: list[str] | None = Field(None, description="phone_numbers parameter")
    pricing_categories: (
        list[whatsappbusinessaccountpricing_analytics_pricing_categories_enum_param] | None
    ) = Field(None, description="pricing_categories parameter")
    pricing_types: (
        list[whatsappbusinessaccountpricing_analytics_pricing_types_enum_param] | None
    ) = Field(None, description="pricing_types parameter")
    start: int | None = Field(None, description="start parameter")
    tiers: list[str] | None = Field(None, description="tiers parameter")


class WhatsAppBusinessAccountDeleteProductCatalogsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.delete_product_catalogs()."""

    model_config = ConfigDict(extra="forbid")
    catalog_id: str | None = Field(None, description="catalog_id parameter")


class WhatsAppBusinessAccountCreateProductCatalogParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_product_catalog()."""

    model_config = ConfigDict(extra="forbid")
    catalog_id: str | None = Field(None, description="catalog_id parameter")


class WhatsAppBusinessAccountCreateSetOboMobilityIntentParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_set_obo_mobility_intent()."""

    model_config = ConfigDict(extra="forbid")
    solution_id: str | None = Field(None, description="solution_id parameter")


class WhatsAppBusinessAccountCreateSetSolutionMigrationIntentParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_set_solution_migration_intent()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")
    solution_id: str | None = Field(None, description="solution_id parameter")


class WhatsAppBusinessAccountCreateSubscribedAppParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_subscribed_app()."""

    model_config = ConfigDict(extra="forbid")
    override_callback_uri: str | None = Field(None, description="override_callback_uri parameter")
    verify_token: str | None = Field(None, description="verify_token parameter")


class WhatsAppBusinessAccountGetTemplateAnalyticsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_template_analytics()."""

    model_config = ConfigDict(extra="forbid")
    end: datetime | None = Field(None, description="end parameter")
    granularity: whatsappbusinessaccounttemplate_analytics_granularity_enum_param | None = Field(
        None, description="granularity parameter"
    )
    metric_types: list[whatsappbusinessaccounttemplate_analytics_metric_types_enum_param] | None = (
        Field(None, description="metric_types parameter")
    )
    product_type: whatsappbusinessaccounttemplate_analytics_product_type_enum_param | None = Field(
        None, description="product_type parameter"
    )
    start: datetime | None = Field(None, description="start parameter")
    template_ids: list[str] | None = Field(None, description="template_ids parameter")


class WhatsAppBusinessAccountGetTemplateGroupAnalyticsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_template_group_analytics()."""

    model_config = ConfigDict(extra="forbid")
    end: datetime | None = Field(None, description="end parameter")
    granularity: whatsappbusinessaccounttemplate_group_analytics_granularity_enum_param | None = (
        Field(None, description="granularity parameter")
    )
    metric_types: (
        list[whatsappbusinessaccounttemplate_group_analytics_metric_types_enum_param] | None
    ) = Field(None, description="metric_types parameter")
    start: datetime | None = Field(None, description="start parameter")
    template_group_ids: list[str] | None = Field(None, description="template_group_ids parameter")


class WhatsAppBusinessAccountCreateTemplateGroupParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_template_group()."""

    model_config = ConfigDict(extra="forbid")
    description: str | None = Field(None, description="description parameter")
    name: str | None = Field(None, description="name parameter")
    whatsapp_business_templates: list[str] | None = Field(
        None, description="whatsapp_business_templates parameter"
    )


class WhatsAppBusinessAccountGetTemplatePerformanceMetricsParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_template_performance_metrics()."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = Field(None, description="name parameter")
    template_id: str | None = Field(None, description="template_id parameter")


class WhatsAppBusinessAccountCreateUpsertMessageTemplateParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.create_upsert_message_template()."""

    model_config = ConfigDict(extra="forbid")
    category: whatsappbusinessaccountupsert_message_templates_category_enum_param | None = Field(
        None, description="category parameter"
    )
    components: list[dict[str, Any]] | None = Field(None, description="components parameter")
    languages: list[str] | None = Field(None, description="languages parameter")
    message_send_ttl_seconds: int | None = Field(
        None, description="message_send_ttl_seconds parameter"
    )
    name: str | None = Field(None, description="name parameter")


class WhatsAppBusinessAccountGetWelcomeMessageSequencesParams(BaseModel):
    """Parameters for WhatsAppBusinessAccount.get_welcome_message_sequences()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")
    sequence_id: str | None = Field(None, description="sequence_id parameter")
