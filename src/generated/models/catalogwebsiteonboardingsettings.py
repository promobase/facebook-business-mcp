"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogWebsiteOnboardingSettingsField = Literal["id", "quality_band", "status"]


class CatalogWebsiteOnboardingSettingsFields(BaseModel):
    """Pydantic model for CatalogWebsiteOnboardingSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    quality_band: str = Field(None, alias="quality_band")
    status: str = Field(None, alias="status")
