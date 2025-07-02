"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
InstagramRelatedProductTagsField = Literal[
    "checkout_setting", "id", "image_uri", "name", "price_label", "sale_price_label"
]


class InstagramRelatedProductTagsFields(BaseModel):
    """Pydantic model for InstagramRelatedProductTags fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    checkout_setting: str = Field(None, alias="checkout_setting")
    id: int = Field(None, alias="id")
    image_uri: str = Field(None, alias="image_uri")
    name: str = Field(None, alias="name")
    price_label: str = Field(None, alias="price_label")
    sale_price_label: str = Field(None, alias="sale_price_label")
