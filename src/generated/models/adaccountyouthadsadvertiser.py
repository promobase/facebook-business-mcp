"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountYouthAdsAdvertiserField = Literal["is_youth_ads_advertiser"]


class AdAccountYouthAdsAdvertiserFields(BaseModel):
    """Pydantic model for AdAccountYouthAdsAdvertiser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_youth_ads_advertiser: bool = Field(None, alias="is_youth_ads_advertiser")
