"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CommercePayoutField = Literal[
    "amount", "payout_date", "payout_reference_id", "status", "transfer_id"
]


class CommercePayoutFields(BaseModel):
    """Pydantic model for CommercePayout fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount: dict[str, Any] = Field(None, alias="amount")
    payout_date: str = Field(None, alias="payout_date")
    payout_reference_id: str = Field(None, alias="payout_reference_id")
    status: str = Field(None, alias="status")
    transfer_id: str = Field(None, alias="transfer_id")
