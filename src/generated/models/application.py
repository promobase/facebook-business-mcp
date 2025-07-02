"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


class applicationcodeless_event_mappings_mutation_method_enum_param(str, Enum):
    """applicationcodeless_event_mappings_mutation_method_enum_param enum values."""

    ADD = "ADD"
    DELETE = "DELETE"
    REPLACE = "REPLACE"


class applicationpermissions_status_enum_param(str, Enum):
    """applicationpermissions_status_enum_param enum values."""

    live = "live"
    unapproved = "unapproved"


class applicationwhatsapp_business_solution_owner_permissions_enum_param(str, Enum):
    """applicationwhatsapp_business_solution_owner_permissions_enum_param enum values."""

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


class applicationda_checks_connection_method_enum_param(str, Enum):
    """applicationda_checks_connection_method_enum_param enum values."""

    ALL = "ALL"
    APP = "APP"
    BROWSER = "BROWSER"
    SERVER = "SERVER"


class applicationadnetworkanalytics_metrics_enum_param(str, Enum):
    """applicationadnetworkanalytics_metrics_enum_param enum values."""

    FB_AD_NETWORK_BIDDING_BID_RATE = "FB_AD_NETWORK_BIDDING_BID_RATE"
    FB_AD_NETWORK_BIDDING_REQUEST = "FB_AD_NETWORK_BIDDING_REQUEST"
    FB_AD_NETWORK_BIDDING_RESPONSE = "FB_AD_NETWORK_BIDDING_RESPONSE"
    FB_AD_NETWORK_BIDDING_REVENUE = "FB_AD_NETWORK_BIDDING_REVENUE"
    FB_AD_NETWORK_BIDDING_WIN_RATE = "FB_AD_NETWORK_BIDDING_WIN_RATE"
    FB_AD_NETWORK_CLICK = "FB_AD_NETWORK_CLICK"
    FB_AD_NETWORK_CPM = "FB_AD_NETWORK_CPM"
    FB_AD_NETWORK_CTR = "FB_AD_NETWORK_CTR"
    FB_AD_NETWORK_FILLED_REQUEST = "FB_AD_NETWORK_FILLED_REQUEST"
    FB_AD_NETWORK_FILL_RATE = "FB_AD_NETWORK_FILL_RATE"
    FB_AD_NETWORK_IMP = "FB_AD_NETWORK_IMP"
    FB_AD_NETWORK_IMPRESSION_RATE = "FB_AD_NETWORK_IMPRESSION_RATE"
    FB_AD_NETWORK_REQUEST = "FB_AD_NETWORK_REQUEST"
    FB_AD_NETWORK_REVENUE = "FB_AD_NETWORK_REVENUE"
    FB_AD_NETWORK_SHOW_RATE = "FB_AD_NETWORK_SHOW_RATE"
    FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE = "FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE"
    FB_AD_NETWORK_VIDEO_MRC = "FB_AD_NETWORK_VIDEO_MRC"
    FB_AD_NETWORK_VIDEO_MRC_RATE = "FB_AD_NETWORK_VIDEO_MRC_RATE"
    FB_AD_NETWORK_VIDEO_VIEW = "FB_AD_NETWORK_VIDEO_VIEW"
    FB_AD_NETWORK_VIDEO_VIEW_RATE = "FB_AD_NETWORK_VIDEO_VIEW_RATE"


class applicationadnetworkanalytics_ordering_type_enum_param(str, Enum):
    """applicationadnetworkanalytics_ordering_type_enum_param enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class applicationapp_indexing_platform_enum_param(str, Enum):
    """applicationapp_indexing_platform_enum_param enum values."""

    ANDROID = "ANDROID"
    IOS = "IOS"


class applicationmobile_sdk_gk_platform_enum_param(str, Enum):
    """applicationmobile_sdk_gk_platform_enum_param enum values."""

    ANDROID = "ANDROID"
    IOS = "IOS"


class applicationwhatsapp_business_solutions_role_enum_param(str, Enum):
    """applicationwhatsapp_business_solutions_role_enum_param enum values."""

    OWNER = "OWNER"
    PARTNER = "PARTNER"


class applicationcodeless_event_mappings_post_method_enum_param(str, Enum):
    """applicationcodeless_event_mappings_post_method_enum_param enum values."""

    CODELESS = "CODELESS"
    EYMT = "EYMT"


class applicationadnetworkanalytics_breakdowns_enum_param(str, Enum):
    """applicationadnetworkanalytics_breakdowns_enum_param enum values."""

    AD_SERVER_CAMPAIGN_ID = "AD_SERVER_CAMPAIGN_ID"
    AD_SPACE = "AD_SPACE"
    AGE = "AGE"
    APP = "APP"
    CLICKED_VIEW_TAG = "CLICKED_VIEW_TAG"
    COUNTRY = "COUNTRY"
    DEAL = "DEAL"
    DEAL_AD = "DEAL_AD"
    DEAL_PAGE = "DEAL_PAGE"
    DELIVERY_METHOD = "DELIVERY_METHOD"
    DISPLAY_FORMAT = "DISPLAY_FORMAT"
    FAIL_REASON = "FAIL_REASON"
    GENDER = "GENDER"
    INSTANT_ARTICLE_ID = "INSTANT_ARTICLE_ID"
    INSTANT_ARTICLE_PAGE_ID = "INSTANT_ARTICLE_PAGE_ID"
    IS_DEAL_BACKFILL = "IS_DEAL_BACKFILL"
    PLACEMENT = "PLACEMENT"
    PLACEMENT_NAME = "PLACEMENT_NAME"
    PLATFORM = "PLATFORM"
    PROPERTY = "PROPERTY"
    SDK_VERSION = "SDK_VERSION"


class applicationapp_indexing_request_type_enum_param(str, Enum):
    """applicationapp_indexing_request_type_enum_param enum values."""

    APP_INDEXING = "APP_INDEXING"
    BUTTON_SAMPLING = "BUTTON_SAMPLING"
    PLUGIN = "PLUGIN"


class applicationaccounts_type_enum_param(str, Enum):
    """applicationaccounts_type_enum_param enum values."""

    TEST_USERS = "test-users"


class applicationwhatsapp_business_solution_partner_permissions_enum_param(str, Enum):
    """applicationwhatsapp_business_solution_partner_permissions_enum_param enum values."""

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


class applicationadnetworkanalytics_ordering_column_enum_param(str, Enum):
    """applicationadnetworkanalytics_ordering_column_enum_param enum values."""

    METRIC = "METRIC"
    TIME = "TIME"
    VALUE = "VALUE"


class applicationactivities_user_id_type_enum_param(str, Enum):
    """applicationactivities_user_id_type_enum_param enum values."""

    INSTANT_GAMES_PLAYER_ID = "INSTANT_GAMES_PLAYER_ID"


class applicationapp_push_device_token_platform_enum_param(str, Enum):
    """applicationapp_push_device_token_platform_enum_param enum values."""

    ANDROID = "ANDROID"
    IOS = "IOS"
    UNKNOWN = "UNKNOWN"


class applicationadnetworkanalytics_aggregation_period_enum_param(str, Enum):
    """applicationadnetworkanalytics_aggregation_period_enum_param enum values."""

    DAY = "DAY"
    TOTAL = "TOTAL"


class applicationuploads_session_type_enum_param(str, Enum):
    """applicationuploads_session_type_enum_param enum values."""

    attachment = "attachment"


class applicationcodeless_event_mappings_platform_enum_param(str, Enum):
    """applicationcodeless_event_mappings_platform_enum_param enum values."""

    ANDROID = "ANDROID"
    IOS = "IOS"


class applicationactivities_event_enum_param(str, Enum):
    """applicationactivities_event_enum_param enum values."""

    CUSTOM_APP_EVENTS = "CUSTOM_APP_EVENTS"
    DEFERRED_APP_LINK = "DEFERRED_APP_LINK"
    MOBILE_APP_INSTALL = "MOBILE_APP_INSTALL"


# Field literal type
ApplicationField = Literal[
    "aam_rules",
    "an_ad_space_limit",
    "an_platforms",
    "android_key_hash",
    "android_sdk_error_categories",
    "app_domains",
    "app_events_config",
    "app_events_feature_bitmask",
    "app_events_session_timeout",
    "app_install_tracked",
    "app_name",
    "app_signals_binding_ios",
    "app_type",
    "auth_dialog_data_help_url",
    "auth_dialog_headline",
    "auth_dialog_perms_explanation",
    "auth_referral_default_activity_privacy",
    "auth_referral_enabled",
    "auth_referral_extended_perms",
    "auth_referral_friend_perms",
    "auth_referral_response_type",
    "auth_referral_user_perms",
    "auto_event_mapping_android",
    "auto_event_mapping_ios",
    "auto_event_setup_enabled",
    "auto_log_app_events_default",
    "auto_log_app_events_enabled",
    "business",
    "canvas_fluid_height",
    "canvas_fluid_width",
    "canvas_url",
    "category",
    "client_config",
    "company",
    "configured_ios_sso",
    "contact_email",
    "created_time",
    "creator_uid",
    "daily_active_users",
    "daily_active_users_rank",
    "deauth_callback_url",
    "default_share_mode",
    "description",
    "enigma_config",
    "financial_id",
    "gdpv4_chrome_custom_tabs_enabled",
    "gdpv4_enabled",
    "gdpv4_nux_content",
    "gdpv4_nux_enabled",
    "has_messenger_product",
    "hosting_url",
    "icon_url",
    "id",
    "ios_bundle_id",
    "ios_sdk_dialog_flows",
    "ios_sdk_error_categories",
    "ios_sfvc_attr",
    "ios_supports_native_proxy_auth_flow",
    "ios_supports_system_auth",
    "ipad_app_store_id",
    "iphone_app_store_id",
    "latest_sdk_version",
    "link",
    "logging_token",
    "logo_url",
    "migrations",
    "mobile_profile_section_url",
    "mobile_web_url",
    "monthly_active_users",
    "monthly_active_users_rank",
    "name",
    "namespace",
    "object_store_urls",
    "owner_business",
    "page_tab_default_name",
    "page_tab_url",
    "photo_url",
    "privacy_policy_url",
    "profile_section_url",
    "property_id",
    "protected_mode_rules",
    "real_time_mode_devices",
    "restrictions",
    "restrictive_data_filter_params",
    "restrictive_data_filter_rules",
    "sdk_update_message",
    "seamless_login",
    "secure_canvas_url",
    "secure_page_tab_url",
    "server_ip_whitelist",
    "smart_login_bookmark_icon_url",
    "smart_login_menu_icon_url",
    "social_discovery",
    "subcategory",
    "suggested_events_setting",
    "supported_platforms",
    "supports_apprequests_fast_app_switch",
    "supports_attribution",
    "supports_implicit_sdk_logging",
    "suppress_native_ios_gdp",
    "terms_of_service_url",
    "url_scheme_suffix",
    "user_support_email",
    "user_support_url",
    "website_url",
    "weekly_active_users",
]


class ApplicationFields(BaseModel):
    """Pydantic model for Application fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    aam_rules: str = Field(None, alias="aam_rules")
    an_ad_space_limit: int = Field(None, alias="an_ad_space_limit")
    an_platforms: list[str] = Field(None, alias="an_platforms")
    android_key_hash: list[str] = Field(None, alias="android_key_hash")
    android_sdk_error_categories: list[dict[str, Any]] = Field(
        None, alias="android_sdk_error_categories"
    )
    app_domains: list[str] = Field(None, alias="app_domains")
    app_events_config: dict[str, Any] = Field(None, alias="app_events_config")
    app_events_feature_bitmask: int = Field(None, alias="app_events_feature_bitmask")
    app_events_session_timeout: int = Field(None, alias="app_events_session_timeout")
    app_install_tracked: bool = Field(None, alias="app_install_tracked")
    app_name: str = Field(None, alias="app_name")
    app_signals_binding_ios: list[dict[str, Any]] = Field(None, alias="app_signals_binding_ios")
    app_type: int = Field(None, alias="app_type")
    auth_dialog_data_help_url: str = Field(None, alias="auth_dialog_data_help_url")
    auth_dialog_headline: str = Field(None, alias="auth_dialog_headline")
    auth_dialog_perms_explanation: str = Field(None, alias="auth_dialog_perms_explanation")
    auth_referral_default_activity_privacy: str = Field(
        None, alias="auth_referral_default_activity_privacy"
    )
    auth_referral_enabled: int = Field(None, alias="auth_referral_enabled")
    auth_referral_extended_perms: list[str] = Field(None, alias="auth_referral_extended_perms")
    auth_referral_friend_perms: list[str] = Field(None, alias="auth_referral_friend_perms")
    auth_referral_response_type: str = Field(None, alias="auth_referral_response_type")
    auth_referral_user_perms: list[str] = Field(None, alias="auth_referral_user_perms")
    auto_event_mapping_android: list[dict[str, Any]] = Field(
        None, alias="auto_event_mapping_android"
    )
    auto_event_mapping_ios: list[dict[str, Any]] = Field(None, alias="auto_event_mapping_ios")
    auto_event_setup_enabled: bool = Field(None, alias="auto_event_setup_enabled")
    auto_log_app_events_default: bool = Field(None, alias="auto_log_app_events_default")
    auto_log_app_events_enabled: bool = Field(None, alias="auto_log_app_events_enabled")
    business: BusinessFields = Field(None, alias="business")
    canvas_fluid_height: bool = Field(None, alias="canvas_fluid_height")
    canvas_fluid_width: int = Field(None, alias="canvas_fluid_width")
    canvas_url: str = Field(None, alias="canvas_url")
    category: str = Field(None, alias="category")
    client_config: dict[str, Any] = Field(None, alias="client_config")
    company: str = Field(None, alias="company")
    configured_ios_sso: bool = Field(None, alias="configured_ios_sso")
    contact_email: str = Field(None, alias="contact_email")
    created_time: datetime = Field(None, alias="created_time")
    creator_uid: str = Field(None, alias="creator_uid")
    daily_active_users: str = Field(None, alias="daily_active_users")
    daily_active_users_rank: int = Field(None, alias="daily_active_users_rank")
    deauth_callback_url: str = Field(None, alias="deauth_callback_url")
    default_share_mode: str = Field(None, alias="default_share_mode")
    description: str = Field(None, alias="description")
    enigma_config: dict[str, Any] = Field(None, alias="enigma_config")
    financial_id: str = Field(None, alias="financial_id")
    gdpv4_chrome_custom_tabs_enabled: bool = Field(None, alias="gdpv4_chrome_custom_tabs_enabled")
    gdpv4_enabled: bool = Field(None, alias="gdpv4_enabled")
    gdpv4_nux_content: str = Field(None, alias="gdpv4_nux_content")
    gdpv4_nux_enabled: bool = Field(None, alias="gdpv4_nux_enabled")
    has_messenger_product: bool = Field(None, alias="has_messenger_product")
    hosting_url: str = Field(None, alias="hosting_url")
    icon_url: str = Field(None, alias="icon_url")
    id: str = Field(None, alias="id")
    ios_bundle_id: list[str] = Field(None, alias="ios_bundle_id")
    ios_sdk_dialog_flows: dict[str, Any] = Field(None, alias="ios_sdk_dialog_flows")
    ios_sdk_error_categories: list[dict[str, Any]] = Field(None, alias="ios_sdk_error_categories")
    ios_sfvc_attr: bool = Field(None, alias="ios_sfvc_attr")
    ios_supports_native_proxy_auth_flow: bool = Field(
        None, alias="ios_supports_native_proxy_auth_flow"
    )
    ios_supports_system_auth: bool = Field(None, alias="ios_supports_system_auth")
    ipad_app_store_id: str = Field(None, alias="ipad_app_store_id")
    iphone_app_store_id: str = Field(None, alias="iphone_app_store_id")
    latest_sdk_version: dict[str, Any] = Field(None, alias="latest_sdk_version")
    link: str = Field(None, alias="link")
    logging_token: str = Field(None, alias="logging_token")
    logo_url: str = Field(None, alias="logo_url")
    migrations: dict[str, bool] = Field(None, alias="migrations")
    mobile_profile_section_url: str = Field(None, alias="mobile_profile_section_url")
    mobile_web_url: str = Field(None, alias="mobile_web_url")
    monthly_active_users: str = Field(None, alias="monthly_active_users")
    monthly_active_users_rank: int = Field(None, alias="monthly_active_users_rank")
    name: str = Field(None, alias="name")
    namespace: str = Field(None, alias="namespace")
    object_store_urls: dict[str, Any] = Field(None, alias="object_store_urls")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    page_tab_default_name: str = Field(None, alias="page_tab_default_name")
    page_tab_url: str = Field(None, alias="page_tab_url")
    photo_url: str = Field(None, alias="photo_url")
    privacy_policy_url: str = Field(None, alias="privacy_policy_url")
    profile_section_url: str = Field(None, alias="profile_section_url")
    property_id: str = Field(None, alias="property_id")
    protected_mode_rules: dict[str, Any] = Field(None, alias="protected_mode_rules")
    real_time_mode_devices: list[str] = Field(None, alias="real_time_mode_devices")
    restrictions: dict[str, Any] = Field(None, alias="restrictions")
    restrictive_data_filter_params: str = Field(None, alias="restrictive_data_filter_params")
    restrictive_data_filter_rules: str = Field(None, alias="restrictive_data_filter_rules")
    sdk_update_message: str = Field(None, alias="sdk_update_message")
    seamless_login: int = Field(None, alias="seamless_login")
    secure_canvas_url: str = Field(None, alias="secure_canvas_url")
    secure_page_tab_url: str = Field(None, alias="secure_page_tab_url")
    server_ip_whitelist: str = Field(None, alias="server_ip_whitelist")
    smart_login_bookmark_icon_url: str = Field(None, alias="smart_login_bookmark_icon_url")
    smart_login_menu_icon_url: str = Field(None, alias="smart_login_menu_icon_url")
    social_discovery: int = Field(None, alias="social_discovery")
    subcategory: str = Field(None, alias="subcategory")
    suggested_events_setting: str = Field(None, alias="suggested_events_setting")
    supported_platforms: list[dict[str, Any]] = Field(None, alias="supported_platforms")
    supports_apprequests_fast_app_switch: dict[str, Any] = Field(
        None, alias="supports_apprequests_fast_app_switch"
    )
    supports_attribution: bool = Field(None, alias="supports_attribution")
    supports_implicit_sdk_logging: bool = Field(None, alias="supports_implicit_sdk_logging")
    suppress_native_ios_gdp: bool = Field(None, alias="suppress_native_ios_gdp")
    terms_of_service_url: str = Field(None, alias="terms_of_service_url")
    url_scheme_suffix: str = Field(None, alias="url_scheme_suffix")
    user_support_email: str = Field(None, alias="user_support_email")
    user_support_url: str = Field(None, alias="user_support_url")
    website_url: str = Field(None, alias="website_url")
    weekly_active_users: str = Field(None, alias="weekly_active_users")


class ApplicationDeleteAccountsParams(BaseModel):
    """Parameters for Application.delete_accounts()."""

    model_config = ConfigDict(extra="forbid")
    type: applicationaccounts_type_enum_param | None = Field(None, description="type parameter")
    uid: int | None = Field(None, description="uid parameter")


class ApplicationGetAccountsParams(BaseModel):
    """Parameters for Application.get_accounts()."""

    model_config = ConfigDict(extra="forbid")
    type: applicationaccounts_type_enum_param | None = Field(None, description="type parameter")


class ApplicationCreateAccountParams(BaseModel):
    """Parameters for Application.create_account()."""

    model_config = ConfigDict(extra="forbid")
    installed: bool | None = Field(None, description="installed parameter")
    minor: bool | None = Field(None, description="minor parameter")
    name: str | None = Field(None, description="name parameter")
    owner_access_token: str | None = Field(None, description="owner_access_token parameter")
    permissions: list[dict[str, Any]] | None = Field(None, description="permissions parameter")
    type: applicationaccounts_type_enum_param | None = Field(None, description="type parameter")
    uid: int | None = Field(None, description="uid parameter")


class ApplicationCreateActivitieParams(BaseModel):
    """Parameters for Application.create_activitie()."""

    model_config = ConfigDict(extra="forbid")
    advertiser_id: str | None = Field(None, description="advertiser_id parameter")
    advertiser_tracking_enabled: bool | None = Field(
        None, description="advertiser_tracking_enabled parameter"
    )
    anon_id: str | None = Field(None, description="anon_id parameter")
    app_user_id: str | None = Field(None, description="app_user_id parameter")
    application_tracking_enabled: bool | None = Field(
        None, description="application_tracking_enabled parameter"
    )
    attribution: str | None = Field(None, description="attribution parameter")
    attribution_referrer: str | None = Field(None, description="attribution_referrer parameter")
    attribution_sources: list[dict[str, Any]] | None = Field(
        None, description="attribution_sources parameter"
    )
    auto_publish: bool | None = Field(None, description="auto_publish parameter")
    bundle_id: str | None = Field(None, description="bundle_id parameter")
    bundle_short_version: str | None = Field(None, description="bundle_short_version parameter")
    bundle_version: str | None = Field(None, description="bundle_version parameter")
    campaign_ids: str | None = Field(None, description="campaign_ids parameter")
    click_id: str | None = Field(None, description="click_id parameter")
    consider_views: bool | None = Field(None, description="consider_views parameter")
    custom_events: list[dict[str, Any]] | None = Field(None, description="custom_events parameter")
    custom_events_file: dict[str, Any] | None = Field(
        None, description="custom_events_file parameter"
    )
    data_processing_options: list[str] | None = Field(
        None, description="data_processing_options parameter"
    )
    data_processing_options_country: int | None = Field(
        None, description="data_processing_options_country parameter"
    )
    data_processing_options_state: int | None = Field(
        None, description="data_processing_options_state parameter"
    )
    device_token: str | None = Field(None, description="device_token parameter")
    event: applicationactivities_event_enum_param | None = Field(
        None, description="event parameter"
    )
    event_id: str | None = Field(None, description="event_id parameter")
    extinfo: dict[str, Any] | None = Field(None, description="extinfo parameter")
    google_install_referrer: str | None = Field(
        None, description="google_install_referrer parameter"
    )
    include_dwell_data: bool | None = Field(None, description="include_dwell_data parameter")
    include_video_data: bool | None = Field(None, description="include_video_data parameter")
    install_id: str | None = Field(None, description="install_id parameter")
    install_referrer: str | None = Field(None, description="install_referrer parameter")
    install_timestamp: int | None = Field(None, description="install_timestamp parameter")
    installer_package: str | None = Field(None, description="installer_package parameter")
    is_fb: bool | None = Field(None, description="is_fb parameter")
    limited_data_use: bool | None = Field(None, description="limited_data_use parameter")
    meta_install_referrer: str | None = Field(None, description="meta_install_referrer parameter")
    migration_bundle: str | None = Field(None, description="migration_bundle parameter")
    operational_parameters: list[dict[str, Any]] | None = Field(
        None, description="operational_parameters parameter"
    )
    page_id: int | None = Field(None, description="page_id parameter")
    page_scoped_user_id: int | None = Field(None, description="page_scoped_user_id parameter")
    receipt_data: str | None = Field(None, description="receipt_data parameter")
    sdk_version: str | None = Field(None, description="sdk_version parameter")
    ud: dict[str, Any] | None = Field(None, description="ud parameter")
    url_schemes: list[str] | None = Field(None, description="url_schemes parameter")
    user_id: str | None = Field(None, description="user_id parameter")
    user_id_type: applicationactivities_user_id_type_enum_param | None = Field(
        None, description="user_id_type parameter"
    )
    vendor_id: str | None = Field(None, description="vendor_id parameter")
    windows_attribution_id: str | None = Field(None, description="windows_attribution_id parameter")


class ApplicationGetAdnetworkPlacementsParams(BaseModel):
    """Parameters for Application.get_adnetwork_placements()."""

    model_config = ConfigDict(extra="forbid")
    request_id: str | None = Field(None, description="request_id parameter")


class ApplicationGetAdNetworkanalyticsParams(BaseModel):
    """Parameters for Application.get_ad_networkanalytics()."""

    model_config = ConfigDict(extra="forbid")
    aggregation_period: applicationadnetworkanalytics_aggregation_period_enum_param | None = Field(
        None, description="aggregation_period parameter"
    )
    breakdowns: list[applicationadnetworkanalytics_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    filters: list[dict[str, Any]] | None = Field(None, description="filters parameter")
    limit: int | None = Field(None, description="limit parameter")
    metrics: list[applicationadnetworkanalytics_metrics_enum_param] | None = Field(
        None, description="metrics parameter"
    )
    ordering_column: applicationadnetworkanalytics_ordering_column_enum_param | None = Field(
        None, description="ordering_column parameter"
    )
    ordering_type: applicationadnetworkanalytics_ordering_type_enum_param | None = Field(
        None, description="ordering_type parameter"
    )
    should_include_until: bool | None = Field(None, description="should_include_until parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class ApplicationCreateAdNetworkanalyticParams(BaseModel):
    """Parameters for Application.create_ad_networkanalytic()."""

    model_config = ConfigDict(extra="forbid")
    aggregation_period: applicationadnetworkanalytics_aggregation_period_enum_param | None = Field(
        None, description="aggregation_period parameter"
    )
    breakdowns: list[applicationadnetworkanalytics_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    filters: list[dict[str, Any]] | None = Field(None, description="filters parameter")
    limit: int | None = Field(None, description="limit parameter")
    metrics: list[applicationadnetworkanalytics_metrics_enum_param] | None = Field(
        None, description="metrics parameter"
    )
    ordering_column: applicationadnetworkanalytics_ordering_column_enum_param | None = Field(
        None, description="ordering_column parameter"
    )
    ordering_type: applicationadnetworkanalytics_ordering_type_enum_param | None = Field(
        None, description="ordering_type parameter"
    )
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class ApplicationGetAdnetworkanalyticsResultsParams(BaseModel):
    """Parameters for Application.get_adnetworkanalytics_results()."""

    model_config = ConfigDict(extra="forbid")
    query_ids: list[str] | None = Field(None, description="query_ids parameter")


class ApplicationGetAemAttributionParams(BaseModel):
    """Parameters for Application.get_aem_attribution()."""

    model_config = ConfigDict(extra="forbid")
    advertiser_ids: list[str] | None = Field(None, description="advertiser_ids parameter")
    fb_content_data: str | None = Field(None, description="fb_content_data parameter")


class ApplicationGetAemConversionConfigsParams(BaseModel):
    """Parameters for Application.get_aem_conversion_configs()."""

    model_config = ConfigDict(extra="forbid")
    advertiser_ids: list[str] | None = Field(None, description="advertiser_ids parameter")


class ApplicationGetAemConversionFilterParams(BaseModel):
    """Parameters for Application.get_aem_conversion_filter()."""

    model_config = ConfigDict(extra="forbid")
    catalog_id: str | None = Field(None, description="catalog_id parameter")
    fb_content_ids: str | None = Field(None, description="fb_content_ids parameter")


class ApplicationCreateAemConversionParams(BaseModel):
    """Parameters for Application.create_aem_conversion()."""

    model_config = ConfigDict(extra="forbid")
    aem_conversions: list[dict[str, Any]] | None = Field(
        None, description="aem_conversions parameter"
    )


class ApplicationCreateAemSkanReadineParams(BaseModel):
    """Parameters for Application.create_aem_skan_readine()."""

    model_config = ConfigDict(extra="forbid")
    app_id: int | None = Field(None, description="app_id parameter")
    is_aem_ready: bool | None = Field(None, description="is_aem_ready parameter")
    is_app_aem_install_ready: bool | None = Field(
        None, description="is_app_aem_install_ready parameter"
    )
    is_app_aem_ready: bool | None = Field(None, description="is_app_aem_ready parameter")
    is_skan_ready: bool | None = Field(None, description="is_skan_ready parameter")
    message: str | None = Field(None, description="message parameter")


class ApplicationCreateAggregateRevenueParams(BaseModel):
    """Parameters for Application.create_aggregate_revenue()."""

    model_config = ConfigDict(extra="forbid")
    ecpms: list[str] | None = Field(None, description="ecpms parameter")
    query_ids: list[str] | None = Field(None, description="query_ids parameter")
    request_id: str | None = Field(None, description="request_id parameter")
    sync_api: bool | None = Field(None, description="sync_api parameter")


class ApplicationCreateAppIndexingParams(BaseModel):
    """Parameters for Application.create_app_indexing()."""

    model_config = ConfigDict(extra="forbid")
    app_version: str | None = Field(None, description="app_version parameter")
    device_session_id: str | None = Field(None, description="device_session_id parameter")
    extra_info: str | None = Field(None, description="extra_info parameter")
    platform: applicationapp_indexing_platform_enum_param | None = Field(
        None, description="platform parameter"
    )
    request_type: applicationapp_indexing_request_type_enum_param | None = Field(
        None, description="request_type parameter"
    )
    tree: dict[str, Any] | None = Field(None, description="tree parameter")


class ApplicationCreateAppIndexingSessionParams(BaseModel):
    """Parameters for Application.create_app_indexing_session()."""

    model_config = ConfigDict(extra="forbid")
    device_session_id: str | None = Field(None, description="device_session_id parameter")
    extinfo: str | None = Field(None, description="extinfo parameter")


class ApplicationGetAppInstalledGroupsParams(BaseModel):
    """Parameters for Application.get_app_installed_groups()."""

    model_config = ConfigDict(extra="forbid")
    group_id: str | None = Field(None, description="group_id parameter")


class ApplicationCreateAppPushDeviceTokenParams(BaseModel):
    """Parameters for Application.create_app_push_device_token()."""

    model_config = ConfigDict(extra="forbid")
    device_id: str | None = Field(None, description="device_id parameter")
    device_token: str | None = Field(None, description="device_token parameter")
    platform: applicationapp_push_device_token_platform_enum_param | None = Field(
        None, description="platform parameter"
    )


class ApplicationCreateAssetParams(BaseModel):
    """Parameters for Application.create_asset()."""

    model_config = ConfigDict(extra="forbid")
    asset: dict[str, Any] | None = Field(None, description="asset parameter")
    comment: str | None = Field(None, description="comment parameter")
    type: str | None = Field(None, description="type parameter")


class ApplicationGetAuthorizedAdaccountsParams(BaseModel):
    """Parameters for Application.get_authorized_adaccounts()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class ApplicationGetButtonAutoDetectionDeviceSelectionParams(BaseModel):
    """Parameters for Application.get_button_auto_detection_device_selection()."""

    model_config = ConfigDict(extra="forbid")
    device_id: str | None = Field(None, description="device_id parameter")


class ApplicationCreateCodelessEventMappingParams(BaseModel):
    """Parameters for Application.create_codeless_event_mapping()."""

    model_config = ConfigDict(extra="forbid")
    mappings: list[dict[str, Any]] | None = Field(None, description="mappings parameter")
    mutation_method: applicationcodeless_event_mappings_mutation_method_enum_param | None = Field(
        None, description="mutation_method parameter"
    )
    platform: applicationcodeless_event_mappings_platform_enum_param | None = Field(
        None, description="platform parameter"
    )
    post_method: applicationcodeless_event_mappings_post_method_enum_param | None = Field(
        None, description="post_method parameter"
    )


class ApplicationGetDaChecksParams(BaseModel):
    """Parameters for Application.get_da_checks()."""

    model_config = ConfigDict(extra="forbid")
    checks: list[str] | None = Field(None, description="checks parameter")
    connection_method: applicationda_checks_connection_method_enum_param | None = Field(
        None, description="connection_method parameter"
    )


class ApplicationCreateDomainReportParams(BaseModel):
    """Parameters for Application.create_domain_report()."""

    model_config = ConfigDict(extra="forbid")
    tracking_domains: list[str] | None = Field(None, description="tracking_domains parameter")


class ApplicationGetIapPurchasesParams(BaseModel):
    """Parameters for Application.get_iap_purchases()."""

    model_config = ConfigDict(extra="forbid")
    order_id: str | None = Field(None, description="order_id parameter")


class ApplicationGetMessageTemplatesParams(BaseModel):
    """Parameters for Application.get_message_templates()."""

    model_config = ConfigDict(extra="forbid")
    template_id: str | None = Field(None, description="template_id parameter")


class ApplicationCreateMmpAuditingParams(BaseModel):
    """Parameters for Application.create_mmp_auditing()."""

    model_config = ConfigDict(extra="forbid")
    advertiser_id: str | None = Field(None, description="advertiser_id parameter")
    attribution: str | None = Field(None, description="attribution parameter")
    attribution_method: str | None = Field(None, description="attribution_method parameter")
    attribution_model: str | None = Field(None, description="attribution_model parameter")
    attribution_referrer: str | None = Field(None, description="attribution_referrer parameter")
    auditing_token: str | None = Field(None, description="auditing_token parameter")
    click_attr_window: int | None = Field(None, description="click_attr_window parameter")
    custom_events: list[dict[str, Any]] | None = Field(None, description="custom_events parameter")
    decline_reason: str | None = Field(None, description="decline_reason parameter")
    device_os: str | None = Field(None, description="device_os parameter")
    engagement_type: str | None = Field(None, description="engagement_type parameter")
    event: str | None = Field(None, description="event parameter")
    event_id: str | None = Field(None, description="event_id parameter")
    event_reported_time: int | None = Field(None, description="event_reported_time parameter")
    fb_ad_id: int | None = Field(None, description="fb_ad_id parameter")
    fb_adgroup_id: int | None = Field(None, description="fb_adgroup_id parameter")
    fb_click_time: int | None = Field(None, description="fb_click_time parameter")
    fb_view_time: int | None = Field(None, description="fb_view_time parameter")
    google_install_referrer: str | None = Field(
        None, description="google_install_referrer parameter"
    )
    inactivity_window_hours: int | None = Field(
        None, description="inactivity_window_hours parameter"
    )
    install_id: str | None = Field(None, description="install_id parameter")
    is_fb: bool | None = Field(None, description="is_fb parameter")
    meta_install_referrer: str | None = Field(None, description="meta_install_referrer parameter")
    used_install_referrer: bool | None = Field(None, description="used_install_referrer parameter")
    view_attr_window: int | None = Field(None, description="view_attr_window parameter")


class ApplicationGetMobileSdkGkParams(BaseModel):
    """Parameters for Application.get_mobile_sdk_gk()."""

    model_config = ConfigDict(extra="forbid")
    device_id: str | None = Field(None, description="device_id parameter")
    extinfo: dict[str, Any] | None = Field(None, description="extinfo parameter")
    os_version: str | None = Field(None, description="os_version parameter")
    platform: applicationmobile_sdk_gk_platform_enum_param | None = Field(
        None, description="platform parameter"
    )
    sdk_version: str | None = Field(None, description="sdk_version parameter")


class ApplicationCreateMonetizedDigitalStoreObjectParams(BaseModel):
    """Parameters for Application.create_monetized_digital_store_object()."""

    model_config = ConfigDict(extra="forbid")
    content_id: str | None = Field(None, description="content_id parameter")
    store: str | None = Field(None, description="store parameter")


class ApplicationCreateOccludespopupParams(BaseModel):
    """Parameters for Application.create_occludespopup()."""

    model_config = ConfigDict(extra="forbid")
    flash: bool | None = Field(None, description="flash parameter")
    unity: bool | None = Field(None, description="unity parameter")


class ApplicationGetPermissionsParams(BaseModel):
    """Parameters for Application.get_permissions()."""

    model_config = ConfigDict(extra="forbid")
    android_key_hash: str | None = Field(None, description="android_key_hash parameter")
    ios_bundle_id: str | None = Field(None, description="ios_bundle_id parameter")
    permission: list[dict[str, Any]] | None = Field(None, description="permission parameter")
    proxied_app_id: int | None = Field(None, description="proxied_app_id parameter")
    status: list[applicationpermissions_status_enum_param] | None = Field(
        None, description="status parameter"
    )


class ApplicationGetProductSParams(BaseModel):
    """Parameters for Application.get_product_s()."""

    model_config = ConfigDict(extra="forbid")
    product_ids: list[str] | None = Field(None, description="product_ids parameter")


class ApplicationGetSgwDatasetStatusParams(BaseModel):
    """Parameters for Application.get_sgw_dataset_status()."""

    model_config = ConfigDict(extra="forbid")
    dataset_id: int | None = Field(None, description="dataset_id parameter")


class ApplicationGetSgwInstallDeferralLinkParams(BaseModel):
    """Parameters for Application.get_sgw_install_deferral_link()."""

    model_config = ConfigDict(extra="forbid")
    client_ip: str | None = Field(None, description="client_ip parameter")
    dataset_id: int | None = Field(None, description="dataset_id parameter")


class ApplicationCreateSubscribedDomainParams(BaseModel):
    """Parameters for Application.create_subscribed_domain()."""

    model_config = ConfigDict(extra="forbid")
    subscribe: list[str] | None = Field(None, description="subscribe parameter")
    unsubscribe: list[str] | None = Field(None, description="unsubscribe parameter")


class ApplicationCreateSubscribedDomainsPhishingParams(BaseModel):
    """Parameters for Application.create_subscribed_domains_phishing()."""

    model_config = ConfigDict(extra="forbid")
    subscribe: list[str] | None = Field(None, description="subscribe parameter")
    unsubscribe: list[str] | None = Field(None, description="unsubscribe parameter")


class ApplicationDeleteSubscriptionsParams(BaseModel):
    """Parameters for Application.delete_subscriptions()."""

    model_config = ConfigDict(extra="forbid")
    fields: list[str] | None = Field(None, description="fields parameter")
    object: str | None = Field(None, description="object parameter")


class ApplicationCreateSubscriptionParams(BaseModel):
    """Parameters for Application.create_subscription()."""

    model_config = ConfigDict(extra="forbid")
    callback_url: str | None = Field(None, description="callback_url parameter")
    fields: list[str] | None = Field(None, description="fields parameter")
    include_values: bool | None = Field(None, description="include_values parameter")
    object: str | None = Field(None, description="object parameter")
    verify_token: str | None = Field(None, description="verify_token parameter")


class ApplicationCreateUploadParams(BaseModel):
    """Parameters for Application.create_upload()."""

    model_config = ConfigDict(extra="forbid")
    file_length: int | None = Field(None, description="file_length parameter")
    file_name: dict[str, Any] | None = Field(None, description="file_name parameter")
    file_type: dict[str, Any] | None = Field(None, description="file_type parameter")
    session_type: applicationuploads_session_type_enum_param | None = Field(
        None, description="session_type parameter"
    )


class ApplicationCreateWhatsappBusinessSolutionParams(BaseModel):
    """Parameters for Application.create_whatsapp_business_solution()."""

    model_config = ConfigDict(extra="forbid")
    owner_permissions: (
        list[applicationwhatsapp_business_solution_owner_permissions_enum_param] | None
    ) = Field(None, description="owner_permissions parameter")
    partner_app_id: str | None = Field(None, description="partner_app_id parameter")
    partner_permissions: (
        list[applicationwhatsapp_business_solution_partner_permissions_enum_param] | None
    ) = Field(None, description="partner_permissions parameter")
    solution_name: str | None = Field(None, description="solution_name parameter")


class ApplicationGetWhatsappBusinessSolutionsParams(BaseModel):
    """Parameters for Application.get_whatsapp_business_solutions()."""

    model_config = ConfigDict(extra="forbid")
    role: applicationwhatsapp_business_solutions_role_enum_param | None = Field(
        None, description="role parameter"
    )
