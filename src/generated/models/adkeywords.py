"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdKeywordsField = Literal["brands", "product_categories", "product_names", "search_terms"]


class AdKeywordsFields(BaseModel):
    """Pydantic model for AdKeywords fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    brands: list[str] = Field(None, alias="brands")
    product_categories: list[str] = Field(None, alias="product_categories")
    product_names: list[str] = Field(None, alias="product_names")
    search_terms: list[str] = Field(None, alias="search_terms")
