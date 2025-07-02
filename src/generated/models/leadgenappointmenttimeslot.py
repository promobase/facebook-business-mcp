"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenAppointmentTimeSlotField = Literal["end_time", "start_time"]


class LeadGenAppointmentTimeSlotFields(BaseModel):
    """Pydantic model for LeadGenAppointmentTimeSlot fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    end_time: int = Field(None, alias="end_time")
    start_time: int = Field(None, alias="start_time")
