"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountPaymentOptionsField = Literal[
    "available_altpay_options",
    "available_card_types",
    "available_payment_options",
    "existing_payment_methods",
]


class AdAccountPaymentOptionsFields(BaseModel):
    """Pydantic model for AdAccountPaymentOptions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    available_altpay_options: list[dict[str, Any]] = Field(None, alias="available_altpay_options")
    available_card_types: list[str] = Field(None, alias="available_card_types")
    available_payment_options: list[str] = Field(None, alias="available_payment_options")
    existing_payment_methods: list[dict[str, Any]] = Field(None, alias="existing_payment_methods")
