"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .location import LocationFields


# Field literal type
PlaceField = Literal["id", "location", "name", "overall_rating"]


class PlaceFields(BaseModel):
    """Pydantic model for Place fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    location: LocationFields = Field(None, alias="location")
    name: str = Field(None, alias="name")
    overall_rating: float = Field(None, alias="overall_rating")
