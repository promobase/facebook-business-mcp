"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageInsightsAsyncExportRunField = Literal[
    "data_level",
    "filters",
    "format",
    "gen_report_date",
    "id",
    "report_end_date",
    "report_start_date",
    "sorters",
    "status",
]


class PageInsightsAsyncExportRunFields(BaseModel):
    """Pydantic model for PageInsightsAsyncExportRun fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    data_level: str = Field(None, alias="data_level")
    filters: list[dict[str, Any]] = Field(None, alias="filters")
    format: str = Field(None, alias="format")
    gen_report_date: int = Field(None, alias="gen_report_date")
    id: str = Field(None, alias="id")
    report_end_date: int = Field(None, alias="report_end_date")
    report_start_date: int = Field(None, alias="report_start_date")
    sorters: list[dict[str, Any]] = Field(None, alias="sorters")
    status: str = Field(None, alias="status")
