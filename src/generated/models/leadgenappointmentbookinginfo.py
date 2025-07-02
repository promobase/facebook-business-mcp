"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgenappointmentslotsbyday import LeadGenAppointmentSlotsByDayFields


# Field literal type
LeadGenAppointmentBookingInfoField = Literal[
    "advertiser_timezone_offset", "appointment_durations", "appointment_slots_by_day"
]


class LeadGenAppointmentBookingInfoFields(BaseModel):
    """Pydantic model for LeadGenAppointmentBookingInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    advertiser_timezone_offset: str = Field(None, alias="advertiser_timezone_offset")
    appointment_durations: list[str] = Field(None, alias="appointment_durations")
    appointment_slots_by_day: list[LeadGenAppointmentSlotsByDayFields] = Field(
        None, alias="appointment_slots_by_day"
    )
