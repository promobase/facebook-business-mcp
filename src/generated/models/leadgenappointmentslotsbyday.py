"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgenappointmenttimeslot import LeadGenAppointmentTimeSlotFields


# Field literal type
LeadGenAppointmentSlotsByDayField = Literal["appointment_slots", "day"]


class LeadGenAppointmentSlotsByDayFields(BaseModel):
    """Pydantic model for LeadGenAppointmentSlotsByDay fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    appointment_slots: list[LeadGenAppointmentTimeSlotFields] = Field(
        None, alias="appointment_slots"
    )
    day: str = Field(None, alias="day")
