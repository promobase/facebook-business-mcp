"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields
    from .videocopyrightgeogate import VideoCopyrightGeoGateFields


# Field literal type
FBImageCopyrightMatchField = Literal[
    "added_to_dashboard_time",
    "applied_actions",
    "audit_log",
    "available_ui_actions",
    "expiration_days",
    "generic_match_data",
    "id",
    "is_business_page_match",
    "last_modified_time",
    "match_data",
    "match_status",
    "ownership_countries",
    "reference_owner",
    "time_to_appeal",
]


class FBImageCopyrightMatchFields(BaseModel):
    """Pydantic model for FBImageCopyrightMatch fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    added_to_dashboard_time: datetime = Field(None, alias="added_to_dashboard_time")
    applied_actions: list[dict[str, dict[str, Any]]] = Field(None, alias="applied_actions")
    audit_log: list[dict[str, Any]] = Field(None, alias="audit_log")
    available_ui_actions: list[str] = Field(None, alias="available_ui_actions")
    expiration_days: int = Field(None, alias="expiration_days")
    generic_match_data: list[dict[str, Any]] = Field(None, alias="generic_match_data")
    id: str = Field(None, alias="id")
    is_business_page_match: bool = Field(None, alias="is_business_page_match")
    last_modified_time: datetime = Field(None, alias="last_modified_time")
    match_data: list[dict[str, Any]] = Field(None, alias="match_data")
    match_status: str = Field(None, alias="match_status")
    ownership_countries: VideoCopyrightGeoGateFields = Field(None, alias="ownership_countries")
    reference_owner: ProfileFields = Field(None, alias="reference_owner")
    time_to_appeal: int = Field(None, alias="time_to_appeal")
