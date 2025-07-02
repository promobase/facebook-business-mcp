"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PagePaymentOptionsField = Literal["amex", "cash_only", "discover", "mastercard", "visa"]


class PagePaymentOptionsFields(BaseModel):
    """Pydantic model for PagePaymentOptions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amex: int = Field(None, alias="amex")
    cash_only: int = Field(None, alias="cash_only")
    discover: int = Field(None, alias="discover")
    mastercard: int = Field(None, alias="mastercard")
    visa: int = Field(None, alias="visa")
