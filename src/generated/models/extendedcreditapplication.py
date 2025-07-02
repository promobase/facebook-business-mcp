"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .currencyamount import CurrencyAmountFields
    from .user import UserFields


# Field literal type
ExtendedCreditApplicationField = Literal[
    "billing_country",
    "city",
    "cnpj",
    "country",
    "display_currency",
    "duns_number",
    "id",
    "invoice_email_address",
    "is_umi",
    "legal_entity_name",
    "original_online_limit",
    "phone_number",
    "postal_code",
    "product_types",
    "proposed_credit_limit",
    "registration_number",
    "run_id",
    "state",
    "status",
    "street1",
    "street2",
    "submitter",
    "tax_exempt_status",
    "tax_id",
    "terms",
]


class ExtendedCreditApplicationFields(BaseModel):
    """Pydantic model for ExtendedCreditApplication fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    billing_country: str = Field(None, alias="billing_country")
    city: str = Field(None, alias="city")
    cnpj: str = Field(None, alias="cnpj")
    country: str = Field(None, alias="country")
    display_currency: str = Field(None, alias="display_currency")
    duns_number: str = Field(None, alias="duns_number")
    id: str = Field(None, alias="id")
    invoice_email_address: str = Field(None, alias="invoice_email_address")
    is_umi: bool = Field(None, alias="is_umi")
    legal_entity_name: str = Field(None, alias="legal_entity_name")
    original_online_limit: CurrencyAmountFields = Field(None, alias="original_online_limit")
    phone_number: str = Field(None, alias="phone_number")
    postal_code: str = Field(None, alias="postal_code")
    product_types: list[str] = Field(None, alias="product_types")
    proposed_credit_limit: CurrencyAmountFields = Field(None, alias="proposed_credit_limit")
    registration_number: str = Field(None, alias="registration_number")
    run_id: str = Field(None, alias="run_id")
    state: str = Field(None, alias="state")
    status: str = Field(None, alias="status")
    street1: str = Field(None, alias="street1")
    street2: str = Field(None, alias="street2")
    submitter: UserFields = Field(None, alias="submitter")
    tax_exempt_status: str = Field(None, alias="tax_exempt_status")
    tax_id: str = Field(None, alias="tax_id")
    terms: str = Field(None, alias="terms")
