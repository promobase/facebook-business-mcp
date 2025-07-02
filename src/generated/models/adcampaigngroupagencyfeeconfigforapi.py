"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignGroupAgencyFeeConfigForApiField = Literal[
    "agency_fee_pct", "is_agency_fee_disabled", "is_default_agency_fee"
]


class AdCampaignGroupAgencyFeeConfigForApiFields(BaseModel):
    """Pydantic model for AdCampaignGroupAgencyFeeConfigForApi fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    agency_fee_pct: float = Field(None, alias="agency_fee_pct")
    is_agency_fee_disabled: bool = Field(None, alias="is_agency_fee_disabled")
    is_default_agency_fee: bool = Field(None, alias="is_default_agency_fee")
