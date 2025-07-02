"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPaymentCycleField = Literal[
    "account_id",
    "created_time",
    "multiplier",
    "requested_threshold_amount",
    "threshold_amount",
    "updated_time",
]


class AdsPaymentCycleFields(BaseModel):
    """Pydantic model for AdsPaymentCycle fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    created_time: datetime = Field(None, alias="created_time")
    multiplier: int = Field(None, alias="multiplier")
    requested_threshold_amount: int = Field(None, alias="requested_threshold_amount")
    threshold_amount: int = Field(None, alias="threshold_amount")
    updated_time: datetime = Field(None, alias="updated_time")
