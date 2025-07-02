"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsReportBuilderField = Literal["headers", "rows", "skan_readiness_status"]


class AdsReportBuilderFields(BaseModel):
    """Pydantic model for AdsReportBuilder fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    headers: dict[str, Any] = Field(None, alias="headers")
    rows: list[dict[str, Any]] = Field(None, alias="rows")
    skan_readiness_status: list[dict[str, str]] = Field(None, alias="skan_readiness_status")
