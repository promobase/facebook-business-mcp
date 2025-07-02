"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenThankYouPageGatedPromoField = Literal["id", "online_offer_url", "online_promo_code"]


class LeadGenThankYouPageGatedPromoFields(BaseModel):
    """Pydantic model for LeadGenThankYouPageGatedPromo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    online_offer_url: str = Field(None, alias="online_offer_url")
    online_promo_code: str = Field(None, alias="online_promo_code")
