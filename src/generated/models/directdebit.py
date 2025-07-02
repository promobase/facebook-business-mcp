"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DirectDebitField = Literal[
    "bank_account_last_4",
    "bank_code_last_4",
    "bank_name",
    "default_receiving_method_products",
    "display_string",
    "id",
    "last_four_digits",
    "onboarding_url",
    "owner_name",
    "status",
]


class DirectDebitFields(BaseModel):
    """Pydantic model for DirectDebit fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    bank_account_last_4: str = Field(None, alias="bank_account_last_4")
    bank_code_last_4: str = Field(None, alias="bank_code_last_4")
    bank_name: str = Field(None, alias="bank_name")
    default_receiving_method_products: list[str] = Field(
        None, alias="default_receiving_method_products"
    )
    display_string: str = Field(None, alias="display_string")
    id: str = Field(None, alias="id")
    last_four_digits: str = Field(None, alias="last_four_digits")
    onboarding_url: str = Field(None, alias="onboarding_url")
    owner_name: str = Field(None, alias="owner_name")
    status: int = Field(None, alias="status")
