"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OfflineConversionDataSetActivitiesField = Literal[
    "actor_id",
    "actor_name",
    "adaccount_id",
    "adaccount_name",
    "event_time",
    "event_type",
    "extra_data",
    "object_id",
    "object_name",
]


class OfflineConversionDataSetActivitiesFields(BaseModel):
    """Pydantic model for OfflineConversionDataSetActivities fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actor_id: int = Field(None, alias="actor_id")
    actor_name: str = Field(None, alias="actor_name")
    adaccount_id: int = Field(None, alias="adaccount_id")
    adaccount_name: str = Field(None, alias="adaccount_name")
    event_time: datetime = Field(None, alias="event_time")
    event_type: str = Field(None, alias="event_type")
    extra_data: str = Field(None, alias="extra_data")
    object_id: int = Field(None, alias="object_id")
    object_name: str = Field(None, alias="object_name")
