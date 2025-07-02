"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdReportRunField = Literal[
    "account_id",
    "async_percent_completion",
    "async_report_url",
    "async_status",
    "date_start",
    "date_stop",
    "emails",
    "error_code",
    "friendly_name",
    "id",
    "is_async_export",
    "is_bookmarked",
    "is_running",
    "schedule_id",
    "time_completed",
    "time_ref",
]


class AdReportRunFields(BaseModel):
    """Pydantic model for AdReportRun fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    async_percent_completion: int = Field(None, alias="async_percent_completion")
    async_report_url: str = Field(None, alias="async_report_url")
    async_status: str = Field(None, alias="async_status")
    date_start: str = Field(None, alias="date_start")
    date_stop: str = Field(None, alias="date_stop")
    emails: list[str] = Field(None, alias="emails")
    error_code: int = Field(None, alias="error_code")
    friendly_name: str = Field(None, alias="friendly_name")
    id: str = Field(None, alias="id")
    is_async_export: int = Field(None, alias="is_async_export")
    is_bookmarked: bool = Field(None, alias="is_bookmarked")
    is_running: bool = Field(None, alias="is_running")
    schedule_id: str = Field(None, alias="schedule_id")
    time_completed: int = Field(None, alias="time_completed")
    time_ref: int = Field(None, alias="time_ref")
