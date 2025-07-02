"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .commerceorder import CommerceOrderFields


# Field literal type
CommerceOrderTransactionDetailField = Literal[
    "merchant_order_id",
    "net_payment_amount",
    "order_created",
    "order_details",
    "order_id",
    "payout_reference_id",
    "postal_code",
    "processing_fee",
    "state",
    "tax_rate",
    "transaction_date",
    "transaction_type",
    "transfer_id",
]


class CommerceOrderTransactionDetailFields(BaseModel):
    """Pydantic model for CommerceOrderTransactionDetail fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    merchant_order_id: str = Field(None, alias="merchant_order_id")
    net_payment_amount: dict[str, Any] = Field(None, alias="net_payment_amount")
    order_created: str = Field(None, alias="order_created")
    order_details: CommerceOrderFields = Field(None, alias="order_details")
    order_id: str = Field(None, alias="order_id")
    payout_reference_id: str = Field(None, alias="payout_reference_id")
    postal_code: str = Field(None, alias="postal_code")
    processing_fee: dict[str, Any] = Field(None, alias="processing_fee")
    state: str = Field(None, alias="state")
    tax_rate: str = Field(None, alias="tax_rate")
    transaction_date: str = Field(None, alias="transaction_date")
    transaction_type: str = Field(None, alias="transaction_type")
    transfer_id: str = Field(None, alias="transfer_id")
