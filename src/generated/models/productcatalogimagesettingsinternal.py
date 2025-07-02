"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productcatalogimagesettingsoperation import ProductCatalogImageSettingsOperationFields


# Field literal type
ProductCatalogImageSettingsInternalField = Literal["carousel_ad", "shops_pdp", "single_ad"]


class ProductCatalogImageSettingsInternalFields(BaseModel):
    """Pydantic model for ProductCatalogImageSettingsInternal fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    carousel_ad: ProductCatalogImageSettingsOperationFields = Field(None, alias="carousel_ad")
    shops_pdp: ProductCatalogImageSettingsOperationFields = Field(None, alias="shops_pdp")
    single_ad: ProductCatalogImageSettingsOperationFields = Field(None, alias="single_ad")
