"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativefeaturecustomizations import AdCreativeFeatureCustomizationsFields


# Field literal type
AdCreativeFeatureDetailsField = Literal["customizations", "enroll_status"]


class AdCreativeFeatureDetailsFields(BaseModel):
    """Pydantic model for AdCreativeFeatureDetails fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    customizations: AdCreativeFeatureCustomizationsFields = Field(None, alias="customizations")
    enroll_status: str = Field(None, alias="enroll_status")
