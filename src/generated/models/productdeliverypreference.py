"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductDeliveryPreferenceField = Literal[
    "ad_object_id", "id", "product_priority", "product_priority_category"
]


class ProductDeliveryPreferenceFields(BaseModel):
    """Pydantic model for ProductDeliveryPreference fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_object_id: str = Field(None, alias="ad_object_id")
    id: str = Field(None, alias="id")
    product_priority: str = Field(None, alias="product_priority")
    product_priority_category: list[str] = Field(None, alias="product_priority_category")
