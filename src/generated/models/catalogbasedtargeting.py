"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogBasedTargetingField = Literal["geo_targeting_type"]


class CatalogBasedTargetingFields(BaseModel):
    """Pydantic model for CatalogBasedTargeting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    geo_targeting_type: str = Field(None, alias="geo_targeting_type")
