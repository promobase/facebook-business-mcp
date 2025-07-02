"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LookalikeSpecField = Literal[
    "country",
    "is_financial_service",
    "origin",
    "origin_event_name",
    "origin_event_source_name",
    "origin_event_source_type",
    "product_set_name",
    "ratio",
    "starting_ratio",
    "target_countries",
    "target_country_names",
    "type",
]


class LookalikeSpecFields(BaseModel):
    """Pydantic model for LookalikeSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    is_financial_service: bool = Field(None, alias="is_financial_service")
    origin: list[dict[str, Any]] = Field(None, alias="origin")
    origin_event_name: str = Field(None, alias="origin_event_name")
    origin_event_source_name: str = Field(None, alias="origin_event_source_name")
    origin_event_source_type: str = Field(None, alias="origin_event_source_type")
    product_set_name: str = Field(None, alias="product_set_name")
    ratio: float = Field(None, alias="ratio")
    starting_ratio: float = Field(None, alias="starting_ratio")
    target_countries: list[str] = Field(None, alias="target_countries")
    target_country_names: dict[str, Any] = Field(None, alias="target_country_names")
    type: str = Field(None, alias="type")
