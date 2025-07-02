"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .business import BusinessFields
    from .offlineconversiondatasetpermissions import OfflineConversionDataSetPermissionsFields
    from .offlineconversiondatasetusage import OfflineConversionDataSetUsageFields
    from .user import UserFields


# Field literal type
AdsDatasetField = Literal[
    "can_proxy",
    "collection_rate",
    "config",
    "creation_time",
    "creator",
    "dataset_id",
    "description",
    "duplicate_entries",
    "enable_auto_assign_to_accounts",
    "enable_automatic_events",
    "enable_automatic_matching",
    "enable_real_time_event_log",
    "event_stats",
    "event_time_max",
    "event_time_min",
    "first_party_cookie_status",
    "has_bapi_domains",
    "has_catalog_microdata_activity",
    "has_ofa_redacted_keys",
    "has_sent_pii",
    "id",
    "is_consolidated_container",
    "is_created_by_business",
    "is_crm",
    "is_eligible_for_sharing_to_ad_account",
    "is_eligible_for_sharing_to_business",
    "is_eligible_for_value_optimization",
    "is_mta_use",
    "is_restricted_use",
    "is_unavailable",
    "last_fired_time",
    "last_upload_app",
    "last_upload_app_changed_time",
    "last_upload_time",
    "late_upload_reminder_eligibility",
    "match_rate_approx",
    "matched_entries",
    "name",
    "no_ads_tracked_for_weekly_uploaded_events_reminder_eligibility",
    "num_active_ad_set_tracked",
    "num_recent_offline_conversions_uploaded",
    "num_uploads",
    "owner_ad_account",
    "owner_business",
    "percentage_of_late_uploads_in_external_suboptimal_window",
    "permissions",
    "server_last_fired_time",
    "show_automatic_events",
    "upload_rate",
    "upload_reminder_eligibility",
    "usage",
    "valid_entries",
]


class AdsDatasetFields(BaseModel):
    """Pydantic model for AdsDataset fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_proxy: bool = Field(None, alias="can_proxy")
    collection_rate: float = Field(None, alias="collection_rate")
    config: str = Field(None, alias="config")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: UserFields = Field(None, alias="creator")
    dataset_id: str = Field(None, alias="dataset_id")
    description: str = Field(None, alias="description")
    duplicate_entries: int = Field(None, alias="duplicate_entries")
    enable_auto_assign_to_accounts: bool = Field(None, alias="enable_auto_assign_to_accounts")
    enable_automatic_events: bool = Field(None, alias="enable_automatic_events")
    enable_automatic_matching: bool = Field(None, alias="enable_automatic_matching")
    enable_real_time_event_log: bool = Field(None, alias="enable_real_time_event_log")
    event_stats: str = Field(None, alias="event_stats")
    event_time_max: int = Field(None, alias="event_time_max")
    event_time_min: int = Field(None, alias="event_time_min")
    first_party_cookie_status: str = Field(None, alias="first_party_cookie_status")
    has_bapi_domains: bool = Field(None, alias="has_bapi_domains")
    has_catalog_microdata_activity: bool = Field(None, alias="has_catalog_microdata_activity")
    has_ofa_redacted_keys: bool = Field(None, alias="has_ofa_redacted_keys")
    has_sent_pii: bool = Field(None, alias="has_sent_pii")
    id: str = Field(None, alias="id")
    is_consolidated_container: bool = Field(None, alias="is_consolidated_container")
    is_created_by_business: bool = Field(None, alias="is_created_by_business")
    is_crm: bool = Field(None, alias="is_crm")
    is_eligible_for_sharing_to_ad_account: bool = Field(
        None, alias="is_eligible_for_sharing_to_ad_account"
    )
    is_eligible_for_sharing_to_business: bool = Field(
        None, alias="is_eligible_for_sharing_to_business"
    )
    is_eligible_for_value_optimization: bool = Field(
        None, alias="is_eligible_for_value_optimization"
    )
    is_mta_use: bool = Field(None, alias="is_mta_use")
    is_restricted_use: bool = Field(None, alias="is_restricted_use")
    is_unavailable: bool = Field(None, alias="is_unavailable")
    last_fired_time: datetime = Field(None, alias="last_fired_time")
    last_upload_app: str = Field(None, alias="last_upload_app")
    last_upload_app_changed_time: int = Field(None, alias="last_upload_app_changed_time")
    last_upload_time: int = Field(None, alias="last_upload_time")
    late_upload_reminder_eligibility: bool = Field(None, alias="late_upload_reminder_eligibility")
    match_rate_approx: int = Field(None, alias="match_rate_approx")
    matched_entries: int = Field(None, alias="matched_entries")
    name: str = Field(None, alias="name")
    no_ads_tracked_for_weekly_uploaded_events_reminder_eligibility: bool = Field(
        None, alias="no_ads_tracked_for_weekly_uploaded_events_reminder_eligibility"
    )
    num_active_ad_set_tracked: int = Field(None, alias="num_active_ad_set_tracked")
    num_recent_offline_conversions_uploaded: int = Field(
        None, alias="num_recent_offline_conversions_uploaded"
    )
    num_uploads: int = Field(None, alias="num_uploads")
    owner_ad_account: AdAccountFields = Field(None, alias="owner_ad_account")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    percentage_of_late_uploads_in_external_suboptimal_window: int = Field(
        None, alias="percentage_of_late_uploads_in_external_suboptimal_window"
    )
    permissions: OfflineConversionDataSetPermissionsFields = Field(None, alias="permissions")
    server_last_fired_time: datetime = Field(None, alias="server_last_fired_time")
    show_automatic_events: bool = Field(None, alias="show_automatic_events")
    upload_rate: float = Field(None, alias="upload_rate")
    upload_reminder_eligibility: bool = Field(None, alias="upload_reminder_eligibility")
    usage: OfflineConversionDataSetUsageFields = Field(None, alias="usage")
    valid_entries: int = Field(None, alias="valid_entries")
