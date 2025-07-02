"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AnalyticsConfigField = Literal[
    "analytics_access_for_authorized_ad_account",
    "breakdowns_config",
    "builtin_fields_config",
    "deprecated_events_config",
    "events_config",
    "ios_purchase_validation_secret",
    "is_any_role_able_to_see_restricted_insights",
    "is_implicit_purchase_logging_on_android_supported",
    "is_implicit_purchase_logging_on_ios_supported",
    "is_track_ios_app_uninstall_supported",
    "journey_backfill_status",
    "journey_conversion_events",
    "journey_enabled",
    "journey_impacting_change_time",
    "journey_timeout",
    "latest_sdk_versions",
    "log_android_implicit_purchase_events",
    "log_automatic_analytics_events",
    "log_implicit_purchase_events",
    "prev_journey_conversion_events",
    "query_approximation_accuracy_level",
    "query_currency",
    "query_timezone",
    "recent_events_update_time",
    "session_timeout_interval",
    "track_ios_app_uninstall",
]


class AnalyticsConfigFields(BaseModel):
    """Pydantic model for AnalyticsConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    analytics_access_for_authorized_ad_account: bool = Field(
        None, alias="analytics_access_for_authorized_ad_account"
    )
    breakdowns_config: list[dict[str, Any]] = Field(None, alias="breakdowns_config")
    builtin_fields_config: list[dict[str, Any]] = Field(None, alias="builtin_fields_config")
    deprecated_events_config: list[dict[str, Any]] = Field(None, alias="deprecated_events_config")
    events_config: list[dict[str, Any]] = Field(None, alias="events_config")
    ios_purchase_validation_secret: str = Field(None, alias="ios_purchase_validation_secret")
    is_any_role_able_to_see_restricted_insights: bool = Field(
        None, alias="is_any_role_able_to_see_restricted_insights"
    )
    is_implicit_purchase_logging_on_android_supported: bool = Field(
        None, alias="is_implicit_purchase_logging_on_android_supported"
    )
    is_implicit_purchase_logging_on_ios_supported: bool = Field(
        None, alias="is_implicit_purchase_logging_on_ios_supported"
    )
    is_track_ios_app_uninstall_supported: bool = Field(
        None, alias="is_track_ios_app_uninstall_supported"
    )
    journey_backfill_status: str = Field(None, alias="journey_backfill_status")
    journey_conversion_events: list[str] = Field(None, alias="journey_conversion_events")
    journey_enabled: bool = Field(None, alias="journey_enabled")
    journey_impacting_change_time: datetime = Field(None, alias="journey_impacting_change_time")
    journey_timeout: str = Field(None, alias="journey_timeout")
    latest_sdk_versions: dict[str, str] = Field(None, alias="latest_sdk_versions")
    log_android_implicit_purchase_events: bool = Field(
        None, alias="log_android_implicit_purchase_events"
    )
    log_automatic_analytics_events: bool = Field(None, alias="log_automatic_analytics_events")
    log_implicit_purchase_events: bool = Field(None, alias="log_implicit_purchase_events")
    prev_journey_conversion_events: list[str] = Field(None, alias="prev_journey_conversion_events")
    query_approximation_accuracy_level: str = Field(
        None, alias="query_approximation_accuracy_level"
    )
    query_currency: str = Field(None, alias="query_currency")
    query_timezone: str = Field(None, alias="query_timezone")
    recent_events_update_time: datetime = Field(None, alias="recent_events_update_time")
    session_timeout_interval: int = Field(None, alias="session_timeout_interval")
    track_ios_app_uninstall: bool = Field(None, alias="track_ios_app_uninstall")
