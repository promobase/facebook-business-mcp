"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemOfferField = Literal["availability_area", "availability_radius", "id"]


class ProductItemOfferFields(BaseModel):
    """Pydantic model for ProductItemOffer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    availability_area: list[dict[str, Any]] = Field(None, alias="availability_area")
    availability_radius: float = Field(None, alias="availability_radius")
    id: str = Field(None, alias="id")
