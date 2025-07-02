"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdEntityTargetSpendField = Literal[
    "amount", "has_error", "is_accurate", "is_prorated", "is_updating"
]


class AdEntityTargetSpendFields(BaseModel):
    """Pydantic model for AdEntityTargetSpend fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount: str = Field(None, alias="amount")
    has_error: bool = Field(None, alias="has_error")
    is_accurate: bool = Field(None, alias="is_accurate")
    is_prorated: bool = Field(None, alias="is_prorated")
    is_updating: bool = Field(None, alias="is_updating")
