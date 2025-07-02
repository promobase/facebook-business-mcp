"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productitemlocalinfolatlongshape import ProductItemLocalInfoLatLongShapeFields


# Field literal type
ProductItemLocalInfoField = Literal[
    "availability_circle_origin",
    "availability_circle_radius",
    "availability_circle_radius_unit",
    "availability_polygon_coordinates",
    "availability_postal_codes",
    "availability_source",
    "id",
    "inferred_circle_origin",
    "inferred_circle_radius",
]


class ProductItemLocalInfoFields(BaseModel):
    """Pydantic model for ProductItemLocalInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    availability_circle_origin: ProductItemLocalInfoLatLongShapeFields = Field(
        None, alias="availability_circle_origin"
    )
    availability_circle_radius: float = Field(None, alias="availability_circle_radius")
    availability_circle_radius_unit: str = Field(None, alias="availability_circle_radius_unit")
    availability_polygon_coordinates: list[ProductItemLocalInfoLatLongShapeFields] = Field(
        None, alias="availability_polygon_coordinates"
    )
    availability_postal_codes: list[str] = Field(None, alias="availability_postal_codes")
    availability_source: str = Field(None, alias="availability_source")
    id: str = Field(None, alias="id")
    inferred_circle_origin: ProductItemLocalInfoLatLongShapeFields = Field(
        None, alias="inferred_circle_origin"
    )
    inferred_circle_radius: float = Field(None, alias="inferred_circle_radius")
