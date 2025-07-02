"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
McomInvoiceStatusField = Literal[
    "bank_account_number",
    "bank_code",
    "invoice_id",
    "invoice_status",
    "page_id",
    "payment_method",
    "payment_type",
    "payout_amount",
    "slip_verification_error",
    "slip_verification_status",
    "transaction_fee",
    "transfer_slip",
]


class McomInvoiceStatusFields(BaseModel):
    """Pydantic model for McomInvoiceStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    bank_account_number: str = Field(None, alias="bank_account_number")
    bank_code: str = Field(None, alias="bank_code")
    invoice_id: str = Field(None, alias="invoice_id")
    invoice_status: str = Field(None, alias="invoice_status")
    page_id: str = Field(None, alias="page_id")
    payment_method: str = Field(None, alias="payment_method")
    payment_type: str = Field(None, alias="payment_type")
    payout_amount: dict[str, Any] = Field(None, alias="payout_amount")
    slip_verification_error: str = Field(None, alias="slip_verification_error")
    slip_verification_status: str = Field(None, alias="slip_verification_status")
    transaction_fee: dict[str, Any] = Field(None, alias="transaction_fee")
    transfer_slip: str = Field(None, alias="transfer_slip")
