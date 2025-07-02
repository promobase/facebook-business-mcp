"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageLocationsBreakdownField = Literal[
    "location_id",
    "location_name",
    "location_type",
    "num_pages",
    "num_pages_eligible_for_store_visit_reporting",
    "num_unpublished_or_closed_pages",
    "parent_country_code",
    "parent_region_id",
    "parent_region_name",
]


class PageLocationsBreakdownFields(BaseModel):
    """Pydantic model for PageLocationsBreakdown fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    location_id: str = Field(None, alias="location_id")
    location_name: str = Field(None, alias="location_name")
    location_type: str = Field(None, alias="location_type")
    num_pages: int = Field(None, alias="num_pages")
    num_pages_eligible_for_store_visit_reporting: int = Field(
        None, alias="num_pages_eligible_for_store_visit_reporting"
    )
    num_unpublished_or_closed_pages: int = Field(None, alias="num_unpublished_or_closed_pages")
    parent_country_code: str = Field(None, alias="parent_country_code")
    parent_region_id: int = Field(None, alias="parent_region_id")
    parent_region_name: str = Field(None, alias="parent_region_name")
