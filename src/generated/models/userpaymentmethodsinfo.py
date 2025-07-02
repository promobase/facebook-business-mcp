"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserPaymentMethodsInfoField = Literal[
    "account_id",
    "available_card_types",
    "available_payment_methods",
    "available_payment_methods_details",
    "country",
    "currency",
    "existing_payment_methods",
]


class UserPaymentMethodsInfoFields(BaseModel):
    """Pydantic model for UserPaymentMethodsInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    available_card_types: list[str] = Field(None, alias="available_card_types")
    available_payment_methods: list[str] = Field(None, alias="available_payment_methods")
    available_payment_methods_details: list[dict[str, Any]] = Field(
        None, alias="available_payment_methods_details"
    )
    country: str = Field(None, alias="country")
    currency: str = Field(None, alias="currency")
    existing_payment_methods: list[dict[str, Any]] = Field(None, alias="existing_payment_methods")
