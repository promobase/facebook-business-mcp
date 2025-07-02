"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductImageField = Literal["height", "id", "image_url", "width"]


class ProductImageFields(BaseModel):
    """Pydantic model for ProductImage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    height: int = Field(None, alias="height")
    id: str = Field(None, alias="id")
    image_url: str = Field(None, alias="image_url")
    width: int = Field(None, alias="width")
