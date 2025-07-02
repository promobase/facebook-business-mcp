"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessPartnerPremiumOptionsField = Literal[
    "enable_basket_insight",
    "enable_extended_audience_retargeting",
    "retailer_custom_audience_config",
]


class BusinessPartnerPremiumOptionsFields(BaseModel):
    """Pydantic model for BusinessPartnerPremiumOptions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    enable_basket_insight: bool = Field(None, alias="enable_basket_insight")
    enable_extended_audience_retargeting: bool = Field(
        None, alias="enable_extended_audience_retargeting"
    )
    retailer_custom_audience_config: dict[str, Any] = Field(
        None, alias="retailer_custom_audience_config"
    )
