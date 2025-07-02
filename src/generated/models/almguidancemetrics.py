"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ALMGuidanceMetricsField = Literal[
    "ad_account_id",
    "adopted_objects",
    "guidance_name",
    "guidance_type",
    "l28_adoption",
    "l28_available",
    "l28_click",
    "l28_conversion",
    "l28_has_click",
    "l28_has_impression",
    "l28_impression",
    "l28_is_actioned",
    "l28_is_adopted",
    "l28_is_available",
    "l28_is_pitched",
    "l28_pitch",
    "l28d_adopted_revenue",
    "last_actioned_ds",
    "last_adopted_ds",
    "last_pitch_ds",
    "parent_advertiser_id",
    "report_ds",
]


class ALMGuidanceMetricsFields(BaseModel):
    """Pydantic model for ALMGuidanceMetrics fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    adopted_objects: list[dict[str, Any]] = Field(None, alias="adopted_objects")
    guidance_name: str = Field(None, alias="guidance_name")
    guidance_type: str = Field(None, alias="guidance_type")
    l28_adoption: int = Field(None, alias="l28_adoption")
    l28_available: int = Field(None, alias="l28_available")
    l28_click: int = Field(None, alias="l28_click")
    l28_conversion: int = Field(None, alias="l28_conversion")
    l28_has_click: bool = Field(None, alias="l28_has_click")
    l28_has_impression: bool = Field(None, alias="l28_has_impression")
    l28_impression: int = Field(None, alias="l28_impression")
    l28_is_actioned: bool = Field(None, alias="l28_is_actioned")
    l28_is_adopted: bool = Field(None, alias="l28_is_adopted")
    l28_is_available: bool = Field(None, alias="l28_is_available")
    l28_is_pitched: bool = Field(None, alias="l28_is_pitched")
    l28_pitch: int = Field(None, alias="l28_pitch")
    l28d_adopted_revenue: float = Field(None, alias="l28d_adopted_revenue")
    last_actioned_ds: str = Field(None, alias="last_actioned_ds")
    last_adopted_ds: str = Field(None, alias="last_adopted_ds")
    last_pitch_ds: str = Field(None, alias="last_pitch_ds")
    parent_advertiser_id: str = Field(None, alias="parent_advertiser_id")
    report_ds: str = Field(None, alias="report_ds")
