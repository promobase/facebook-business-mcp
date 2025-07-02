"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountAmountSpentHistoryField = Literal["amount_spent", "spend_cap", "time_start", "time_stop"]


class AdAccountAmountSpentHistoryFields(BaseModel):
    """Pydantic model for AdAccountAmountSpentHistory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount_spent: int = Field(None, alias="amount_spent")
    spend_cap: int = Field(None, alias="spend_cap")
    time_start: str = Field(None, alias="time_start")
    time_stop: str = Field(None, alias="time_stop")
