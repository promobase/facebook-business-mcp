"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ThirdPartyPartnerPanelScheduled_status(str, Enum):
    """ThirdPartyPartnerPanelScheduled_status enum values."""

    CANCELLED = "CANCELLED"
    CREATED = "CREATED"
    FINISHED = "FINISHED"
    ONGOING = "ONGOING"


class ThirdPartyPartnerPanelScheduled_study_type(str, Enum):
    """ThirdPartyPartnerPanelScheduled_study_type enum values."""

    BRAND_LIFT = "BRAND_LIFT"
    PANEL_SALES_ATTRIBUTION = "PANEL_SALES_ATTRIBUTION"
    REACH = "REACH"


# Field literal type
ThirdPartyPartnerPanelScheduledField = Literal[
    "adentities_ids",
    "cadence",
    "country",
    "created_time",
    "description",
    "end_time",
    "id",
    "modified_time",
    "owner_instance_id",
    "owner_panel_id",
    "owner_panel_name",
    "start_time",
    "status",
    "study_type",
]


class ThirdPartyPartnerPanelScheduledFields(BaseModel):
    """Pydantic model for ThirdPartyPartnerPanelScheduled fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adentities_ids: list[str] = Field(None, alias="adentities_ids")
    cadence: str = Field(None, alias="cadence")
    country: str = Field(None, alias="country")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    end_time: datetime = Field(None, alias="end_time")
    id: str = Field(None, alias="id")
    modified_time: datetime = Field(None, alias="modified_time")
    owner_instance_id: str = Field(None, alias="owner_instance_id")
    owner_panel_id: str = Field(None, alias="owner_panel_id")
    owner_panel_name: str = Field(None, alias="owner_panel_name")
    start_time: datetime = Field(None, alias="start_time")
    status: dict[str, Any] = Field(None, alias="status")
    study_type: dict[str, Any] = Field(None, alias="study_type")
