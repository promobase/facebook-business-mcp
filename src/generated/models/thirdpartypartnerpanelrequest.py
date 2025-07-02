"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ThirdPartyPartnerPanelRequest_status(str, Enum):
    """ThirdPartyPartnerPanelRequest_status enum values."""

    CREATED = "CREATED"
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"
    SCHEDULED = "SCHEDULED"
    SUCCESS = "SUCCESS"


class ThirdPartyPartnerPanelRequest_study_type(str, Enum):
    """ThirdPartyPartnerPanelRequest_study_type enum values."""

    BRAND_LIFT = "BRAND_LIFT"
    PANEL_SALES_ATTRIBUTION = "PANEL_SALES_ATTRIBUTION"
    REACH = "REACH"


# Field literal type
ThirdPartyPartnerPanelRequestField = Literal[
    "adentities_ids",
    "country",
    "created_time",
    "description",
    "id",
    "modified_time",
    "owner_instance_id",
    "owner_panel_id",
    "owner_panel_name",
    "status",
    "study_end_time",
    "study_start_time",
    "study_type",
]


class ThirdPartyPartnerPanelRequestFields(BaseModel):
    """Pydantic model for ThirdPartyPartnerPanelRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adentities_ids: list[str] = Field(None, alias="adentities_ids")
    country: str = Field(None, alias="country")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    modified_time: datetime = Field(None, alias="modified_time")
    owner_instance_id: str = Field(None, alias="owner_instance_id")
    owner_panel_id: str = Field(None, alias="owner_panel_id")
    owner_panel_name: str = Field(None, alias="owner_panel_name")
    status: dict[str, Any] = Field(None, alias="status")
    study_end_time: datetime = Field(None, alias="study_end_time")
    study_start_time: datetime = Field(None, alias="study_start_time")
    study_type: dict[str, Any] = Field(None, alias="study_type")
