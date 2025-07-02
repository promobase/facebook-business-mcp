"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessSettingLogsDataField = Literal[
    "actor", "event_object", "event_time", "event_type", "extra_data"
]


class BusinessSettingLogsDataFields(BaseModel):
    """Pydantic model for BusinessSettingLogsData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actor: dict[str, Any] = Field(None, alias="actor")
    event_object: dict[str, Any] = Field(None, alias="event_object")
    event_time: str = Field(None, alias="event_time")
    event_type: str = Field(None, alias="event_type")
    extra_data: dict[str, Any] = Field(None, alias="extra_data")
