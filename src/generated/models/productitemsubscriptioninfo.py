"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemSubscriptionInfoField = Literal[
    "is_subscribable", "subscription_billing_period", "subscription_billing_type"
]


class ProductItemSubscriptionInfoFields(BaseModel):
    """Pydantic model for ProductItemSubscriptionInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_subscribable: bool = Field(None, alias="is_subscribable")
    subscription_billing_period: int = Field(None, alias="subscription_billing_period")
    subscription_billing_type: str = Field(None, alias="subscription_billing_type")
