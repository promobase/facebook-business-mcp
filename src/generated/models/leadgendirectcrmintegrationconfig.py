"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgenform import LeadgenFormFields


# Field literal type
LeadGenDirectCRMIntegrationConfigField = Literal[
    "auth_id",
    "creation_time",
    "id",
    "lead_gen_data",
    "matched_fields",
    "matched_fields_labels",
    "resources",
    "third_party_app_id",
]


class LeadGenDirectCRMIntegrationConfigFields(BaseModel):
    """Pydantic model for LeadGenDirectCRMIntegrationConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    auth_id: str = Field(None, alias="auth_id")
    creation_time: datetime = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    lead_gen_data: LeadgenFormFields = Field(None, alias="lead_gen_data")
    matched_fields: list[dict[str, str]] = Field(None, alias="matched_fields")
    matched_fields_labels: list[dict[str, str]] = Field(None, alias="matched_fields_labels")
    resources: list[dict[str, str]] = Field(None, alias="resources")
    third_party_app_id: str = Field(None, alias="third_party_app_id")
