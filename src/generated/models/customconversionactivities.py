"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomConversionActivitiesField = Literal["app_id", "data", "event_type", "timestamp"]


class CustomConversionActivitiesFields(BaseModel):
    """Pydantic model for CustomConversionActivities fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: int = Field(None, alias="app_id")
    data: str = Field(None, alias="data")
    event_type: str = Field(None, alias="event_type")
    timestamp: datetime = Field(None, alias="timestamp")
