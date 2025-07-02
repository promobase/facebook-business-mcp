"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsReportBuilderMMMReportField = Literal[
    "async_status",
    "export_format",
    "export_name",
    "export_type",
    "has_seen",
    "id",
    "mmm_status",
    "time_start",
]


class AdsReportBuilderMMMReportFields(BaseModel):
    """Pydantic model for AdsReportBuilderMMMReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    async_status: str = Field(None, alias="async_status")
    export_format: str = Field(None, alias="export_format")
    export_name: str = Field(None, alias="export_name")
    export_type: str = Field(None, alias="export_type")
    has_seen: bool = Field(None, alias="has_seen")
    id: str = Field(None, alias="id")
    mmm_status: str = Field(None, alias="mmm_status")
    time_start: datetime = Field(None, alias="time_start")
