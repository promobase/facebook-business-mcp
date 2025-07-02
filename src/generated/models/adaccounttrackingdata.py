"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .conversionactionquery import ConversionActionQueryFields


# Field literal type
AdAccountTrackingDataField = Literal["tracking_specs"]


class AdAccountTrackingDataFields(BaseModel):
    """Pydantic model for AdAccountTrackingData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    tracking_specs: ConversionActionQueryFields = Field(None, alias="tracking_specs")
