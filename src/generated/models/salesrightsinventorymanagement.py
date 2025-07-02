"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
SalesRightsInventoryManagementField = Literal[
    "available_impressions",
    "booked_impressions",
    "overbooked_impressions",
    "supported_countries",
    "total_impressions",
    "unavailable_impressions",
    "warning_messages",
]


class SalesRightsInventoryManagementFields(BaseModel):
    """Pydantic model for SalesRightsInventoryManagement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    available_impressions: int = Field(None, alias="available_impressions")
    booked_impressions: int = Field(None, alias="booked_impressions")
    overbooked_impressions: int = Field(None, alias="overbooked_impressions")
    supported_countries: list[str] = Field(None, alias="supported_countries")
    total_impressions: int = Field(None, alias="total_impressions")
    unavailable_impressions: int = Field(None, alias="unavailable_impressions")
    warning_messages: list[str] = Field(None, alias="warning_messages")
