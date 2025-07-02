"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .crmaddress import CRMAddressFields
    from .extendedcreditemail import ExtendedCreditEmailFields


# Field literal type
ExtendedCreditInvoiceGroupField = Literal[
    "auto_enroll",
    "bill_to_address",
    "customer_po_number",
    "email",
    "emails",
    "id",
    "liable_address",
    "name",
    "sold_to_address",
]


class ExtendedCreditInvoiceGroupFields(BaseModel):
    """Pydantic model for ExtendedCreditInvoiceGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    auto_enroll: bool = Field(None, alias="auto_enroll")
    bill_to_address: CRMAddressFields = Field(None, alias="bill_to_address")
    customer_po_number: str = Field(None, alias="customer_po_number")
    email: ExtendedCreditEmailFields = Field(None, alias="email")
    emails: list[str] = Field(None, alias="emails")
    id: str = Field(None, alias="id")
    liable_address: CRMAddressFields = Field(None, alias="liable_address")
    name: str = Field(None, alias="name")
    sold_to_address: CRMAddressFields = Field(None, alias="sold_to_address")


class ExtendedCreditInvoiceGroupDeleteAdAccountsParams(BaseModel):
    """Parameters for ExtendedCreditInvoiceGroup.delete_ad_accounts()."""

    model_config = ConfigDict(extra="forbid")
    ad_account_id: str | None = Field(None, description="ad_account_id parameter")


class ExtendedCreditInvoiceGroupCreateAdAccountParams(BaseModel):
    """Parameters for ExtendedCreditInvoiceGroup.create_ad_account()."""

    model_config = ConfigDict(extra="forbid")
    ad_account_id: str | None = Field(None, description="ad_account_id parameter")
