"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsStartYourDayWidgetField = Literal["id", "widget_id"]


class AdsStartYourDayWidgetFields(BaseModel):
    """Pydantic model for AdsStartYourDayWidget fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    widget_id: str = Field(None, alias="widget_id")
