"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .currencyamount import CurrencyAmountFields
    from .extendedcreditallocationconfig import ExtendedCreditAllocationConfigFields


# Field literal type
ManagedPartnerExtendedCreditField = Literal[
    "id", "max_balance", "receiving_credit_allocation_config"
]


class ManagedPartnerExtendedCreditFields(BaseModel):
    """Pydantic model for ManagedPartnerExtendedCredit fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    max_balance: CurrencyAmountFields = Field(None, alias="max_balance")
    receiving_credit_allocation_config: ExtendedCreditAllocationConfigFields = Field(
        None, alias="receiving_credit_allocation_config"
    )
