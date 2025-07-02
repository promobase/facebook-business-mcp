"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogAdvertiserInsightField = Literal["category", "country"]


class CatalogAdvertiserInsightFields(BaseModel):
    """Pydantic model for CatalogAdvertiserInsight fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    category: str = Field(None, alias="category")
    country: str = Field(None, alias="country")
