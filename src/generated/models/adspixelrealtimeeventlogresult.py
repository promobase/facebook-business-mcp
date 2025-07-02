"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelRealTimeEventLogResultField = Literal[
    "data_json",
    "dedup_data",
    "device_type",
    "domain_control_rule_rejection",
    "event",
    "event_detection_method",
    "in_iframe",
    "matched_rule_conditions",
    "resolved_link",
    "source_rule_condition",
    "timestamp",
    "trace_id",
    "url",
]


class AdsPixelRealTimeEventLogResultFields(BaseModel):
    """Pydantic model for AdsPixelRealTimeEventLogResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    data_json: str = Field(None, alias="data_json")
    dedup_data: str = Field(None, alias="dedup_data")
    device_type: str = Field(None, alias="device_type")
    domain_control_rule_rejection: str = Field(None, alias="domain_control_rule_rejection")
    event: str = Field(None, alias="event")
    event_detection_method: str = Field(None, alias="event_detection_method")
    in_iframe: bool = Field(None, alias="in_iframe")
    matched_rule_conditions: str = Field(None, alias="matched_rule_conditions")
    resolved_link: str = Field(None, alias="resolved_link")
    source_rule_condition: str = Field(None, alias="source_rule_condition")
    timestamp: str = Field(None, alias="timestamp")
    trace_id: str = Field(None, alias="trace_id")
    url: str = Field(None, alias="url")
