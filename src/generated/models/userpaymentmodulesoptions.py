"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserPaymentModulesOptionsField = Literal[
    "account_id", "available_payment_options", "country", "currency"
]


class UserPaymentModulesOptionsFields(BaseModel):
    """Pydantic model for UserPaymentModulesOptions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    available_payment_options: list[dict[str, Any]] = Field(None, alias="available_payment_options")
    country: str = Field(None, alias="country")
    currency: str = Field(None, alias="currency")
