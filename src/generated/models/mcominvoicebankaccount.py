"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
McomInvoiceBankAccountField = Literal[
    "num_pending_verification_accounts",
    "num_verified_accounts",
    "pending_verification_accounts",
    "verified_accounts",
]


class McomInvoiceBankAccountFields(BaseModel):
    """Pydantic model for McomInvoiceBankAccount fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    num_pending_verification_accounts: int = Field(None, alias="num_pending_verification_accounts")
    num_verified_accounts: int = Field(None, alias="num_verified_accounts")
    pending_verification_accounts: list[dict[str, Any]] = Field(
        None, alias="pending_verification_accounts"
    )
    verified_accounts: list[dict[str, Any]] = Field(None, alias="verified_accounts")
