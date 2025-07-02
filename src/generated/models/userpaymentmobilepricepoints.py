"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserPaymentMobilePricepointsField = Literal[
    "mobile_country", "phone_number_last4", "pricepoints", "user_currency"
]


class UserPaymentMobilePricepointsFields(BaseModel):
    """Pydantic model for UserPaymentMobilePricepoints fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    mobile_country: str = Field(None, alias="mobile_country")
    phone_number_last4: str = Field(None, alias="phone_number_last4")
    pricepoints: list[dict[str, Any]] = Field(None, alias="pricepoints")
    user_currency: str = Field(None, alias="user_currency")
