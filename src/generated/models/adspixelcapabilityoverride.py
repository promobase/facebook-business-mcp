"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelCapabilityOverrideField = Literal["capability", "id", "override_value", "reason"]


class AdsPixelCapabilityOverrideFields(BaseModel):
    """Pydantic model for AdsPixelCapabilityOverride fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    capability: str = Field(None, alias="capability")
    id: str = Field(None, alias="id")
    override_value: str = Field(None, alias="override_value")
    reason: str = Field(None, alias="reason")
