"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adspixel import AdsPixelFields


# Field literal type
AdsSignalDiagnosticIssueField = Literal[
    "data_source_id",
    "data_source_type",
    "diagnostic_type",
    "event_name",
    "traffic_anomaly_drop_percentage",
    "traffic_anomaly_drop_timestamp",
]


class AdsSignalDiagnosticIssueFields(BaseModel):
    """Pydantic model for AdsSignalDiagnosticIssue fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    data_source_id: AdsPixelFields = Field(None, alias="data_source_id")
    data_source_type: str = Field(None, alias="data_source_type")
    diagnostic_type: str = Field(None, alias="diagnostic_type")
    event_name: str = Field(None, alias="event_name")
    traffic_anomaly_drop_percentage: float = Field(None, alias="traffic_anomaly_drop_percentage")
    traffic_anomaly_drop_timestamp: datetime = Field(None, alias="traffic_anomaly_drop_timestamp")
