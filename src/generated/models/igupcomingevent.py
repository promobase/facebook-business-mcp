"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGUpcomingEventField = Literal[
    "end_time", "id", "notification_subtypes", "notification_target_time", "start_time", "title"
]


class IGUpcomingEventFields(BaseModel):
    """Pydantic model for IGUpcomingEvent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    end_time: datetime = Field(None, alias="end_time")
    id: str = Field(None, alias="id")
    notification_subtypes: list[str] = Field(None, alias="notification_subtypes")
    notification_target_time: str = Field(None, alias="notification_target_time")
    start_time: datetime = Field(None, alias="start_time")
    title: str = Field(None, alias="title")
