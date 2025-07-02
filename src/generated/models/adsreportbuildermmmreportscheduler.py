"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsReportBuilderMMMReportSchedulerField = Literal[
    "ad_account_ids", "filtering", "id", "report_name", "schedule_frequency"
]


class AdsReportBuilderMMMReportSchedulerFields(BaseModel):
    """Pydantic model for AdsReportBuilderMMMReportScheduler fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_ids: list[str] = Field(None, alias="ad_account_ids")
    filtering: list[dict[str, Any]] = Field(None, alias="filtering")
    id: str = Field(None, alias="id")
    report_name: str = Field(None, alias="report_name")
    schedule_frequency: str = Field(None, alias="schedule_frequency")
