"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CPASMerchantConfigField = Literal[
    "accepted_tos",
    "beta_features",
    "business_outcomes_status",
    "id",
    "is_test_merchant",
    "outcomes_compliance_status",
    "qualified_to_onboard",
]


class CPASMerchantConfigFields(BaseModel):
    """Pydantic model for CPASMerchantConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    accepted_tos: bool = Field(None, alias="accepted_tos")
    beta_features: list[str] = Field(None, alias="beta_features")
    business_outcomes_status: list[dict[str, str]] = Field(None, alias="business_outcomes_status")
    id: str = Field(None, alias="id")
    is_test_merchant: bool = Field(None, alias="is_test_merchant")
    outcomes_compliance_status: list[dict[str, dict[str, Any]]] = Field(
        None, alias="outcomes_compliance_status"
    )
    qualified_to_onboard: bool = Field(None, alias="qualified_to_onboard")
