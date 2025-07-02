"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productset import ProductSetFields


# Field literal type
ProductSetUsageField = Literal["id", "product_set", "usage_type"]


class ProductSetUsageFields(BaseModel):
    """Pydantic model for ProductSetUsage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    product_set: ProductSetFields = Field(None, alias="product_set")
    usage_type: str = Field(None, alias="usage_type")
