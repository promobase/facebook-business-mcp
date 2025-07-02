"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .fundingsourcedetailscoupontiering import FundingSourceDetailsCouponTieringFields


# Field literal type
FundingSourceDetailsCouponField = Literal[
    "amount",
    "campaign_ids",
    "child_ad_account_id",
    "child_bm_id",
    "coupon_id",
    "coupon_tiering",
    "currency",
    "display_amount",
    "expiration",
    "original_amount",
    "original_display_amount",
    "start_date",
    "vendor_id",
]


class FundingSourceDetailsCouponFields(BaseModel):
    """Pydantic model for FundingSourceDetailsCoupon fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount: int = Field(None, alias="amount")
    campaign_ids: list[int] = Field(None, alias="campaign_ids")
    child_ad_account_id: str = Field(None, alias="child_ad_account_id")
    child_bm_id: str = Field(None, alias="child_bm_id")
    coupon_id: str = Field(None, alias="coupon_id")
    coupon_tiering: FundingSourceDetailsCouponTieringFields = Field(None, alias="coupon_tiering")
    currency: str = Field(None, alias="currency")
    display_amount: str = Field(None, alias="display_amount")
    expiration: datetime = Field(None, alias="expiration")
    original_amount: int = Field(None, alias="original_amount")
    original_display_amount: str = Field(None, alias="original_display_amount")
    start_date: datetime = Field(None, alias="start_date")
    vendor_id: str = Field(None, alias="vendor_id")
