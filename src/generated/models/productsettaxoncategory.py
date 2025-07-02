"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductSetTaxonCategoryField = Literal["category_id", "category_name", "image_url"]


class ProductSetTaxonCategoryFields(BaseModel):
    """Pydantic model for ProductSetTaxonCategory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    category_id: int = Field(None, alias="category_id")
    category_name: str = Field(None, alias="category_name")
    image_url: str = Field(None, alias="image_url")
