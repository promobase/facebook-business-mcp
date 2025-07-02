"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MerchantComplianceField = Literal[
    "active_campaigns",
    "compliance_status",
    "count_down_start_time",
    "purchase",
    "purchase_conversion_value",
]


class MerchantComplianceFields(BaseModel):
    """Pydantic model for MerchantCompliance fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    active_campaigns: int = Field(None, alias="active_campaigns")
    compliance_status: str = Field(None, alias="compliance_status")
    count_down_start_time: int = Field(None, alias="count_down_start_time")
    purchase: int = Field(None, alias="purchase")
    purchase_conversion_value: float = Field(None, alias="purchase_conversion_value")
