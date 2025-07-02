"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


# Field literal type
AdsReportBuilderSavedReportField = Literal[
    "action_report_time",
    "ad_account_id",
    "attribution_windows",
    "comparison_date_interval",
    "creation_source",
    "creation_time",
    "currency",
    "date_interval",
    "date_preset",
    "default_attribution_windows",
    "dimension_groups",
    "dimensions",
    "filtering",
    "formatting",
    "id",
    "last_access_by",
    "last_access_time",
    "last_report_snapshot_id",
    "last_report_snapshot_time",
    "last_shared_report_expiration",
    "limit",
    "locked_dimensions",
    "metrics",
    "report_name",
    "report_snapshot_async_percent_completion",
    "report_snapshot_async_status",
    "schedule_frequency",
    "scope",
    "show_deprecate_aw_banner",
    "sorting",
    "start_date",
    "status",
    "subscribers",
    "update_by",
    "update_time",
    "user",
    "user_dimensions",
    "user_metrics",
    "view_type",
]


class AdsReportBuilderSavedReportFields(BaseModel):
    """Pydantic model for AdsReportBuilderSavedReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_report_time: str = Field(None, alias="action_report_time")
    ad_account_id: str = Field(None, alias="ad_account_id")
    attribution_windows: list[str] = Field(None, alias="attribution_windows")
    comparison_date_interval: dict[str, Any] = Field(None, alias="comparison_date_interval")
    creation_source: str = Field(None, alias="creation_source")
    creation_time: datetime = Field(None, alias="creation_time")
    currency: str = Field(None, alias="currency")
    date_interval: dict[str, Any] = Field(None, alias="date_interval")
    date_preset: str = Field(None, alias="date_preset")
    default_attribution_windows: list[str] = Field(None, alias="default_attribution_windows")
    dimension_groups: list[list[str]] = Field(None, alias="dimension_groups")
    dimensions: list[str] = Field(None, alias="dimensions")
    filtering: dict[str, Any] = Field(None, alias="filtering")
    formatting: list[dict[str, list[dict[str, Any]]]] = Field(None, alias="formatting")
    id: str = Field(None, alias="id")
    last_access_by: ProfileFields = Field(None, alias="last_access_by")
    last_access_time: datetime = Field(None, alias="last_access_time")
    last_report_snapshot_id: str = Field(None, alias="last_report_snapshot_id")
    last_report_snapshot_time: datetime = Field(None, alias="last_report_snapshot_time")
    last_shared_report_expiration: datetime = Field(None, alias="last_shared_report_expiration")
    limit: int = Field(None, alias="limit")
    locked_dimensions: int = Field(None, alias="locked_dimensions")
    metrics: list[str] = Field(None, alias="metrics")
    report_name: str = Field(None, alias="report_name")
    report_snapshot_async_percent_completion: int = Field(
        None, alias="report_snapshot_async_percent_completion"
    )
    report_snapshot_async_status: str = Field(None, alias="report_snapshot_async_status")
    schedule_frequency: str = Field(None, alias="schedule_frequency")
    scope: str = Field(None, alias="scope")
    show_deprecate_aw_banner: bool = Field(None, alias="show_deprecate_aw_banner")
    sorting: list[dict[str, Any]] = Field(None, alias="sorting")
    start_date: str = Field(None, alias="start_date")
    status: str = Field(None, alias="status")
    subscribers: list[str] = Field(None, alias="subscribers")
    update_by: ProfileFields = Field(None, alias="update_by")
    update_time: datetime = Field(None, alias="update_time")
    user: ProfileFields = Field(None, alias="user")
    user_dimensions: list[str] = Field(None, alias="user_dimensions")
    user_metrics: list[str] = Field(None, alias="user_metrics")
    view_type: str = Field(None, alias="view_type")
