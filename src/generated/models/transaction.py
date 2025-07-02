"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class Transaction_product_type(str, Enum):
    """Transaction_product_type enum values."""

    cp_return_label = "cp_return_label"
    facebook_ad = "facebook_ad"
    ig_ad = "ig_ad"
    whatsapp = "whatsapp"
    workplace = "workplace"


# Field literal type
TransactionField = Literal[
    "account_id",
    "app_amount",
    "billing_end_time",
    "billing_reason",
    "billing_start_time",
    "card_charge_mode",
    "charge_type",
    "checkout_campaign_group_id",
    "credential_id",
    "fatura_id",
    "id",
    "is_business_ec_charge",
    "is_funding_event",
    "payment_option",
    "product_type",
    "provider_amount",
    "status",
    "time",
    "tracking_id",
    "transaction_type",
    "tx_type",
    "vat_invoice_id",
]


class TransactionFields(BaseModel):
    """Pydantic model for Transaction fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    app_amount: dict[str, Any] = Field(None, alias="app_amount")
    billing_end_time: int = Field(None, alias="billing_end_time")
    billing_reason: str = Field(None, alias="billing_reason")
    billing_start_time: int = Field(None, alias="billing_start_time")
    card_charge_mode: int = Field(None, alias="card_charge_mode")
    charge_type: str = Field(None, alias="charge_type")
    checkout_campaign_group_id: str = Field(None, alias="checkout_campaign_group_id")
    credential_id: str = Field(None, alias="credential_id")
    fatura_id: int = Field(None, alias="fatura_id")
    id: str = Field(None, alias="id")
    is_business_ec_charge: bool = Field(None, alias="is_business_ec_charge")
    is_funding_event: bool = Field(None, alias="is_funding_event")
    payment_option: str = Field(None, alias="payment_option")
    product_type: dict[str, Any] = Field(None, alias="product_type")
    provider_amount: dict[str, Any] = Field(None, alias="provider_amount")
    status: str = Field(None, alias="status")
    time: int = Field(None, alias="time")
    tracking_id: str = Field(None, alias="tracking_id")
    transaction_type: str = Field(None, alias="transaction_type")
    tx_type: int = Field(None, alias="tx_type")
    vat_invoice_id: str = Field(None, alias="vat_invoice_id")
