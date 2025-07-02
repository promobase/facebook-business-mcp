"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PaymentRequestDetailsField = Literal[
    "amount",
    "creation_time",
    "note",
    "payment_request_id",
    "receiver_id",
    "reference_number",
    "sender_id",
    "status",
    "transaction_time",
]


class PaymentRequestDetailsFields(BaseModel):
    """Pydantic model for PaymentRequestDetails fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount: dict[str, Any] = Field(None, alias="amount")
    creation_time: int = Field(None, alias="creation_time")
    note: str = Field(None, alias="note")
    payment_request_id: str = Field(None, alias="payment_request_id")
    receiver_id: str = Field(None, alias="receiver_id")
    reference_number: str = Field(None, alias="reference_number")
    sender_id: str = Field(None, alias="sender_id")
    status: str = Field(None, alias="status")
    transaction_time: int = Field(None, alias="transaction_time")
