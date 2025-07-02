"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .fundingsourcedetailscoupon import FundingSourceDetailsCouponFields


# Field literal type
FundingSourceDetailsField = Literal["coupon", "coupons", "display_string", "id", "type"]


class FundingSourceDetailsFields(BaseModel):
    """Pydantic model for FundingSourceDetails fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    coupon: FundingSourceDetailsCouponFields = Field(None, alias="coupon")
    coupons: list[FundingSourceDetailsCouponFields] = Field(None, alias="coupons")
    display_string: str = Field(None, alias="display_string")
    id: str = Field(None, alias="id")
    type: int = Field(None, alias="type")
