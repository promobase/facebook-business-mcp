"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CurrencyField = Literal["currency_offset", "usd_exchange", "usd_exchange_inverse", "user_currency"]


class CurrencyFields(BaseModel):
    """Pydantic model for Currency fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    currency_offset: int = Field(None, alias="currency_offset")
    usd_exchange: float = Field(None, alias="usd_exchange")
    usd_exchange_inverse: float = Field(None, alias="usd_exchange_inverse")
    user_currency: str = Field(None, alias="user_currency")
