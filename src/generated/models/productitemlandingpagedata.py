"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ProductItemLandingPageData_availability(str, Enum):
    """ProductItemLandingPageData_availability enum values."""

    AVAILABLE_FOR_ORDER = "available for order"
    discontinued = "discontinued"
    IN_STOCK = "in stock"
    mark_as_sold = "mark_as_sold"
    OUT_OF_STOCK = "out of stock"
    pending = "pending"
    preorder = "preorder"


# Field literal type
ProductItemLandingPageDataField = Literal["availability"]


class ProductItemLandingPageDataFields(BaseModel):
    """Pydantic model for ProductItemLandingPageData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    availability: dict[str, Any] = Field(None, alias="availability")
