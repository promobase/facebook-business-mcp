"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeProductDataField = Literal["product_id", "product_source"]


class AdCreativeProductDataFields(BaseModel):
    """Pydantic model for AdCreativeProductData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    product_id: str = Field(None, alias="product_id")
    product_source: str = Field(None, alias="product_source")
