"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
ThirdPartyMeasurementReportDatasetField = Literal["category", "id", "partner", "product", "schema"]


class ThirdPartyMeasurementReportDatasetFields(BaseModel):
    """Pydantic model for ThirdPartyMeasurementReportDataset fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    category: str = Field(None, alias="category")
    id: str = Field(None, alias="id")
    partner: BusinessFields = Field(None, alias="partner")
    product: str = Field(None, alias="product")
    schema_: list[dict[str, Any]] = Field(None, alias="schema")
