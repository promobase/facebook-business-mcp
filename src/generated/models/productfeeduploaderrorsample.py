"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductFeedUploadErrorSampleField = Literal["id", "retailer_id", "row_number"]


class ProductFeedUploadErrorSampleFields(BaseModel):
    """Pydantic model for ProductFeedUploadErrorSample fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    retailer_id: str = Field(None, alias="retailer_id")
    row_number: int = Field(None, alias="row_number")
