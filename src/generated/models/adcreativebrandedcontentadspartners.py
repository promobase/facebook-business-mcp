"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeBrandedContentAdsPartnersField = Literal[
    "fb_page_id", "has_create_ads_access", "identity_type", "ig_asset_id", "ig_user_id"
]


class AdCreativeBrandedContentAdsPartnersFields(BaseModel):
    """Pydantic model for AdCreativeBrandedContentAdsPartners fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    fb_page_id: str = Field(None, alias="fb_page_id")
    has_create_ads_access: bool = Field(None, alias="has_create_ads_access")
    identity_type: str = Field(None, alias="identity_type")
    ig_asset_id: str = Field(None, alias="ig_asset_id")
    ig_user_id: str = Field(None, alias="ig_user_id")
