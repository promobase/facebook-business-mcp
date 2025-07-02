"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .business import BusinessFields
    from .offlineconversiondatasetusage import OfflineConversionDataSetUsageFields
    from .user import UserFields


class adspixelassigned_users_tasks_enum_param(str, Enum):
    """adspixelassigned_users_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    EDIT = "EDIT"
    UPLOAD = "UPLOAD"


class adspixelagencies_permitted_tasks_enum_param(str, Enum):
    """adspixelagencies_permitted_tasks_enum_param enum values."""

    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    EDIT = "EDIT"
    UPLOAD = "UPLOAD"


class adspixeloffline_event_uploads_sort_by_enum_param(str, Enum):
    """adspixeloffline_event_uploads_sort_by_enum_param enum values."""

    API_CALLS = "API_CALLS"
    CREATION_TIME = "CREATION_TIME"
    EVENT_TIME_MAX = "EVENT_TIME_MAX"
    EVENT_TIME_MIN = "EVENT_TIME_MIN"
    FIRST_UPLOAD_TIME = "FIRST_UPLOAD_TIME"
    IS_EXCLUDED_FOR_LIFT = "IS_EXCLUDED_FOR_LIFT"
    LAST_UPLOAD_TIME = "LAST_UPLOAD_TIME"


class adspixelda_checks_connection_method_enum_param(str, Enum):
    """adspixelda_checks_connection_method_enum_param enum values."""

    ALL = "ALL"
    APP = "APP"
    BROWSER = "BROWSER"
    SERVER = "SERVER"


class adspixelstats_aggregation_enum_param(str, Enum):
    """adspixelstats_aggregation_enum_param enum values."""

    browser_type = "browser_type"
    custom_data_field = "custom_data_field"
    device_os = "device_os"
    device_type = "device_type"
    event = "event"
    event_detection_method = "event_detection_method"
    event_processing_results = "event_processing_results"
    event_source = "event_source"
    event_total_counts = "event_total_counts"
    event_value_count = "event_value_count"
    had_pii = "had_pii"
    host = "host"
    match_keys = "match_keys"
    pixel_fire = "pixel_fire"
    url = "url"
    url_by_rule = "url_by_rule"


class adspixeloffline_event_uploads_order_enum_param(str, Enum):
    """adspixeloffline_event_uploads_order_enum_param enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


# Field literal type
AdsPixelField = Literal[
    "automatic_matching_fields",
    "can_proxy",
    "code",
    "config",
    "creation_time",
    "creator",
    "data_use_setting",
    "description",
    "duplicate_entries",
    "enable_auto_assign_to_accounts",
    "enable_automatic_matching",
    "event_stats",
    "event_time_max",
    "event_time_min",
    "first_party_cookie_status",
    "has_1p_pixel_event",
    "id",
    "is_consolidated_container",
    "is_created_by_business",
    "is_crm",
    "is_mta_use",
    "is_restricted_use",
    "is_unavailable",
    "last_fired_time",
    "last_upload_app",
    "last_upload_app_changed_time",
    "match_rate_approx",
    "matched_entries",
    "name",
    "owner_ad_account",
    "owner_business",
    "usage",
    "user_access_expire_time",
    "valid_entries",
]


class AdsPixelFields(BaseModel):
    """Pydantic model for AdsPixel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    automatic_matching_fields: list[str] = Field(None, alias="automatic_matching_fields")
    can_proxy: bool = Field(None, alias="can_proxy")
    code: str = Field(None, alias="code")
    config: str = Field(None, alias="config")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: UserFields = Field(None, alias="creator")
    data_use_setting: str = Field(None, alias="data_use_setting")
    description: str = Field(None, alias="description")
    duplicate_entries: int = Field(None, alias="duplicate_entries")
    enable_auto_assign_to_accounts: bool = Field(None, alias="enable_auto_assign_to_accounts")
    enable_automatic_matching: bool = Field(None, alias="enable_automatic_matching")
    event_stats: str = Field(None, alias="event_stats")
    event_time_max: int = Field(None, alias="event_time_max")
    event_time_min: int = Field(None, alias="event_time_min")
    first_party_cookie_status: str = Field(None, alias="first_party_cookie_status")
    has_1p_pixel_event: bool = Field(None, alias="has_1p_pixel_event")
    id: str = Field(None, alias="id")
    is_consolidated_container: bool = Field(None, alias="is_consolidated_container")
    is_created_by_business: bool = Field(None, alias="is_created_by_business")
    is_crm: bool = Field(None, alias="is_crm")
    is_mta_use: bool = Field(None, alias="is_mta_use")
    is_restricted_use: bool = Field(None, alias="is_restricted_use")
    is_unavailable: bool = Field(None, alias="is_unavailable")
    last_fired_time: datetime = Field(None, alias="last_fired_time")
    last_upload_app: str = Field(None, alias="last_upload_app")
    last_upload_app_changed_time: int = Field(None, alias="last_upload_app_changed_time")
    match_rate_approx: int = Field(None, alias="match_rate_approx")
    matched_entries: int = Field(None, alias="matched_entries")
    name: str = Field(None, alias="name")
    owner_ad_account: AdAccountFields = Field(None, alias="owner_ad_account")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    usage: OfflineConversionDataSetUsageFields = Field(None, alias="usage")
    user_access_expire_time: datetime = Field(None, alias="user_access_expire_time")
    valid_entries: int = Field(None, alias="valid_entries")


class AdsPixelGetAdaccountsParams(BaseModel):
    """Parameters for AdsPixel.get_adaccounts()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class AdsPixelDeleteAgenciesParams(BaseModel):
    """Parameters for AdsPixel.delete_agencies()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class AdsPixelCreateAgencieParams(BaseModel):
    """Parameters for AdsPixel.create_agencie()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")
    permitted_tasks: list[adspixelagencies_permitted_tasks_enum_param] | None = Field(
        None, description="permitted_tasks parameter"
    )


class AdsPixelCreateAhpConfigParams(BaseModel):
    """Parameters for AdsPixel.create_ahp_config()."""

    model_config = ConfigDict(extra="forbid")
    applink_autosetup: bool | None = Field(None, description="applink_autosetup parameter")


class AdsPixelGetAssignedUsersParams(BaseModel):
    """Parameters for AdsPixel.get_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class AdsPixelCreateAssignedUserParams(BaseModel):
    """Parameters for AdsPixel.create_assigned_user()."""

    model_config = ConfigDict(extra="forbid")
    tasks: list[adspixelassigned_users_tasks_enum_param] | None = Field(
        None, description="tasks parameter"
    )
    user: int | None = Field(None, description="user parameter")


class AdsPixelGetDaChecksParams(BaseModel):
    """Parameters for AdsPixel.get_da_checks()."""

    model_config = ConfigDict(extra="forbid")
    checks: list[str] | None = Field(None, description="checks parameter")
    connection_method: adspixelda_checks_connection_method_enum_param | None = Field(
        None, description="connection_method parameter"
    )


class AdsPixelCreateEventParams(BaseModel):
    """Parameters for AdsPixel.create_event()."""

    model_config = ConfigDict(extra="forbid")
    data: list[str] | None = Field(None, description="data parameter")
    namespace_id: str | None = Field(None, description="namespace_id parameter")
    partner_agent: str | None = Field(None, description="partner_agent parameter")
    platforms: list[dict[str, Any]] | None = Field(None, description="platforms parameter")
    progress: dict[str, Any] | None = Field(None, description="progress parameter")
    test_event_code: str | None = Field(None, description="test_event_code parameter")
    trace: int | None = Field(None, description="trace parameter")
    upload_id: str | None = Field(None, description="upload_id parameter")
    upload_source: str | None = Field(None, description="upload_source parameter")
    upload_tag: str | None = Field(None, description="upload_tag parameter")


class AdsPixelGetOfflineEventUploadsParams(BaseModel):
    """Parameters for AdsPixel.get_offline_event_uploads()."""

    model_config = ConfigDict(extra="forbid")
    end_time: datetime | None = Field(None, description="end_time parameter")
    order: adspixeloffline_event_uploads_order_enum_param | None = Field(
        None, description="order parameter"
    )
    sort_by: adspixeloffline_event_uploads_sort_by_enum_param | None = Field(
        None, description="sort_by parameter"
    )
    start_time: datetime | None = Field(None, description="start_time parameter")
    upload_tag: str | None = Field(None, description="upload_tag parameter")


class AdsPixelDeleteSharedAccountsParams(BaseModel):
    """Parameters for AdsPixel.delete_shared_accounts()."""

    model_config = ConfigDict(extra="forbid")
    account_id: str | None = Field(None, description="account_id parameter")
    business: str | None = Field(None, description="business parameter")


class AdsPixelGetSharedAccountsParams(BaseModel):
    """Parameters for AdsPixel.get_shared_accounts()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class AdsPixelCreateSharedAccountParams(BaseModel):
    """Parameters for AdsPixel.create_shared_account()."""

    model_config = ConfigDict(extra="forbid")
    account_id: str | None = Field(None, description="account_id parameter")
    business: str | None = Field(None, description="business parameter")


class AdsPixelGetStatsParams(BaseModel):
    """Parameters for AdsPixel.get_stats()."""

    model_config = ConfigDict(extra="forbid")
    aggregation: adspixelstats_aggregation_enum_param | None = Field(
        None, description="aggregation parameter"
    )
    end_time: datetime | None = Field(None, description="end_time parameter")
    event: str | None = Field(None, description="event parameter")
    event_source: str | None = Field(None, description="event_source parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")
