"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CreatorAssetCreativeField = Literal[
    "id",
    "image_url",
    "moderation_status",
    "product_item_retailer_id",
    "product_url",
    "retailer_id",
    "video_url",
]


class CreatorAssetCreativeFields(BaseModel):
    """Pydantic model for CreatorAssetCreative fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    image_url: str = Field(None, alias="image_url")
    moderation_status: str = Field(None, alias="moderation_status")
    product_item_retailer_id: str = Field(None, alias="product_item_retailer_id")
    product_url: str = Field(None, alias="product_url")
    retailer_id: str = Field(None, alias="retailer_id")
    video_url: str = Field(None, alias="video_url")
