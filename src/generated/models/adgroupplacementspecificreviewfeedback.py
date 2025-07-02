"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdgroupPlacementSpecificReviewFeedbackField = Literal[
    "account_admin",
    "ad",
    "ads_conversion_experiences",
    "b2c",
    "b2c_commerce_unified",
    "bsg",
    "city_community",
    "commerce",
    "compromise",
    "daily_deals",
    "daily_deals_legacy",
    "dpa",
    "dri_copyright",
    "dri_counterfeit",
    "facebook",
    "facebook_pages_live_shopping",
    "independent_work",
    "instagram",
    "instagram_shop",
    "job_search",
    "lead_gen_honeypot",
    "marketplace",
    "marketplace_home_rentals",
    "marketplace_home_sales",
    "marketplace_motors",
    "marketplace_shops",
    "max_review_placements",
    "neighborhoods",
    "page_admin",
    "product",
    "product_service",
    "profile",
    "seller",
    "shops",
    "traffic_quality",
    "unified_commerce_content",
    "whatsapp",
]


class AdgroupPlacementSpecificReviewFeedbackFields(BaseModel):
    """Pydantic model for AdgroupPlacementSpecificReviewFeedback fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_admin: dict[str, str] = Field(None, alias="account_admin")
    ad: dict[str, str] = Field(None, alias="ad")
    ads_conversion_experiences: dict[str, str] = Field(None, alias="ads_conversion_experiences")
    b2c: dict[str, str] = Field(None, alias="b2c")
    b2c_commerce_unified: dict[str, str] = Field(None, alias="b2c_commerce_unified")
    bsg: dict[str, str] = Field(None, alias="bsg")
    city_community: dict[str, str] = Field(None, alias="city_community")
    commerce: dict[str, str] = Field(None, alias="commerce")
    compromise: dict[str, str] = Field(None, alias="compromise")
    daily_deals: dict[str, str] = Field(None, alias="daily_deals")
    daily_deals_legacy: dict[str, str] = Field(None, alias="daily_deals_legacy")
    dpa: dict[str, str] = Field(None, alias="dpa")
    dri_copyright: dict[str, str] = Field(None, alias="dri_copyright")
    dri_counterfeit: dict[str, str] = Field(None, alias="dri_counterfeit")
    facebook: dict[str, str] = Field(None, alias="facebook")
    facebook_pages_live_shopping: dict[str, str] = Field(None, alias="facebook_pages_live_shopping")
    independent_work: dict[str, str] = Field(None, alias="independent_work")
    instagram: dict[str, str] = Field(None, alias="instagram")
    instagram_shop: dict[str, str] = Field(None, alias="instagram_shop")
    job_search: dict[str, str] = Field(None, alias="job_search")
    lead_gen_honeypot: dict[str, str] = Field(None, alias="lead_gen_honeypot")
    marketplace: dict[str, str] = Field(None, alias="marketplace")
    marketplace_home_rentals: dict[str, str] = Field(None, alias="marketplace_home_rentals")
    marketplace_home_sales: dict[str, str] = Field(None, alias="marketplace_home_sales")
    marketplace_motors: dict[str, str] = Field(None, alias="marketplace_motors")
    marketplace_shops: dict[str, str] = Field(None, alias="marketplace_shops")
    max_review_placements: dict[str, str] = Field(None, alias="max_review_placements")
    neighborhoods: dict[str, str] = Field(None, alias="neighborhoods")
    page_admin: dict[str, str] = Field(None, alias="page_admin")
    product: dict[str, str] = Field(None, alias="product")
    product_service: dict[str, str] = Field(None, alias="product_service")
    profile: dict[str, str] = Field(None, alias="profile")
    seller: dict[str, str] = Field(None, alias="seller")
    shops: dict[str, str] = Field(None, alias="shops")
    traffic_quality: dict[str, str] = Field(None, alias="traffic_quality")
    unified_commerce_content: dict[str, str] = Field(None, alias="unified_commerce_content")
    whatsapp: dict[str, str] = Field(None, alias="whatsapp")
