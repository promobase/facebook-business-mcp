"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productcatalog import ProductCatalogFields


# Field literal type
FavoriteCatalogField = Literal["catalog", "id"]


class FavoriteCatalogFields(BaseModel):
    """Pydantic model for FavoriteCatalog fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    catalog: ProductCatalogFields = Field(None, alias="catalog")
    id: str = Field(None, alias="id")
