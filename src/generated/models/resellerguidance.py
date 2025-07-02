"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
ResellerGuidanceField = Literal[
    "ad_account_first_spend_date",
    "ad_account_id",
    "adopted_guidance_l7d",
    "advertiser_name",
    "attributed_to_reseller_l7d",
    "available_guidance",
    "guidance_adoption_rate_l7d",
    "nurtured_by_reseller_l7d",
    "planning_agency_name",
    "recommendation_time",
    "reporting_ds",
    "reseller",
    "revenue_l30d",
    "ultimate_advertiser_name",
]


class ResellerGuidanceFields(BaseModel):
    """Pydantic model for ResellerGuidance fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_first_spend_date: str = Field(None, alias="ad_account_first_spend_date")
    ad_account_id: str = Field(None, alias="ad_account_id")
    adopted_guidance_l7d: list[str] = Field(None, alias="adopted_guidance_l7d")
    advertiser_name: str = Field(None, alias="advertiser_name")
    attributed_to_reseller_l7d: bool = Field(None, alias="attributed_to_reseller_l7d")
    available_guidance: list[str] = Field(None, alias="available_guidance")
    guidance_adoption_rate_l7d: float = Field(None, alias="guidance_adoption_rate_l7d")
    nurtured_by_reseller_l7d: bool = Field(None, alias="nurtured_by_reseller_l7d")
    planning_agency_name: str = Field(None, alias="planning_agency_name")
    recommendation_time: datetime = Field(None, alias="recommendation_time")
    reporting_ds: str = Field(None, alias="reporting_ds")
    reseller: BusinessFields = Field(None, alias="reseller")
    revenue_l30d: float = Field(None, alias="revenue_l30d")
    ultimate_advertiser_name: str = Field(None, alias="ultimate_advertiser_name")
