"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductCatalogFacetsField = Literal["facets", "item_count"]


class ProductCatalogFacetsFields(BaseModel):
    """Pydantic model for ProductCatalogFacets fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    facets: list[dict[str, list[dict[str, Any]]]] = Field(None, alias="facets")
    item_count: int = Field(None, alias="item_count")
