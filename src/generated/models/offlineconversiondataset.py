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


class offlineconversiondatasetshared_agencies_action_source_enum_param(str, Enum):
    """offlineconversiondatasetshared_agencies_action_source_enum_param enum values."""

    PHYSICAL_STORE = "PHYSICAL_STORE"
    WEBSITE = "WEBSITE"


class offlineconversiondatasetshared_accounts_action_source_enum_param(str, Enum):
    """offlineconversiondatasetshared_accounts_action_source_enum_param enum values."""

    PHYSICAL_STORE = "PHYSICAL_STORE"
    WEBSITE = "WEBSITE"


class offlineconversiondatasetuploads_order_enum_param(str, Enum):
    """offlineconversiondatasetuploads_order_enum_param enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class offlineconversiondatasetstats_aggr_time_enum_param(str, Enum):
    """offlineconversiondatasetstats_aggr_time_enum_param enum values."""

    event_time = "event_time"
    upload_time = "upload_time"


class offlineconversiondatasetuploads_sort_by_enum_param(str, Enum):
    """offlineconversiondatasetuploads_sort_by_enum_param enum values."""

    API_CALLS = "API_CALLS"
    CREATION_TIME = "CREATION_TIME"
    EVENT_TIME_MAX = "EVENT_TIME_MAX"
    EVENT_TIME_MIN = "EVENT_TIME_MIN"
    FIRST_UPLOAD_TIME = "FIRST_UPLOAD_TIME"
    IS_EXCLUDED_FOR_LIFT = "IS_EXCLUDED_FOR_LIFT"
    LAST_UPLOAD_TIME = "LAST_UPLOAD_TIME"


class offlineconversiondatasetaudiences_action_source_enum_param(str, Enum):
    """offlineconversiondatasetaudiences_action_source_enum_param enum values."""

    PHYSICAL_STORE = "PHYSICAL_STORE"
    WEBSITE = "WEBSITE"


class offlineconversiondatasetstats_granularity_enum_param(str, Enum):
    """offlineconversiondatasetstats_granularity_enum_param enum values."""

    daily = "daily"
    hourly = "hourly"
    six_hourly = "six_hourly"


# Field literal type
OfflineConversionDataSetField = Literal[
    "automatic_matching_fields",
    "business",
    "can_proxy",
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
    "valid_entries",
]


class OfflineConversionDataSetFields(BaseModel):
    """Pydantic model for OfflineConversionDataSet fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    automatic_matching_fields: list[str] = Field(None, alias="automatic_matching_fields")
    business: BusinessFields = Field(None, alias="business")
    can_proxy: bool = Field(None, alias="can_proxy")
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
    valid_entries: int = Field(None, alias="valid_entries")


class OfflineConversionDataSetGetAdAccountsParams(BaseModel):
    """Parameters for OfflineConversionDataSet.get_ad_accounts()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class OfflineConversionDataSetGetAudiencesParams(BaseModel):
    """Parameters for OfflineConversionDataSet.get_audiences()."""

    model_config = ConfigDict(extra="forbid")
    action_source: offlineconversiondatasetaudiences_action_source_enum_param | None = Field(
        None, description="action_source parameter"
    )
    ad_account: str | None = Field(None, description="ad_account parameter")


class OfflineConversionDataSetGetCustomConversionsParams(BaseModel):
    """Parameters for OfflineConversionDataSet.get_custom_conversions()."""

    model_config = ConfigDict(extra="forbid")
    ad_account: str | None = Field(None, description="ad_account parameter")


class OfflineConversionDataSetGetSharedAccountsParams(BaseModel):
    """Parameters for OfflineConversionDataSet.get_shared_accounts()."""

    model_config = ConfigDict(extra="forbid")
    action_source: offlineconversiondatasetshared_accounts_action_source_enum_param | None = Field(
        None, description="action_source parameter"
    )
    business: str | None = Field(None, description="business parameter")


class OfflineConversionDataSetGetSharedAgenciesParams(BaseModel):
    """Parameters for OfflineConversionDataSet.get_shared_agencies()."""

    model_config = ConfigDict(extra="forbid")
    action_source: offlineconversiondatasetshared_agencies_action_source_enum_param | None = Field(
        None, description="action_source parameter"
    )


class OfflineConversionDataSetGetStatsParams(BaseModel):
    """Parameters for OfflineConversionDataSet.get_stats()."""

    model_config = ConfigDict(extra="forbid")
    aggr_time: offlineconversiondatasetstats_aggr_time_enum_param | None = Field(
        None, description="aggr_time parameter"
    )
    end: int | None = Field(None, description="end parameter")
    granularity: offlineconversiondatasetstats_granularity_enum_param | None = Field(
        None, description="granularity parameter"
    )
    skip_empty_values: bool | None = Field(None, description="skip_empty_values parameter")
    start: int | None = Field(None, description="start parameter")
    user_timezone_id: int | None = Field(None, description="user_timezone_id parameter")


class OfflineConversionDataSetGetUploadsParams(BaseModel):
    """Parameters for OfflineConversionDataSet.get_uploads()."""

    model_config = ConfigDict(extra="forbid")
    end_time: datetime | None = Field(None, description="end_time parameter")
    order: offlineconversiondatasetuploads_order_enum_param | None = Field(
        None, description="order parameter"
    )
    sort_by: offlineconversiondatasetuploads_sort_by_enum_param | None = Field(
        None, description="sort_by parameter"
    )
    start_time: datetime | None = Field(None, description="start_time parameter")
    upload_tag: str | None = Field(None, description="upload_tag parameter")
