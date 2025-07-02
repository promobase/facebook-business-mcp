"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
McomPayoutsField = Literal[
    "number_of_orders",
    "order_ids",
    "payout_amount",
    "payout_provider_reference_id",
    "payout_status",
    "payout_time",
    "provider",
]


class McomPayoutsFields(BaseModel):
    """Pydantic model for McomPayouts fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    number_of_orders: int = Field(None, alias="number_of_orders")
    order_ids: list[str] = Field(None, alias="order_ids")
    payout_amount: dict[str, Any] = Field(None, alias="payout_amount")
    payout_provider_reference_id: str = Field(None, alias="payout_provider_reference_id")
    payout_status: str = Field(None, alias="payout_status")
    payout_time: int = Field(None, alias="payout_time")
    provider: str = Field(None, alias="provider")
