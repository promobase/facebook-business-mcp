"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BrandedContentShadowIGMediaIDField = Literal[
    "eligibility_errors",
    "has_permission_for_partnership_ad",
    "id",
    "owner_id",
    "permalink",
    "recommended_campaign_objectives",
]


class BrandedContentShadowIGMediaIDFields(BaseModel):
    """Pydantic model for BrandedContentShadowIGMediaID fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    eligibility_errors: list[str] = Field(None, alias="eligibility_errors")
    has_permission_for_partnership_ad: bool = Field(None, alias="has_permission_for_partnership_ad")
    id: str = Field(None, alias="id")
    owner_id: str = Field(None, alias="owner_id")
    permalink: str = Field(None, alias="permalink")
    recommended_campaign_objectives: list[str] = Field(
        None, alias="recommended_campaign_objectives"
    )
