"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsAnomalyDetectionField = Literal["anomaly_data", "day"]


class AdsAnomalyDetectionFields(BaseModel):
    """Pydantic model for AdsAnomalyDetection fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    anomaly_data: list[dict[str, Any]] = Field(None, alias="anomaly_data")
    day: int = Field(None, alias="day")
