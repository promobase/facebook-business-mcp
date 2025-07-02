"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
McomInvoiceDetailsField = Literal[
    "additional_amounts",
    "buyer_notes",
    "currency_amount",
    "external_invoice_id",
    "features",
    "invoice_created",
    "invoice_id",
    "invoice_instructions",
    "invoice_instructions_image_url",
    "invoice_updated",
    "outstanding_amount",
    "paid_amount",
    "payments",
    "platform_logo_url",
    "platform_name",
    "product_items",
    "shipping_address",
    "status",
    "tracking_info",
]


class McomInvoiceDetailsFields(BaseModel):
    """Pydantic model for McomInvoiceDetails fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    additional_amounts: list[dict[str, Any]] = Field(None, alias="additional_amounts")
    buyer_notes: str = Field(None, alias="buyer_notes")
    currency_amount: dict[str, Any] = Field(None, alias="currency_amount")
    external_invoice_id: str = Field(None, alias="external_invoice_id")
    features: dict[str, Any] = Field(None, alias="features")
    invoice_created: int = Field(None, alias="invoice_created")
    invoice_id: str = Field(None, alias="invoice_id")
    invoice_instructions: str = Field(None, alias="invoice_instructions")
    invoice_instructions_image_url: str = Field(None, alias="invoice_instructions_image_url")
    invoice_updated: int = Field(None, alias="invoice_updated")
    outstanding_amount: dict[str, Any] = Field(None, alias="outstanding_amount")
    paid_amount: dict[str, Any] = Field(None, alias="paid_amount")
    payments: list[dict[str, Any]] = Field(None, alias="payments")
    platform_logo_url: str = Field(None, alias="platform_logo_url")
    platform_name: str = Field(None, alias="platform_name")
    product_items: list[dict[str, Any]] = Field(None, alias="product_items")
    shipping_address: dict[str, Any] = Field(None, alias="shipping_address")
    status: str = Field(None, alias="status")
    tracking_info: dict[str, Any] = Field(None, alias="tracking_info")
