"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsCustomPivotsPreviewField = Literal[
    "account_id",
    "account_name",
    "ad_id",
    "ad_name",
    "adset_id",
    "adset_name",
    "campaign_id",
    "campaign_name",
    "custom_breakdown",
]


class AdsCustomPivotsPreviewFields(BaseModel):
    """Pydantic model for AdsCustomPivotsPreview fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    account_name: str = Field(None, alias="account_name")
    ad_id: str = Field(None, alias="ad_id")
    ad_name: str = Field(None, alias="ad_name")
    adset_id: str = Field(None, alias="adset_id")
    adset_name: str = Field(None, alias="adset_name")
    campaign_id: str = Field(None, alias="campaign_id")
    campaign_name: str = Field(None, alias="campaign_name")
    custom_breakdown: list[str] = Field(None, alias="custom_breakdown")
