"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductVariantField = Literal["label", "options", "product_field"]


class ProductVariantFields(BaseModel):
    """Pydantic model for ProductVariant fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    label: str = Field(None, alias="label")
    options: list[str] = Field(None, alias="options")
    product_field: str = Field(None, alias="product_field")
