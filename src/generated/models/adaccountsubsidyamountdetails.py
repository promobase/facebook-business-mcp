"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .currencyamount import CurrencyAmountFields


# Field literal type
AdAccountSubsidyAmountDetailsField = Literal["entered_amount", "fee_amount", "total_amount"]


class AdAccountSubsidyAmountDetailsFields(BaseModel):
    """Pydantic model for AdAccountSubsidyAmountDetails fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    entered_amount: CurrencyAmountFields = Field(None, alias="entered_amount")
    fee_amount: CurrencyAmountFields = Field(None, alias="fee_amount")
    total_amount: CurrencyAmountFields = Field(None, alias="total_amount")
