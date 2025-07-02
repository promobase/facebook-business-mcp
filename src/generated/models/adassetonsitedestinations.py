"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAssetOnsiteDestinationsField = Literal[
    "auto_optimization",
    "details_page_product_id",
    "shop_collection_product_set_id",
    "source",
    "storefront_shop_id",
]


class AdAssetOnsiteDestinationsFields(BaseModel):
    """Pydantic model for AdAssetOnsiteDestinations fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    auto_optimization: str = Field(None, alias="auto_optimization")
    details_page_product_id: str = Field(None, alias="details_page_product_id")
    shop_collection_product_set_id: str = Field(None, alias="shop_collection_product_set_id")
    source: str = Field(None, alias="source")
    storefront_shop_id: str = Field(None, alias="storefront_shop_id")
