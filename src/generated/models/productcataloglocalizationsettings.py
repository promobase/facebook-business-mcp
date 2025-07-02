"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductCatalogLocalizationSettingsField = Literal["default_country", "default_language", "id"]


class ProductCatalogLocalizationSettingsFields(BaseModel):
    """Pydantic model for ProductCatalogLocalizationSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    default_country: str = Field(None, alias="default_country")
    default_language: str = Field(None, alias="default_language")
    id: str = Field(None, alias="id")
