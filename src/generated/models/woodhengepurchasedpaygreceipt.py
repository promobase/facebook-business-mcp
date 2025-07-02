"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
WoodhengePurchasedPAYGReceiptField = Literal[
    "id", "number_of_subscriptions_purchased", "purchase_time", "user"
]


class WoodhengePurchasedPAYGReceiptFields(BaseModel):
    """Pydantic model for WoodhengePurchasedPAYGReceipt fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    number_of_subscriptions_purchased: int = Field(None, alias="number_of_subscriptions_purchased")
    purchase_time: datetime = Field(None, alias="purchase_time")
    user: UserFields = Field(None, alias="user")
