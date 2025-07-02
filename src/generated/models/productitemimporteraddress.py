"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemImporterAddressField = Literal[
    "city", "country", "postal_code", "region", "street1", "street2"
]


class ProductItemImporterAddressFields(BaseModel):
    """Pydantic model for ProductItemImporterAddress fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    city: str = Field(None, alias="city")
    country: str = Field(None, alias="country")
    postal_code: str = Field(None, alias="postal_code")
    region: str = Field(None, alias="region")
    street1: str = Field(None, alias="street1")
    street2: str = Field(None, alias="street2")
