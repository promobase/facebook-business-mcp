"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountPromotionProgressBarField = Literal[
    "adaccount_permission",
    "coupon_currency",
    "coupon_value",
    "expiration_time",
    "progress_completed",
    "promotion_type",
    "spend_requirement_in_cent",
    "spend_since_enrollment",
]


class AdAccountPromotionProgressBarFields(BaseModel):
    """Pydantic model for AdAccountPromotionProgressBar fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adaccount_permission: bool = Field(None, alias="adaccount_permission")
    coupon_currency: str = Field(None, alias="coupon_currency")
    coupon_value: int = Field(None, alias="coupon_value")
    expiration_time: datetime = Field(None, alias="expiration_time")
    progress_completed: bool = Field(None, alias="progress_completed")
    promotion_type: str = Field(None, alias="promotion_type")
    spend_requirement_in_cent: int = Field(None, alias="spend_requirement_in_cent")
    spend_since_enrollment: int = Field(None, alias="spend_since_enrollment")
