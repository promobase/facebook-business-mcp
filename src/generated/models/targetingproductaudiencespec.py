"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .targetingproductaudiencesubspec import TargetingProductAudienceSubSpecFields


# Field literal type
TargetingProductAudienceSpecField = Literal["exclusions", "inclusions", "product_set_id"]


class TargetingProductAudienceSpecFields(BaseModel):
    """Pydantic model for TargetingProductAudienceSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    exclusions: list[TargetingProductAudienceSubSpecFields] = Field(None, alias="exclusions")
    inclusions: list[TargetingProductAudienceSubSpecFields] = Field(None, alias="inclusions")
    product_set_id: str = Field(None, alias="product_set_id")
