"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountSpendLimitField = Literal[
    "amount_spent", "group_id", "limit_id", "limit_value", "time_created", "time_start", "time_stop"
]


class AdAccountSpendLimitFields(BaseModel):
    """Pydantic model for AdAccountSpendLimit fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount_spent: str = Field(None, alias="amount_spent")
    group_id: str = Field(None, alias="group_id")
    limit_id: str = Field(None, alias="limit_id")
    limit_value: str = Field(None, alias="limit_value")
    time_created: int = Field(None, alias="time_created")
    time_start: int = Field(None, alias="time_start")
    time_stop: int = Field(None, alias="time_stop")
