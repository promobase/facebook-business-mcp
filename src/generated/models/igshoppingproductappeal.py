"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGShoppingProductAppealField = Literal[
    "eligible_for_appeal",
    "product_appeal_status",
    "product_id",
    "rejection_reasons",
    "review_status",
]


class IGShoppingProductAppealFields(BaseModel):
    """Pydantic model for IGShoppingProductAppeal fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    eligible_for_appeal: bool = Field(None, alias="eligible_for_appeal")
    product_appeal_status: str = Field(None, alias="product_appeal_status")
    product_id: int = Field(None, alias="product_id")
    rejection_reasons: list[str] = Field(None, alias="rejection_reasons")
    review_status: str = Field(None, alias="review_status")
