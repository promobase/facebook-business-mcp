"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .advideo import AdVideoFields
    from .photo import PhotoFields


# Field literal type
EventTourField = Literal[
    "description",
    "dominant_color",
    "end_time",
    "id",
    "is_past",
    "last_event_timestamp",
    "name",
    "num_events",
    "photo",
    "scheduled_publish_timestamp",
    "start_time",
    "ticketing_uri",
    "video",
]


class EventTourFields(BaseModel):
    """Pydantic model for EventTour fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    dominant_color: str = Field(None, alias="dominant_color")
    end_time: str = Field(None, alias="end_time")
    id: str = Field(None, alias="id")
    is_past: bool = Field(None, alias="is_past")
    last_event_timestamp: int = Field(None, alias="last_event_timestamp")
    name: str = Field(None, alias="name")
    num_events: int = Field(None, alias="num_events")
    photo: PhotoFields = Field(None, alias="photo")
    scheduled_publish_timestamp: int = Field(None, alias="scheduled_publish_timestamp")
    start_time: str = Field(None, alias="start_time")
    ticketing_uri: str = Field(None, alias="ticketing_uri")
    video: AdVideoFields = Field(None, alias="video")
