"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields


# Field literal type
AdAccountBillingDatePreferenceField = Literal[
    "ad_account", "day_of_month", "id", "next_bill_date", "time_created", "time_effective"
]


class AdAccountBillingDatePreferenceFields(BaseModel):
    """Pydantic model for AdAccountBillingDatePreference fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account: AdAccountFields = Field(None, alias="ad_account")
    day_of_month: int = Field(None, alias="day_of_month")
    id: str = Field(None, alias="id")
    next_bill_date: datetime = Field(None, alias="next_bill_date")
    time_created: datetime = Field(None, alias="time_created")
    time_effective: datetime = Field(None, alias="time_effective")
