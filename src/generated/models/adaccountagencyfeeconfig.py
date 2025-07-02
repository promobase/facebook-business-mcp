"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdAccountAgencyFeeConfig_status(str, Enum):
    """AdAccountAgencyFeeConfig_status enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DRAFT = "DRAFT"
    UNKNOWN = "UNKNOWN"


# Field literal type
AdAccountAgencyFeeConfigField = Literal[
    "can_add_agency_fee_to_invoice",
    "default_agency_fee_pct",
    "id",
    "is_agency_fee_disabled",
    "status",
]


class AdAccountAgencyFeeConfigFields(BaseModel):
    """Pydantic model for AdAccountAgencyFeeConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_add_agency_fee_to_invoice: bool = Field(None, alias="can_add_agency_fee_to_invoice")
    default_agency_fee_pct: float = Field(None, alias="default_agency_fee_pct")
    id: str = Field(None, alias="id")
    is_agency_fee_disabled: bool = Field(None, alias="is_agency_fee_disabled")
    status: dict[str, Any] = Field(None, alias="status")
