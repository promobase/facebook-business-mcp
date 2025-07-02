"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ALMGuidanceField = Literal[
    "ad_account_id",
    "guidances",
    "opportunity_score",
    "parent_advertiser_id",
    "parent_advertiser_name",
]


class ALMGuidanceFields(BaseModel):
    """Pydantic model for ALMGuidance fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    guidances: list[dict[str, Any]] = Field(None, alias="guidances")
    opportunity_score: float = Field(None, alias="opportunity_score")
    parent_advertiser_id: str = Field(None, alias="parent_advertiser_id")
    parent_advertiser_name: str = Field(None, alias="parent_advertiser_name")
