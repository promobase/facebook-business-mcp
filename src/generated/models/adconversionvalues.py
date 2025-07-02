"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdConversionValuesField = Literal["adgroup_id", "campaign_id", "values"]


class AdConversionValuesFields(BaseModel):
    """Pydantic model for AdConversionValues fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adgroup_id: str = Field(None, alias="adgroup_id")
    campaign_id: str = Field(None, alias="campaign_id")
    values: dict[str, Any] = Field(None, alias="values")
