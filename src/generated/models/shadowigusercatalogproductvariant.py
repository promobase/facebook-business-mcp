"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ShadowIGUserCatalogProductVariantField = Literal["product_id", "variant_name"]


class ShadowIGUserCatalogProductVariantFields(BaseModel):
    """Pydantic model for ShadowIGUserCatalogProductVariant fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    product_id: int = Field(None, alias="product_id")
    variant_name: str = Field(None, alias="variant_name")
