"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productset import ProductSetFields


# Field literal type
DynamicItemDisplayBundleField = Literal[
    "additional_urls", "description", "id", "name", "product_set", "text_tokens", "url"
]


class DynamicItemDisplayBundleFields(BaseModel):
    """Pydantic model for DynamicItemDisplayBundle fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    additional_urls: list[dict[str, str]] = Field(None, alias="additional_urls")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    product_set: ProductSetFields = Field(None, alias="product_set")
    text_tokens: list[dict[str, str]] = Field(None, alias="text_tokens")
    url: str = Field(None, alias="url")
