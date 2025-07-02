"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
CollaborativeAdsPartnerBusinessesField = Literal[
    "collaborative_ads_partner_businesses_info", "dedicated_partner_business_info"
]


class CollaborativeAdsPartnerBusinessesFields(BaseModel):
    """Pydantic model for CollaborativeAdsPartnerBusinesses fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    collaborative_ads_partner_businesses_info: list[BusinessFields] = Field(
        None, alias="collaborative_ads_partner_businesses_info"
    )
    dedicated_partner_business_info: BusinessFields = Field(
        None, alias="dedicated_partner_business_info"
    )
