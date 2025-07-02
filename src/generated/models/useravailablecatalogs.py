"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserAvailableCatalogsField = Literal["catalog_id", "catalog_name", "product_count", "shop_name"]


class UserAvailableCatalogsFields(BaseModel):
    """Pydantic model for UserAvailableCatalogs fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    catalog_id: str = Field(None, alias="catalog_id")
    catalog_name: str = Field(None, alias="catalog_name")
    product_count: int = Field(None, alias="product_count")
    shop_name: str = Field(None, alias="shop_name")
