"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adstudy import AdStudyFields


# Field literal type
PartnerStudyField = Literal[
    "additional_info",
    "brand",
    "client_name",
    "emails",
    "id",
    "input_ids",
    "is_export",
    "lift_study",
    "location",
    "match_file_ds",
    "name",
    "partner_defined_id",
    "partner_household_graph_dataset_id",
    "status",
    "study_end_date",
    "study_start_date",
    "study_type",
    "submit_date",
]


class PartnerStudyFields(BaseModel):
    """Pydantic model for PartnerStudy fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    additional_info: str = Field(None, alias="additional_info")
    brand: str = Field(None, alias="brand")
    client_name: str = Field(None, alias="client_name")
    emails: str = Field(None, alias="emails")
    id: str = Field(None, alias="id")
    input_ids: list[str] = Field(None, alias="input_ids")
    is_export: bool = Field(None, alias="is_export")
    lift_study: AdStudyFields = Field(None, alias="lift_study")
    location: str = Field(None, alias="location")
    match_file_ds: str = Field(None, alias="match_file_ds")
    name: str = Field(None, alias="name")
    partner_defined_id: str = Field(None, alias="partner_defined_id")
    partner_household_graph_dataset_id: str = Field(
        None, alias="partner_household_graph_dataset_id"
    )
    status: str = Field(None, alias="status")
    study_end_date: datetime = Field(None, alias="study_end_date")
    study_start_date: datetime = Field(None, alias="study_start_date")
    study_type: str = Field(None, alias="study_type")
    submit_date: datetime = Field(None, alias="submit_date")
