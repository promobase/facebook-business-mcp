"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CPASAdvertiserPartnershipRecommendationField = Literal[
    "advertiser_business_id",
    "brand_business_id",
    "brands",
    "countries",
    "id",
    "merchant_business_id",
    "merchant_categories",
    "status",
    "status_reason",
]


class CPASAdvertiserPartnershipRecommendationFields(BaseModel):
    """Pydantic model for CPASAdvertiserPartnershipRecommendation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    advertiser_business_id: str = Field(None, alias="advertiser_business_id")
    brand_business_id: str = Field(None, alias="brand_business_id")
    brands: list[str] = Field(None, alias="brands")
    countries: list[str] = Field(None, alias="countries")
    id: str = Field(None, alias="id")
    merchant_business_id: str = Field(None, alias="merchant_business_id")
    merchant_categories: list[str] = Field(None, alias="merchant_categories")
    status: str = Field(None, alias="status")
    status_reason: str = Field(None, alias="status_reason")
