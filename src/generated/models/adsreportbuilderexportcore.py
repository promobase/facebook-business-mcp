"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsReportBuilderExportCoreField = Literal[
    "async_percent_completion",
    "async_report_url",
    "async_status",
    "client_creation_value",
    "expiry_time",
    "export_download_time",
    "export_format",
    "export_name",
    "export_type",
    "has_seen",
    "id",
    "is_sharing",
    "link_sharing_expiration_time",
    "link_sharing_uri",
    "time_completed",
    "time_start",
]


class AdsReportBuilderExportCoreFields(BaseModel):
    """Pydantic model for AdsReportBuilderExportCore fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    async_percent_completion: int = Field(None, alias="async_percent_completion")
    async_report_url: str = Field(None, alias="async_report_url")
    async_status: str = Field(None, alias="async_status")
    client_creation_value: str = Field(None, alias="client_creation_value")
    expiry_time: datetime = Field(None, alias="expiry_time")
    export_download_time: datetime = Field(None, alias="export_download_time")
    export_format: str = Field(None, alias="export_format")
    export_name: str = Field(None, alias="export_name")
    export_type: str = Field(None, alias="export_type")
    has_seen: bool = Field(None, alias="has_seen")
    id: str = Field(None, alias="id")
    is_sharing: bool = Field(None, alias="is_sharing")
    link_sharing_expiration_time: datetime = Field(None, alias="link_sharing_expiration_time")
    link_sharing_uri: str = Field(None, alias="link_sharing_uri")
    time_completed: datetime = Field(None, alias="time_completed")
    time_start: datetime = Field(None, alias="time_start")
