"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativePortraitCustomizationsField = Literal["carousel_delivery_mode", "specifications"]


class AdCreativePortraitCustomizationsFields(BaseModel):
    """Pydantic model for AdCreativePortraitCustomizations fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    carousel_delivery_mode: str = Field(None, alias="carousel_delivery_mode")
    specifications: list[dict[str, Any]] = Field(None, alias="specifications")
