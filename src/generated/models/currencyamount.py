"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CurrencyAmountField = Literal["amount", "amount_in_hundredths", "currency", "offsetted_amount"]


class CurrencyAmountFields(BaseModel):
    """Pydantic model for CurrencyAmount fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount: str = Field(None, alias="amount")
    amount_in_hundredths: str = Field(None, alias="amount_in_hundredths")
    currency: str = Field(None, alias="currency")
    offsetted_amount: str = Field(None, alias="offsetted_amount")
