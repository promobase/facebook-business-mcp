"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ThirdPartyPartnerLiftRequest_status(str, Enum):
    """ThirdPartyPartnerLiftRequest_status enum values."""

    CREATED = "CREATED"
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"
    SCHEDULED = "SCHEDULED"
    SUCCESS = "SUCCESS"


# Field literal type
ThirdPartyPartnerLiftRequestField = Literal[
    "ad_entities",
    "country",
    "created_time",
    "description",
    "holdout_size",
    "id",
    "legacy_ads_data_partner_id",
    "legacy_ads_data_partner_name",
    "modified_time",
    "owner_instance_id",
    "partner_household_graph_dataset_id",
    "region",
    "status",
    "study_cells",
    "study_end_time",
    "study_start_time",
]


class ThirdPartyPartnerLiftRequestFields(BaseModel):
    """Pydantic model for ThirdPartyPartnerLiftRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_entities: list[str] = Field(None, alias="ad_entities")
    country: str = Field(None, alias="country")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    holdout_size: float = Field(None, alias="holdout_size")
    id: str = Field(None, alias="id")
    legacy_ads_data_partner_id: str = Field(None, alias="legacy_ads_data_partner_id")
    legacy_ads_data_partner_name: str = Field(None, alias="legacy_ads_data_partner_name")
    modified_time: datetime = Field(None, alias="modified_time")
    owner_instance_id: str = Field(None, alias="owner_instance_id")
    partner_household_graph_dataset_id: str = Field(
        None, alias="partner_household_graph_dataset_id"
    )
    region: str = Field(None, alias="region")
    status: dict[str, Any] = Field(None, alias="status")
    study_cells: list[str] = Field(None, alias="study_cells")
    study_end_time: datetime = Field(None, alias="study_end_time")
    study_start_time: datetime = Field(None, alias="study_start_time")
