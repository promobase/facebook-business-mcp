"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
FundingSourceDetailsCouponTieringField = Literal[
    "coupon_tiering_new", "coupon_tiering_reactivation"
]


class FundingSourceDetailsCouponTieringFields(BaseModel):
    """Pydantic model for FundingSourceDetailsCouponTiering fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    coupon_tiering_new: dict[str, Any] = Field(None, alias="coupon_tiering_new")
    coupon_tiering_reactivation: dict[str, Any] = Field(None, alias="coupon_tiering_reactivation")
