"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelRawFiresResultField = Literal[
    "data_json",
    "device_type",
    "event",
    "event_detection_method",
    "event_src",
    "placed_url",
    "timestamp",
    "user_pii_keys",
]


class AdsPixelRawFiresResultFields(BaseModel):
    """Pydantic model for AdsPixelRawFiresResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    data_json: str = Field(None, alias="data_json")
    device_type: str = Field(None, alias="device_type")
    event: str = Field(None, alias="event")
    event_detection_method: str = Field(None, alias="event_detection_method")
    event_src: str = Field(None, alias="event_src")
    placed_url: str = Field(None, alias="placed_url")
    timestamp: datetime = Field(None, alias="timestamp")
    user_pii_keys: str = Field(None, alias="user_pii_keys")
