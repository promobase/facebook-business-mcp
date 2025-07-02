"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .currencyamount import CurrencyAmountFields


# Field literal type
OmegaCustomerTrxField = Literal[
    "ad_account_ids",
    "advertiser_name",
    "amount",
    "amount_due",
    "billed_amount_details",
    "billing_period",
    "cdn_download_uri",
    "currency",
    "download_uri",
    "due_date",
    "entity",
    "id",
    "invoice_date",
    "invoice_id",
    "invoice_type",
    "liability_type",
    "payment_status",
    "payment_term",
    "type",
]


class OmegaCustomerTrxFields(BaseModel):
    """Pydantic model for OmegaCustomerTrx fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_ids: list[str] = Field(None, alias="ad_account_ids")
    advertiser_name: str = Field(None, alias="advertiser_name")
    amount: str = Field(None, alias="amount")
    amount_due: CurrencyAmountFields = Field(None, alias="amount_due")
    billed_amount_details: dict[str, Any] = Field(None, alias="billed_amount_details")
    billing_period: str = Field(None, alias="billing_period")
    cdn_download_uri: str = Field(None, alias="cdn_download_uri")
    currency: str = Field(None, alias="currency")
    download_uri: str = Field(None, alias="download_uri")
    due_date: datetime = Field(None, alias="due_date")
    entity: str = Field(None, alias="entity")
    id: str = Field(None, alias="id")
    invoice_date: datetime = Field(None, alias="invoice_date")
    invoice_id: str = Field(None, alias="invoice_id")
    invoice_type: str = Field(None, alias="invoice_type")
    liability_type: str = Field(None, alias="liability_type")
    payment_status: str = Field(None, alias="payment_status")
    payment_term: str = Field(None, alias="payment_term")
    type: str = Field(None, alias="type")
