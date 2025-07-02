"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountSpendCapChangeHistoryField = Literal["action", "spend_cap", "time_start", "time_stop"]


class AdAccountSpendCapChangeHistoryFields(BaseModel):
    """Pydantic model for AdAccountSpendCapChangeHistory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action: str = Field(None, alias="action")
    spend_cap: int = Field(None, alias="spend_cap")
    time_start: str = Field(None, alias="time_start")
    time_stop: str = Field(None, alias="time_stop")
