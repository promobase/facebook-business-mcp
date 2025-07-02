"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountMaxBidField = Literal["max_bid"]


class AdAccountMaxBidFields(BaseModel):
    """Pydantic model for AdAccountMaxBid fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    max_bid: int = Field(None, alias="max_bid")
