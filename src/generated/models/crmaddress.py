"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CRMAddressField = Literal[
    "city",
    "cnpj_tax_id",
    "country",
    "id",
    "postal_code",
    "registration_label",
    "registration_number",
    "state",
    "street1",
    "street2",
    "street3",
    "street4",
    "validation_status",
    "vat_tax_id",
]


class CRMAddressFields(BaseModel):
    """Pydantic model for CRMAddress fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    city: str = Field(None, alias="city")
    cnpj_tax_id: str = Field(None, alias="cnpj_tax_id")
    country: str = Field(None, alias="country")
    id: str = Field(None, alias="id")
    postal_code: str = Field(None, alias="postal_code")
    registration_label: str = Field(None, alias="registration_label")
    registration_number: str = Field(None, alias="registration_number")
    state: str = Field(None, alias="state")
    street1: str = Field(None, alias="street1")
    street2: str = Field(None, alias="street2")
    street3: str = Field(None, alias="street3")
    street4: str = Field(None, alias="street4")
    validation_status: str = Field(None, alias="validation_status")
    vat_tax_id: str = Field(None, alias="vat_tax_id")
