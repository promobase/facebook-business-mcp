"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CreditCardField = Literal[
    "billing_address",
    "card_cobadging",
    "card_holder_name",
    "card_type",
    "credential_id",
    "default_receiving_method_products",
    "expiry_month",
    "expiry_year",
    "id",
    "is_cvv_tricky_bin",
    "is_enabled",
    "is_last_used",
    "is_network_tokenized_in_india",
    "is_soft_disabled",
    "is_user_verified",
    "is_zip_verified",
    "last4",
    "readable_card_type",
    "time_created",
    "time_created_ts",
    "type",
]


class CreditCardFields(BaseModel):
    """Pydantic model for CreditCard fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    billing_address: dict[str, Any] = Field(None, alias="billing_address")
    card_cobadging: str = Field(None, alias="card_cobadging")
    card_holder_name: str = Field(None, alias="card_holder_name")
    card_type: str = Field(None, alias="card_type")
    credential_id: int = Field(None, alias="credential_id")
    default_receiving_method_products: list[str] = Field(
        None, alias="default_receiving_method_products"
    )
    expiry_month: str = Field(None, alias="expiry_month")
    expiry_year: str = Field(None, alias="expiry_year")
    id: str = Field(None, alias="id")
    is_cvv_tricky_bin: bool = Field(None, alias="is_cvv_tricky_bin")
    is_enabled: bool = Field(None, alias="is_enabled")
    is_last_used: bool = Field(None, alias="is_last_used")
    is_network_tokenized_in_india: bool = Field(None, alias="is_network_tokenized_in_india")
    is_soft_disabled: bool = Field(None, alias="is_soft_disabled")
    is_user_verified: bool = Field(None, alias="is_user_verified")
    is_zip_verified: bool = Field(None, alias="is_zip_verified")
    last4: str = Field(None, alias="last4")
    readable_card_type: str = Field(None, alias="readable_card_type")
    time_created: datetime = Field(None, alias="time_created")
    time_created_ts: int = Field(None, alias="time_created_ts")
    type: str = Field(None, alias="type")
