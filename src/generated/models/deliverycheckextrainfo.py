"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DeliveryCheckExtraInfoField = Literal["adgroup_ids", "campaign_ids", "countries"]


class DeliveryCheckExtraInfoFields(BaseModel):
    """Pydantic model for DeliveryCheckExtraInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adgroup_ids: list[str] = Field(None, alias="adgroup_ids")
    campaign_ids: list[str] = Field(None, alias="campaign_ids")
    countries: list[str] = Field(None, alias="countries")
