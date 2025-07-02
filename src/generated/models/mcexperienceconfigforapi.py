"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MCExperienceConfigForApiField = Literal["is_campaign_enabled", "is_terms_signed", "merchant_type"]


class MCExperienceConfigForApiFields(BaseModel):
    """Pydantic model for MCExperienceConfigForApi fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_campaign_enabled: bool = Field(None, alias="is_campaign_enabled")
    is_terms_signed: bool = Field(None, alias="is_terms_signed")
    merchant_type: str = Field(None, alias="merchant_type")
