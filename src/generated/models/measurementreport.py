"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MeasurementReportField = Literal["download_urls", "id", "metadata", "report_type", "status"]


class MeasurementReportFields(BaseModel):
    """Pydantic model for MeasurementReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    download_urls: list[str] = Field(None, alias="download_urls")
    id: str = Field(None, alias="id")
    metadata: dict[str, Any] = Field(None, alias="metadata")
    report_type: str = Field(None, alias="report_type")
    status: str = Field(None, alias="status")
