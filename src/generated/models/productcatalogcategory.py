"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductCatalogCategoryField = Literal[
    "criteria_value", "description", "destination_uri", "image_url", "name", "num_items", "tokens"
]


class ProductCatalogCategoryFields(BaseModel):
    """Pydantic model for ProductCatalogCategory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    criteria_value: str = Field(None, alias="criteria_value")
    description: str = Field(None, alias="description")
    destination_uri: str = Field(None, alias="destination_uri")
    image_url: str = Field(None, alias="image_url")
    name: str = Field(None, alias="name")
    num_items: int = Field(None, alias="num_items")
    tokens: list[dict[str, str]] = Field(None, alias="tokens")
