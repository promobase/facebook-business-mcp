"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DynamicPriceConfigByDateField = Literal["checkin_date", "prices", "prices_pretty"]


class DynamicPriceConfigByDateFields(BaseModel):
    """Pydantic model for DynamicPriceConfigByDate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    checkin_date: str = Field(None, alias="checkin_date")
    prices: str = Field(None, alias="prices")
    prices_pretty: list[dict[str, Any]] = Field(None, alias="prices_pretty")
