"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .currencyamount import CurrencyAmountFields


# Field literal type
AdAccountPaymentDetailsField = Literal[
    "amount", "create_date", "id", "last_action_status", "metadata", "payment_details_id"
]


class AdAccountPaymentDetailsFields(BaseModel):
    """Pydantic model for AdAccountPaymentDetails fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount: CurrencyAmountFields = Field(None, alias="amount")
    create_date: int = Field(None, alias="create_date")
    id: str = Field(None, alias="id")
    last_action_status: str = Field(None, alias="last_action_status")
    metadata: dict[str, Any] = Field(None, alias="metadata")
    payment_details_id: str = Field(None, alias="payment_details_id")
