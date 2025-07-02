"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ExternalEventSourceCPASEventsDebuggingField = Literal[
    "actual_event_time",
    "app_version",
    "content_url",
    "device_os",
    "diagnostic",
    "event_name",
    "event_time",
    "missing_ids",
    "severity",
]


class ExternalEventSourceCPASEventsDebuggingFields(BaseModel):
    """Pydantic model for ExternalEventSourceCPASEventsDebugging fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actual_event_time: int = Field(None, alias="actual_event_time")
    app_version: str = Field(None, alias="app_version")
    content_url: str = Field(None, alias="content_url")
    device_os: str = Field(None, alias="device_os")
    diagnostic: str = Field(None, alias="diagnostic")
    event_name: str = Field(None, alias="event_name")
    event_time: int = Field(None, alias="event_time")
    missing_ids: str = Field(None, alias="missing_ids")
    severity: str = Field(None, alias="severity")
