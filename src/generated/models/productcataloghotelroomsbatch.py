"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductCatalogHotelRoomsBatchField = Literal["errors", "errors_total_count", "handle", "status"]


class ProductCatalogHotelRoomsBatchFields(BaseModel):
    """Pydantic model for ProductCatalogHotelRoomsBatch fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    errors: list[dict[str, Any]] = Field(None, alias="errors")
    errors_total_count: int = Field(None, alias="errors_total_count")
    handle: str = Field(None, alias="handle")
    status: str = Field(None, alias="status")
