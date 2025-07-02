"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OfflineConversionDataSetUsageField = Literal["num_lift_studies"]


class OfflineConversionDataSetUsageFields(BaseModel):
    """Pydantic model for OfflineConversionDataSetUsage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    num_lift_studies: int = Field(None, alias="num_lift_studies")
