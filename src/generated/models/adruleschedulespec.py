"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adruleschedule import AdRuleScheduleFields


# Field literal type
AdRuleScheduleSpecField = Literal["schedule", "schedule_type"]


class AdRuleScheduleSpecFields(BaseModel):
    """Pydantic model for AdRuleScheduleSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    schedule: list[AdRuleScheduleFields] = Field(None, alias="schedule")
    schedule_type: str = Field(None, alias="schedule_type")
