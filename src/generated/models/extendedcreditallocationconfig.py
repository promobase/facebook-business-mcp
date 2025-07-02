"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .currencyamount import CurrencyAmountFields
    from .extendedcredit import ExtendedCreditFields


# Field literal type
ExtendedCreditAllocationConfigField = Literal[
    "currency_amount",
    "id",
    "liability_type",
    "owning_business",
    "owning_credential",
    "partition_type",
    "receiving_business",
    "receiving_credential",
    "request_status",
    "send_bill_to",
]


class ExtendedCreditAllocationConfigFields(BaseModel):
    """Pydantic model for ExtendedCreditAllocationConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    currency_amount: CurrencyAmountFields = Field(None, alias="currency_amount")
    id: str = Field(None, alias="id")
    liability_type: str = Field(None, alias="liability_type")
    owning_business: BusinessFields = Field(None, alias="owning_business")
    owning_credential: ExtendedCreditFields = Field(None, alias="owning_credential")
    partition_type: str = Field(None, alias="partition_type")
    receiving_business: BusinessFields = Field(None, alias="receiving_business")
    receiving_credential: ExtendedCreditFields = Field(None, alias="receiving_credential")
    request_status: str = Field(None, alias="request_status")
    send_bill_to: str = Field(None, alias="send_bill_to")
