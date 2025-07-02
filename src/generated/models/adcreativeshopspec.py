"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeShopSpecField = Literal["collection_id", "landing_view", "shop_id"]


class AdCreativeShopSpecFields(BaseModel):
    """Pydantic model for AdCreativeShopSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    collection_id: str = Field(None, alias="collection_id")
    landing_view: str = Field(None, alias="landing_view")
    shop_id: str = Field(None, alias="shop_id")
