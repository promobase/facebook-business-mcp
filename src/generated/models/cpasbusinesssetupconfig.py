"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
CPASBusinessSetupConfigField = Literal[
    "accepted_collab_ads_tos",
    "business",
    "business_capabilities_status",
    "capabilities_compliance_status",
    "id",
]


class CPASBusinessSetupConfigFields(BaseModel):
    """Pydantic model for CPASBusinessSetupConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    accepted_collab_ads_tos: bool = Field(None, alias="accepted_collab_ads_tos")
    business: BusinessFields = Field(None, alias="business")
    business_capabilities_status: list[dict[str, str]] = Field(
        None, alias="business_capabilities_status"
    )
    capabilities_compliance_status: list[dict[str, dict[str, Any]]] = Field(
        None, alias="capabilities_compliance_status"
    )
    id: str = Field(None, alias="id")
