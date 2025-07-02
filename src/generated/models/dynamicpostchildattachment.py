"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DynamicPostChildAttachmentField = Literal[
    "description", "image_url", "link", "place_id", "product_id", "title"
]


class DynamicPostChildAttachmentFields(BaseModel):
    """Pydantic model for DynamicPostChildAttachment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    image_url: str = Field(None, alias="image_url")
    link: str = Field(None, alias="link")
    place_id: str = Field(None, alias="place_id")
    product_id: str = Field(None, alias="product_id")
    title: str = Field(None, alias="title")
