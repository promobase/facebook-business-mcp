"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageParkingField = Literal["lot", "street", "valet"]


class PageParkingFields(BaseModel):
    """Pydantic model for PageParking fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    lot: int = Field(None, alias="lot")
    street: int = Field(None, alias="street")
    valet: int = Field(None, alias="valet")
