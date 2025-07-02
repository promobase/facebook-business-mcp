"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductCatalogImageSettingsOperationField = Literal["transformation_type"]


class ProductCatalogImageSettingsOperationFields(BaseModel):
    """Pydantic model for ProductCatalogImageSettingsOperation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    transformation_type: str = Field(None, alias="transformation_type")
