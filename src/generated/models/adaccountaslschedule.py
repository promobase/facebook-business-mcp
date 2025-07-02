"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields


# Field literal type
AdAccountASLScheduleField = Literal["ad_account", "id", "time_created", "time_updated"]


class AdAccountASLScheduleFields(BaseModel):
    """Pydantic model for AdAccountASLSchedule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account: AdAccountFields = Field(None, alias="ad_account")
    id: str = Field(None, alias="id")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")
