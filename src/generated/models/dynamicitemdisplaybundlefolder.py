"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productcatalog import ProductCatalogFields
    from .productset import ProductSetFields


# Field literal type
DynamicItemDisplayBundleFolderField = Literal[
    "categorization_criteria", "id", "name", "product_catalog", "product_set", "valid_labels"
]


class DynamicItemDisplayBundleFolderFields(BaseModel):
    """Pydantic model for DynamicItemDisplayBundleFolder fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    categorization_criteria: str = Field(None, alias="categorization_criteria")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    product_catalog: ProductCatalogFields = Field(None, alias="product_catalog")
    product_set: ProductSetFields = Field(None, alias="product_set")
    valid_labels: list[dict[str, list[str]]] = Field(None, alias="valid_labels")
