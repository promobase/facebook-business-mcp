"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageRestaurantSpecialtiesField = Literal["breakfast", "coffee", "dinner", "drinks", "lunch"]


class PageRestaurantSpecialtiesFields(BaseModel):
    """Pydantic model for PageRestaurantSpecialties fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    breakfast: int = Field(None, alias="breakfast")
    coffee: int = Field(None, alias="coffee")
    dinner: int = Field(None, alias="dinner")
    drinks: int = Field(None, alias="drinks")
    lunch: int = Field(None, alias="lunch")
