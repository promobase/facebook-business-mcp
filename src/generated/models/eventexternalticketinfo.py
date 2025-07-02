"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .currencyamount import CurrencyAmountFields


# Field literal type
EventExternalTicketInfoField = Literal["id", "max_sales_price", "min_sales_price", "sales_status"]


class EventExternalTicketInfoFields(BaseModel):
    """Pydantic model for EventExternalTicketInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    max_sales_price: CurrencyAmountFields = Field(None, alias="max_sales_price")
    min_sales_price: CurrencyAmountFields = Field(None, alias="min_sales_price")
    sales_status: str = Field(None, alias="sales_status")
